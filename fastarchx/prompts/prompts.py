import questionary
from fastarchx.core.config import ProjectConfig

def prompt_project_config() -> ProjectConfig:
    name = questionary.text("Project name:").ask()
    if not name:
        print("Project name cannot be empty.")
        exit(1)

    arch = questionary.select(
        "Select architecture:",
        choices=["Layered", "Clean", "Hexagonal", "Modular Monolith", "MVC"]
    ).ask()
    if not arch:
        print("Architecture selection is required.")
        exit(1)

    features = questionary.checkbox(
        "Select features:",
        choices=["Database", "Authentication", "Testing", "Docker", "Environment Variables"]
    ).ask()
    
    return ProjectConfig(name=name, arch=arch, features=features)
