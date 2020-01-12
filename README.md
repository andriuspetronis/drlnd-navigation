# Project: Navigation

The goal of this project project is to train an agent to navigate (and collect bananas!) in a large, square world.

![Alt Text](https://video.udacity-data.com/topher/2018/June/5b1ab4b0_banana/banana.gif)

### Project Details

**State:** The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction.

**Action:** The agent has to learn how to best select actions. Four discrete actions are available, corresponding to:

`0` - move forward.  
`1` - move backward.  
`2` - turn left.  
`3` - turn right.  

**Reward:** A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.

**Solution:** The task is episodic, and in order to solve the environment, your agent must get an average score of +13 over 100 consecutive episodes.


### Getting Started
For this project, you could download a pre-built Unity environment from one of the links below. You need only select the environment that matches your operating system:

- Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
- Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
- Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
- Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)

Then, place the file in the `data/` folder in the DRLND GitHub repository, and unzip (or decompress) the file.

(*For Windows users*) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

(*For AWS*) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux_NoVis.zip) to obtain the "headless" version of the environment. You will not be able to watch the agent without enabling a virtual screen, but you will be able to train the agent. (*To watch the agent, you should follow the instructions to [enable a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md), and then download the environment for the Linux operating system above.*)

**Further setup steps to run code locally:**

1. Create a new environment:
```
conda create --name drlnd python=3.6
source activate drlnd
```
2. Install Jupyter notebook:
```
conda install jupyter notebook
```
3. Place extracted `Banana_Linux` folder in the `data/` directory:
```
./data/Banana_Linux/Banana.x86_64
```


### Instructions
Follow the instructions in Navigation.ipynb to get started with training your own agent!

**Note:** The original notebook has been trained on the Udacity DRLND workspace with GPU, so it might take a lot of time to train the algorithm locally wih CPU. Here is the specific line for training the agent:

```
scores = dqn()
```

**Reference:** [Udacity Deep Reinforcement Learning Nanodegree Program](https://www.udacity.com/course/deep-reinforcement-learning-nanodegree--nd893)