from pathlib import Path

import duckdb
import pandas as pd


def execute_ddl_stmt(stmt: str, db_path: Path) -> None:
    with duckdb.connect(database=str(db_path), read_only=False) as conn:
        with conn.cursor() as cursor:
            cursor.execute(stmt)
        conn.commit()


def execute_query(query: str, db_path: Path) -> pd.DataFrame:
    with duckdb.connect(database=str(db_path)) as conn:
        df = conn.execute(query).fetchdf()
    return df