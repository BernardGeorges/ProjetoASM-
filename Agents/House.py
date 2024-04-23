from spade import agent
import random

from Behaviours.InformEnergyNeeded_behav import InformEnergyNeeded_behav
from aux_classes.HouseRequest import HouseRequest

class HouseAgent(agent.Agent):

    energyNeeded = {'unoccupied': (5,15), 'occupied': (10,50)}

    async def setup(self):
        print("House Agent starting...")
        self.battery = 0

        behav = InformEnergyNeeded_behav(period=1)
        self.add_behaviour(behav)


    def getNeededEnergy(self, maxTime = 1):
        request = HouseRequest(self.jid, random.uniform(self.energyNeeded['occupied'][0], self.energyNeeded['occupied'][1]), random.randint(1, maxTime))
        return request

