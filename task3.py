import sys
import colorama
import pathlib

def draw_path(path: pathlib.Path, level: int = 0) -> None:
    color = colorama.Fore.BLUE if path.is_dir() else colorama.Fore.GREEN
    name = path.name

    if path.is_dir():
        name += '/'

    print(color, level * 4 * ' ', name)
    if path.is_dir():
        for node in path.iterdir():
            draw_path(node, level + 1)

path = pathlib.Path(sys.argv[1])
draw_path(path)