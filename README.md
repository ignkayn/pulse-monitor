# pulse-monitor
Lightweight service health monitor with automated CI checks and clean architecture.
# Pulse Monitor

![CI Status](https://github.com)
![License: MIT](https://shields.io)

A modular, zero-dependency service health checker built with clean architecture and automated testing.

## Project Structure

```text
├── .github/
│   ├── workflows/ci.yml    # Automated test pipeline
│   └── pull_request_template.md
├── src/
│   └── monitor.py          # Core health-check logic
└── tests/
    └── test_monitor.py     # Unit test suite
```

## Quick Start

```bash
python3 src/monitor.py
```
