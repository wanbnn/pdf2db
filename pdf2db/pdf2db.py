import os
import re
from pdf_extractor import PDFExtractor
from db_handler import DBHandler
from text_processor import TextProcessor

def clean_book_name(file_name):
    """
    Limpa e formata o nome do arquivo para ser usado como book_name.
    """
    cleaned_name = re.sub(r'[_\.]', ' ', file_name)
    cleaned_name = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned_name)
    cleaned_name = re.sub(r'\s+', ' ', cleaned_name).strip()
    return cleaned_name

def process_pdf(pdf_path, db_path, book_name=None):
    """
    Processa um único arquivo PDF e insere o conteúdo no banco de dados.
    """
    if book_name is None:
        book_name = clean_book_name(os.path.splitext(os.path.basename(pdf_path))[0])
    
    pdf_extractor = PDFExtractor()
    pdf_text = pdf_extractor.extract_text(pdf_path)
    if not pdf_text.strip():
        raise ValueError(f"Erro: Não foi possível extrair texto do PDF '{pdf_path}'.")
    
    text_processor = TextProcessor()
    processed_content = text_processor.process_text(pdf_text)
    
    db_handler = DBHandler(db_path)
    if db_handler.conn is None:
        raise ConnectionError("Erro: Não foi possível conectar ao banco de dados.")
    
    db_handler.create_table()
    for content_type, content_text in processed_content:
        db_handler.insert_content(book_name, content_type, content_text)
    
    db_handler.close()

def process_folder(folder_path, db_path):
    """
    Processa todos os arquivos PDF em uma pasta e insere o conteúdo no banco de dados.
    """
    pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    if not pdf_files:
        raise FileNotFoundError("Nenhum arquivo PDF encontrado na pasta.")
    
    db_handler = DBHandler(db_path)
    if db_handler.conn is None:
        raise ConnectionError("Erro: Não foi possível conectar ao banco de dados.")
    
    db_handler.create_table()
    for pdf_file in pdf_files:
        pdf_path = os.path.join(folder_path, pdf_file)
        book_name = clean_book_name(os.path.splitext(pdf_file)[0])
        
        pdf_extractor = PDFExtractor()
        pdf_text = pdf_extractor.extract_text(pdf_path)
        if not pdf_text.strip():
            print(f"Aviso: Não foi possível extrair texto do PDF '{pdf_file}'.")
            continue
        
        text_processor = TextProcessor()
        processed_content = text_processor.process_text(pdf_text)
        
        for content_type, content_text in processed_content:
            db_handler.insert_content(book_name, content_type, content_text)
    
    db_handler.close()
