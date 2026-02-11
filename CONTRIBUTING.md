# Contributing to Redbook Cover Generator

This document outlines the workflow for contributing to this project.

## Development Setup

1.  **Clone the repository**:

    ```bash
    git clone https://github.com/The-AlexLiu/redbook-cover-generator.git
    cd redbook-cover-generator
    ```

2.  **Install Dependencies**:

    ```bash
    pip install -r requirements.txt
    playwright install chromium
    ```

3.  **Run Development Server**:
    ```bash
    python3 server.py
    ```

## Git Workflow (Best Practices)

1.  **Create a Branch**:
    Never push directly to `main`. Create a feature branch:

    ```bash
    git checkout -b feature/new-style
    ```

2.  **Commit Often**:
    Make small, atomic commits with clear messages:

    ```bash
    git commit -m "feat: add new gradient background style"
    ```

3.  **Push and Pull Request**:
    Push your branch and create a Pull Request (PR) on GitHub for review.

## Code Style

- Python: Follow PEP 8 guidelines.
- HTML/CSS: Keep structure clean and use Tailwind utility classes where possible.
