# unieuro-projeto-paralela-202501-mpi

## MPI - Introdução

O MPI (Message Passing Interface) é um modelo de comunicação utilizado para programação paralela e distribuída

## Código Exemplo em Python

```
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
    print(f"Processo {rank} recebeu: {data}")´

```

### Para executar um programa python com MPI:

mpiexec -n 2 python nome_do_arquivo.py

Onde 2 representa o número de processos desejados.

## Instalação

### Lib python

pip install mpi4py

## Lib windows

Instalar o MPI para windows (10 ou 11) do link: https://www.microsoft.com/en-us/download/details.aspx?id=105289

