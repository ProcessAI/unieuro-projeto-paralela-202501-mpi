import random
import os

def gerar_arquivo_aleatorio(nome_arquivo, tamanho_mb=500):
    tamanho_total_bytes = tamanho_mb * 1024 * 1024  # 500 MB
    flush_interval_bytes = 10 * 1024 * 1024         # 10 MB
    opcoes = [-1, 0, 1]

    bytes_escritos = 0
    bytes_desde_ultimo_flush = 0

    with open(nome_arquivo, 'w', newline='\n') as arquivo:
        while bytes_escritos < tamanho_total_bytes:
            numero = str(random.choice(opcoes)) + '\n'
            arquivo.write(numero)

            tamanho_numero = len(numero.encode('utf-8'))  # garante medição precisa em bytes
            bytes_escritos += tamanho_numero
            bytes_desde_ultimo_flush += tamanho_numero

            if bytes_desde_ultimo_flush >= flush_interval_bytes:
                arquivo.flush()
                bytes_desde_ultimo_flush = 0

    print(f"Arquivo '{nome_arquivo}' gerado com sucesso com cerca de {tamanho_mb}MB.")

# Executar
gerar_arquivo_aleatorio("saida_aleatoria.txt", tamanho_mb=5000)
