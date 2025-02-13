# Gello_sim
This project is aiming at load gello model into MuJoCo and connect it with certain robot arm. [GELLO](https://wuphilipp.github.io/gello_site/) is a general framework for building low-cost and intuitive teleoperation systems for robotic manipulation. For further information, you can find it here: [Software](https://github.com/wuphilipp/gello_software) and [Hardware](https://github.com/wuphilipp/gello_mechanical). 
* `UR5`: contains STL meshes and XML file that needed to run the the [UR5 arm model](https://github.com/google-deepmind/mujoco_menagerie/tree/main/universal_robots_ur5e) and its gello model
    * `UR5/ur5`: contains meshes and XML file for the general UR5 arm
    * `UR5/gello_ur5`: contains meshes and XML file for the gello ur5 
    * `UR5/scene.xml`: An overall XML file that contain both the robot arm and its xml file

* `AgileX_Piper`: contains STL meshes and XML file that needed to run the the [AgileX Piper arm](https://github.com/agilexrobotics/Piper_ros) model and its gello model (Have not uplaoded yet)
* `main.py`: The main script to run the simulation

# Launch Simulation
* For UR5 model
```
python main.py 
--model ur5
--info True  ## To print out the joints info
```

* For AgileX Piper model (Have not uplaoded yet)
```
python main.py 
--model agilex_piper
--info True  ## To print out the joints info
```


- Now you after you launch the simulatiuon, you can double click the end effector to select it and move it with right mouse while pressing ctrl!
- For more information you can press F1 or go to left UI `option`->`help`



