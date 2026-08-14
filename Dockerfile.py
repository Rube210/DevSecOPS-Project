FROM alpine

# Use a dedicated app directory inside the container.
WORKDIR /app

# Install Python3 (no cache) and utilities.
RUN apk add --no-cache python3 py3-pip

# Copy our source code into the image.
COPY backend.py backend.py
COPY index.html index.html

# Create a non-root user with no password (-D) and home at /app.
RUN adduser -D dudleydev -h /app

# Set ownership to the created user (group name matches the user on Alpine).
RUN chown -R dudleydev:dudleydev /app

# Switch to a non-root user.
USER dudleydev

# Identify what TCP port will be used by our server.
EXPOSE 8080

# Start the server with python3 (python binary on Alpine is python3).
CMD ["python3", "backend.py"]