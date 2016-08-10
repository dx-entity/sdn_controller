from base_device import TerminalDevice


class SimpleHost(TerminalDevice):
    _device_type = 'host'

    def __init__(self, device_id=None, mac=None, ip=None, name=None):
        super(SimpleHost, self).__init__(mac, ip, SimpleHost._device_type)
        self.name = name
        self.device_id = device_id

    def set_mac(self, mac):
        self.mac = mac

    def set_ip(self, ip):
        self.ip = ip

    def get_mac(self):
        return self.mac

    def get_ip(self):
        return self.ip

    def set_device_id(self, device_id):
        self.device_id = device_id

    def get_device_id(self):
        return self.device_id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class SimpleServer(TerminalDevice):
    _device_type = 'server'

    def __init__(self, mac=None, ip=None, name=None):
        super(SimpleServer, self).__init__(mac, ip, SimpleServer._device_type)
        self.name = name
