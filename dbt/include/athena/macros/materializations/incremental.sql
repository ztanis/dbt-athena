
{% materialization incremental, adapter='athena' -%}
  {{ exceptions.raise_not_implemented(
    'incremental materialization not implemented for '+adapter.type())
  }}
{% endmaterialization %}
