# ROS2_basic
Implementing a basic ros humble publisher and subscriber 

# Goal
Given two ROS topics /input(msgs/Int8MultiArray) and /target (msgs/Int8), return the indices of two numbers that add up to target from input in ROS topic /solution

# Solution
We use Docker for cross platform compatibility 
Steps to build and run the docker:
1) Build the docker image: docker build -t <docker name: will use ros2_custom_topics> .
2) Running the container (mounts the local directory): docker run -it --rm -v "$(pwd)/ros2_ws:/root/ros2_ws" <docker name: ros2_custom_topics> 
3) Starting additional sessions: docker exec -it <docker name: ros2_custom_topics> bash

Steps to build new changes:
1) go to directory: cd /root/ros2_ws
2) build: colcon build
3) source the new install: source ~/ros2_ws/install/setup.bash

Commands to run in each terminal:
1) data publisher: ros2 run custom_topics data_publisher
2) solution publisher: ros2 run custom_topics solution_publisher