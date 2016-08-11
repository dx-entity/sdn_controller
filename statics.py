TABLEMISSPRIORITY = 0

MAXPRIORITY = 6000

CLASSIFYTABLE = 0
ARPTABLE = 1
MACTABLE = 2

FLOODMAC = "ff:ff:ff:ff:ff:ff"


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
