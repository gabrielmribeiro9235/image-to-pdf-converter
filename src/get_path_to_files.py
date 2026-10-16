from pathlib import Path

def get_path_to_files():
    root_path = Path(__file__).resolve().parent.parent

    resources_path = root_path / "resources"

    files = []

    for file in resources_path.iterdir():
        if file.is_file() and file.name != ".gitkeep":
            files.append(f"{resources_path}\\{file.name}")

    return files
