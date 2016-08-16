TABLEMISSPRIORITY = 0
MACTABLEPRIORITY = 10

MAXPRIORITY = 6000

CLASSIFYTABLE = 0
ARPTABLE = 1
MACTABLE = 2

FLOODMAC = "ff:ff:ff:ff:ff:ff"

PORTACCESS = "access"
PORTTRUNK = "trunk"
PORTHYBRID = "hybrid"

VLANID_NONE = 0
VLANID_MIN = 2
VLANID_MAX = 4094

TRUE = "True"
FALSE = "False"


class CONFIG:
    class CONTOLLER:
        SECTION_NAME = "controller"
        NAME = "name"

    class NETWORK:
        SECTION_NAME = "network"
        TOPOFILE = "topofile"
        CONTROLLER = "controller"
        CLI = "cli"

    class REST:
        SECION_NAME = "restful"
        START_REST = "startrest"


class TOPO:
    class TAG:
        HOST = "host"
        SWITCH = "switch"
        INTERFACE = "interface"
        LINK = "link"
        ID = "id"
        TYPE = "type"
