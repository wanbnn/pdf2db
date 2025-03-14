from pdf_extractor import PDFExtractor
from db_handler import DBHandler
from text_processor import TextProcessor
import os
import re

def clean_book_name(file_name):
    """
    Limpa e formata o nome do arquivo para ser usado como book_name.

    Args:
        file_name (str): Nome do arquivo sem extensão.

    Returns:
        str: Nome do livro formatado.
    """
    # Remove caracteres especiais e substitui "_" ou "." por espaços
    cleaned_name = re.sub(r'[_\.]', ' ', file_name)
    # Remove outros caracteres não alfanuméricos (exceto espaços)
    cleaned_name = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned_name)
    # Remove múltiplos espaços e trim
    cleaned_name = re.sub(r'\s+', ' ', cleaned_name).strip()
    return cleaned_name

def process_folder(folder_path, db_path):
    """
    Processa todos os arquivos PDF em uma pasta.

    Args:
        folder_path (str): Caminho para a pasta contendo os arquivos PDF.
        db_path (str): Caminho para o arquivo do banco de dados SQLite.
    """
    # Lista todos os arquivos .pdf na pasta
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    if not pdf_files:
        print("Nenhum arquivo PDF encontrado na pasta.")
        return

    # Conecta ao banco de dados
    db_handler = DBHandler(db_path)
    if db_handler.conn is None:
        print("Erro: Não foi possível conectar ao banco de dados.")
        return

    # Cria a tabela no banco de dados
    db_handler.create_table()

    # Processa cada arquivo PDF
    for pdf_file in pdf_files:
        # Define o caminho completo do arquivo PDF
        pdf_path = os.path.join(folder_path, pdf_file)

        # Extrai o nome do arquivo (sem extensão) e trata como book_name
        book_name = clean_book_name(os.path.splitext(pdf_file)[0])

        # Extrai texto do PDF
        pdf_extractor = PDFExtractor()
        pdf_text = pdf_extractor.extract_text(pdf_path)
        if not pdf_text.strip():
            print(f"Erro: Não foi possível extrair texto do PDF '{pdf_file}'.")
            continue

        # Processa o texto
        text_processor = TextProcessor()
        processed_content = text_processor.process_text(pdf_text)

        # Insere os dados no banco de dados
        for content_type, content_text in processed_content:
            db_handler.insert_content(book_name, content_type, content_text)

    # Fecha a conexão com o banco de dados
    db_handler.close()

def main():
    # Configurações
    choice = input("Deseja processar um único PDF (1) ou uma pasta de PDFs (2)? ")

    if choice == "1":
        # Processamento de um único PDF
        pdf_path = input("Digite o caminho para o arquivo PDF: ")
        db_path = input("Digite o caminho para o banco de dados SQLite: ")
        book_name = input("Digite o nome do livro: ")

        # Extrai texto do PDF
        pdf_extractor = PDFExtractor()
        pdf_text = pdf_extractor.extract_text(pdf_path)
        if not pdf_text.strip():
            print("Erro: Não foi possível extrair texto do PDF.")
            return

        # Processa o texto
        text_processor = TextProcessor()
        processed_content = text_processor.process_text(pdf_text)

        # Conecta ao banco de dados
        db_handler = DBHandler(db_path)
        if db_handler.conn is None:
            print("Erro: Não foi possível conectar ao banco de dados.")
            return

        # Cria a tabela e insere os dados
        db_handler.create_table()
        for content_type, content_text in processed_content:
            db_handler.insert_content(book_name, content_type, content_text)

        # Fecha a conexão com o banco de dados
        db_handler.close()

    elif choice == "2":
        # Processamento de uma pasta de PDFs
        folder_path = input("Digite o caminho para a pasta contendo os PDFs: ")
        db_path = input("Digite o caminho para o banco de dados SQLite: ")
        process_folder(folder_path, db_path)

    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()