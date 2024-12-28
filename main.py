from lib.streamer import Streamer
from configparser import ConfigParser
from subprocess import Popen

streams = ConfigParser()
streams.read('conf/stream.ini')

try:
    for item in streams.sections():
        player = Streamer()
        command = player.start(streams[item]['url'], streams[item]['width'], streams[item]['height'], streams[item]['x'], streams[item]['y'])
        Popen(command)

except KeyboardInterrupt:
    pass