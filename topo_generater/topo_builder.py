from mininet.topo import Topo


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
            if info["is_switch"]:
                device = self.addHost(info["name"])
            else:
                device = self.addSwitch(name=info["name"], dpid=info["dpid"])
            device_record[device_id] = device
            for link in info["link"]:
                if set(link) not in link_record:
                    link_record.append(set(link))
                    
        for l in link_record:
            self.addLink(device_record[l.pop()], device_record[l.pop()])


def build_topo(topoinfo):
    topo = CustomTopo(topoinfo)
