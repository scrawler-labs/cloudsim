# Cloudsim
A platform to simulate cloud enviornment using simpy as simulation engine
To learn more about usage please see `example.py`
you can clone the repository and run exmple using following 
```bash
git clone git@github.com:cloudsim-py/cloudsim.git
pip install simpy
python example.py
```

## Entity
Cloudsi-py has the following entitiy to build your cloud enviornment 

### PE (Processing Element.)
A Processing Element (PE) is a fundamental unit of computation within a computer system, executing instructions to perform operations on data. An individual host can have one or more PEs, collectively contributing to its processing capabilities.

Example of creating PE
```python
mips = 1000  # MIPS (Million Instructions Per Second) rating of the computing resource
pe = PE(mips)
```
### Host
A host is a computing entity that provides resources, such as processing power, memory, storage, and bandwidth, within a computer system. It serves as a platform for running VM.
A datacenter can have one or more hosts, each contributing to its computational capacity.
A host can run multiple VM

Example of host properties:
```python
pe_list = []            # List to store processing elements (PEs) in a host
ram = 2048              # Host memory capacity in megabytes (MB)
storage = 1000000       # Host storage capacity in megabytes (MB)
bw = 10000              # Host bandwidth capacity in megabits per second (Mbps)
```
Example for creating host:
```python
 pe_list = [Pe(1000),Pe(1000),Pe(1000)]  # Assuming mips value is 1000

ram = 2048  # host memory (MB)
storage = 1000000  # host storage
bw = 10000

$host = Host(ram, bw, storage, pe_list)

```

### Datacenter
A datacenter is a central facility that stores, manages, and processes data. It houses hosts with resources like processing power and storage. 

Example of datcenter properties:
```python
host_list = [],        # List to store host machines in the datacenter
arch = "x86"           # Architecture of the datacenter (e.g., x86)
os = "Linux"           # Operating system of the datacenter (e.g., Linux)
vmm = "Xen"            # Virtual machine monitor (e.g., Xen)
time_zone = 10.0       # Time zone of the datacenter
cost = 3.0             # Overall cost of the datacenter
cost_per_mem = 0.05    # Cost per unit of memory in the datacenter
cost_per_storage = 0.001  # Cost per unit of storage in the datacenter
cost_per_bw = 0.0      # Cost per unit of bandwidth in the datacenter
storage_list = []      # List to store storage devices in the datacenter

```
Example for creating datacenter:
```python
def create_datacenter(name):
    # 1. Create a list to store our machine
    host_list = []

    # 2. Create PEs and add these into a list.
    pe_list = [Pe(1000),Pe(1000),Pe(1000)]  # Assuming mips value is 1000

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

```
### VM
Virtual Machine (VM) acts as a virtualized computing instance for running applications (cloudlets). It emulates the behavior of a physical machine, facilitating efficient resource allocation and management within the simulated cloud environment.

Example of VM properties:
```python
mips = 250
size = 10000  # image size (MB)
ram = 1024  # vm memory (MB)
bw = 2000
pes_number = 1  # number of cpus
vmm = "Xen" 
```
Example for creating vm:
```python
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
vm1 = Vm(broker_id, mips, pes_number, ram, bw, size, vmm)  # Replace None with the appropriate CloudletScheduler
vm2 = Vm(broker_id, mips * 2, pes_number*2, ram, bw, size, vmm)  # Replace None with the appropriate CloudletScheduler

# add the VMs to the vmList
vmlist.append(vm1)
vmlist.append(vm2)
```


### Cloudlet 
A cloudlet is akin to an application that runs on a virtual machine (VM). It represents a specific computing task or set of tasks offloaded to the cloud for execution.

Example of cloudlet properties:
```python
length = 10        # Duration of the cloudlet's execution in simulation time units.
pes_number = 1     # Number of Processing Elements (PEs) required for the cloudlet.
file_size = 50     # Size of the input file associated with the cloudlet (e.g., in megabytes).
output_size = 50   # Size of the output file produced by the cloudlet (e.g., in megabytes).
```

Example for creating datacenter:
```python
cloudlet1 = Cloudlet( length=10, pes_number=1, file_size=50, output_size=50)
cloudlet2 = Cloudlet( length=15, pes_number=2, file_size=100, output_size=100)
cloudlet3 = Cloudlet( length=8, pes_number=1, file_size=30, output_size=30)
```

## Simulation / Feature
simcloud-py provides following simulations / Feature

### Getting details of datacenter
Example usage :
```python
datacenter_instance.get_details()
```

Example output:
```
Datacenter name: MyDatacenter
Number of hosts: 1
Number of VMs: 2

Host ID: 0c05847d-d7b1-4685-875b-8297bd480830
RAM: 2048
BW: 10000
Storage: 1000000
PEs: 3)

VM ID: 4bcbc66d-4d22-4eda-8a1c-63e12399da58
MIPS: 250
PEs: 1
RAM: 1024
BW: 2000
Size: 10000
VMM: Xen

VM ID: 94244787-3503-4981-8ff6-8e8dd47d8693
MIPS: 500
PEs: 2
RAM: 1024
BW: 2000
Size: 10000
VMM: Xen
```

### Getting cost of datacenter

Example usage:
```python
datacenter_instance.get_total_cost()
```

Example output:
```
Datacenter cost:  3.0
Memory cost:  102.4
Storage cost:  1000.0
Bandwidth cost:  0.0
Total cost:  1105.4
```

### Simulating cloudlet Execution
```python
# Create a list of Cloudlets
cloudlet1 = Cloudlet(length=10, pes_number=1, file_size=50, output_size=50)
cloudlet2 = Cloudlet(length=15, pes_number=2, file_size=100, output_size=100)
cloudlet3 = Cloudlet(length=8, pes_number=1, file_size=30, output_size=30)

cloudlet_list = [cloudlet1, cloudlet2, cloudlet3]

# Execute the Cloudlets in the datacenter
cloudlet_execution = CloudletExecution(cloudlet_list, datacenter_instance)
cloudlet_execution.execute()
```
Example output:
```
Cloudlet 39e06124-919f-41b5-956a-d028033ebb8f starts execution on VM 10078ab6-c844-4e4a-beab-cffd823b16eb at 0
Cloudlet ba8da363-5a1d-42a6-9fe7-bef2fa58bac7 starts execution on VM 348469dd-f98a-47e5-9892-bf5c460573a1 at 0
Cloudlet 39e06124-919f-41b5-956a-d028033ebb8f completes execution on VM 10078ab6-c844-4e4a-beab-cffd823b16eb at 10
Cloudlet 4eff8fdd-b3e8-4cd2-ab3c-44cfa8b1b4ac starts execution on VM 10078ab6-c844-4e4a-beab-cffd823b16eb at 10
Cloudlet ba8da363-5a1d-42a6-9fe7-bef2fa58bac7 completes execution on VM 348469dd-f98a-47e5-9892-bf5c460573a1 at 15
Cloudlet 4eff8fdd-b3e8-4cd2-ab3c-44cfa8b1b4ac completes execution on VM 10078ab6-c844-4e4a-beab-cffd823b16eb at 18
```
