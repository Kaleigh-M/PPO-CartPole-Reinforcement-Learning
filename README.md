## PPO CartPole Reinforcement Learning

This project demonstrates how to train a reinforcement learning model using Proximal Policy Optimization (PPO) on the CartPole-v1 environment. The code uses the stable-baselines3 library and Gymnasium to train, save, and test the model.
Prerequisites

Before running the code, ensure you have the following libraries installed:

- gymnasium
- stable-baselines3

You can install these libraries using pip:


    pip install gymnasium stable-baselines3


## Description

This script trains a reinforcement learning agent to balance a pole on a cart using the PPO algorithm. The environment used is CartPole-v1, a classic control problem where the goal is to keep the pole upright by moving the cart left or right.
Key Steps:

  Environment Creation: The CartPole-v1 environment is created using gymnasium.

  Environment Wrapping: The environment is wrapped with DummyVecEnv, which is necessary for parallel processing with stable-baselines3.

  Model Initialization: The PPO model is initialized with a Multi-Layer Perceptron (MLP) policy.

  Model Training: The model is trained for 10,000 timesteps.

  Model Saving: After training, the model is saved to a file named ppo_cartpole.

  Model Loading: The saved model is loaded for testing.

  Model Testing: The trained model is tested in the environment for 1,000 steps, where it attempts to balance the pole.


## Running the Code

To run the code:

 - Clone the repository or copy the script to your local machine.

 - Make sure you have the necessary dependencies installed (see Prerequisites).

  Run the script using Python:


    python ppo_cartpole.py

## Saving and Loading the Model

  The model is saved to a file named ppo_cartpole after training.
  The model can be loaded using PPO.load('ppo_cartpole') for further testing or evaluation.

## Testing the Trained Model

The trained model is tested by running it in the CartPole-v1 environment for 1,000 steps. The environment is rendered to visualize the agent's performance.
Environment Render

The environment is rendered during testing to provide a visual representation of the CartPole balancing task. The render_mode='human' parameter is specified when creating the environment to enable rendering.
Closing the Environment

The environment is closed at the end of the script to free up resources.
