from os import getcwd
from pathlib import Path
import yaml


root_path = Path(getcwd()).parent.parent
paths_config = root_path / "config" / "paths_config.yml"

def load_config(file_config: Path) -> None:
    with open(file_config, 'r') as file:
        return yaml.safe_load(file)

paths_config = load_config(paths_config)


sample_data_path = Path(getcwd()).parent.parent / "sample_data" 