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
        """
            path -> Caminho até o executável
            Recebe o caminho do executável, executa-o e no fim coleta
            a quantidade de trocas de contexto, a quantidade de tempo gasto em cada modo
            e, no fim, o total de memória utilizada pelo processo
        """
        pid = subprocess.Popen(args=path.split()).pid # Executa o processo e salva o PID (Process ID) dele nessa variável
        process = psutil.Process(pid=pid) # Dentro da biblioteca Psutil é uma classe que representa um processo dentro do python
        switches = process.num_ctx_switches() # Pega as trocas de contexto voluntárias e involuntárias
        voluntary_switches = switches.voluntary
        involuntary_switches = switches.involuntary
        total_virtual_memory_usage = process.memory_info().vms / (1024 ** 2) # Pega a quantidade de memória em bytes e converte para Megabytes
        times = process.cpu_times() # Obtém o tempo gasto em modo usuário e modo núcleo
        print(f"Quantidade de trocas de contexto voluntárias: {voluntary_switches}")
        print(f"Quantidade de trocas de contexto involuntárias: {involuntary_switches}")
        print(f"Total de memória virtual utilizada pelo processo: {total_virtual_memory_usage:.3f} MB")
        print(f"Quantidade de tempo gasto em modo usuário: {times.user:.4f} s")
        print(f"Quantidade de tempo gasto em modo núcleo: {times.system:.4f} s")