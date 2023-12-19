# Python Environment
ARG PYTHON_VERSION=3.11.3-bullseye

# Base stage: install packages required for the app to run
FROM python:${PYTHON_VERSION} AS base

# Stage 1: Build stage
FROM base as python-build-stage
ARG BUILD_ENVIRONMENT=local

# Install system packages and # Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev

# Copy from host machine to docker container .
COPY ./requirements .  

# specifies the directory where the wheels will be stored #only builds the packages but doesnt install them
RUN pip wheel --wheel-dir /usr/src/app/wheels \
    -r local.txt


# Stage 2: Run stage
FROM base as python-run-stage
ARG BUILD_ENVIRONMENT=local

ARG APP_HOME=/app

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV BUILD_ENV local

WORKDIR /app
# commands ran after this line will be ran in the /app directory
# Install system packages and # Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    gettext \
    && apt-get purge -y --auto-remove -o \
    APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Copy wheels packages from stage1 to a new location
COPY --from=python-build-stage /usr/src/app/wheels /wheels/
# Installing the packages
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/

COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
# set up permissions for entrypoint.sh scripts #database services
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
# set up permissions for start.sh scripts #models migration
RUN chmod +x /start

# For celery and flower #check the docker-compose.yml file(local.yml)
COPY ./docker/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./docker/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower


# Copy the rest of the application code
COPY . /app

ENTRYPOINT ["/entrypoint"]
