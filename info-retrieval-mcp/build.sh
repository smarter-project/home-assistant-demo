#!/bin/bash

# Build script for info-retrieval-mcp Docker image

set -e

echo "Building info-retrieval-mcp Docker image..."

# Build the Docker image
docker build -t local_mw/edge_ai/info-retrieval-mcp:latest .

echo "Docker image built successfully!"
echo "Image: local_mw/edge_ai/info-retrieval-mcp:latest"

# # Optional: Test the image locally
# if [ "$1" = "--test" ]; then
#     echo "Testing the image locally..."
#     docker run --rm -it \
#         --env DANGEROUSLY_OMIT_AUTH=true \
#         --env MQTT_BROKER=localhost \
#         --env MQTT_PORT=1883 \
#         local_mw/edge_ai/info-retrieval-mcp:latest
# fi 