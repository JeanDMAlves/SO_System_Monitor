from psutil import virtual_memory, cpu_count
import platform

class GeneralInformation:
    def bytes_to_gigas(self, value):
        return value / (1024**3)
    
    def print_virtual_memory(self):
        """
            Método para verificar a quantidade de memória ram total no computador, 
            juntamente com a memória ram disponível, qual a porcentagem usada de memória ram 
            e a memória ram absoluta usada
        """
        vm = virtual_memory()
        print(f"Total de memória virtual na máquina: {self.bytes_to_gigas(vm.total):.2f} GB")
        print(f"Memória Virtual disponível: {self.bytes_to_gigas(vm.available):.2f} GB")
        print(f"Percentual de memória usado (%) : {vm.percent:.2f}")
        print(f"Memória Virtual Usada: {self.bytes_to_gigas(vm.used):.2f} GB")
        return True

    def print_system_information(self):
        print(f"Sistema Operacional: {platform.system()}")
        print(f"Processador: {platform.processor()}")
        print(f"Quantidade CPU(s) lógicos (Núcleos + Threads): {cpu_count()}")
        print(f"Quantidade CPU(s) físicos (Núcleos): {cpu_count(logical=False)}")
        return True
        
    
if __name__ == "__main__":
    infos = generalInformation()
    infos.print_virtual_memory()
    infos.print_system_information()