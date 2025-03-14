# PDF2DB - Extração e Armazenamento de Conteúdo de PDFs em Banco de Dados

## Visão Geral

O **PDF2DB** é uma ferramenta Python projetada para extrair, processar e armazenar o conteúdo de arquivos PDF diretamente em um banco de dados. Este projeto foi desenvolvido para facilitar a digitalização e organização de grandes volumes de documentos, permitindo que os usuários convertam rapidamente arquivos PDF em registros estruturados no banco de dados.

Com suporte tanto para processamento de arquivos individuais quanto para pastas contendo múltiplos arquivos PDF, o PDF2DB é uma solução flexível e eficiente para gerenciamento de conteúdos digitais.

---

## Funcionalidades Principais

1. **Extração de Texto**: Utiliza a classe `PDFExtractor` para extrair texto de arquivos PDF.
2. **Processamento de Texto**: Aplica transformações e limpezas no texto extraído através da classe `TextProcessor`.
3. **Armazenamento em Banco de Dados**: Insere o conteúdo processado em um banco de dados SQLite usando a classe `DBHandler`.
4. **Suporte a Pastas**: Processa todos os arquivos PDF em uma pasta automaticamente.
5. **Nomes Limpos**: Formata nomes de arquivos para uso como identificadores no banco de dados.

---

## Estrutura do Projeto

```plaintext
pdf2db/
├── pdf_extractor.py       # Classe responsável pela extração de texto de PDFs
├── text_processor.py      # Classe responsável pelo processamento e limpeza de texto
├── db_handler.py          # Classe responsável pela interação com o banco de dados
└── main.py                # Funções principais para processamento de PDFs
```

---

## Requisitos

### Dependências

- Python 3.8 ou superior
- Bibliotecas Python:
  - `PyPDF2` (para extração de texto)
  - `sqlite3` (para interação com o banco de dados)

Instale as dependências necessárias com o seguinte comando:

```bash
pip install https://github.com/wanbnn/pdf2db/raw/refs/heads/main/dist/pdf2db-0.1.0-py3-none-any.whl
```

---

## Como Usar

### Configuração Inicial

1. Clone este repositório:
   ```bash
   git clone https://github.com/wanbnn/pdf2db.git
   cd pdf2db
   ```

2. Crie um banco de dados SQLite vazio para armazenar os dados (Ou caso ele não exista ela será criada automaticamente):
   ```bash
   touch database.db
   ```

### Processamento de Arquivos PDF

#### Processar um Único Arquivo PDF

Use a função `process_pdf` para processar um único arquivo PDF:

```python
from main import process_pdf

pdf_path = "caminho/para/arquivo.pdf"
db_path = "caminho/para/database.db"

process_pdf(pdf_path, db_path)
```

Opcionalmente, você pode especificar um nome personalizado para o livro:

```python
process_pdf(pdf_path, db_path, book_name="Meu Livro")
```

#### Processar Todos os PDFs em uma Pasta

Use a função `process_folder` para processar todos os arquivos PDF em uma pasta:

```python
from main import process_folder

folder_path = "caminho/para/pasta_com_pdfs"
db_path = "caminho/para/database.db"

process_folder(folder_path, db_path)
```

### Exemplo de Uso Prático

Suponha que você tenha uma pasta chamada `documentos` contendo vários arquivos PDF e deseja armazenar seus conteúdos em um banco de dados SQLite chamado `biblioteca.db`. Execute o seguinte código:

```python
from main import process_folder

process_folder("documentos", "biblioteca.db")
```

---

## Detalhes Técnicos

### Limpeza de Nomes de Arquivos

A função `clean_book_name` remove caracteres especiais e substitui sublinhados (`_`) e pontos (`.`) por espaços. O resultado é um nome limpo e formatado para ser usado como identificador no banco de dados.

Exemplo:

```python
clean_book_name("livro_exemplo_v1.pdf")  # Resultado: "livro exemplo v1"
```

### Tratamento de Erros

O PDF2DB inclui tratamento robusto de erros para garantir uma experiência confiável:

- **Arquivos Corrompidos ou Sem Texto**: Se um PDF não puder ser lido ou estiver vazio, o sistema emitirá um aviso e continuará processando os próximos arquivos.
- **Conexão com o Banco de Dados**: Caso o banco de dados não possa ser acessado, o sistema lançará um erro explícito.

---

## Contribuição

Contribuições são bem-vindas! Se você deseja melhorar o PDF2DB.

---

## Licença

Este projeto está licenciado sob a **MIT License**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
