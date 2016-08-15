from mininet.net import Mininet


class GlobalNetInfo:
    _instance = None

    def __init__(self):
        self.net_mapping = list()
        self.device_info = dict()

    @staticmethod
    def get_instance():
        if not GlobalNetInfo._instance:
            GlobalNetInfo._instance = GlobalNetInfo()
        return GlobalNetInfo._instance

    def store_net(self, net):
        if isinstance(net, Mininet):
            self.net_mapping.append(net)

    def get_net(self):
        return self.net_mapping if self.net_mapping else None

    def store_device_info(self, *args):
        if not self.device_info.get(args[0], None):
            self.device_info[args[0]] = args[1]

    def get_device_info(self, dpid):
        if isinstance(dpid, str):
            dpid = int(dpid)
        return self.device_info.get(str(dpid), None)

    def remove_device_info(self, dpid):
        if isinstance(dpid, str):
            dpid = int(dpid)
        dpid = str(dpid)
        if self.device_info.has_key(dpid):
            device_type = self.device_info[dpid]
            del self.device_info[dpid]
            return True, device_type
        else:
            return False, None
