from pathlib import Path
import shutil
import click
import rich
import os

@click.command()
@click.option('--path', type=click.Path(exists=True), prompt='Enter the path', help='The name of the path')
def _path_organizer(path: str) -> None:
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

if __name__ == '__main__':
    _path_organizer()