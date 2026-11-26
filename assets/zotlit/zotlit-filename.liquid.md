{% comment -%}
Bootstrap filename only. After resolving the verified method name, place the ZotLit main note at <literature-root>/<paper-name>/<paper-name>.md through a supported destination or Obsidian rename/move. Do not guess a zt.methodName field.
{%- endcomment -%}
{{ zt.citationKey | default: zt.DOI | default: zt.title | default: zt.key }}{% suffix %}
