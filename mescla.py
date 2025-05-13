import PyPDF2
import os

# Mesclador
merger = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"Arquivos/{arquivo}")

try:     
    merger.write(f"Arquivos/3.PDF Mesclado.pdf")
    merger.close()
    print("Arquivo Gerado com Sucesso")
except Exception as e:
    print(f"Erro ao Gerar {e}")




