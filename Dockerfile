# Use official ROS 2 Humble image as base
FROM osrf/ros:humble-desktop

# Set up environment variables
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# Install essential ROS 2 packages and tools
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install ROS 2 dependencies and development tools
RUN apt-get update && apt-get install -y \
    ros-humble-rmw-cyclonedds-cpp \
    ros-humble-ros-base \
    ros-humble-ros-workspace \
    ros-humble-demo-nodes-cpp \
    && rm -rf /var/lib/apt/lists/*

# Source ROS 2 setup script automatically when the container is started
SHELL ["/bin/bash", "-c"]
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

# Set default entrypoint
CMD ["/bin/bash"]