---
title: "tags"
layout: default
permalink: "/tags"
order: 1
---

<div class="container">
	<div class="row">
        {% include menu-categories.html %}
    </div>
</div>
<br>
<div class="container">
    <div class="card-columns">
    {% for tag in site.tags %}
    </div> 
    
    <h3 class="mt-4 display-4" id="{{ tag[0] | downcase }}"><small class="text-muted">#</small> {{ tag[0] }}</h3><hr>
    
    <div class="card-columns">

        {% assign pages_list = tag[1] %}
        {% for post in pages_list %}
          {% if post.title != null %}
              {% if group == null or group == post.group %}
                {% include article-content.html %}
              {% endif %}
          {% endif %}
        {% endfor %}
        {% assign pages_list = nil %}
        {% assign group = nil %}

    {% endfor %}
    </div>
</div>