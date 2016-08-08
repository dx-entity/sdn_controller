from abc import ABCMeta, abstractmethod


class OFDevice(object):
    __metaclass__ = ABCMeta

    TYPEPOOL=['Switch2L', 'Switch3L', 'Router', 'Firewall', 'Ids', 'Ips']

    def __init__(self, dp, device_type):
        self.dpid = dp
        self.type = device_type if device_type in OFDevice.TYPEPOOL else None

    @abstractmethod
    def handle_specific_task(self): pass

    @abstractmethod
    def add_default_flow(self): pass

    @abstractmethod
    def handle_message(self):pass


class TerminalDevice(object):
    __metaclass__ = ABCMeta

    TYPEPOOL = ['host', 'server']

    def __init__(self, mac, ip, device_type):
        self.mac = mac
        self.ip = ip
        self.type = device_type if device_type in TerminalDevice.TYPEPOOL else None
