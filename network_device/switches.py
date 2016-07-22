import base_device


class SwitchL2(base_device.OFDevice):

    def __init__(self, dp, device_type):
        super(SwitchL2, self).__init__(dp, device_type)
        self.mac_table = {}
        self.port_table = {}

    def handle_specific_task(self):
        pass

    def add_default_flow(self):
        pass