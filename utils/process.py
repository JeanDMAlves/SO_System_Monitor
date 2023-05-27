import psutil
import subprocess

class Process():
    def len_active_processes(self):
        """
            Printa a quantidade de processos ativos
        """
        print(len(psutil.pids()))
        
    def print_active_processes(self):
        """
            Printa todos os processos ativos
        """
        for process in psutil.process_iter():
            print(process)

    def exec(self, path):
        pid = subprocess.Popen(args=path.split()).pid
        process = psutil.Process(pid=pid)
        switches = process.num_ctx_switches()
        voluntary_switches = switches.voluntary
        involuntary_switches = switches.involuntary
        total_virtual_memory_usage = process.memory_info().vms / (1024 ** 2)
        times = process.cpu_times()
        print(f"Quantidade de trocas de contexto voluntárias: {voluntary_switches}")
        print(f"Quantidade de trocas de contexto involuntárias: {involuntary_switches}")
        print(f"Total de memória virtual utilizada pelo processo: {total_virtual_memory_usage:.3f} MB")
        print(f"Quantidade de tempo gasto em modo usuário: {times.user:.4f} s")
        print(f"Quantidade de tempo gasto em modo núcleo: {times.system:.4f} s")