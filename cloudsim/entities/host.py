from pysimcloud.entities.entity import Entity

class Host(Entity):
    def __init__(self, ram, bw, storage, pe_list):
        super().__init__()
        self.host_id = super().getId()
        self.ram = ram
        self.bw = bw
        self.storage = storage
        self.pe_list = pe_list
        self.assigned_vms = []

    def set_datacenter(self, datacenter):
        self.datacenter = datacenter

    def available_resources(self):
        # Calculate available resources by subtracting used resources from total resources
        used_ram = sum(vm.ram for vm in self.assigned_vms)
        used_bw = sum(vm.bw for vm in self.assigned_vms)
        used_storage = sum(vm.size for vm in self.assigned_vms)
        pes = sum(vm.pes_number for vm in self.assigned_vms)

        available_ram = self.ram - used_ram
        available_bw = self.bw - used_bw
        available_storage = self.storage - used_storage
        available_pes = len(self.pe_list) - pes

        return available_ram, available_bw, available_storage, available_pes
    
    def has_enough_resources(self, vm):
        # Check if the host has enough resources to accommodate the VM
        available_ram, available_bw, available_storage, available_pes = self.available_resources()
        return (vm.ram <= available_ram) and (vm.bw <= available_bw) and (vm.size <= available_storage) and (vm.pes_number <= available_pes)

    def assign_vm(self, vm):
         # Check if there are enough resources to assign the VM
        available_ram, available_bw, available_storage, available_pes = self.available_resources()

        if (vm.ram > available_ram) or (vm.bw > available_bw) or (vm.size > available_storage) or (vm.pes_number > available_pes):
            raise ValueError("Not enough resources available to allocate VM.")

        # Assign the VM to the host
        self.assigned_vms.append(vm)

    def get_details(self):
         print(f"Host ID: {self.host_id}\nRAM: {self.ram}\nBW: {self.bw}\nStorage: {self.storage}\nPEs: {len(self.pe_list)})\n")
         for vm in self.assigned_vms:
             vm.get_details()
            