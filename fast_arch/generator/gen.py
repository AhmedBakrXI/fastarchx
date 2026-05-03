from fast_arch.utils.fs import create_dir, create_file
from fast_arch.core.config import ProjectConfig
from fast_arch.schema.arch_schema import ArchitectureConfig
from fast_arch.utils.json_reader import read_arch_config_json


def generate_gitignore(project_name: str) -> bool:
    gitignore_content = """__pycache__/
*.pyc
*.pyo
*.pyd
env/
venv/
ENV/
venv.bak/
*.swp
.DS_Store
.idea/
.vscode/
*.log
"""
    return create_file(f"{project_name}/.gitignore", gitignore_content)


def generate_project(project_config: ProjectConfig) -> bool:
    app_file_content = (
        f"from fastapi import FastAPI\n\napp = FastAPI(title='{project_config.name}')"
    )

    # Create project directory
    if not create_dir(project_config.name):
        print("Failed to create project directory.")
        return False
    # Create main app file
    app_file_path = f"{project_config.name}/app.py"
    if not create_file(app_file_path, app_file_content):
        print("Failed to create app.py file.")
        return False

    arch_config: ArchitectureConfig = read_arch_config_json()
    arch = next(
        (a for a in arch_config.architectures if a.name == project_config.arch), None
    )
    if not arch:
        print(f"Architecture {project_config.arch} not found in config.")
        return False
    # Create folders based on selected architecture
    for folder in arch.folders:
        if not create_dir(f"{project_config.name}/{folder}"):
            print(f"Failed to create folder: {folder}")
            return False
    print(
        f"Project '{project_config.name}' generated successfully with {project_config.arch} architecture."
    )

    for file in arch.files:
        file_path = f"{project_config.name}/{file}"
        if not create_file(file_path):
            print(f"Failed to create file: {file}")
            return False
    print("All files created successfully.")

    for feature in project_config.features:
        if feature.lower() in arch.features:
            feature_info = arch.features[feature.lower()]
            for file in feature_info.files:
                file_path = f"{project_config.name}/{file}"
                if not create_file(file_path):
                    print(f"Failed to create feature file: {file}")
                    return False

    for feature in project_config.features:
        if feature.lower() == "docker":
            docker_content = 'FROM python:3.9-slim\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\nCMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]'
            create_file(f"{project_config.name}/Dockerfile", docker_content)
            create_file(f"{project_config.name}/docker-compose.yml")

        if feature.lower() == "environment variables":
            env_content: str = ""
            env_content += "DATABASE_URL=\n"
            env_content += "USERNAME=\n"
            env_content += "PASSWORD=\n"
            create_file(f"{project_config.name}/.env", env_content)
            create_file(f"{project_config.name}/.env.example", env_content)

    create_file(f"{project_config.name}/requirements.txt", "fastapi\nuvicorn\n")
    generate_gitignore(project_config.name)
    print("All feature files created successfully.")
    return True
