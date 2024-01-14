import numpy as np

class Agent:
    def __init__(self, environment_size):
        self.environment_size = environment_size
        self.belief_environment = np.ones((environment_size, environment_size)) / (environment_size**2)
        self.belief_self = np.ones(2) / 2  # Two possible self-states (e.g., awake or asleep)

    def update_belief_environment(self, sensory_input):
        # Bayesian update of belief about the environment based on sensory input
        self.belief_environment = self.belief_environment * sensory_input
        self.belief_environment /= np.sum(self.belief_environment)

    def select_action(self):
        # Simple action selection, e.g., move in a random direction
        return np.random.choice(['up', 'down', 'left', 'right'])

    def update_belief_self(self, self_action):
        # Bayesian update of belief about self based on the action taken
        # This can represent the agent's understanding of how its actions affect itself
        pass  # This can be extended based on specific scenarios

# Example usage
environment_size = 5
agent = Agent(environment_size)

# Simulate agent-environment interaction
for _ in range(10):
    sensory_input = np.random.rand(environment_size, environment_size)
    agent.update_belief_environment(sensory_input)
    action = agent.select_action()
    agent.update_belief_self(action)

# Visualize beliefs (for illustration, not a complete visualization)
print("Belief about Environment:")
print(agent.belief_environment)
print("Belief about Self:")
print(agent.belief_self)