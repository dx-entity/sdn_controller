from abc import ABCMeta, abstractmethod

from ryu.controller.controller import Datapath


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

    @abstractmethod
    def install_rules(self): pass

    @abstractmethod
    def init_pipeline(self): pass


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

    def install_rules(self, priority, match, actions, buffer_id=None):
        ofproto = self.dp.ofproto
        parser = ofproto.ofproto_parser

        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACIONS,
                                             actions)]

        mod = parser.OFPFlowMod(datapath=self.dp, priority=priority, match=match, instructions=inst)

        self.dp.send_msg(mod)

    def init_port_status(self):
        ofp = self.dp.ofproto
        ofp_parser = self.dp.ofproto_parser

        req = ofp_parser.OFPPortDescStatsRequest(self.dp, 0)
        self.dp.send_msg(req)

    def init_pipeline(self):
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

    def set_dp(self, dp):
        if isinstance(dp, Datapath) and self.dp is not None:
            self.dp = dp
            return True
        else:
            return False

    def get_dp(self):
        return self.dp

    def __call__(self, *args, **kwargs):
        self.init_port_status()
        self.init_pipeline()


class TerminalDevice(object):
    __metaclass__ = ABCMeta

    TYPEPOOL = ['host', 'server']

    def __init__(self, mac, ip, device_type):
        self.mac = mac
        self.ip = ip
        self.type = device_type if device_type in TerminalDevice.TYPEPOOL else None
