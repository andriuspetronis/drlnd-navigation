# Project: Navigation

The goal of this project project is to train an agent to navigate (and collect bananas!) in a large, square world.

![Alt Text](https://video.udacity-data.com/topher/2018/June/5b1ab4b0_banana/banana.gif)


### Learning Algorithm
 Deep Q-Learning algorithm represents the optimal action-value function as a neural network (instead of a table). This is more based to the way the brains work and allows agent to solve more complicated tasks with multiple state values.

Here is an example for a potential [network architecture](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf):

![Model architecture](https://imgur.com/sCI1640.png)

The general idea is to have a high-dimentional sate input, which is then mapped to a set of action values using a neural network architecture. The training process updates weights in order to solve the provided environment and its reward function.

Also, the model uses two additional features in order to address potential instabilities:

- Experience Replay
- Fixed Q-Targets

Please, read the following part for more details.

##### Experience Replay
An issue with the agent interaction with the environment is that experience tuples could be highly correlated. Therefore, learning from sequential observations could bias the model and complicate the learning process. One of the suggested solutions is to keep a *replay buffer* and use it for *experience replay*, which means a random sampling from this buffer in order to avoid issues mentioned before. Also, it becomes possible to learn from individual observations multiple times, including cases that happen relatively rarely.

##### Fixed Q-Targets
Another issue with Q-learning is related to weight updates. More specifically, a guess is updated with another guess, so it makes sense to separate the two processes. To avoid this, we can update the parameters in the network to better approximate the action value corresponding to state and action with the following update rule:

![Q-learnign](https://imgur.com/1VVTIrV.png)

where w<sup>-</sup> are the weights of a separate target network that are not changed during the learning step, and *(S, A, R, S')* is an experience tuple.

**Hyperparameters:**

| Parameter | Value | Description |
|---|---|---|
| n_episodes | 2000 | maximum number of training episodes |
| max_t | 1000 | maximum number of timesteps per episode |
| eps_start | 1.0 | starting value of epsilon, for epsilon-greedy action selection |
| eps_end | 0.01 | minimum value of epsilon |
| eps_decay | 0.995 | multiplicative factor (per episode) for decreasing epsilon |
| BUFFER_SIZE | 1e5 | replay buffer size |
| BATCH_SIZE | 64 | minibatch size |
| TAU | 1e-3 | for soft update of target parameters |
| LR | 5e-4 | learning rate |
| UPDATE_EVERY | 4 | how often to update the network |

**Neural network architecture:**
The neural network consists of two hidden layers (`size = 64`), which help to map 37 different states to 4 actions. Also, it uses a **rectified linear unit (ReLU)** activation function. More information about the network architecture could be found in the `model.py` file. 


### Plot of Rewards
The environment is considered solved after the agent receives an average reward (over 100 episodes) of at least +13. The current architecture allows the agent to solve it over 411 episodes.

```
Episode 100	Average Score: 0.57
Episode 200	Average Score: 4.27
Episode 300	Average Score: 7.86
Episode 400	Average Score: 9.81
Episode 500	Average Score: 12.87
Episode 511	Average Score: 13.02
Environment solved in 411 episodes!	Average Score: 13.02
```

A plot of rewards per episode:

![Rewards plot](https://i.imgur.com/9VSQDxO.png)


### Ideas for Future Work
There are several possible improvements for the current implementation:

- Double DQN
- Prioritized Experience Replay
- Dueling DQN

Please, read the following part for more details.

##### Double DQN

Deep Q-Learning [tends to overestimate](https://www.ri.cmu.edu/pub_files/pub1/thrun_sebastian_1993_1/thrun_sebastian_1993_1.pdf) action values. [Double Q-Learning](https://arxiv.org/abs/1509.06461) has been shown to work well in practice to help with this. The general idea is to decouple sellection of the maximing action value from its evalution using a separate set of weights.

##### Prioritized Experience Replay
Deep Q-Learning samples experience transitions uniformly from a replay memory. [Prioritized experienced replay](https://arxiv.org/abs/1511.05952) is based on the idea that the agent can learn more effectively from some transitions than from others, and the more important transitions should be sampled with higher probability.

##### Dueling DQN
Currently, in order to determine which states are (or are not) valuable, we have to estimate the corresponding action values for each action. However, by replacing the traditional Deep Q-Network (DQN) architecture with a [dueling architecture](https://arxiv.org/abs/1511.06581), we can assess the value of each state, without having to learn the effect of each action.

**Reference:** [Udacity Deep Reinforcement Learning Nanodegree Program](https://www.udacity.com/course/deep-reinforcement-learning-nanodegree--nd893)