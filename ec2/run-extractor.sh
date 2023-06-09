#!/bin/bash

start_number=0
end_number=20

for ((container_number = start_number; container_number <= end_number; container_number++)); do
    docker run --name leetcode_$container_number -v /home/ec2-user/data:/app/data -v /home/ec2-user/screenshots:/app/screenshots ahilio/leetcode-linux:1 $container_number
    docker wait leetcode_$container_number
    # docker rm leetcode_$container_number
done