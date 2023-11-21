from cloudsim.entities.entity import Entity

class Vm(Entity):
    def __init__(self, broker_id, mips, pes_number, ram, bw, size, vmm):
        super().__init__()
        self.vmid = self.getId()
        self.broker_id = broker_id
        self.mips = mips
        self.pes_number = pes_number
        self.ram = ram
        self.bw = bw
        self.size = size
        self.vmm = vmm

    def get_id(self):
        return self.vmid

    def get_details(self):
        print(f"VM ID: {self.vmid}\nMIPS: {self.mips}\nPEs: {self.pes_number}\nRAM: {self.ram}\nBW: {self.bw}\nSize: {self.size}\nVMM: {self.vmm}\n")
