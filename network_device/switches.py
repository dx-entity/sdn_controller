import base_device

from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types


class Switch2L(base_device.OFDevice):

    def __init__(self, dp):
        super(Switch2L, self).__init__(dp, Switch2L.__name__)

        self.mac_table = {}
        self.port_table = {}

    def handle_specific_task(self):
        pass

    def add_default_flow(self):
        pass

    def handle_message(self, msg):
        pass


class Switch3L(base_device.OFDevice):

    def __init__(self, dp):
        super(Switch3L, self).__init__(dp, Switch3L.__name__)

        self.mac_table = {}
        self.port_table = {}
        self.route_table = {}

    def handle_specific_task(self):
        pass

    def add_default_flow(self):
        pass

    def handle_message(self):
        pass