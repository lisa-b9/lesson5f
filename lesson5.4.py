class Engine:

    def start_engine(self):
        print("Starting Engine")

    def charge_engine(self):
        print("Charging engine")


class ElectricVehicle:

    def start_electric(self):
        print("Starting ElectricVehicle")

    def charge_electric(self):
        print("Charging ElectricVehicle")


class HybridCar(Engine, ElectricVehicle):

    def start_hybrid(self):
        print("Starting Hybrid")
    def charging_hybrid(self):
        print("Charging Hybrid")
    def drive_hybrid(self):
        print("Driving Hybrid")


player = HybridCar()

player.start_hybrid()
player.start_engine()
player.start_electric()
player.charge_engine()
player.charge_electric()
player.charging_hybrid()
player.drive_hybrid()
