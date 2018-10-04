---
layout: index
---

#### Overview

The goal of this class is two-fold. First, to introduce you to core database concepts (e.g., data modeling, logical design, SQL) so that you too can build a billion dollar application. Second, to teach enough about database engine internals (e.g., physical database design, query optimization, transaction processing) so you have a good sense of why queries may be running slowly/incorrectly.

**Advanced Assignments**  There will be an experimental set of [optional extra-credit assignments](https://github.com/w4111/advanced) that will dive deeper into concepts introduced in class.   Some of them will involve extending a simple Python-based database engine with additional functionality!  They are labeled `AA#` in the schedule.  There is no obligation to do these, but they are available if you want to do then in addition to, or in lieu of the normal assignments.


#### Recent Announcements

* (10/4) Click here [for previous midterms](https://github.com/w4111/w4111.github.io/tree/master/files/reading).  Midterm will cover content up to, and including, the SQL lectures.  
* (10/4) Click here for the [SQL instabase examples shown in class](https://www.instabase.com/user/ewu-nb/notebooks/ewu/w4111-public/fs/Instabase%20Drive/Examples/Fall2018SQLlectureexamples.ipynb)
* Updated [AA1](https://github.com/w4111/advanced/blob/master/databass/offset.md) to clarify what to do if offset is negative: your code should raise an exception.  We have also updated the databass-public repo in `ops.py` so that LIMIT obeys the same semantics.  Issue a `git pull` in your copy of the codebase to see the changes.
* (9/16) Professor Wu will have extra office hours Tuesday 9/18 at 5:30-6:15PM to go over DataBass questions and the codebase for studens working on [AA1](https://github.com/w4111/advanced).
* (9/5) Do you have trouble figuring out what your Python code is doing?  [PythonTutor](http://pythontutor.com/) visualizes what Python is doing at each step in the program.  See if it helps!
* (9/5) You are welcome to find project partner on your own.  If you want to be auto-matched with a project partner,  [sign up here](https://goo.gl/forms/ail3TK0sNpRi7qFR2) by 9/7 10AM EST, and we will auto-match you will a teammate by 9/10.  Matches are **binding** so be sure you want to be matched automatically before submitting.
* (9/1) Please do not email me with questions about registration and enrollment.  Enrollments will be based on the waitlist and completion of HW0.   Historically, students that stick with the class have been able to enroll.

#### Schedule

<table class="table table-striped schedule">
  <thead>
  <tr>
    <th class="idx"></th>
    <th class="date" style="width: 4em; max-width: 4em;"> <p> <span>Date </span> </p> </th>
    <th style="min-width: 20%;"> <p> <span>Topic </span> </p> </th>
    <!--<th style="width: 15%"> <p> <span>Readings </span> </p> </th>-->
    <th style="width: 25%;"> <p> <span>Assigned</span> </p> </th>
    <th style="width: 25%;"> <p> <span>Due</span> </p> </th>
  </tr>
  </thead>
{% assign idx = 0 %}

{% for r in site.data.schedule %}
  {% assign idx = idx | plus: 1  %}
  <tr style="background-color: {{r.color}}; ">
    <td class="idx">L{{idx}}</td>
    <td class="date">{{r.date}}</td>
    <td class="slug">
      {% if r.lshow == "1" %} <a href="{{r.link}}"> {% endif %}
        {{r.slug}}
      {% if r.lshow == "1" %} </a> {% endif %}
      <br/>{{r.title}}
      {% if r.optional %}<br/>{% endif%}
      {{r.optional | safe}}
      </td>
    <!--<td class="readings">{{r.readings | safe}}</td>-->
    <td>{% if 1 or r.ashow == "1" %} {{r.assigned | safe}} {% endif %}</td>
    <td>{% if 1 or r.dshow == "1" %} {{r.due | safe}} {% endif %}</td>
  </tr>
{% endfor %}
</table>


