from typing import List

from datasource_utils import SourceFileType, FileDataSource

BFS_ANNUAL_COUNTY_DATA = FileDataSource(
    url="https://www.census.gov/econ/bfs/xlsx/bfs_county_apps_annual.xlsx",
    source_file_type=SourceFileType.DATA,
)

BFS_ANNUAL_COUNTY_DATA_DICTIONARY = FileDataSource(
    url="https://www.census.gov/econ/bfs/pdf/bfs_county_data_dictionary.pdf",
    source_file_type=SourceFileType.DATA_DOC,
)

BFS_WEEKLY_US_BIS_APPLICATIONS_DATA = FileDataSource(
    url="https://www.census.gov/econ/bfs/csv/bfs_us_apps_weekly_nsa.csv",
    source_file_type=SourceFileType.DATA,
)

BFS_WEEKLY_REGIONAL_BIS_APPLICATIONS_DATA = FileDataSource(
    url="https://www.census.gov/econ/bfs/csv/bfs_region_apps_weekly_nsa.csv",
    source_file_type=SourceFileType.DATA,
)

BFS_WEEKLY_STATE_BIS_APPLICATIONS_DATA = FileDataSource(
    url="https://www.census.gov/econ/bfs/csv/bfs_state_apps_weekly_nsa.csv",
    source_file_type=SourceFileType.DATA,
)

BFS_WEEKLY_DATA_DICTIONARY = FileDataSource(
    url="https://www.census.gov/econ/bfs/pdf/bfs_weekly_data_dictionary.pdf",
    source_file_type=SourceFileType.DATA_DOC,
)


def all_file_data_sources() -> List[FileDataSource]:
    file_data_sources = []
    for name, obj in globals().items():
        if isinstance(obj, FileDataSource):
            file_data_sources.append(obj)
    return file_data_sources
