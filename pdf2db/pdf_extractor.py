import PyPDF2

class PDFExtractor:
    """Classe para extrair texto de arquivos PDF."""

    @staticmethod
    def extract_text(pdf_path):
        """
        Extrai texto de um arquivo PDF.

        Args:
            pdf_path (str): Caminho para o arquivo PDF.

        Returns:
            str: Texto extraído do PDF.
        """
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                return text
        except Exception as e:
            print(f"Erro ao extrair texto do PDF: {e}")
            return ""