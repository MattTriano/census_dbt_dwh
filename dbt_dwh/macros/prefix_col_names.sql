{#
Pivot values from columns to rows. Similar to pandas DataFrame melt() function.

Example Usage: {{ prefix_col_names(relation=ref('users'), exclude=['id','created_at'], prefix='y') }}

Arguments:
    relation: Relation object, required.
    exclude:  A list of columns to keep but exclude from the unpivot operation. Default is none.
    prefix:   The string to prefix all col names with
#}

{% macro prefix_col_names(relation=none, exclude=none, prefix='y') -%}
    {{ return(adapter.dispatch('prefix_col_name')(relation, exclude, prefix)) }}
{% endmacro %}

{% macro default_prefix_col_name(relation=none, exclude=none, prefix='y') -%}

    {% if not relation %}
        {{ exceptions.raise_compiler_error("Error: argument `relation` is required for `prefix_col_name` macro.") }}
    {% endif %}

  {%- set exclude = exclude if exclude is not none else [] %}

  {%- set include_cols = [] %}

  {%- set table_columns = {} %}

  {%- do table_columns.update({relation: []}) %}

  {%- do dbt_utils._is_relation(relation, 'prefix_col_name') -%}
  {%- do dbt_utils._is_ephemeral(relation, 'prefix_col_name') -%}
  {%- set cols = adapter.get_columns_in_relation(relation) %}

  {%- for col in cols -%}
    {%- if col.column.lower() not in exclude|map('lower') -%}
      {% do include_cols.append(col) %}
    {%- endif %}
  {%- endfor %}

     select
      {%- for exclude_col in exclude %}
        {{ exclude_col }},
      {%- endfor %}
      {%- for col in include_cols -%}
        {{- prefix -}}{{- col -}}{% if not loop.last -%},{% endif -%}
      {%- endfor -%} 
    from {{ relation }}

{%- endmacro %}

