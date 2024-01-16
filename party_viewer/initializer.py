from pathlib import Path


def list_directories(path):
    suffixes = ['.gba', '.gbc', '.gb', '.nds']
    cwd = Path(path.root, path)
    return [ i for i in cwd.iterdir() if i.is_dir() or i.suffix in suffixes ]
    # for index in range(1, len(valid_dirs) + 1):
    #     print(f'{index}: {valid_dirs[index - 1]}')
        # print(type(valid_dirs[index - 1].suffix))

def select_path(starting_path):
    while True:
        dirs = list_directories(starting_path)
        for index in range(1, len(dirs) + 1):
            print(f'{index}: {dirs[index - 1].name}')
        
        selection = int(input('Select a file or directory: '))
        selected_item = dirs[selection - 1]
        if selected_item.is_dir():
            select_path(Path(Path.cwd(), selected_item))
            
select_path(Path.cwd())