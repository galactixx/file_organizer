from rich.console import Console
from rich.table import Table
from pathlib import Path
import shutil
import click
import os

NUM_FOLDERS = 3

def _truncate_path(path: str) -> str:
    """Truncate path to shorten length of string in rich output."""
    path = os.path.normpath(path)
    path_split = path.split(os.sep)
    if len(path_split) <= NUM_FOLDERS:
        return path
    else:
        return os.path.join(*path_split[-NUM_FOLDERS:])

@click.command()
@click.option('--path', type=click.Path(exists=True), prompt='Enter the path', help='The name of the path')
def _file_organizer(path: str) -> None:
    """CLI for organizing files in a given directory by file type."""

    # instance of rich table & console
    console = Console()
    table = Table(title='Files that were Organized')
    table.add_column('File Type', style='cyan')
    table.add_column('Source Path', style='magenta')
    table.add_column('Destination Path', style='green')

    contents = [i for i in os.listdir(path) if not os.path.isdir(os.path.join(path, i))]
    if not contents:
        click.echo('Error: There are no files in this path, please specify path with files.')
    else:
        # iterate through each file in contents
        for file in contents:

            # generate all relevant paths
            file_type = Path(file).suffix[1:]
            source_path = os.path.join(path, file)
            destination_path_main = os.path.join(path, f'{file_type} files')
            destination_path = os.path.join(destination_path_main, file)

            # make directory and move file
            os.makedirs(destination_path_main, exist_ok=True)
            shutil.move(source_path, destination_path)
            table.add_row(file_type,
                          _truncate_path(path=source_path),
                          _truncate_path(path=destination_path))

        # print table in console
        console.print(table)

if __name__ == '__main__':
    _file_organizer()