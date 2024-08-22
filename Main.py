import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv

# Create CartPole-v1 environment
env = gym.make('CartPole-v1', render_mode='human')  # Specify render_mode

# Wrap the environment in DummyVecEnv
env = DummyVecEnv([lambda: env])

# Start the PPO model with a Multi-Layer Perceptron policy
model = PPO('MlpPolicy', env, verbose=1)

model.learn(total_timesteps=10000)

# Save the trained model
model.save('ppo_cartpole')

# Load the model
model = PPO.load('ppo_cartpole')

# Test the trained model
obs = env.reset()
for _ in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, rewards, done, info = env.step(action)
    env.render()  # Render the environment
    if done:
        obs = env.reset()

env.close()
