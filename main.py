from utils.general_information import GeneralInformation
from utils.process import Process

executable_path = "Coloque o caminho do executável relativo ou absoluto aqui"

systemInformation = GeneralInformation()
process = Process()

print("Primeiro algumas informações sobre o sistema:")
systemInformation.print_system_information()
systemInformation.print_virtual_memory()

print("------------------------------------------------------------------------------")
print("Agora vamos executar o programa passado e coletar algumas informações:")
process.exec(path = executable_path)