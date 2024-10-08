# Use an official Python runtime as a parent image
FROM python:3.11-slim as base

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install poetry
RUN pip install poetry

# Install main project dependencies by default
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-dev

# Create a new stage for development dependencies
FROM base as development

# Install development dependencies
RUN poetry install --no-interaction --no-ansi

# Run app.py when the container launches
CMD ["python", "-m", "bot"]
