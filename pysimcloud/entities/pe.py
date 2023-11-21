from pysimcloud.entities.entity import Entity

class Pe(Entity):
    def __init__(self, mips_rating):
        super().__init__()
        self.pe_id = super().getId()
        self.mips_rating = mips_rating