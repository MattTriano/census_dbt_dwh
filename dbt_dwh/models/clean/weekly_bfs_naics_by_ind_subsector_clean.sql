with wide_to_long_transform AS (
    {{ dbt_utils.unpivot(
        relation=ref('weekly_bfs_naics_by_ind_subsector_clean_prefix'),
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
        (substring(week, 7, 2)::int - 1) * 7,
        (substring(week, 2, 4) || '-01-01')::DATE
    ) as date,
    business_applications
from wide_to_long_transform 
order by naics3 asc, date asc
