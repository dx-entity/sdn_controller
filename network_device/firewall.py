import base_device


class Firewall(base_device.OFDevice):

    def __init__(self, dp):
        super(Firewall, self).__init__(self, dp, Firewall.__name__)

    def handle_specific_task(self):
        pass

    def handle_message(self):
        pass

    def add_flow(self):
        pass