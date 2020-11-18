![Ros2TangleCover](https://github.com/HackTheAlps/Ros2Tangle/blob/main/img/cover.png?raw=true)

# Ros2Tangle
In 2019 more than 5.4 million robots are already running on ROS (Robot Operating System). In 2024 it is expected that additional 8.1 million robots are running with ROS. These numbers are taken from [Statista](https://www.statista.com/statistics/1084823/global-ros-based-robot-market-volume/), the global No.1 Business Data Plattform. More and more robots work in our daily lifes (f. ex. agriculture, industrial, environment, supply chain,...).

We focused to make it __extremly easy__ to connect also your __robot to the cloud__. In this example we send the robot data to [__IOTA streams__](https://www.iota.org/solutions/streams). Using the IOT2TANGLE Streams gateway is easy to use: via HTTP or MQTT this gateway can recieve sensor data and act as entry point to the tangle. We used Oracle __ for data storage and __ as a visualization example.

In case something is unclear, please let us know so that we can make it clear. Thank you!

## Prerequisite
- [Ubuntu 16.04 Xenial Xerus](https://releases.ubuntu.com/16.04/) installed
- [IOTA streams gateway](https://github.com/iotaledger/streams) is setup and running

## Projet Setup
This project contains tree folders
- robot: robot data is taken and published to IOTA tangle
- storage
- visu

## Side notice
This project was developed for the [IOT2Tangle Hackathon](https://hackathon.iot2tangle.io/) (October 26th, 2020 - November 26th, 2020).

This Hackathon aims to generate quality open-source integrations that will be valuable stepping-stones for subsequent development projects that connect IOT devices with Distributed Ledger Technologies. Details about the guidelines can be found on [this site](https://hackathon.iot2tangle.io/hackathon-bases.html)
