---
id: b7t
title: "Replacing Your Database with Beam Pipelines"
url: /sessions/replacing-your-database-with-beam-pipelines
speakers:
  - Vinay Mayar

time_start: 2020-08-25T20:20:00.000Z
time_end:   2020-08-25T21:00:00.000Z
day_num: 2
---

We use streaming Beam pipelines to index data into an object store (S3) and compute summaries of new data with periodic batch pipelines. These summaries are analogous to indices in a database and allow for efficient lookup along a fixed set of axes. The result is a scalable and inexpensive data storage solution for applications that serve data with limited query patterns.
