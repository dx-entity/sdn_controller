# Copyright (C) 2013 Nippon Telegraph and Telephone Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from ryu.base import app_manager
from ryu.controller import dpset
from ryu.controller import ofp_event

from ryu.controller.handler import set_ev_cls
from ryu.controller.handler import MAIN_DISPATCHER
from ryu.controller.handler import CONFIG_DISPATCHER

from ryu.lib import dpid as dpid_lib

from ryu.ofproto import ofproto_v1_0
from ryu.ofproto import ofproto_v1_2
from ryu.ofproto import ofproto_v1_3

from utils.log_formatter import LogFormat
from utils.global_data import GlobalData
from core.flow_manage import FlowManage
from core.packet_analyser import PacketRouter


class MyDemo(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION,
                    ofproto_v1_2.OFP_VERSION,
                    ofproto_v1_3.OFP_VERSION]

    _CONTEXTS = {'dpset': dpset.DPSet}

    def __init__(self, *args, **kwargs):
        super(MyDemo, self).__init__(*args, **kwargs)

        self.logger = LogFormat().getLogger(self.__class__.__name__)

        self.gd = GlobalData.get_instance()

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def handle_switch_features(self, ev):
        if not ev.msg.datapath.ofproto.OFP_VERSION in self.OFP_VERSIONS:
            raise NameError

        FlowManage.get_flow_concoller('add_default_flow')(ev.msg.datapath)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def handle_in_packets(self, ev):
        if not ev.msg.datapath.ofproto.OFP_VERSION in MyDemo.OFP_VERSIONS:
            raise NameError

        msg = ev.msg

        device = self.gd.get_device(ev.msg.datapath.id)
        if device:
            device.handle_message(msg)
        PacketRouter.route_pkt(msg)

    @set_ev_cls(dpset.EventDP, MAIN_DISPATCHER)
    def dp_connect_in(self, ev):
        dpid = dpid_lib.dpid_to_str(ev.dp.id)
        dp = ev.dp
        if ev.enter:
            self.gd.register_device(dpid, dp)
            self.logger.info("ovs has connected to controller, id: %s" % (dpid))
        else:
            self.gd.unregister_device(dpid)
            self.logger.info("ovs has disconnected to controller, id: %s" % (dpid))
