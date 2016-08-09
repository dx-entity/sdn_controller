class GlobalTopoInfo():
    def __init__(self):
        self.topo = {}

    def get_topo(self, topo):
        return self.topo.get(topo, None)

    def set_topo(self, topo):
        return

    def del_topo(self, topo):
        return self.topo.pop(topo, None)

    def add_host(self, topo, host, link):
        return

    def add_switch(self, topo, host, link):
        return

    def del_host(self, topo, host):
        return

    def del_switch(self, topo, switch):
        return
