# Set the base image for the new image
FROM mambaorg/micromamba:1.4.2-bullseye-slim

# Copy the environment.yml file to /tmp/env.yaml
# and set the owner to $MAMBA_USER
COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yml /tmp/env.yaml

# Install the environment specified in /tmp/env.yaml
# and then clean up the installation cache
RUN micromamba install -y -n base -f /tmp/env.yaml && \
    micromamba clean --all --yes

# Set environment variables for the server
ENV PORT=8000
ENV HOST=0.0.0.0

# Copy the application source code to /app directory
COPY ./src /app

# Set /app as the working directory
WORKDIR /app

# Cache the predict model by running it once
ARG MAMBA_DOCKERFILE_ACTIVATE=1
RUN python -m model.predict 

# Run the server using the _entrypoint.sh script
# and specify the port and host using the environment variables
ENTRYPOINT /usr/local/bin/_entrypoint.sh \
    uvicorn main:app \
    --port ${PORT} \
    --host ${HOST}
