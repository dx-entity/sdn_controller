from ryu.lib.packet import packet
from ryu.lib.packet import ethernet

import statics as data
import base_device
from utils.packets.packet_classifier import PacketClassifier


class Switch2L(base_device.CustomSwitch):
    def __init__(self, device_id=None, dp=None):
        super(Switch2L, self).__init__(device_id, dp, Switch2L.__name__.lower())
        self.mac_table = {}
        self.port_table = {}
        self.port_vlan = {}

    def handle_specific_task(self):
        pass

    def handle_message(self, msg):
        if PacketClassifier.is_ipv6_packet(msg) or PacketClassifier.is_lldp_msg(msg):
            return

        if PacketClassifier.is_arp_packet(msg):
            pass

        if PacketClassifier.is_ipv4_packet(msg):
            print "ipv4"

        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocols(ethernet.ethernet)[0]
        in_port = msg.match["in_port"]
        reason = msg.reason
        table_id = msg.table_id
        src_mac = eth.src
        dst_mac = eth.dst

        if reason == self.ofproto.OFPR_NO_MATCH:
            if src_mac not in self.mac_table:
                self.mac_table[src_mac] = in_port

            if dst_mac == data.FLOODMAC or dst_mac not in self.mac_table:
                port = self.ofproto.OFPP_FLOOD
            else:
                if src_mac not in self.mac_table:
                    self.mac_table[src_mac] = in_port
                port = self.mac_table[dst_mac]

            if port != self.ofproto.OFPP_FLOOD:
                match = self.parser.OFPMatch(eth_dst=dst_mac)
                actions = [self.parser.OFPActionOutput(port)]
                inst = [self.parser.OFPInstructionActions(self.ofproto.OFPIT_APPLY_ACTIONS, actions)]

                self.add_flow(data.MACTABLEPRIORITY, match, inst, table_id)

            self.send_pkt_out(msg, port)

    def init_pipeline(self):
        match_table_miss = self.parser.OFPMatch()

        actions = [self.parser.OFPActionOutput(self.ofproto.OFPP_CONTROLLER, self.ofproto.OFPCML_NO_BUFFER)]
        inst = [self.parser.OFPInstructionActions(self.ofproto.OFPIT_APPLY_ACTIONS, actions)]

        self.add_flow(data.TABLEMISSPRIORITY, match_table_miss, inst)

    def send_pkt_out(self, msg, port):
        send_data = None

        if msg.buffer_id == self.ofproto.OFP_NO_BUFFER:
            send_data = msg.data

        if port == self.ofproto.OFPP_FLOOD:
            actions = [self.parser.OFPActionOutput(self.ofproto.OFPP_FLOOD)]
        else:
            actions = [self.parser.OFPActionOutput(port)]

        out = self.parser.OFPPacketOut(datapath=self.dp, buffer_id=msg.buffer_id,
                                       in_port=msg.match['in_port'], actions=actions, data=send_data)
        self.dp.send_msg(out)

    def init_port(self, ev):
        for p in ev.msg.body:
            self.port_table[p.port_no] = dict(name=p.name, mac=p.hw_addr)


class Switch3L(base_device.CustomSwitch):
    def __init__(self, device_id=None, dp=None):
        super(Switch3L, self).__init__(dp, Switch3L.__name__.lower())
        self.id = device_id
        self.mac_table = {}
        self.port_table = {}
        self.route_table = {}

    def handle_specific_task(self):
        pass

    def add_flow(self):
        pass

    def handle_message(self):
        pass

    def init_pipeline(self):
        pass
