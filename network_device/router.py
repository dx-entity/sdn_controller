import base_device


class Router(base_device.OFDevice):

    def __init__(self, dp):
        super(Router, self).__init__(dp, Router.__name__)

        self.route_table = {}

    def handle_message(self):
        pass

    def handle_specific_task(self):
        pass

    def add_flow(self):
        pass