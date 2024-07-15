from flask import Flask
from mcstatus import JavaServer

app = Flask(__name__)

server_list = ['zeus', 'zeus:25566']


@app.route('/')
def root():
    return f'The Minecraft Server Name {server_list}'


@app.route('/metrics')
def metrics():    # If you know the host and port, you may skip this and use MinecraftServer("example.org", 1234)
    ans = ''
    for server_name in server_list:
        server = JavaServer.lookup(server_name)
        s = server.status()
        ans += 'minecraft_latency{server="%s"} %s\n' % (s.description, s.latency)
        ans += 'minecraft_version{server="%s"} %s\n' % (s.description, s.version.name)
        ans += 'minecraft_users_max{server="%s"} %s\n' % (s.description, s.players.max)
        ans += 'minecraft_users_online{server="%s"} %s\n' % (s.description, s.players.online)
        if s.players.sample:
            for player in s.players.sample:
                ans += 'minecraft_players{server="%s", name="%s", uuid="%s"} 1\n' % (s.description, player.name, player.uuid)
    return ans


if __name__ == '__main__':
    app.run()
