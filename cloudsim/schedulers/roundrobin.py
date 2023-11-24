from cloudsim.schedulers.cloudlet_scheduler import CloudletScheduler

class CloudletSchedulerRoundRobin(CloudletScheduler):
    def __init__(self, env, datacenter, time_slice=1):
        super().__init__(env, datacenter)
        self.time_slice = time_slice
        self.total_execution_time = 0
        self.total_turn_around_time = 0

    def schedule_cloudlets(self, cloudlets):
        remaining_cloudlets = list(cloudlets)
        while remaining_cloudlets:
            for cloudlet in remaining_cloudlets[:]:
                yield self.env.process(self.schedule_cloudlet(cloudlet))
                remaining_cloudlets.remove(cloudlet)

        for vm in self.max_utilization:
            print(f"\nVM {vm} utilization:\n {self.max_utilization[vm][0] * 100}% PEs\n, {self.max_utilization[vm][1] * 100}% RAM\n, {self.max_utilization[vm][2] *100}% Storage")

        print(f"\nTotal Execution Time: {self.total_execution_time}")

    def schedule_cloudlet(self, cloudlet):
        while cloudlet.length > 0:
            for selected_vm in self.free_vms[:]:
                if self.has_enough_resources(selected_vm, cloudlet):
                    self.free_vms.remove(selected_vm)
                    cloudlet.set_vm(selected_vm)
                    self.running_vms.append(selected_vm)
                    self.max_utilization[selected_vm.get_id()] = max(self.max_utilization[selected_vm.get_id()],
                                                                     self.get_utilization(selected_vm, cloudlet))
                    
                    print(f"Cloudlet {cloudlet.cloudlet_id} starts execution on VM {cloudlet.get_vm().get_id()} at {self.env.now}")

                    execution_time = min(self.time_slice, cloudlet.length)
                    yield self.env.timeout(execution_time)
                    cloudlet.length -= execution_time

                    print(f"Cloudlet {cloudlet.cloudlet_id} completes execution on VM {cloudlet.get_vm().get_id()} at {self.env.now}")

                    self.running_vms.remove(selected_vm)
                    self.free_vms.append(selected_vm)

                    self.total_execution_time += execution_time
                    break
            else:
                yield self.env.timeout(1)
