from pysimcloud.entities.entity import Entity

class Broker(Entity):
    def __init__(self,datacenter):
        super().__init__()
        self.broker_id = super().getId()
        self.datacenter = datacenter
        self.host_list = datacenter.get_host_list()

    def assign_vm_to_host(self, vm):

        # Check if there is any host with enough resources to accommodate the new VM
        available_hosts = [host for host in self.host_list if host.has_enough_resources(vm)]

        if not available_hosts:
            raise ValueError("No available host with enough resources to allocate VM.")
        # Find the host with the most available resources
        selected_host = max(self.host_list, key=lambda host: host.available_resources())

        # Assign the VM to the selected host
        selected_host.assign_vm(vm)