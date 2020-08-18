---
id: a6s
title: "Mining scientific literature with Apache Beam"
url: /sessions/mining-scientific-literature
speakers:
  - Christian Battista

time_start: 2020-08-24T20:00:00.000Z
time_end:   2020-08-24T20:20:00.000Z
day_num: 1
---

At BenchSci, we mine a subset of the world’s biological research papers (about 10 million of them) with the aim of extracting info that will accelerate future pharmaceutical research programs by enabling more reproducible experiments. While we have the luxury of processing this information in batch, it is not without its challenges. Information comes to us in a wide variety of data types and formats, from archives to individual documents, with little to no visibility into what the contents will be, or whether they will be consistent or not.

Our first approaches to this problem involved a myriad of technologies which quickly became unmaintainable and difficult to orchestrate, and we turned to Beam (Dataflow Runner) in the hopes that it was the right data processing abstraction. It was. However, one surprising effect was the impact of Beam’s programming model on the quality and maintainability of the codebase we ported over (from Spark & Airflow). Specifically, the constraints imposed by Beam prompted us to morph our existing codebase into something that was simpler to test and reason about. In sharing this use case we hope to provide others with a set of expectations about the benefits and work involved with migrating an existing pipeline to Beam.