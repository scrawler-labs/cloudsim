from pysimcloud.entities.entity import Entity
from pysimcloud.entities.broker import Broker


class DatacenterCharacteristics:
    def __init__(self, arch, os, vmm, host_list, time_zone, cost, cost_per_mem, cost_per_storage, cost_per_bw):
        self.arch = arch
        self.os = os
        self.vmm = vmm
        self.host_list = host_list
        self.time_zone = time_zone
        self.cost = cost
        self.cost_per_mem = cost_per_mem
        self.cost_per_storage = cost_per_storage
        self.cost_per_bw = cost_per_bw
        self.number_of_pes = 0
        self.set_number_of_pes()
        self.id = 0

    def set_number_of_pes(self):
        for host in self.host_list:
            self.number_of_pes += len(host.pe_list)

    def set_id(self, id):
        self.id = id



class Datacenter(Entity):
    def __init__(self, name, characteristics, vm_allocation_policy, storage_list, scheduling_interval):
        super().__init__()
        # Assuming the super() call corresponds to a parent class with a setName() method
        # and getId() method.
        self.setName(name)

        self.characteristics = characteristics
        self.vm_allocation_policy = vm_allocation_policy
        self.last_process_time = 0.0
        self.storage_list = storage_list
        self.vm_list = []
        self.scheduling_interval = scheduling_interval
        self.broker = Broker(self)

        for host in self.characteristics.host_list:
            host.set_datacenter(self)

        if self.characteristics.number_of_pes == 0 and len(self.characteristics.host_list) != 0:
            raise Exception(f"{super().getName()}: Error - this entity has no PEs. Therefore, can't process any Cloudlets.")

        if self.characteristics.number_of_pes != 0 and len(self.characteristics.host_list) != 0:
            print(f"{name}: inter-cloud networking topology created...")

        self.characteristics.set_id(super().getId())

    def set_vms(self, vm_list):
        self.vm_list = vm_list
        for vm in vm_list:
            self.broker.assign_vm_to_host(vm)
    
    def get_host_list(self):
        return self.characteristics.host_list
    
    def get_broker_id(self):
        return self.broker.broker_id
    
    def get_vm_list(self):
        return self.vm_list
    
    def get_total_cost(self):
        print("Datacenter cost: ", self.characteristics.cost)
        memory_cost = self.characteristics.cost_per_mem * sum(host.ram for host in self.characteristics.host_list)
        print("Memory cost: ", memory_cost)
        storage_cost = self.characteristics.cost_per_storage * sum(host.storage for host in self.characteristics.host_list)
        print("Storage cost: ", storage_cost)
        bw_cost = self.characteristics.cost_per_bw * sum(host.bw for host in self.characteristics.host_list)
        print("Bandwidth cost: ", bw_cost)
        total_cost = self.characteristics.cost + memory_cost + storage_cost + bw_cost
        print("Total cost: ", total_cost)
        print()

    
    def get_details(self):
         print(f"Datacenter name: {self.name}\n Number of hosts: {len(self.get_host_list())}\n Number of VMs: {len(self.get_vm_list())}")
         for host in self.get_host_list():
            host.get_details()



