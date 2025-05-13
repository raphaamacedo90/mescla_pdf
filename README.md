# 🔗 Mesclar Arquivos PDF com Python

Este projeto em Python utiliza a biblioteca `PyPDF2` para **mesclar automaticamente todos os arquivos PDF** de uma pasta em um único documento final.

É uma solução simples, prática e eficiente para o dia a dia de escritórios, contadores, advogados, estudantes e qualquer pessoa que lida com múltiplos PDFs.

---

## 📁 Como funciona?

1. O script lê todos os arquivos da pasta `arquivos/`.
2. Ordena os nomes dos arquivos (alfabeticamente).
3. Filtra apenas os arquivos `.pdf`.
4. Mescla os arquivos em ordem e gera um único documento com o nome:  
   `3.PDF Mesclado.pdf`.
5. **Verifica automaticamente se o arquivo foi gerado com sucesso**, exibindo uma mensagem final.

---

## ⚙️ Requisitos

- Python 3.x instalado
- Biblioteca PyPDF2

Instale o pacote necessário com:

```bash
pip install PyPDF2
```

---

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/raphaamacedo90/mescla_pdf.git
cd mescla_pdf
```

2. Coloque os arquivos `.pdf` que deseja mesclar dentro da pasta `arquivos/`.

3. Execute o script:

```bash
python mesclar_pdfs.py
```

4. O resultado será salvo automaticamente em:

```
arquivos/3.PDF Mesclado.pdf
```

---

## ✅ Saída esperada

Se tudo ocorrer corretamente:

```bash
📄 Arquivos encontrados: ['1.pdf', '2.pdf']
✅ Arquivo mesclado gerado com sucesso!
```

Se houver erro:

```bash
❌ Falha ao gerar o arquivo PDF mesclado.
```

---

## 📌 Estrutura do projeto

```
mescla_pdf/
├── arquivos/                 # Onde devem ser colocados os PDFs
├── mesclar_pdfs.py          # Script principal
└── README.md                # Este arquivo
```

---

## 👨‍💻 Autor

Desenvolvido por Raphael Macedo  
📎 [LinkedIn](https://www.linkedin.com/in/raphael-macedo10/)  
💻 [GitHub](https://github.com/raphaamacedo90)

---

## 📃 Licença

Este projeto está licenciado sob a licença MIT – sinta-se livre para usar, modificar e compartilhar!

---
