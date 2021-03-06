import gym
from gym import spaces
from gym.utils import seeding
import numpy as np

class KArmedBanditsEnv(gym.Env):
	
	'''
	k-armed bandits environment (chapter-2, from the book Reinforcement Learning: 
	An Inroduction, Richard S. Sutton & Andrew G. Barto)

	True Action values [i.e q*(a), a = 1 to k] are sampled from a standard Gaussian/Normal distribution i.e N(0,1).
	Reward values sampled from the N(mean(q*(A_t),1) distribution.
	'''

	metadata={'render.modes':['human']}
	
	def __init__(self,k=10):
		self.k = k
		self.action_vals = [np.random.normal(0,1) for i in range(self.k)]
		self.action_space = spaces.Discrete(self.k)
		self.observation_space = spaces.Discrete(1)
		self.done = False
		self._seed()

	def _seed(self, seed=None):
		self.np_random, seed = seeding.np_random(seed)
		return([seed])

	def step(self,action):
		assert self.action_space.contains(action), "%r (%s) invalid"%(action, type(action))
		self.done = True
		reward = np.random.normal(self.action_vals[action],1)
		return(0,reward,self.done,None)

	def reset(self):
		self.done = False

	def render(self):
		pass
		
