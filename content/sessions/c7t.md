---
id: c7t
title: "Simpler Python Pipelines with Schemas, SQL, and Dataframes"
url: /sessions/simpler-python-pipelines
speakers:
  - Brian Hulette
time_start: 2020-08-26T20:20:00.000Z
time_end:   2020-08-26T21:00:00.000Z
day_num: 3
---

While the Beam Python SDK is highly scalable and has advanced streaming capabilities, its unfamiliar API has been a significant barrier for many Python users. Recently there have been several improvements in usability aimed at closing this gap: first-class support for schemas, the ability to embed SQL in a pipeline, and a pandas-compatible Dataframe API.

In this talk we will introduce these new APIs and how they can be used. We will then discuss some of the details of their implementation, including the challenges involved in writing a distributed, faithful, drop-in replacement for Pandas, as well as how we are able to leverage Beam's portability framework and cross-language transforms to execute SQL with Java.