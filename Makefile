# System Python
PYTHON := python3
BIN := ./venv/bin
VERSION := $(shell git describe)
MC_SERVER_LIST := "192.168.0.30, 192.168.0.30:25566"

.PHONY: start
start: image
	podman stop -i mcs
	podman rm -i mcs
	podman run -d --restart=always --name mcs -p 8080:5000 -e MC_SERVER_LIST=$(MC_SERVER_LIST) mcs:$(VERSION)

.PHONY: image
image: venv version.py
	podman build . -t mcs:$(VERSION)

.PHONY: version.py
version.py:
	echo version = \"$(VERSION)\" > $@
	echo commit = \"`git rev-parse HEAD`\" >> $@
	echo commit_short = \"`git rev-parse --short HEAD`\" >> $@

venv:
	$(PYTHON) -m venv venv
	$(BIN)/pip install -r requirements.txt

.PHONY: venv-update
venv-update: venv
	$(BIN)/pip install --upgrade pip setuptools

.PHONY:
clean:
	rm -f version.py

.PHONY: venv-clean
venv-clean:
	rm -rf venv

.PHONY: clean-all
clean-all: clean venv-clean

.PHONY: test
test:
	$(BIN)/$(PYTHON) -m unittest discover tests "*_test.py"
