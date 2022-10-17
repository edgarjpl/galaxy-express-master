#!/bin/bash
# Be it for local development or production, this script provides a
# consistent entrypoint for running the service in a container.
#
# The following environment variables can be set to change behavior:
#
# * BASEPLATE_CONFIG_PATH: Full path to your service's
#      baseplate config file.

baseplate_config_path=${BASEPLATE_CONFIG_PATH:-"/src/example.ini"}
echo "Running baseplate service with config ${baseplate_config_path}"
exec baseplate-serve --bind 0.0.0.0:9090 "${baseplate_config_path}"
