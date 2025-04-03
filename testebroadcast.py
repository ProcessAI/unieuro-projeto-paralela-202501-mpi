
from mpi4py import MPI

# Obtenha o comunicador e o rank de cada processo
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Dados a serem transmitidos
if rank == 0:  # O processo raiz (rank 0) vai enviar o dado
    data = 100  # Dado que será enviado
    print(f"Processo {rank} enviando dado {data} para todos os processos.")
else:
    data = None  # Outros processos começam sem dados

# O comando Bcast envia 'data' do processo raiz (rank 0) para todos os outros
data = comm.bcast(data, root=0)

# Todos os processos imprimem o dado recebido
print(f"Processo {rank} recebeu o dado {data}")