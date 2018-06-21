---
layout: index
---

#### Overview

The goal of this class is two-fold. First, to introduce you to core database concepts (e.g., data modeling, logical design, SQL) so that you too can build a billion dollar application. Second, to teach enough about database engine internals (e.g., physical database design, query optimization, transaction processing) so you have a good sense of why queries may be running slowly/incorrectly.

<b>Advanced Assignments</b>  There will be an experimental set of optional extra-credit assignments that will dive into more advanced database topics. These assignments will involve extending a simple Python-based database engine with additional functionality, or optimizations described in class..  


#### Recent Announcements


#### Schedule

<table class="table table-striped schedule">
  <thead>
  <tr>
    <th class="date" style="min-width: 5em;"> <p> <span>Date </span> </p> </th>
    <th style="min-width: 400px;"> <p> <span>Topic </span> </p> </th>
    <th style="min-width: 100px"> <p> <span>Readings </span> </p> </th>
    <th style="width: 100px;"> <p> <span>Assigned</span> </p> </th>
    <th style="width: 200px;"> <p> <span>Due</span> </p> </th>
  </tr>
  </thead>
{% for r in site.data.schedule %}
  <tr style="background-color: {{r.color}};">
    <td class="date">{{r.date}}</td>
    <td class="slug"><a href="{{r.link}}">{{r.slug}}</a><br/>{{r.title}}</td>
    <td class="readings">{{r.readings | safe}}</td>
    <td>{% if r.ashow == "1" %} {{r.assigned | safe}} {% endif %}</td>
    <td>{% if r.dshow == "1" %} {{r.due | safe}} {% endif %}</td>
  </tr>
{% endfor %}
</table>
