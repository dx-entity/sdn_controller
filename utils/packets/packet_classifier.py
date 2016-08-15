from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types


class PacketClassifier(object):
    def __init__(self):
        super(PacketClassifier, self).__init__(self)

    @staticmethod
    def _get_eth_header(msg):
        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocols(ethernet.ethernet)[0]
        return eth.ethertype

    @staticmethod
    def is_arp_packet(msg):
        return ether_types.ETH_TYPE_ARP == PacketClassifier._get_eth_header(msg)

    @staticmethod
    def is_ipv4_packet(msg):
        return ether_types.ETH_TYPE_IP == PacketClassifier._get_eth_header(msg)

    @staticmethod
    def is_ipv6_packet(msg):
        return ether_types.ETH_TYPE_IPV6 == PacketClassifier._get_eth_header(msg)

    @staticmethod
    def is_lldp_msg(msg):
        return ether_types.ETH_TYPE_LLDP == PacketClassifier._get_eth_header(msg)

    @staticmethod
    def is_vlan_msg(msg):
        return ether_types.ETH_TYPE_8021Q == PacketClassifier._get_eth_header(msg)