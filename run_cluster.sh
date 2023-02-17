#!/bin/bash

# create new network
docker network create hadoop_network

# build docker image dengan nama image hadoop-base:3.3.1
# kemudian mencari file bernama dockerfile
docker build -t hadoop-base:3.3.1 .
# running image menjadi container
#-d untuk berjalan di background
docker-compose up -d