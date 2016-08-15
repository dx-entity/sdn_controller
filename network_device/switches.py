import base_device

from ryu.lib.packet import packet
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types


class Switch2L(base_device.CustomSwitch):
    def __init__(self, device_id=None, dp=None):
        super(Switch2L, self).__init__(device_id, dp, Switch2L.__name__.lower())
        self.mac_table = {}
        self.port_table = {}
        self.port_vlan = {}

    def handle_specific_task(self):
        pass

    def add_default_flow(self):
        pass

    def handle_message(self, msg):
        pass

    def init_pipeline(self):
        pass

    def init_port(self, ev):
        for p in ev.msg.body:
            self.port_table[p.port_no] = dict(name=p.name, mac=p.hw_addr,)


class Switch3L(base_device.CustomSwitch):
    def __init__(self, device_id=None, dp=None):
        super(Switch3L, self).__init__(dp, Switch3L.__name__.lower())
        self.id = device_id
        self.mac_table = {}
        self.port_table = {}
        self.route_table = {}

    def handle_specific_task(self):
        pass

    def add_default_flow(self):
        pass

    def handle_message(self):
        pass

    def init_pipeline(self):
        pass
