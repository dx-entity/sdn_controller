from itertools import chain

from xml.etree import ElementTree as ET
import statics as data

from network_device.device_factory import DeviceFactory
from topo_builder import build_topo

dpid_begin = 10


def xml_analyzer(topofile, controller):
    tree = ET.ElementTree(file=topofile)
    host = tree.iter(tag=data.TOPO.TAG.HOST)
    switch = tree.iter(tag=data.TOPO.TAG.SWITCH)

    def gen(x, y):
        return x[:1] + y

    base_info_topo = {}

    for s in chain(switch, host):
        dpid = None
        device_id = s.attrib.get(data.TOPO.TAG.ID, None)
        is_switch = True if s.tag == data.TOPO.TAG.SWITCH else False

        device_type = s.attrib.get(data.TOPO.TAG.TYPE, None) if is_switch else s.tag

        dev = DeviceFactory.get_device(device_type)
        dev.set_device_id(device_id)
        dev.set_name(gen(str(s.tag), device_id))
        if is_switch:
            dpid = dpid_gen()
            dev.set_dpid(dpid)
        interface = s.iter(tag=data.TOPO.TAG.INTERFACE)
        link = [[i.find(data.TOPO.TAG.LINK).text, device_id] for i in interface]
        device_info = {"link": link, "controller": None, "dpid": dpid,
                       "name": dev.get_name(), "is_switch": is_switch, "device_type": device_type}
        base_info_topo[device_id] = device_info

    build_topo(base_info_topo, controller)

    return base_info_topo


def dpid_gen():
    global dpid_begin
    dpid_begin += 1
    return str(dpid_begin)
