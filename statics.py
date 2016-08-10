TABLEMISSPRIORITY = 0

MAXPRIORITY = 6000

CLASSIFYTABLE = 0
ARPTABLE = 1
MACTABLE = 2

FLOODMAC = "ff:ff:ff:ff:ff:ff"


class CONFIG(object):
    class CONTOLLER(object):
        SECTION_NAME = "controller"
        NAME = "name"
    class NETWORK(object):
        SECTION_NAME = "network"
        TOPOFILE = "topofile"
        CONTROLLER = "controller"


class TOPO(object):
    class TAG(object):
        HOST = "host"
        SWITCH = "switch"
        INTERFACE = "interface"
        LINK = "link"
        ID = "id"
        TYPE = "type"
