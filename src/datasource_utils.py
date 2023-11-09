from dataclasses import dataclass
from enum import Enum
from typing import Optional

from setup_infra import get_project_root_dir


class SourceFileType(Enum):
    DATA = "data"
    DATA_DOC = "docs"


@dataclass(frozen=True)
class FileDataSource:
    url: str
    source_file_type: SourceFileType
    file_name: Optional[str] = None

    @property
    def file_path(self):
        proj_root = get_project_root_dir()
        if self.file_name:
            return proj_root.joinpath(self.source_file_type.value, self.file_name)
        else:
            return proj_root.joinpath(self.source_file_type.value, self.url.split("/")[-1])
