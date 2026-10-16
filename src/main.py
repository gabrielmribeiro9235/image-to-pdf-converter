from converter import converter
from get_path_to_files import get_path_to_files

if __name__ == "__main__":
    try:
        converter(get_path_to_files())
    except Exception as error:
        print("\033[31mFailed to convert\033[0m")
        print(error)
