from pysimcloud.entities.datacenter import Datacenter, DatacenterCharacteristics
from collections import deque
from pysimcloud.entities.vm import Vm
from pysimcloud.entities.host import Host
from pysimcloud.entities.pe import Pe

def create_datacenter(name):
    # 1. Create a list to store our machine
    host_list = []

    # 2. Create PEs and add these into a list.
    pe_list = [Pe(1000),Pe(1000)]  # Assuming mips value is 1000

    # 3. Create Host with its id and list of PEs and add them to the list of machines
    ram = 2048  # host memory (MB)
    storage = 1000000  # host storage
    bw = 10000

    host_list.append(
        Host(
            ram,
            bw,
            storage,
            pe_list
        )
    )  # This is our machine

    # 5. Create a DatacenterCharacteristics object
    arch = "x86"
    os = "Linux"
    vmm = "Xen"
    time_zone = 10.0
    cost = 3.0
    cost_per_mem = 0.05
    cost_per_storage = 0.001
    cost_per_bw = 0.0
    storage_list = deque()  # we are not adding SAN devices by now

    characteristics = DatacenterCharacteristics(
        arch, os, vmm, host_list, time_zone, cost, cost_per_mem, cost_per_storage, cost_per_bw
    )

    # 6. Finally, create a Datacenter object.
    datacenter = None
  
    datacenter = Datacenter(name, characteristics, None, storage_list, 0)
   

    return datacenter

# Example usage:
datacenter_instance = create_datacenter("MyDatacenter")

# Assuming you already have brokerId from somewhere
broker_id = datacenter_instance.get_broker_id()  

vmlist = []

# VM description
mips = 250
size = 10000  # image size (MB)
ram = 1024  # vm memory (MB)
bw = 2000
pes_number = 1  # number of cpus
vmm = "Xen"  # VMM name

# create two VMs
vm1 = Vm(broker_id, mips, pes_number, ram, bw, size, vmm, None)  # Replace None with the appropriate CloudletScheduler
vm2 = Vm(broker_id, mips * 2, pes_number, ram, bw, size, vmm, None)  # Replace None with the appropriate CloudletScheduler

# add the VMs to the vmList
vmlist.append(vm1)
vmlist.append(vm2)

datacenter_instance.set_vms(vmlist)

datacenter_instance.get_details()
