from converter import converter
from get_path_to_files import get_path_to_files

if __name__ == "__main__":
    try:
        images = get_path_to_files()

        if not images:
            print("No images found in the resources directory.")
        else:
            converter(get_path_to_files())
            print("PDF generated successfully.")

    except Exception as error:
        print("\033[31mFailed to convert\033[0m")
        print(error)
