"""
Minimal RL Training Demo: PPO on CartPole
Run: source .hermes/venvs/rl-experiment/bin/activate && python3 rl_demo.py

This is your first step into embodied RL. CartPole is a toy problem,
but the same code structure scales to robot locomotion (HalfCheetah, Ant, Humanoid)
when you have a GPU machine.
"""

import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import EvalCallback
import numpy as np

# 1. Create environment
env = gym.make("CartPole-v1")
eval_env = gym.make("CartPole-v1")

# 2. Create PPO agent
model = PPO(
    "MlpPolicy",
    env,
    verbose=1,
    learning_rate=3e-4,
    n_steps=2048,
    batch_size=64,
    n_epochs=10,
    gamma=0.99,
    gae_lambda=0.95,
    clip_range=0.2,
    ent_coef=0.0,
    tensorboard_log="./tb_logs/",
)

# 3. Train (takes ~2-3 minutes on this CPU)
print("=" * 50)
print("Training PPO on CartPole-v1...")
print("Goal: balance the pole for 500 steps (episode length)")
print("=" * 50)

model.learn(total_timesteps=20000, progress_bar=True)

# 4. Evaluate
print("\n" + "=" * 50)
print("Evaluating trained agent...")
print("=" * 50)

episode_rewards = []
for ep in range(20):
    obs, _ = eval_env.reset()
    done = False
    total_rew = 0
    while not done:
        action, _ = model.predict(obs, deterministic=True)
        obs, rew, term, trunc, _ = eval_env.step(action)
        total_rew += rew
        done = term or trunc
    episode_rewards.append(total_rew)
    print(f"Episode {ep+1}: reward = {total_rew:.0f}")

avg_reward = np.mean(episode_rewards)
print(f"\nAverage reward over 20 episodes: {avg_reward:.1f}")
print(f"CartPole solved threshold: 475.0")
print(f"{'✅ SOLVED!' if avg_reward > 475 else '❌ Not yet solved'}")

env.close()
eval_env.close()

# 5. Save model
model.save("./cartpole_ppo")
print("\nModel saved to ./cartpole_ppo.zip")
print("Load with: model = PPO.load('./cartpole_ppo')")
