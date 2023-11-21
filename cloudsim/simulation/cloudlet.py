#simulate cloud load using datacenter and simpy tool
import simpy
from cloudsim.entities.datacenter import Datacenter
from cloudsim.scheduler import CloudletScheduler

class CloudletExecution:
    def __init__(self, cloudlet_list,datacenter):
        self.cloudlet_list = cloudlet_list
        self.env = simpy.Environment()
        self.scheduler = CloudletScheduler(self.env,datacenter)
       

    def execute(self):
        self.env.process(self.scheduler.schedule_cloudlets(self.cloudlet_list))
        self.env.run()
