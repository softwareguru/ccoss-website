---
id: a4t
title: "From Pipeline To Execution - What happens when you run() your pipeline?"
url: /sessions/pipeline-to-execution
speakers:
  - Maximilian Michels
time_start: 2020-08-24T17:00:00.000Z
time_end:   2020-08-24T17:40:00.000Z
day_num: 1
---

Apache Beam is a powerful framework: unified batch and stream processing, support for multiple execution engines, as well as writing code in multiple languages. It can be hard to wrap your head around how all of this works.

Fortunately, Beam's architecture can be broken down into several components which are easy to understand. Let's look at what happens when you run your Beam pipeline, how it gets translated, submitted, and executed. To make this more practical, we will use the Flink Runner as an example.

This talk is for people new to Beam who want to learn about Beam's architecture, as well as potential Runner authors eager to learn how to integrate with Beam.