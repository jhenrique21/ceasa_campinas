
import wget
import os

#Apaga arquivos que existam para não sobrecarregar o diretório
for indice in range(1,6):
    try:
        arquivo = f"cardapio_{indice}.pdf"
        os.remove(arquivo)
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {arquivo}')
    except OSError as e:
        print(f'Erro ao apagar o arquivo: {e}')


#Arquivo URL com http básico
URL = "http://ceasacampinas.empresarial.ws/ae/principal/baixa.php"
for numero in range(1,6):
    #mescla a url básica com a extensão para cardápios de 1 a 5
    FULL = f"{URL}?file=rcee1%20{numero}&tipo=pdf"
    SAIDA = f"cardapio_{numero}.pdf"
    wget.download(FULL, SAIDA)