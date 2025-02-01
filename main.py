import mujoco
import mujoco.viewer as viewer
import argparse

def main(xml_path):
    
    # Load the model and data
    model = mujoco.MjModel.from_xml_path(xml_path)
    data = mujoco.MjData(model)

    
    # Launch the viewer
    with mujoco.viewer.launch_passive(model, data) as viewer:
        while viewer.is_running():

            # teleoperation
            for i in range(6):
                data.qpos[i+6] = data.qpos[i]
            mujoco.mj_step(model, data)
   
            viewer.sync()


def print_info(xnl_path): 
    """
        Print the robot joints info
    """
    model = mujoco.MjModel.from_xml_path(xml_path)
    data = mujoco.MjData(model)
    for i in range(model.nq):
        joint_name = model.joint(i).name
        joint_position = data.qpos[i]
        print(f"Joint ID: {i}, Name: {joint_name}, Position: {joint_position}")


def test(xml_path):
    """
        Doing the easiest test run
    """
    model = mujoco.MjModel.from_xml_path(xml_path)
    data = mujoco.MjData(model)
    viewer.launch(model, data)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', default='ur5', type=str)
    parser.add_argument("--info", default=False, type=bool)
    args = parser.parse_args()

    if args.model == 'agilex_piper':
        xml_path = "./agilex_piper.xml"
    elif args.model == 'ur5':
        xml_path = "./UR5/scene.xml"

    if args.info:
        print_info(xml_path)

    main(xml_path)


    
    # test(xml_path)
    

    