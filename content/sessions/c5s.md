---
id: c5s
title: "Four Apache Technologies Combined for Fun and Profit"
url: /sessions/apache-technologies-combined-fun-profit
speakers:
  - Tobias Kaymak

time_start: 2020-08-26T17:40:00.000Z
time_end:   2020-08-26T18:00:00.000Z
day_num: 3
---

When enriching one stream of data from another stream of data, one pretty easy way on GCP is to ingest both via Apache Beam into a zero-maintenance SQL database like BigQuery and doing a join there. However, since the cost for BigQuery is based on the number of bytes scanned and it's a columnar oriented database, this is not the optimal solution.

In some reference architectures BigQuery and BigTable, a wide-column NoSQL database allowing fast key-based lookups, are fed at the same time by Beam to provide data for different use cases. BigTable on the other hand, has a higher up-front cost as you need to deploy a cluster of at least 3 nodes to start playing with it.

Since DataStax released the Kubernetes operator to deploy Apache Cassandra, an open-source NoSQL database, on Kubernetes, the financial burden to play with this architecture pattern with open-source technologies has been substantially lowered.
This talk presents three Apache Beam pipelines that can be executed on the Apache Flink runner: The first one is going to batch load the historical data from BigQuery to Cassandra, the second one streaming the most recent data continuously from Apache Kafka to Cassandra, and the final one doing a lookup towards Cassandra while reading from Kafka and writing the enriched result to BigQuery.