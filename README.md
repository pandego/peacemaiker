# Viewpoint Comparison Tool

A Streamlit application that helps compare different viewpoints on a situation using Pydantic.AI capabilities. The app facilitates understanding and mediating between different perspectives by collecting structured responses and generating AI-powered summaries.

## Features

- Dual viewpoint input interface with example responses
- Structured question format for thorough perspective analysis
- Parallel viewpoint summary generation using asyncio for improved performance
- AI-powered summary generation using OpenAI GPT models
- Session state management for response persistence
- Docker support for easy deployment

## Prerequisites

- Python 3.11+
- Poetry 2.0+
- Docker (optional)

## Setup

1. Clone the repository
2. Copy `.env.template` to `.env` and add your OpenAI API key:
```bash
cp .env.template .env
```

3. Install dependencies with Poetry:
```bash
poetry install --no-root
```

## Development

### Running the Application

```bash
poetry run streamlit run src/app.py
```

### Running Tests

```bash
poetry run pytest tests/
```

### Code Quality

Run the following commands to ensure code quality:

```bash
# Format code
poetry run black src/ tests/
poetry run isort src/ tests/

# Check code quality
poetry run flake8 src/ tests/
poetry run mypy src/ tests/
poetry run pylint src/ tests/

# Run tests with coverage
poetry run pytest --cov=src tests/
```

## Docker

### Building the Image

```bash
docker build -t viewpoint-comparison .
```

### Running the Container

```bash
docker run -p 8501:8501 -e OPENAI_API_KEY=your_api_key viewpoint-comparison
```

Then visit `http://localhost:8501` in your browser.

## Example Usage

The app comes with pre-filled examples of a cross-cultural holiday dinner discussion between an American and Portuguese couple. You can:

1. Review the example responses in both viewpoints
2. Modify the responses or input your own scenario
3. Click "Generate Summaries" to get AI-powered analysis of both perspectives

## Contributing

1. Ensure you have all development dependencies installed
2. Make your changes
3. Run all code quality checks and tests
4. Submit a pull request
