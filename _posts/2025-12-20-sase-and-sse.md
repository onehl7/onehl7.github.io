---
layout: post
title: "SASE and SSE Vendor Comparison"
category: technology
---

## SASE and SSE Vendor Comparison

This table compares different SASE and SSE vendors across various dimensions. 
The content for this table is managed in the `_data/sase_sse.yml` file, making it easy to edit and update.

<style>
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 25px 0;
    font-size: 0.9em;
    font-family: 'Inter', sans-serif;
    background-color: #1e293b; /* A dark slate color */
    color: #e0e6f5;
  }
  table thead tr {
    background-color: #0f172a; /* A darker slate color */
    color: #ffffff;
    text-align: left;
    border-bottom: 2px solid #5eead4; /* A teal color for the header bottom border */
  }
  table th,
  table td {
    padding: 12px 15px;
    border: 1px solid #334155; /* A lighter slate for borders */
  }
  table tbody tr {
    border-bottom: 1px solid #334155;
  }
  table tbody tr:nth-of-type(even) {
    background-color: #0f172a; /* Use the darker slate for alternating rows */
  }
</style>

<table>
  <thead>
    <tr>
      {% for header in site.data.sase_sse.headers %}
        <th>{{ header }}</th>
      {% endfor %}
    </tr>
  </thead>
  <tbody>
    {% for row in site.data.sase_sse.rows %}
      <tr>
        {% for cell in row %}
          <td>{{ cell }}</td>
        {% endfor %}
      </tr>
    {% endfor %}
  </tbody>
</table>
