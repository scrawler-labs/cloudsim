#simulate cloud load using datacenter and simpy tool
import simpy
from cloudsim.schedulers.fcfs import CloudletSchedulerFCFS
from cloudsim.schedulers.sjf import CloudletSchedulerSJF

class CloudletExecution:
    def __init__(self,schedular,cloudlet_list,datacenter):
        self.cloudlet_list = cloudlet_list
        self.scheduler = schedular
        self.env = simpy.Environment()
        if self.scheduler == "FCFS":
            self.scheduler_instance = CloudletSchedulerFCFS(self.env,datacenter)
        if self.scheduler == "SJF":
            self.scheduler_instance = CloudletSchedulerSJF(self.env,datacenter)

       

    def execute(self):
        print(f"Using {self.scheduler} scheduler \n")
        self.env.process(self.scheduler_instance.schedule_cloudlets(self.cloudlet_list))
        self.env.run()
