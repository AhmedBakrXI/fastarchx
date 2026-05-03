import os

def create_dir(path: str) -> bool:
    """Creates a directory if it doesn't exist."""
    try:
        os.makedirs(path, exist_ok=True)
        return True
    except Exception as e:
        print(f"Error creating directory {path}: {e}")
        return False
    
def create_file(path: str, content: str = "") -> bool:
    """Creates a file with the given content."""
    try:
        with open(path, 'w') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error creating file {path}: {e}")
        return False
    
def delete_dir(path: str) -> bool:
    """Deletes a directory and all its contents."""
    try:
        if os.path.exists(path):
            os.rmdir(path)
        return True
    except Exception as e:
        print(f"Error deleting directory {path}: {e}")
        return False
    