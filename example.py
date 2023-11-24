from cloudsim.entities.datacenter import Datacenter, DatacenterCharacteristics
from collections import deque
from cloudsim.entities.vm import Vm
from cloudsim.entities.host import Host
from cloudsim.entities.pe import Pe
from cloudsim.entities.cloudlet import Cloudlet
from cloudsim.simulation.cloudlet import CloudletExecution

def create_datacenter(name):
    # Create a list to store the host machines
    host_list = []

    # Create PEs (Processing Elements) and add them to the list
    pe_list = [Pe(1000), Pe(1000), Pe(1000)]  # Assuming MIPS value is 1000

    # Create a Host with its specifications and add it to the list
    ram = 2048  # Host memory (MB)
    storage = 1000000  # Host storage
    bw = 10000

    host_list.append(
        Host(
            ram,
            bw,
            storage,
            pe_list
        )
    )  # This is our host machine

    # Create a DatacenterCharacteristics object
    arch = "x86"
    os = "Linux"
    vmm = "Xen"
    time_zone = 10.0
    cost = 3.0
    cost_per_mem = 0.05
    cost_per_storage = 0.001
    cost_per_bw = 0.0
    storage_list = deque()  # We are not adding SAN devices for now

    characteristics = DatacenterCharacteristics(
        arch, os, vmm, host_list, time_zone, cost, cost_per_mem, cost_per_storage, cost_per_bw
    )

    # Finally, create a Datacenter object
    datacenter = Datacenter(name, characteristics, None, storage_list, 0)

    return datacenter

# Example usage:
datacenter_instance = create_datacenter("MyDatacenter")

broker_id = datacenter_instance.get_broker_id()  

# Create a list to store the VMs
vmlist = []

# VM specifications
mips = 250
size = 10000  # Image size (MB)
ram = 1024  # VM memory (MB)
bw = 2000
pes_number = 1  # Number of CPUs
vmm = "Xen"  # VMM name

# Create two VMs
vm1 = Vm(broker_id, mips, pes_number, ram, bw, size, vmm)
vm2 = Vm(broker_id, mips * 2, pes_number * 2, ram, bw, size, vmm)

# Add the VMs to the vmList
vmlist.extend([vm1, vm2])

# Set the VMs for the datacenter
datacenter_instance.set_vms(vmlist)

# Display details of the datacenter and calculate total cost
datacenter_instance.get_details()
datacenter_instance.get_total_cost()

# Create a list of Cloudlets
cloudlet1 = Cloudlet(length=10, pes_number=1, file_size=50, output_size=50)
cloudlet2 = Cloudlet(length=15, pes_number=2, file_size=100, output_size=100)
cloudlet3 = Cloudlet(length=8, pes_number=1, file_size=30, output_size=30)

cloudlet_list = [cloudlet1, cloudlet2, cloudlet3]

# Execute the Cloudlets in the datacenter
cloudlet_execution = CloudletExecution("FCFS",cloudlet_list, datacenter_instance)
cloudlet_execution.execute()

cloudlet_execution = CloudletExecution("SJF",cloudlet_list, datacenter_instance)
cloudlet_execution.execute()