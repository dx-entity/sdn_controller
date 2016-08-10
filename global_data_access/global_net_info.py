from mininet.net import Mininet


class GlobalNetInfo:
    _instance = None

    def __init__(self):
        self.net_mapping = list()

    @staticmethod
    def get_instance():
        if not GlobalNetInfo._instance:
            GlobalNetInfo._instance = GlobalNetInfo()
        return GlobalNetInfo._instance

    def store_net(self, net):
        if isinstance(net, Mininet):
            self.net_mapping.append(net)
