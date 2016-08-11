from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI

from global_data_access.global_net_info import GlobalNetInfo


class CustomTopo(Topo):
    # def __init__(self, *args, **params):
    #     super(CustomTopo, self).__init__(args, params)

    def build(self, *args, **params):
        if len(args) < 1:
            return
        topo_info = args[0]
        device_record = {}
        link_record = []
        for device_id, info in topo_info.iteritems():
            # print device_id
            # print info
            if not info["is_switch"]:
                device = self.addHost(info["name"])
            else:
                device = self.addSwitch(name=info["name"], dpid=info["dpid"])
            device_record[device_id] = device
            for link in info["link"]:
                if set(link) not in link_record:
                    link_record.append(set(link))

        for l in link_record:
            self.addLink(device_record[l.pop()], device_record[l.pop()])


def build_topo(kwargs):
    topoinfo = kwargs.get("base_info_topo", None)
    if not topoinfo:
        return
    topo = CustomTopo(topoinfo)

    net = Mininet(topo=topo, controller=RemoteController)
    net.start()
    gni = GlobalNetInfo.get_instance()
    gni.store_net(net)
    # if kwargs.get("cli", None):
    #     CLI(net)
