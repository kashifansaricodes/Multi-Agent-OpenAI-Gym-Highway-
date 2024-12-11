import pprint
import gymnasium
import highway_env
from matplotlib import pyplot as plt
# Instead of %matplotlib inline, use this:
plt.ion()  # Turn on interactive mode

env = gymnasium.make('highway-v0', render_mode='rgb_array')
# env.unwrapped.config["lanes_count"] = 2
env.reset()
for _ in range(3):
    action = env.unwrapped.action_type.actions_indexes["IDLE"]
    obs, reward, done, truncated, info = env.step(action)
    env.render()

plt.imshow(env.render())
plt.show()

pprint.pprint(env.unwrapped.config)