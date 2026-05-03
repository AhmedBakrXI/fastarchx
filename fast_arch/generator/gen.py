from fast_arch.utils.fs import create_dir, create_file
from fast_arch.core.config import ProjectConfig
from fast_arch.schema.arch_schema import Architecture, ArchitectureConfig
from fast_arch.utils.json_reader import read_arch_config_json


GITIGNORE_CONTENT = """__pycache__/
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

DOCKERFILE_CONTENT = """FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
"""


def generate_gitignore(project_name: str) -> bool:
    return create_file(f"{project_name}/.gitignore", GITIGNORE_CONTENT)


def create_base_project(project_config: ProjectConfig) -> bool:
    if not create_dir(project_config.name):
        print("Failed to create project directory.")
        return False

    app_content = f"from fastapi import FastAPI\n\napp = FastAPI(title='{project_config.name}')"
    if not create_file(f"{project_config.name}/app.py", app_content):
        print("Failed to create app.py file.")
        return False

    return True


def get_architecture(project_config: ProjectConfig) -> Architecture:
    arch_config = read_arch_config_json()

    for arch in arch_config.architectures:
        if arch.name == project_config.arch:
            return arch

    raise ValueError(f"Architecture '{project_config.arch}' not found")

def create_arch_structure(project_name: str, arch) -> bool:
    for folder in arch.folders:
        if not create_dir(f"{project_name}/{folder}"):
            print(f"Failed to create folder: {folder}")
            return False

    for file in arch.files:
        if not create_file(f"{project_name}/{file}"):
            print(f"Failed to create file: {file}")
            return False

    return True


def create_feature_files(project_config: ProjectConfig, arch) -> bool:
    for feature in project_config.features:
        feature_key = feature.lower()

        if feature_key in arch.features:
            for file in arch.features[feature_key].files:
                if not create_file(f"{project_config.name}/{file}"):
                    print(f"Failed to create feature file: {file}")
                    return False

    return True


def handle_special_features(project_config: ProjectConfig) -> None:
    project_name = project_config.name
    features = {f.lower() for f in project_config.features}

    if "docker" in features:
        create_file(f"{project_name}/Dockerfile", DOCKERFILE_CONTENT)
        create_file(f"{project_name}/docker-compose.yml")

    if "environment variables" in features:
        env_content = ""
        if "database" in features:
            env_content += "DATABASE_URL=\nUSERNAME=\nPASSWORD=\n"

        create_file(f"{project_name}/.env", env_content)
        create_file(f"{project_name}/.env.example", env_content)


def finalize_project(project_name: str) -> None:
    create_file(f"{project_name}/requirements.txt", "fastapi\nuvicorn\n")
    generate_gitignore(project_name)


def generate_project(project_config: ProjectConfig) -> bool:
    if not create_base_project(project_config):
        return False

    arch = get_architecture(project_config)
    if not arch:
        print(f"Architecture {project_config.arch} not found in config.")
        return False

    if not create_arch_structure(project_config.name, arch):
        return False

    print(
        f"Project '{project_config.name}' generated successfully with {project_config.arch} architecture."
    )

    if not create_feature_files(project_config, arch):
        return False

    handle_special_features(project_config)
    finalize_project(project_config.name)

    print("Project setup completed successfully.")
    return True