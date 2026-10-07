# Employee Management System

A command-line employee management application written in Python. It lets you add, update, remove, search, and list employees, and view employee counts by department along with salary statistics. Employee records are stored as JSON in `data/records.json`.

## Requirements

- Python 3.13 or newer
- [Poetry](https://python-poetry.org/)

## Install and run

From the project directory, install the dependencies and start the interactive menu:

```bash
poetry install
poetry run python main.py
```

Choose an option from the menu and follow the prompts. The application reads and saves its employee records in `data/records.json`.

## Run the tests

```bash
poetry run pytest
```
