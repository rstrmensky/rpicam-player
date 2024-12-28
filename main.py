from lib.streamer import Streamer
from configparser import ConfigParser
from subprocess import Popen
import time

streams = ConfigParser()
streams.read('conf/stream.ini')

time.sleep(30)

try:
    for item in streams.sections():
        player = Streamer()
        command = player.start(streams[item]['url'], streams[item]['width'], streams[item]['height'], streams[item]['x'], streams[item]['y'])
        Popen(command)

except KeyboardInterrupt:
    pass