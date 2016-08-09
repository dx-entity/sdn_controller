import sys

import eventlet
import ConfigParser
from ryu.cmd.manager import main as ryu_manager

import statics as data


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
    pool.spawn(ryu_manager, app_name)

    pool.waitall()


if __name__ == '__main__':
    main()
