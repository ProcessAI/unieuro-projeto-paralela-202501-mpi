from mpi4py import MPI

# Obtém o comunicador
comm = MPI.COMM_WORLD

# Obtém o número de processos
size = comm.Get_size()

# Obtém o rank (identificador único) do processo
rank = comm.Get_rank()

# Processo 0 envia uma mensagem para o processo 1
if rank == 0:
    data = "Olá do processo 0"
    print(f"Processo {rank} enviando: {data}")
    comm.send(data, dest=1)  # Envia a mensagem para o processo 1
elif rank == 1:
    data = comm.recv(source=0)  # Recebe a mensagem do processo 0
    print(f"Processo {rank} recebeu: {data}")
