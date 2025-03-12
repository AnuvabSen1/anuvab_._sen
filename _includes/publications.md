<div class="pub-row" style="display: flex; align-items: flex-start; margin-bottom: 1em;">
  <div class="col-sm-3 abbr" style="padding: 0 15px;">
    <img src="{{ link.image }}" class="teaser img-fluid z-depth-1" style="width: 100%; height: auto;">
    <abbr class="badge">{{ link.conference_short }}</abbr>
  </div>
  <div class="col-sm-9" style="padding: 0 15px 0 20px; text-align: left;">
    <div class="title" style="margin: 0; text-indent: 0; white-space: normal; word-wrap: break-word;">
      <a href="{{ link.pdf }}">{{ link.title }}</a>
    </div>
    <div class="author" style="margin: 0; text-indent: 0; white-space: normal; word-wrap: break-word;">
      {{ link.authors }}
    </div>
    <div class="periodical" style="margin: 0; text-indent: 0; white-space: normal; word-wrap: break-word;">
      <em>{{ link.conference }}</em>
    </div>
    <div class="links" style="margin: 0; text-indent: 0;">
      {% if link.pdf %} 
      <a href="{{ link.pdf }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">PDF</a>
      {% endif %}
      {% if link.code %} 
      <a href="{{ link.code }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">Code</a>
      {% endif %}
      {% if link.page %} 
      <a href="{{ link.page }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">Project Page</a>
      {% endif %}
      {% if link.data %} 
      <a href="{{ link.data }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">Dataset</a>
      {% endif %}
      {% if link.bibtex %} 
      <a href="{{ link.bibtex }}" class="btn btn-sm z-depth-0" role="button" target="_blank" style="font-size:12px;">BibTex</a>
      {% endif %}
      {% if link.notes %} 
      <strong><i style="color:#e74d3c; font-weight:600">{{ link.notes }}</i></strong>
      {% endif %}
      {% if link.others %} 
      {{ link.others }}
      {% endif %}
    </div>
  </div>
</div>
