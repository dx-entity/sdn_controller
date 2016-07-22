
class GlobalData(dict):

    _instance = None

    def __init__(self):
        super(GlobalData, self).__init__()

        self.device_pool = {}
        self.dpid_arp_tmp = {}

    @staticmethod
    def get_instance():
        if not GlobalData._instance:
            GlobalData._instance = GlobalData()
        return GlobalData._instance

    def register_device(self, dpid, dp):
        self.device_pool[dpid] = dp

    def unregister_device(self, dpid):
        dev = self.device_pool.get(dpid, None)
        if not dev:
            return

        del self.device_pool[dpid]

    def get_datapath(self, dpid):
        return self.device_pool.get(dpid, None)