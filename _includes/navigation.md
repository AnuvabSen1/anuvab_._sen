{% for link in site.data.navigation.main %}
  {% if link.right %}
    <a class="normal right" href="{{ site.baseurl }}{{ link.url }}">{{ link.title }}</a>
  {% else %}
    <a class="normal" href="{{ site.baseurl }}{{ link.url }}">{{ link.title }}</a>
  {% endif %}
{% endfor %}
