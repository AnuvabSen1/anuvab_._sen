<h2 style="margin: 60px 0px 10px;">Selected Publications</h2>

<div class="selected-pubs">

{% for link in site.data.selected_pubs.main %}
<div class="sel-pub-card">
  <div class="sel-pub-venue-badge {{ link.badge_class }}">{{ link.conference_short }}</div>
  <div class="sel-pub-body">
    <div class="sel-pub-title"><a href="{{ link.pdf }}">{{ link.title }}</a></div>
    <div class="sel-pub-authors">{{ link.authors }}</div>
    <div class="sel-pub-conf"><em>{{ link.conference }}</em>
    {% if link.notes %} 
    <span style="display:inline-block; background:#e74d3c; color:#fff; padding:2px 8px; border-radius:3px; font-size:11px; font-weight:600; margin-left:4px;">{{ link.notes }}</span>
    {% endif %}
    </div>
  </div>
</div>
{% endfor %}

</div>

<div style="text-align: right; margin-top: 8px;">
  <a href="./publications/" style="font-size: 14px; font-weight: 500;">View all publications →</a>
</div>
