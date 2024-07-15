import sys
from colorama import Fore, Back, Style
from os import listdir, path, readlink


def print_directory_structure(directory: str, level: int = 0) -> None:
    try:
        for dir_item in listdir(directory):
            if path.islink(directory + '/' + dir_item):
                print(f'{Fore.LIGHTCYAN_EX}{'\t' * level}{dir_item} -> {Fore.CYAN}{readlink(directory + '/' + dir_item)}{Style.RESET_ALL}')
            elif path.isfile(directory + '/' + dir_item):
                print(f'{Fore.BLUE}{'\t' * level}{dir_item}{Style.RESET_ALL}')
            elif path.isdir(directory + '/' + dir_item):
                print(f'{Fore.GREEN}{'\t' * level}{dir_item}/{Style.RESET_ALL}')
                print_directory_structure(directory + '/' + dir_item, level + 1)

    except FileNotFoundError:
        print(f'{Fore.WHITE}{Back.RED}Директорії {directory} не існує{Style.RESET_ALL}')
    except PermissionError:
        print(f'{Fore.WHITE}{Back.RED}Бракує прав на читання директорії {directory}{Style.RESET_ALL}')
    except NotADirectoryError:
        print(f'{Fore.WHITE}{Back.RED}{directory} не є директорією{Style.RESET_ALL}')


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print(f'{Fore.WHITE}{Back.RED}Бракує аргументу з шляхом до директорії{Style.RESET_ALL}')
        exit(0)

    print_directory_structure(sys.argv[1])