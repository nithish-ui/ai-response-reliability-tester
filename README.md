# AI Response Reliability Tester

A Python-based automation testing framework designed to evaluate the reliability,
consistency, and robustness of AI/NLP systems under edge-case inputs.

## Features
- Automated response consistency testing
- Latency threshold validation
- Edge-case and noisy input handling
- Mock LLM simulation (no external APIs)

## Tech Stack
- Python
- PyTest
- Requests
- Logging

## Use Case
Useful for testing AI chatbots, RAG systems, and NLP pipelines for production readiness.

## How to Run
pip install -r requirements.txt

pytest

pytest --json-report --json-report-file=report.json

