# Use mambaorg/micromamba:1.4.2-bullseye-slim as the base image
FROM mambaorg/micromamba:1.4.2-bullseye-slim

# Copy the environment.yml file into the container
COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yml /tmp/env.yaml

# Install the packages listed in environment.yml in a new conda environment and
# clean up the installation cache
RUN micromamba install -y -n base -f /tmp/env.yaml && \
    micromamba clean --all --yes

# Install the required system library libgl1-mesa-dev to support OpenGL-based
# visualization libraries
USER root
RUN apt-get update && \
    apt-get install -y libgl1-mesa-dev && \
    rm -rf /var/lib/apt/lists/*
USER $MAMBA_USER

# Copy the application source code into the container
COPY ./src /app

# Set the working directory to /app
WORKDIR /app

# Set environment variables for the application
ENV URL_BACKEND="http://localhost:8000/"
ENV PORT=8501
ENV HOST=0.0.0.0

# Start the Streamlit server
ENTRYPOINT /usr/local/bin/_entrypoint.sh \
    streamlit run app.py \
    --server.headless true \
    --server.port ${PORT} \
    --server.address ${HOST}
