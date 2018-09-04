---
layout: index
---

#### Overview

The goal of this class is two-fold. First, to introduce you to core database concepts (e.g., data modeling, logical design, SQL) so that you too can build a billion dollar application. Second, to teach enough about database engine internals (e.g., physical database design, query optimization, transaction processing) so you have a good sense of why queries may be running slowly/incorrectly.

**Advanced Assignments**  There will be an experimental set of [optional extra-credit assignments](https://github.com/w4111/advanced) that will dive deeper into concepts introduced in class.   Some of them will involve extending a simple Python-based database engine with additional functionality!  They are labeled `AA#` in the schedule.  There is no obligation to do these, but they are available if you want to do then in addition to, or in lieu of the normal assignments.


#### Recent Announcements

* Want to be auto-matched with a project partner?  [Sign up here](https://goo.gl/forms/ail3TK0sNpRi7qFR2) by 9/7 10AM EST, and we will auto-match you will a teammate by 9/10.  Matches are **binding** so be sure you want to be matched automatically before submitting.
* Please do not email me with questions about registration and enrollment.  Enrollments will be based on the waitlist and completion of HW0.   Historically, students that stick with the class have been able to enroll.

#### Schedule

<table class="table table-striped schedule">
  <thead>
  <tr>
    <th class="date" style="width: 4em; max-width: 4em;"> <p> <span>Date </span> </p> </th>
    <th style="min-width: 20%;"> <p> <span>Topic </span> </p> </th>
    <!--<th style="width: 15%"> <p> <span>Readings </span> </p> </th>-->
    <th style="width: 25%;"> <p> <span>Assigned</span> </p> </th>
    <th style="width: 25%;"> <p> <span>Due</span> </p> </th>
  </tr>
  </thead>
{% for r in site.data.schedule %}
  <tr style="background-color: {{r.color}};">
    <td class="date">{{r.date}}</td>
    <td class="slug"><a href="{{r.link}}">{{r.slug}}</a><br/>{{r.title}}</td>
    <!--<td class="readings">{{r.readings | safe}}</td>-->
    <td>{% if 1 or r.ashow == "1" %} {{r.assigned | safe}} {% endif %}</td>
    <td>{% if 1 or r.dshow == "1" %} {{r.due | safe}} {% endif %}</td>
  </tr>
{% endfor %}
</table>
