#!/bin/bash

start_number=1
end_number=90

for ((container_number = start_number; container_number <= end_number; container_number++)); do
    docker run --name leetcode_$container_number -v /home/ec2-user/data:/app/data ahilio/leetcode-linux:1 $container_number
    docker wait leetcode_$container_number
    docker rm leetcode_$container_number
done