---
layout: default
---
# iPython Projects

This Github repo contains several iPython notebooks.

{% for post in site.posts %}
* [{{ post.title }}](/ipython{{ post.url }})
{% endfor %}

