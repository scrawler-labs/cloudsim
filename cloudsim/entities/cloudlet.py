from cloudsim.entities.entity import Entity

class Cloudlet(Entity):
    def __init__(self, length, pes_number, file_size, output_size):
        super().__init__()
        self.cloudlet_id = super().getId()
        self.length = length
        self.pes_number = pes_number
        self.file_size = file_size
        self.output_size = output_size
        self.vm = None
        self.status = "Created"
        self.finish_time = None

    def set_vm(self, vm):
        self.vm = vm

    def get_vm(self):
        return self.vm

    def get_status(self):
        return self.status

    def get_finish_time(self):
        return self.finish_time

