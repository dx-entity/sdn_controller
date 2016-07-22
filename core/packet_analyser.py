
from abc import ABCMeta, abstractmethod

from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
from ryu.lib import dpid as dpid_lib

from utils.log_formatter import LogFormat
from utils.global_data import GlobalData
from flow_manage import FlowManage
import statics as data

gd = GlobalData.get_instance()


class PacketRouter(object):
    def __init__(self):
        pass

    @staticmethod
    def route_pkt(msg):

        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocols(ethernet.ethernet)[0]
        dpid = msg.datapath.id

        if eth.ethertype == ether_types.ETH_TYPE_ARP:
            # logger.info("got an arp pkt")
            print "%s get an arp pkt" % (str(dpid))
            aph = ArpPacketHandler(msg)
            aph.handle_msg()
        elif eth.ethertype == ether_types.ETH_TYPE_IP:
            print "%s get an ip pkt" % (str(dpid))
            aph = IpPacketHandler(msg)
            aph.handle_msg()


class BasePacketHandler(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def install_flow(self, datapath):
        pass


class ArpPacketHandler(BasePacketHandler):
    def __init__(self, msg):
        self.msg = msg
        self.datapath = msg.datapath
        self.ofproto = self.datapath.ofproto
        self.parser = self.datapath.ofproto_parser

    def install_flow(self, datapath, matches, inst, table_id):
        parser = datapath.ofproto_parser

        mod = parser.OFPFlowMod(datapath=datapath, priority=data.MAXPRIORITY,
                                match=matches, instructions=inst, table_id=table_id)
        datapath.send_msg(mod)

    def analyse_msg(self):
        datapath = self.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        in_port = self.msg.match['in_port']

        table_id = self.msg.table_id

        pkt = packet.Packet(self.msg.data)
        eth = pkt.get_protocol(ethernet.ethernet)
        src = eth.src

        matches = parser.OFPMatch(eth_dst=src)
        actions = [parser.OFPActionOutput(port=in_port)]
        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]
        self.install_flow(datapath, matches, inst, table_id)
        return data.FLOODMAC

    def handle_msg(self):
        res = self.analyse_msg()

        send_data = None

        if self.msg.buffer_id == self.ofproto.OFP_NO_BUFFER:
            send_data = self.msg.data

        if res == data.FLOODMAC:
            actions = [self.parser.OFPActionOutput(self.ofproto.OFPP_FLOOD)]
            print "flood this pkt"
        else:
            actions = [self.parser.OFPActionOutput(port=res)]
            print "redirect this pkt"

        out = self.parser.OFPPacketOut(datapath=self.datapath, buffer_id=self.msg.buffer_id,
                                       in_port=self.msg.match['in_port'], actions=actions, data=send_data)

        self.datapath.send_msg(out)


class IpPacketHandler(BasePacketHandler):

    def __init__(self, msg):
        self.msg = msg
        self.datapath = msg.datapath
        self.ofproto = self.datapath.ofproto
        self.parser = self.datapath.ofproto_parser

    def analyse_msg(self):
        pass

    def install_flow(self, datapath):
        pass

    def handle_msg(self):
        self.analyse_msg()