---
layout: page
permalink: /blogs/
title: Blogs
description: Blog posts and essays.
page_class: page-blogs
nav: true
nav_order: 2
---

<!-- _pages/blogs.md -->

<div class="publications">

{%- assign current_year = 'now' | date: '%Y' | plus: 0 -%}
{%- assign start_year = 2010 -%}
{%- for y in (start_year..current_year) reversed -%}
	{%- capture year_entries -%}
		{% bibliography -f blogs -q @*[year={{y}}]* %}
	{%- endcapture -%}
	{%- if year_entries contains '<li>' -%}
		<h2 class="year"><span>{{y}}</span></h2>
		{{ year_entries }}
	{%- endif -%}
{%- endfor -%}

</div>