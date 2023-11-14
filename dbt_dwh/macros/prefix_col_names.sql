{#
Prefix all column names (except for those in the exclude param) with a given prefix. 

Example Usage: {{ prefix_col_names(relation=ref('users'), exclude=['id','created_at'], prefix='') }}

Arguments:
    relation: Relation object, required.
    exclude:  A list of columns to keep but exclude from the prefixing operation. Default is ''.
    prefix:   The string to prefix all col names with
#}

{% macro prefix_col_names(relation=none, exclude=none, prefix='') -%}
    {{ return(adapter.dispatch('prefix_col_names')(relation, exclude, prefix)) }}
{% endmacro %}

{% macro default__prefix_col_names(relation=none, exclude=none, prefix='') -%}

    {% if not relation %}
        {{ exceptions.raise_compiler_error("Error: argument `relation` is required for `prefix_col_names` macro.") }}
    {% endif %}

  {%- set exclude = exclude if exclude is not none else [] %}
  {%- set column_names = [] %}
  {%- set table_columns = {} %}

  {%- do table_columns.update({relation: []}) %}

  {%- do dbt_utils._is_relation(relation, 'prefix_col_names') -%}
  {%- do dbt_utils._is_ephemeral(relation, 'prefix_col_names') -%}
  {%- set cols = adapter.get_columns_in_relation(relation) %}

  {%- for col in cols -%}
    {%- if col.name.lower() not in exclude|map('lower') -%}
      {%- do column_names.append(prefix ~ col.name) -%}
    {% else %}
      {%- do column_names.append(col.name) -%}
    {%- endif %}
  {%- endfor %}

  select
    {%- for col in cols %}
      "{{ col.name }}" as {{ column_names[loop.index0] -}}{% if not loop.last -%},{% endif %}
    {%- endfor %}
  from {{ relation }}

{%- endmacro %}

