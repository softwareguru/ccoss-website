---
id: a7t
title: "The Nitty-Gritty of Moving Data with Beam"
url: /sessions/nitty-gritty-moving-data-with-beam
speakers:
  - Jeff Klukas
time_start: 2020-08-24T20:20:00.000Z
time_end:   2020-08-24T21:00:00.000Z
day_num: 1
---

In this session, you won't learn about joins or windows or timers or any other advanced features of Beam. Instead, we will focus on the real-world complexity that comes from simply moving data from one system to another safely. How do we model data as it passes from one transform to another? How do we handle errors? How do we test the system? How do we organize the code to make the pipeline configurable for different source and destination systems?

We will explore how each of these questions are addressed in Mozilla's open source codebase [0] for ingesting telemetry data from Firefox clients. By the end of the session, you'll be equipped to explore the codebase and documentation on your own to see how these concepts are composed together.
