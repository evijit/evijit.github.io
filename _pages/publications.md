---
layout: page
permalink: /publications/
title: Papers
description: A list of my publications.
page_class: page-papers
hero_link_text: View my Google Scholar Page
hero_link_url: https://scholar.google.com/citations?user=X9y2jJIAAAAJ
nav: true
nav_order: 1
---
<!-- _pages/publications.md -->

<div class="publications">

{%- assign current_year = 'now' | date: '%Y' | plus: 0 -%}
{%- assign start_year = 2010 -%}
{%- for y in (start_year..current_year) reversed -%}
	{%- capture year_entries -%}
		{% bibliography -f papers -q @*[year={{y}}]* %}
	{%- endcapture -%}
	{%- if year_entries contains '<li>' -%}
		<h2 class="year"><span>{{y}}</span></h2>
		{{ year_entries }}
	{%- endif -%}
{%- endfor -%}

</div>
