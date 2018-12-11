class WeaponDispenser:
    def __init__(self):
        self.weapons = ["katana", "suriken", "poison"]

    def dispense(self):
        if self.weapons:
            return self.weapons.pop()
        return None

    def easter_egg(self):
        # return "Eggs!"
        raise NotImplemented