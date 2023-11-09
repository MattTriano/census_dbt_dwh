# Census dbt Data Warehouse

This project is uses `dbt`, `duckdb`, and a little bit of python code to collect, extract, load, and transform some data sets, curating a local data warehouse.

## Data Sources

* Census [Business Formation Statistics](https://www.census.gov/econ/bfs/data/weeklynaics.html)

## Setup

Do the basics:
* Clone and `cd` into the repo
* Create and activate the conda env (`conda env create -f environment.yml` and then `conda activate elt_env`)

Then call `python src/setup_infra.py` to create the necessary directory structure and initialize the `metadata` database.

## Data Collection

```python
from src.file_utils import collect_data_to_file_from_url
from src.setup_infra import get_project_root_dir

data_dir = get_project_root_dir().joinpath("data")
collect_data_to_file_from_url(
    file_path=data_dir.joinpath("weekly_bfs_naics_by_industry_subsector.csv"),
    url="https://www.census.gov/econ/bfs/csv/naics3.csv"
)
```

To refresh all sources defined in `src/sources.py`

```python
from sources import all_file_data_sources
from file_utils import collect_data_to_file_from_url

for fds in all_file_data_sources():
    collect_data_to_file_from_url(url=fds.url, file_path=fds.file_path)
```

## Steps Taken

```bash
dbt init dbt_dwh
```
And select the `duckdb` option.

`cd` into `/dbt_dwh/` then modify the `dwh_project.yml` file:
* add `docs-paths: ["docs"]`
* in the `dbt_dwh:` section of `models:`, add `data_raw: -> +materialized: table` and `clean: +materialized: table`

Add a `dependencies.yml` file, add [dbt_utils](https://hub.getdbt.com/dbt-labs/dbt_utils/latest) and any other packages with version numbers, then run `dbt deps`

Add `/data_raw/` and `/clean/` dirs to the `/models/` dir, and then add `.sql` files to `/data_raw/` with the format:
* file_name: `dataset_name_raw.sql`
* file contents: `select * from read_csv("../data/dataset_name.csv", AUTO_DETECT=TRUE)`

Then run `dbt run`

## Data

### Business Formation Statistics

#### Annual County Data

[Data page](https://www.census.gov/econ/bfs/data/county.html)

