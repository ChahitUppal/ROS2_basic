# ROS2_basic
Implementing a basic ros humble publisher and subscriber 

# Goal
Given two ROS topics /input(msgs/Int8MultiArray) and /target (msgs/Int8), return the indices of two numbers that add up to target from input in ROS topic /solution

# Solution
We use Docker for cross platform compatibility 
Steps to build and run the docker:
1) Build the docker image: docker build -t <docker name: will use ros2_custom_topics> .
2) Running the container: docker run -it <docker name: ros2_custom_topics>
3) Starting additional sessions: docker exec -it <docker name: ros2_custom_topics> bash
