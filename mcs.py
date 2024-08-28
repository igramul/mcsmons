import os

from flask import Flask
from mcstatus import JavaServer

import version

app = Flask(__name__)

counter = 0
server_list = [x.strip() for x in os.getenv('MC_SERVER_LIST').split(',')]


@app.route('/')
def root():
    global counter
    ans = f'Version: {version.version}. Counter: {counter}. Minecraft Server List {server_list}'
    counter += 1
    return ans


@app.route('/metrics')
def metrics():
    global counter
    ans = ''
    for server_name in server_list:
        server = JavaServer.lookup(server_name)
        try:
            s = server.status()
        except ConnectionRefusedError as e:
            print(f'Minecraft server error: {e}')
            ans += 'server_online{server_name="%s"} %s\n' % (server_name, 0)
        else:
            ans += 'server_online{server_name="%s"} %s\n' % (server_name, 1)
            ans += 'minecraft_latency{server="%s"} %s\n' % (s.description, s.latency)
            ans += 'minecraft_version{server="%s"} %s\n' % (s.description, s.version.name)
            ans += 'minecraft_users_max{server="%s"} %s\n' % (s.description, s.players.max)
            ans += 'minecraft_users_online{server="%s"} %s\n' % (s.description, s.players.online)
            if s.players.sample:
                for player in s.players.sample:
                    ans += 'minecraft_players{server="%s", name="%s", uuid="%s"} 1\n' % (s.description, player.name, player.uuid)
    ans += 'minecraft_mcs_count{version="%s"} %s\n' % (version.version, counter)
    counter += 1
    return ans


if __name__ == '__main__':
    app.run()
