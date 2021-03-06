import sys

import eventlet
import ConfigParser
from ryu.cmd.manager import main as ryu_manager
import daemon

import statics as data
import topo_generater.topo_analyzer as topo


def main():
    config = ConfigParser.ConfigParser()
    config_file = sys.argv[1] if len(sys.argv) > 1 else "config.ini"
    try:
        config.readfp(open(config_file, 'r'))
        controller_name = config.get(data.CONFIG.CONTOLLER.SECTION_NAME, data.CONFIG.CONTOLLER.NAME)
        app_name = controller_name.split(',')
    except Exception, e:
        print e
    # add eventlet pool
    pool = eventlet.GreenPool()

    # start sdn controller
    # pool.spawn(ryu_manager, app_name)

    # start build network
    topofile = config.get(data.CONFIG.NETWORK.SECTION_NAME, data.CONFIG.NETWORK.TOPOFILE)
    controller = config.get(data.CONFIG.NETWORK.SECTION_NAME, data.CONFIG.NETWORK.CONTROLLER)
    cli = config.get(data.CONFIG.NETWORK.SECTION_NAME, data.CONFIG.NETWORK.CLI)
    pool.spawn(topo.xml_analyzer, topofile=topofile, controller=controller, cli=cli)

    # start rest if needed
    rest = config.get(data.CONFIG.REST.SECION_NAME, data.CONFIG.REST.START_REST) is data.TRUE
    if rest:
        from rest.wsgi_server import start_rest_server
        start_rest_server()

    pool.waitall()


if __name__ == '__main__':
    main()
