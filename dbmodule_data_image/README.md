# DB Module Data Image

This Docker image contains the initial data for the DB modules (FaceDB and SensorDB) and is used to populate the persistent volumes.

## Structure

The image contains the following data structure:
```
/data/
├── FaceDB/
│   ├── known_people/
│   └── vectorDB/
└── SensorDB/
    ├── SensorData/
    └── InfluxDB_Data/
```

## Building the Image

To build the image with your data:

```bash
cd dbmodule_data_image
./build.sh
```

This script will:
1. Copy the data from `../rag_edge_v2/volumes/` to the build context
2. Build the Docker image as `local_mw/edge_ai/dbmodule-data:latest`
3. Clean up the build context

## Usage

The image is used by the `dbmodule_data_init.yaml` job to copy data to persistent volumes:

- `/data/FaceDB/known_people/*` → `/facedb-known-people/`
- `/data/FaceDB/vectorDB/*` → `/facedb-vector-db/`
- `/data/SensorDB/SensorData/*` → `/sensordb-data/`
- `/data/SensorDB/InfluxDB_Data/*` → `/influxdb-data/`

## Updating Data

To update the data:

1. Modify your data in `../rag_edge_v2/volumes/`
2. Rebuild the image: `./build.sh`
3. Delete the old job: `kubectl delete job dbmodule-data-init`
4. Reapply the job: `kubectl apply -f ../dbmodule_data_init.yaml`

## Benefits

- **Self-contained**: All data is packaged in the image
- **Versioned**: Each image version contains specific data
- **Reproducible**: Same data every time the job runs
- **No external dependencies**: No need for separate volume mounting 