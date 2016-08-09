import switches
import firewall


class DeviceFactory(object):

    _PRODUCTION_LIST = {
        'switch2l': switches.Switch2L,
        'switch3l': switches.Switch3L,
        'firewall': firewall.Firewall
    }

    def __init__(self):
        #TODO: maybe add some examinations
        pass

    def get_device(self, dp):
        device_type = self.get_device_type(dp)
        if device_type not in self._PRODUCTION_LIST.keys():
            return NameError
        return self._PRODUCTION_LIST.get(device_type, None)(dp)


    def get_device_type(self, dp):
        dpid = dp.id
        #TODO: look up device type in configure file
        device_type = ''
        return device_type
