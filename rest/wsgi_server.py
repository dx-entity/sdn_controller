import eventlet
import eventlet.wsgi

from wsgi_app import WSGIApplication
from global_controller import GlobalController

"""
This class implement a simple wsgi server, future maybe better
"""


class WsgiServer(object):
    def __init__(self, listen_info=None, handle=None):
        if not listen_info:
            listen_info = ("192.168.122.34", 8010)
        self.server = eventlet.listen(listen_info)
        self.handle = handle

    def serve_forever(self):
        eventlet.wsgi.server(self.server, self.handle)

    def __call__(self):
        self.serve_forever()


def add_url_pattern(handle):
    mapper = handle.mapper
    path_net = "/global/net"
    mapper.connect("global", path_net, controller=GlobalController,
                   action='get_net', conditions=dict(method=["GET"]))

    path_net_node = "/global/net/{nodename}"
    mapper.connect("global", path_net_node, controller=GlobalController,
                   action='get_net_node', conditions=dict(method=["GET"]))

    path_node_cmd = "/global/net/{nodename}/{cmd}"
    mapper.connect("global", path_node_cmd, controller=GlobalController,
                   action='node_cmd', conditions=dict(method=["GET"]))


def start_rest_server():
    handle = WSGIApplication()
    add_url_pattern(handle=handle)
    ws = WsgiServer(handle=handle)
    ws()
