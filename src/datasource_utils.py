from dataclasses import dataclass
from enum import Enum

from setup_infra import get_project_root_dir


class SourceFileType(Enum):
    DATA = "data"
    DATA_DOC = "docs"


@dataclass(frozen=True)
class FileDataSource:
    url: str
    source_file_type: SourceFileType

    @property
    def file_path(self):
        return get_project_root_dir().joinpath(self.source_file_type.value, self.url.split("/")[-1])
