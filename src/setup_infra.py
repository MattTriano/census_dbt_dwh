from pathlib import Path


def get_project_root_dir() -> Path:
    try:
        return Path(__file__).joinpath("..", "..").resolve()
    except Exception as err:
        raise


def main() -> None:
    proj_root_dir = get_project_root_dir()
    db_dir = proj_root_dir.joinpath("db")
    db_dir.mkdir(exist_ok=True)
    data_dir = proj_root_dir.joinpath("data")
    data_dir.joinpath("archive").mkdir(parents=True, exist_ok=True)
    docs_dir = proj_root_dir.joinpath("docs")
    docs_dir.joinpath("archive").mkdir(parents=True, exist_ok=True)
    dwh_db_path = db_dir.joinpath("dwh.duckdb")


if __name__ == "__main__":
    main()
