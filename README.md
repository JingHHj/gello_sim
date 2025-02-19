# Gello_sim
This project is aiming at load gello model into MuJoCo and connect it with certain robot arm. [GELLO](https://wuphilipp.github.io/gello_site/) is a general framework for building low-cost and intuitive teleoperation systems for robotic manipulation. For further information, you can find it here: [Software] (https://github.com/wuphilipp/gello_software) and [Hardware] (https://github.com/wuphilipp/gello_mechanical). 
* `UR5`: contains STL meshes and XML file that needed to run the the [UR5 arm model](https://github.com/google-deepmind/mujoco_menagerie/tree/main/universal_robots_ur5e) and its gello model
    * `UR5/ur5`: contains meshes and XML file for the general UR5 arm
    * `UR5/gello_ur5`: contains meshes and XML file for the gello ur5 
    * `UR5/ur5_scene.xml`: An overall XML file that contain both the robot arm and its xml file

* `AgileX_Piper`: contains STL meshes and XML file that needed to run the the AgileX Piper arm model and its gello model (Have not uplaoded yet)
    * `AgileX_Piper/mesher`: contains all the meshes of AgileX Piper(including original urdf discription) and AgileX Piper gello 
    * `AgileX_Piper/agilex_piper.xml`: xml discription of original aiglex piper arm
    * `AgileX_Piper/agilex_piper.xml`: xml discription of gello aiglex piper arm
    * `AgileX_Piper/piper_scene.xml`:` An overall XML file that contain both the robot arm 
* `main.py`: The main script to run the simulation

# Launch Simulation
* For UR5 model
```
python main.py 
--model ur5
--info True  ## To print out the joints info
```

* For AgileX Piper model 
```
python main.py 
--model agilex_piper
--info True  ## To print out the joints info
```


- Now you after you launch the simulatiuon, you can double click the end effector to select it and move it with right mouse while pressing ctrl!
- For more information you can press F1 or go to left UI `option`->`help`



