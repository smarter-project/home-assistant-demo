FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY homeassistant_camera_mcp.py .

ENV DANGEROUSLY_OMIT_AUTH=true 

CMD ["fastmcp","run","homeassistant_camera_mcp.py","--transport","http","--port","9000", "--host", "0.0.0.0"]

