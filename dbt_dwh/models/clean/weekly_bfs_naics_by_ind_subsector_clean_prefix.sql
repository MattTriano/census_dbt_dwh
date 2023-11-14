{{ config(materialized='view') }}

with fixed_cols AS (
    {{ prefix_col_names(
        relation=ref('weekly_bfs_naics_by_ind_subsector_raw'),
        exclude=['naics3', 'description'],
        prefix='y'
    ) }}
)

select *
from fixed_cols

