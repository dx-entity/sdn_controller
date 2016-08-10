import switches
import firewall
import host


class DeviceFactory(object):
    _PRODUCTION_LIST = {
        'switch2l': switches.Switch2L,
        'switch3l': switches.Switch3L,
        'firewall': firewall.Firewall,
        'host': host.SimpleHost,
        'server': host.SimpleServer
    }

    def __init__(self):
        # TODO: maybe add some examinations
        pass

    @staticmethod
    def get_device(device_type):
        if device_type not in DeviceFactory._PRODUCTION_LIST.keys():
            return NameError
        return DeviceFactory._PRODUCTION_LIST.get(device_type, None)()

