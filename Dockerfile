# Use official ROS 2 Humble image as base
FROM osrf/ros:humble-desktop

# Set up environment variables
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Install essential ROS 2 packages, development tools, and vim
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    build-essential \
    git \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Install ROS 2 dependencies
RUN apt-get update && apt-get install -y \
    ros-humble-rmw-cyclonedds-cpp \
    ros-humble-ros-base \
    ros-humble-ros-workspace \
    ros-humble-demo-nodes-py \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /root/ros2_ws/src

# Build the workspace (this will be done on the host side)
CMD ["/bin/bash"]