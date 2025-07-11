# Minecraft Server Monitoring Service (MCSMONS) Service in Flask

A Flask web server for Minecraft Server monitoring with Prometheus.

    ./build.sh

    podman run --name mcsmons -p 8080:5000 -d mcsmons

    curl -v localhost:8080/metrics

Setup environment variables

    MC_SERVER_LIST=zeus, zeus:25566

## Grafana Dashboard

See [grafana](./grafana) for dashboard json file and screen shot.