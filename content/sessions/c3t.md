---
id: c3t
title: "Building Stateful Streaming Pipelines with Beam"
url: /sessions/building-stateful-streaming-pipelines
speakers:
  - Ankit Jhalaria
time_start: 2020-08-26T16:20:00.000Z
time_end:   2020-08-26T17:00:00.000Z
day_num: 3
---

Building a streaming data platform from the ground up is a daunting yet fun task. Walk developers's through GoDaddy's journey of building production pipelines at scale using Apache Beam as the foundation layer for writing pipelines and building abstractions on top of it to make it easier to on board new pipelines on to the data platform.

Beam supports the ability to deploy the same pipeline code on multiple runners. Talk about how we extensively use the same pipeline code to run in batch/streaming mode on Flink/Spark to support both legacy on-premise cluster and running pipelines on the cloud.

Do a code walk thru of some of the abstractions that we have built at GoDaddy that make it super easy to build a pipeline that can do streaming joins, read and write to hdfs/s3 and other sources and sinks.