---
id: b4t
title: "Wiggly Air and Data Processing at Spotify"
url: /sessions/wiggly-air-data-processing-spotify
speakers:
  - Lynn Root

time_start: 2020-08-25T17:00:00.000Z
time_end:   2020-08-25T17:40:00.000Z
day_num: 2

---

Digital signal processing (DSP) has been made easy with the help of many Python libraries, allowing engineers and researchers to quickly and effortlessly analyze audio, images, and video. However, scaling these algorithms and models to process millions of files has not been equally as seamless. At Spotify, we’re trying to address scaling DSP over our catalog of over 50 million songs. This talk will discuss the challenges we’ve encountered while building the infrastructure needed to support audio processing at scale. I’ll discuss the how we’ve leveraged Apache Beam for streaming data pipelines and the tooling we’ve built on top of Beam to support our heavy resource requirements.

