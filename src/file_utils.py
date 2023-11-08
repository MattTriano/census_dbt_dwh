import os
from pathlib import Path
import shutil
from urllib.request import urlretrieve

import pandas as pd


def collect_data_to_file_from_url(file_path: Path, url: str) -> None:
    data_dir = file_path.parent
    if not file_path.is_file():
        urlretrieve(url=url, filename=file_path)
    else:
        file_name = file_path.name
        temp_file_path = file_path.parent.joinpath(file_name.replace(".csv", "_temp.csv"))
        urlretrieve(url=url, filename=temp_file_path)
        prior_df = pd.read_csv(file_path)
        new_df = pd.read_csv(temp_file_path)
        if not prior_df.equals(new_df):
            last_modified_time = dt.datetime.fromtimestamp(
                os.path.getmtime(file_path)
            ).strftime("%Y_%m_%d__%H_%M_%S")
            new_file_name = file_name.replace(".csv", f"{last_modified_time}.csv")
            shutil.move(src=file_path, dst=data_dir.joinpath("archive", new_file_name))
            shutil.move(src=temp_file_path, dst=file_path)
        else:
            os.remove(temp_file_path)