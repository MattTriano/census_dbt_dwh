with wide_to_long_transform AS (
    {{ dbt_utils.unpivot(
        relation=ref('weekly_bfs_naics_by_ind_subsector_raw'),
        cast_to='integer',
        exclude=['naics3', 'description'],
        field_name='week',
        value_name='business_applications'
    ) }}
)

select
    naics3,
    description,
    date_add(
        (substring(week, 6, 2)::int - 1) * 7,
        (substring(year_week, 1, 4) || '-01-01')::DATE
    ) as date,
    business_applications
from wide_to_long_transform 

