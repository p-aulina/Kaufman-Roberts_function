# Kaufman-Roberts function
This code calculates following data in a fully accessible system with multi-service traffic:
- blocking probability, 
- occupancy probability distribution,
- average number of requests per occupation state.

## Purpose
Kaufman-Roberts is a multi-dimentional Erlang method used in ICT systems that enable multiple services share a common resource pool. It computes the probability of blocking when the total capacity of a link is composed of different number of traffic flows or channels, and each flow or channel is smaller than the maximum capacity of the link.

## System parameters
This program requires following input data:
- a_min - minimum traffic offered per one unit of system capacity
- a_max - maximum traffic offered per one unit of system capacity
- a_step - calculation step
- C - system capacity
- t - requests
- m - class (number of request flows)

**Code includes default values of system parameters**

## Saving output
Output is written in .txt files that are created automatically after running the program:
- blocking.txt - blocking probability,
- occupancy.txt - occupancy probability distribution,
- requests.txt - average number of requests per occupation state.

**With every run the program overwrites data in each .txt file.**