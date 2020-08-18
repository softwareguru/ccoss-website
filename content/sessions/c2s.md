---
id: c2s
title: "API Sink Connector: A Configurable Beam Pipeline for Connecting to Third-Party Data Stores"
url: /sessions/api-sink-connector
speakers:
  - John Stimac

time_start: 2020-08-26T16:00:00.000Z
time_end:   2020-08-26T16:20:00.000Z
day_num: 3
---
At Yelp, we use Apache Flink and Beam to build generic tools for performing common streaming operations. Feature team developers can then use these tools to build complex systems, without requiring them to learn all the details of our streaming infrastructure.

One common operation we do at Yelp is to move data from Kafka to external, third-party data stores (like Salesforce or Oracle) via public APIs. This necessitates a number of complex operations, such as transforming data with business logic, batching data into bulk requests, and ordering data to resolve foreign key dependencies. Previously, we did all these steps in Python code, running as standalone Kafka consumers or daily batches. These systems were becoming hard to maintain, performed poorly as scale increased, and resulted in fractured architecture as multiple systems were built by different teams.

Enter, the API Sink Connector. The API Sink Connector is a new tool we’ve built which runs as a user-configurable Beam app, and provides a framework for feature developers to build apps connecting Kafka to third-party data stores. It uses stateful Beam processing to handle complex operations. It doesn't require extensive stream processing knowledge to use. And, since it’s built on Beam, it allows feature developers to easily reuse existing Python business logic from legacy systems.

My talk will enumerate the challenges of moving data from Kafka to third-party data stores, look in depth at how the API Sink Connector uses stateful Beam processing to solve those challenges, and show how Beam allows us to provide an interface for feature developers to extend the app with custom Python logic.