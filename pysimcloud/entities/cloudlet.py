from pysimcloud.entities.entity import Entity

class Cloudlet(Entity):
    def __init__(self, cloudlet_id, length, pes_number, file_size, output_size, cloudlet_scheduler):
        self.cloudlet_id = cloudlet_id
        self.length = length
        self.pes_number = pes_number
        self.file_size = file_size
        self.output_size = output_size
        self.cloudlet_scheduler = cloudlet_scheduler
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

    def execute(self):
        if self.vm is not None:
            self.status = "InExecution"
            self.cloudlet_scheduler.cloudlet_execute(self)
            self.status = "Completed"
            self.finish_time = self.cloudlet_scheduler.get_clock_time() + self.length