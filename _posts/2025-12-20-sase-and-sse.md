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
    font-family: sans-serif;
    min-width: 400px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
  }
  table thead tr {
    background-color: #009879;
    color: #ffffff;
    text-align: left;
  }
  table th,
  table td {
    padding: 12px 15px;
    border: 1px solid #dddddd;
  }
  table tbody tr {
    border-bottom: 1px solid #dddddd;
  }
  table tbody tr:nth-of-type(even) {
    background-color: #f3f3f3;
  }
  table tbody tr:last-of-type {
    border-bottom: 2px solid #009879;
  }
  table tbody tr.active-row {
    font-weight: bold;
    color: #009879;
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
