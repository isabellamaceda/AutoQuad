from unityagents import UnityEnvironment
import numpy as np
from keras.models import load_model

env = UnityEnvironment(file_name="drone_sim_external", worker_id=0)

num_trajectories = 1
frequency = 4
states_taken = []
actions_taken = []
threshold = 10
model = load_model('trained_model.h5')
for i in range(num_trajectories):
    done = False
    env.reset(train_mode=True)
    states = np.zeros((1, 13))
    while not done:
        action = model.predict(states)
        print(action)
        brainInf = env.step(action)['DroneBrain']
        states = brainInf.states
        norm = np.linalg.norm(states[0][3:6] - states[0][9:12])
        print(norm)

