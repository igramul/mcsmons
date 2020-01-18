
from flask import Flask

from mcstatus import MinecraftServer

app = Flask(__name__)

@app.route('/')
@app.route('/query')
def root():
    # If you know the host and port, you may skip this and use MinecraftServer("example.org", 1234)
    server = MinecraftServer.lookup('gaia')

    # 'query' has to be enabled in a servers' server.properties file.
    # It may give more information than a ping, such as a full player list or mod information.
    query = server.query()
    return 'The server has the following players online: {0}'.format(', '.join(query.players.names))


@app.route('/status')
def status():
    # If you know the host and port, you may skip this and use MinecraftServer("example.org", 1234)
    server = MinecraftServer.lookup('gaia')

    # 'status' is supported by all Minecraft servers that are version 1.7 or higher.
    status = server.status()
    return 'The server has {0} players and replied in {1} ms'.format(status.players.online, status.latency)


@app.route('/ping')
def print():
    server = MinecraftServer.lookup('gaia')

    # 'ping' is supported by all Minecraft servers that are version 1.7 or higher.
    # It is included in a 'status' call, but is exposed separate if you do not require the additional info.
    latency = server.ping()
    return 'The server replied in {0} ms'.format(latency)


if __name__ == '__main__':
    app.run()
