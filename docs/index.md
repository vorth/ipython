---
title: This is my title
layout: post
---
# iPython Projects

This Github repo contains several iPython notebooks.

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
