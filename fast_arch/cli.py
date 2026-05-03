from fast_arch.prompts.prompts import prompt_project_config

from fast_arch.generator.gen import generate_project

from fast_arch.utils.fs import delete_dir

def main():
    project_config = prompt_project_config()
    try:
        if not generate_project(project_config):
            raise Exception("Project generation failed.")
    except Exception as e:
        print(f"Error: {e}")
        print("Cleaning up generated files...")
        if delete_dir(project_config.name):
            print("Cleanup successful.")
        else:
            print("Cleanup failed. Please check the project directory and remove it manually if necessary.")
        exit(1)
            

if __name__ == "__main__":
    main()

