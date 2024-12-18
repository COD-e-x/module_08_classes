from computer_components import PowerSupply, Motherboard, CPU, RAM, SSD, GraphicsCard

class ComputerCase:
    def __init__(
        self, power, chipset, clock_speed, cores, memory_size_ram, frequency, capacity, model, memory_size_graf
    ):
        self.power_supply = PowerSupply(power)
        self.motherboard = Motherboard(chipset)
        self.cpu = CPU(clock_speed, cores)
        self.ram = RAM(memory_size_ram, frequency)
        self.ssd = SSD(capacity)
        self.graphics_card = GraphicsCard(model, memory_size_graf)

    def start_computer(self):
        return f'{self.power_supply.supply_voltage()}\n{self.motherboard.redistribute_voltage()}\n{self.graphics_card.display_image()}'


if __name__ == '__main__':
    print(f'\nФайл - {__file__.split('\\')[-1]}\n')
    computer = ComputerCase(
        750,
        'AMD B650',
        8,
        3.5,
        32,
        5000,
        1000,
        'GeForce RTX 4090',
        24
    )
    print(computer.start_computer())
    print()

    print(f'Производительность компьютера {computer.cpu.get_cores()}')
    print(computer.cpu.activate_turbo_mode())
    print()

    print(computer.ram.load_data(2.5))
    print(computer.ram.load_data(2.5))
    print(computer.ram.unload_data(4))
    print()

    print(computer.ssd.save_data(100))
    print(computer.ssd.save_data(200))
    print(computer.ssd.delete_data(150))

