# Minecraft Status (MCS) Service in Flask

A Flask web server for Minecraft servers monitoring.

    ./build.sh

    podman run --name mcs -p 8080:5000 -d mcs

    curl -v localhost:8080/metrics

Setup environment variables

    MC_SERVER_LIST=zeus, zeus:25566
