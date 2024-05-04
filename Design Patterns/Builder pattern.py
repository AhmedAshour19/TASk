# Product class
class Computer:
    def __init__(self, cpu=None, ram_gb=None, storage_gb=None, gpu=None, monitor=None):
        self.cpu = cpu
        self.ram_gb = ram_gb
        self.storage_gb = storage_gb
        self.gpu = gpu
        self.monitor = monitor

    def __str__(self):
        return f"CPU: {self.cpu}, RAM: {self.ram_gb}GB, Storage: {self.storage_gb}GB, GPU: {self.gpu}, Monitor: {self.monitor}"

# Builder class
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram_gb(self, ram_gb):
        self.computer.ram_gb = ram_gb
        return self

    def set_storage_gb(self, storage_gb):
        self.computer.storage_gb = storage_gb
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_monitor(self, monitor):
        self.computer.monitor = monitor
        return self

    def build(self):
        return self.computer

# Usage
computer = (ComputerBuilder()
            .set_cpu("AMD Ryzen 9")
            .set_ram_gb(32)
            .set_storage_gb(1024)
            .set_gpu("AMD Radeon RX 6900 XT")
            .set_monitor("32-inch 4K")
            .build())

print(computer)
