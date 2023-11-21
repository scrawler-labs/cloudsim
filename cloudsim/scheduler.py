from pysimcloud.entities.entity import Entity

class CloudletScheduler(Entity):
    def __init__(self, env, datacenter):
        super().__init__()
        self.env = env
        self.vm_list = datacenter.vm_list
        self.free_vms = [vm for vm in self.vm_list]  # Initially, all VMs are free
        self.running_vms = []
        self.clock_time = 0

    def schedule_cloudlets(self, cloudlets):
       processes = [self.env.process(self.schedule_cloudlet(cloudlet)) for cloudlet in cloudlets]        
       yield self.env.all_of(processes)

    def schedule_cloudlet(self, cloudlet):
        # Place the cloudlet on hold until a free VM with enough available resources becomes available
        while True:
            selected_vm = next((vm for vm in self.free_vms if self.has_enough_resources(vm, cloudlet)), None)
            if selected_vm:
                self.free_vms.remove(selected_vm)
                cloudlet.set_vm(selected_vm)
                self.running_vms.append(selected_vm)
                yield self.env.process(self.execute_cloudlet(cloudlet))
                break
            else:
                yield self.env.timeout(1)

    def has_enough_resources(self, vm, cloudlet):
        return vm.pes_number >= cloudlet.pes_number and vm.ram >= cloudlet.file_size and vm.size >= cloudlet.output_size

    def execute_cloudlet(self, cloudlet):
        print(f"Cloudlet {cloudlet.cloudlet_id} starts execution on VM {cloudlet.get_vm().get_id()} at {self.env.now}")
        yield self.env.timeout(cloudlet.length)
        print(f"Cloudlet {cloudlet.cloudlet_id} completes execution on VM {cloudlet.get_vm().get_id()} at {self.env.now}")
        # As soon as the cloudlet finishes executing, add the VM back to free_vms
        self.free_vms.append(cloudlet.get_vm())
        self.running_vms.remove(cloudlet.get_vm())


    def get_clock_time(self):
        return self.env.now