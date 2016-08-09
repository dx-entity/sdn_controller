from utils.global_data import GlobalData
from utils.log_formatter import LogFormat
import statics as data

logger = LogFormat().getLogger("flow_manage")


def add_default_flow(dp):
    """
    currently default action is only table-miss, and send to controllers
    :param dpid:
    :return:
    """

    datapath = dp
    ofproto = dp.ofproto

    rule_list = [[data.CLASSIFYTABLE, data.MACTABLE],
                 [data.ARPTABLE, data.MACTABLE], [data.MACTABLE, ofproto.OFPP_CONTROLLER]]

    install_table_miss(datapath, rule_list)

    ofproto = datapath.ofproto
    parser = datapath.ofproto_parser

    match_table_miss = parser.OFPMatch()
    actions_table_miss = [parser.OFPInstructionGotoTable(data.MACTABLE)]

    add_flow(datapath, data.TABLEMISSPRIORITY, match_table_miss, actions_table_miss, table_id=data.CLASSIFYTABLE)


def install_table_miss(dp, rule_list):
    datapath = dp

    ofproto = datapath.ofproto
    parser = datapath.ofproto_parser

    match_table_miss = parser.OFPMatch()

    for rule in rule_list:
        if rule[1] != ofproto.OFPP_CONTROLLER:
            inst = [parser.OFPInstructionGotoTable(rule[1])]
        else:

            actions = [parser.OFPActionOutput(rule[1], ofproto.OFPCML_NO_BUFFER)]
            inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]

        add_flow(datapath, data.TABLEMISSPRIORITY, match_table_miss, inst, table_id=rule[0])
    return


def add_flow(datapath, priority, match, inst, table_id=0):
    parser = datapath.ofproto_parser

    mod = parser.OFPFlowMod(datapath=datapath, priority=priority,
                            match=match, instructions=inst, table_id=table_id)
    datapath.send_msg(mod)


class FlowManage(object):
    _manage_type = {
        'add_default_flow': add_default_flow,
        'add_flow': add_flow
    }

    @staticmethod
    def get_flow_concoller(con_name):
        return FlowManage._manage_type.get(con_name, None)
