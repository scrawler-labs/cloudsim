from cloudsim.schedulers.cloudlet_scheduler import CloudletScheduler

class CloudletSchedulerSJF(CloudletScheduler):

    def schedule_cloudlets(self, cloudlets):
        # Sort cloudlets based on their lengths (SJF)
        sorted_cloudlets = sorted(cloudlets, key=lambda x: x.length)
        processes = [self.env.process(self.schedule_cloudlet(cloudlet)) for cloudlet in sorted_cloudlets]
        yield self.env.all_of(processes)

        for vm in self.max_utilization:
            print(f"\nVM {vm} utilization:\n {self.max_utilization[vm][0] * 100}% PEs\n, {self.max_utilization[vm][1] * 100}% RAM\n, {self.max_utilization[vm][2] *100}% Storage")

   