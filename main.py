from utils.general_information import GeneralInformation
from utils.process import Process

executable_path = input("Digite o caminho absoluto até o executável: ")
systemInformation = GeneralInformation()
process = Process()

print("Primeiro algumas informações sobre o sistema:")
print()
systemInformation.print_system_information()
systemInformation.print_virtual_memory()

print("------------------------------------------------------------------------------")
print("Agora vamos executar o programa passado e coletar algumas informações:")
print()
process.exec(path = executable_path)