# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install poetry
RUN pip install poetry==2.0.0

# Copy project files
COPY pyproject.toml poetry.lock ./
COPY src/ ./src/
COPY tests/ ./tests/
COPY .env.template ./.env

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Expose Streamlit port
EXPOSE 8501

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Run Streamlit
CMD ["poetry", "run", "streamlit", "run", "src/app.py", "--server.address", "0.0.0.0"]
