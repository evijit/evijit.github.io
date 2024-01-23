---
layout: page
permalink: /publications/
title: Publications
description: 
years: [2024, 2023, 2022, 2021, 2019, 2018, 2017]
nav: true
nav_order: 1
---
<!-- _pages/publications.md -->

A list of my publications. [<u>View my Google Scholar Page here.</u>](https://scholar.google.com/citations?user=X9y2jJIAAAAJ)

<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
