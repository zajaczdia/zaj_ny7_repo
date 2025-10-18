# `speed_monitor` package
ROS 2 python package.  [![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)
## Packages and build

It is assumed that the workspace is `~/ros2_ws/`.

### Clone the packages
``` r
cd ~/ros2_ws/src
```
``` r
git clone https://github.com/zajaczdia/zaj_ny7_repo
```

### Build ROS 2 packages
``` r
cd ~/ros2_ws
```
``` r
colcon build --packages-select speed_monitor --symlink-install
```

<details>
<summary> Don't forget to source before ROS commands.</summary>

``` bash
source ~/ros2_ws/install/setup.bash
```
</details>

``` r
ros2 launch speed_monitor speed_monitor_launch.py
```
A package két node-ból áll. Az első a speed_generator node, aminek a feladata szimulálni a jármű sebességét véletlenszerűen 0-130 km/h között. A sebességet a speed_data topicban hirdeti (std_msgs/msg/Float32). A második node a speed_observer, aminek a feladata a speed_data topicot figyelni és ha a sebesség meghaladja a 90 km/h-t, akkor figyelmeztetést ad a felhasználónak. Ez a node az alert topicban hirdet (std_msgs/msg/String).
```mermaid
    graph TD
        A[Package: speed_monitor] --- B[Node: speed_generator]
        A --- C[Node: speed_observer]


        B -- Publishes --> D[(Topic: /speed_data<br/>Type: std_msgs/msg/Float32)]
        C -- Subscribes --> D


        subgraph "speed_monitor package"
            B:::publisher
            C:::subscriber
    end
