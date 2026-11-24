{% if zt.notes.size > 0 %}
## Zotero 笔记

{% for note in zt.notes %}
- {{ note.noteLink }}
{% endfor %}
{% endif %}
{% if zt.annotations.size > 0 %}
## Zotero 批注

{% for annotation in zt.annotations %}
{% render "annotation" with annotation as zt %}
{% endfor %}
{% endif %}
