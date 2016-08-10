from abc import ABCMeta, abstractmethod


class OFDevice(object):
    __metaclass__ = ABCMeta

    TYPEPOOL = ['switch2l', 'switch3l', 'router', 'firewall', 'ids', 'ips']

    def __init__(self, dp=None, device_type=None):
        self.dp = dp
        self.type = device_type if device_type in OFDevice.TYPEPOOL else None

    @abstractmethod
    def handle_specific_task(self): pass

    @abstractmethod
    def add_default_flow(self): pass

    @abstractmethod
    def handle_message(self): pass


class CustomSwitch(OFDevice):
    def __init__(self, name=None, device_id=None, dp=None, device_type=None):
        super(CustomSwitch, self).__init__(dp, device_type)
        self.device_id = device_id
        self.name = name
        self.dpid = None

    def handle_specific_task(self):
        pass

    def add_default_flow(self):
        pass

    def handle_message(self):
        pass

    def set_device_id(self, device_id):
        self.device_id = device_id

    def get_device_id(self):
        return self.device_id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_dpid(self, dpid):
        if self.dpid:
            return False
        self.dpid = str(dpid)
        return True

    def get_dpid(self):
        return self.dpid


class TerminalDevice(object):
    __metaclass__ = ABCMeta

    TYPEPOOL = ['host', 'server']

    def __init__(self, mac, ip, device_type):
        self.mac = mac
        self.ip = ip
        self.type = device_type if device_type in TerminalDevice.TYPEPOOL else None
