FROM alpine:latest

# Install necessary tools
RUN apk add --no-cache python3 py3-pip

# Create directories for the data
RUN mkdir -p /data/FaceDB/known_people
RUN mkdir -p /data/FaceDB/vectorDB
RUN mkdir -p /data/SensorDB/SensorData
RUN mkdir -p /data/SensorDB/InfluxDB_Data

# Copy the data from the build context
COPY volumes/FaceDB/known_people/ /data/FaceDB/known_people/
COPY volumes/FaceDB/vectorDB/ /data/FaceDB/vectorDB/
COPY volumes/SensorDB/SensorData/ /data/SensorDB/SensorData/
COPY volumes/SensorDB/InfluxDB_Data/ /data/SensorDB/InfluxDB_Data/

# Create a script to copy data to persistent volumes
RUN echo '#!/bin/sh' > /copy_data.sh && \
    echo 'echo "Copying FaceDB known_people data..."' >> /copy_data.sh && \
    echo 'cp -r /data/FaceDB/known_people/* /facedb-known-people/ 2>/dev/null || echo "No known_people data found"' >> /copy_data.sh && \
    echo 'echo "Copying FaceDB vectorDB data..."' >> /copy_data.sh && \
    echo 'cp -r /data/FaceDB/vectorDB/* /facedb-vector-db/ 2>/dev/null || echo "No vectorDB data found"' >> /copy_data.sh && \
    echo 'echo "Copying SensorDB data..."' >> /copy_data.sh && \
    echo 'cp -r /data/SensorDB/SensorData/* /sensordb-data/ 2>/dev/null || echo "No SensorData found"' >> /copy_data.sh && \
    echo 'echo "Copying InfluxDB data..."' >> /copy_data.sh && \
    echo 'cp -r /data/SensorDB/InfluxDB_Data/* /influxdb-data/ 2>/dev/null || echo "No InfluxDB_Data found"' >> /copy_data.sh && \
    echo 'echo "Data copy complete!"' >> /copy_data.sh && \
    chmod +x /copy_data.sh

# Set the default command
CMD ["/copy_data.sh"] 