#!/bin/bash

# Build script for DB module data image
# This script copies the rag_edge_v2/volumes data and builds the Docker image

echo "Building DB module data image..."

# Create volumes directory in build context
mkdir -p volumes

# Copy the volumes data from rag_edge_v2
echo "Copying volumes data..."
cp -r ../../rag_edge_v2/volumes/* volumes/

# Build the Docker image
echo "Building Docker image..."
docker build -t local_mw/edge_ai/dbmodule-data:latest .

# Clean up
echo "Cleaning up build context..."
rm -rf volumes

echo "Build complete! Image: local_mw/edge_ai/dbmodule-data:latest" 