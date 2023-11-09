import datetime as dt
import hashlib
import os
from pathlib import Path
import shutil
from urllib.request import urlretrieve

import pandas as pd


def hash_file(file_path: Path, method: str = "sha256") -> str:
    hash_func = getattr(hashlib, method)()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_func.update(chunk)
    return hash_func.hexdigest()


def are_small_files_identical(file_path0: Path, file_path1: Path) -> bool:
    with open(file_path0, "rb") as f0, open(file_path1, "rb") as f1:
        return f0.read() == f1.read()


def are_large_files_identical(file_path0: Path, file_path1: Path, method: str = "sha256") -> bool:
    return hash_file(file_path0, method) == hash_file(file_path1, method)


def are_files_identical(
    file_path0: Path, file_path1: Path, min_large_file_size: int = 2**25
) -> bool:
    file_path0_size = os.path.getsize(file_path0)
    file_path1_size = os.path.getsize(file_path1)
    if file_path0_size != file_path1_size:
        return False
    elif file_path0_size >= min_large_file_size:
        return are_large_files_identical(file_path0=file_path0, file_path1=file_path1)
    else:
        return are_small_files_identical(file_path0=file_path0, file_path1=file_path1)


def collect_data_to_file_from_url(file_path: Path, url: str) -> None:
    data_dir = file_path.parent
    if not file_path.is_file():
        urlretrieve(url=url, filename=file_path)
    else:
        temp_file_path = data_dir.joinpath(file_path.stem + "_temp" + file_path.suffix)
        urlretrieve(url=url, filename=temp_file_path)
        if not are_files_identical(file_path0=file_path, file_path1=temp_file_path):
            last_modified_time = dt.datetime.fromtimestamp(os.path.getmtime(file_path)).strftime(
                "%Y_%m_%d__%H_%M_%S"
            )
            new_file_name = file_path.stem + last_modified_time + file_path.suffix
            shutil.move(src=file_path, dst=data_dir.joinpath("archive", new_file_name))
            shutil.move(src=temp_file_path, dst=file_path)
        else:
            os.remove(temp_file_path)
