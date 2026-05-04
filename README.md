# FastArchX

FastArchX is a Python-based CLI tool designed to help you quickly generate and explore various software architecture templates for your projects. It provides ready-to-use architecture blueprints and utilities to streamline your project setup and maintain best practices.

## Features
- Generate project structures based on popular software architectures (e.g., Clean, Hexagonal, Layered, Modular Monolith, MVC)
- Easily browse architecture documentation and JSON schemas
- Extensible and modular codebase for adding new architectures
- Utility functions for file system operations and JSON reading

## Project Structure
```
fastarchx/
    __init__.py
    cli.py                # CLI entry point
    architectures/        # Architecture templates and docs
        arch.json
        Clean.md
        Hexagonal.md
        Layered.md
        Modular Monolith.md
        MVC.md
    core/
        __init__.py
        config.py         # Core configuration
    generator/
        gen.py            # Project generator logic
    prompts/
        __init__.py
        prompts.py        # CLI prompts and interactions
    schema/
        arch_schema.py    # Architecture JSON schema
    utils/
        __init__.py
        fs.py             # File system utilities
        json_reader.py    # JSON reading utilities
pyproject.toml            # Project metadata and dependencies
```

## Getting Started

### Prerequisites
- Python 3.8+
- (Optional) Virtual environment (recommended)

### Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd fast-arch
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -e .
   ```

### Usage
Run the CLI tool:
```bash
python -m fastarchx.cli
```

Follow the prompts to select and generate a project architecture.

You can also install it using pip
```bash
pip install fastarchx
```
and then run the command `fastarchx` in your terminal.



## Contributing
Contributions are welcome! Please open issues or submit pull requests for new features, bug fixes, or improvements.

