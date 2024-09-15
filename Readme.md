# Minecraft Server Monitoring Service (MCSMONS) Service in Flask

A Flask web server for Minecraft Server monitoring.

    ./build.sh

    podman run --name mcsmons -p 8080:5000 -d mcsmons

    curl -v localhost:8080/metrics

Setup environment variables

    MC_SERVER_LIST=zeus, zeus:25566
