{% for link in site.data.navigation.main %}
  {% if link.right %}
    <a class="normal right" href="{{ link.url | relative_url }}">{{ link.title }}</a>
  {% else %}
    <a class="normal" href="{{ link.url | relative_url }}">{{ link.title }}</a>
  {% endif %}
{% endfor %}
