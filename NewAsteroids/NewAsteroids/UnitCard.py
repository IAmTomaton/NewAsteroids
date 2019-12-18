class UnitCard:

    def __init__(self, unit_type, max_count, delay, rotate,
                 evolution_time, evolution_count):
        self.unit_type = unit_type
        self.max_count = max_count
        self.cooldown = delay
        self.standart_delay = delay
        self.delay = delay
        self.evolution_time = evolution_time
        self.evolution_count = evolution_count
        self.rotate = rotate
