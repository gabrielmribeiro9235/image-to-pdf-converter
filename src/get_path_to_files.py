from pathlib import Path

def get_path_to_files():
    root_path = Path(__file__).resolve().parent.parent

    resources_path = root_path / "resources"

    extensions = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff"}

    return sorted(
        (
            path
            for path in resources_path.iterdir()
            if path.is_file() and path.suffix.lower() in extensions
        ),
        key=lambda path : path.name.lower()
    )
