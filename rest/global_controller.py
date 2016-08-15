import json

from wsgi_app import BaseController
from webob import Response

from global_data_access.global_net_info import GlobalNetInfo


def rest_command(func):
    def _rest_conmmand(*args, **kwargs):
        msg = func(*args, **kwargs)
        return Response(content_type="application/json",
                        body=json.dumps(msg))

    return _rest_conmmand


class GlobalController(BaseController):
    def __init__(self, req):
        super(GlobalController, self).__init__(req)

    @rest_command
    def get_net(self, *args, **kwargs):
        gni = GlobalNetInfo.get_instance()
        res = gni.get_net()
        if not res:
            return "no net is running"
        else:
            return [[name for name in node] for node in res]

    @rest_command
    def get_net_node(self, *args, **kwargs):
        gni = GlobalNetInfo.get_instance()
        res = gni.get_net()
        node_name = kwargs.get("nodename", None)
        if not res or not node_name:
            return "no net is running"
        return {"node_ip": str(res[0].get(node_name).IP())}

    @rest_command
    def node_cmd(self, *args, **kwargs):
        cmd = kwargs.get("cmd", None)
        nodename = kwargs.get("nodename", None)
        timesout = kwargs.get("timesout", 1000)
        if "ping" in cmd:
            print "ping"
        gni = GlobalNetInfo.get_instance()
        res = gni.get_net()
        if not res or not nodename:
            return "info wrong"
        node = res[0].get(nodename)
        data = node.cmd(cmd)
        if node.waiting:
            data = self.node.monitor(timesout)
        return data
