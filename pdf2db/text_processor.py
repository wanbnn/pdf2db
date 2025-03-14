import re

class TextProcessor:
    """Classe para processar e classificar texto extraído."""

    @staticmethod
    def process_text(text):
        """
        Processa o texto e classifica os elementos.

        Args:
            text (str): Texto extraído.

        Returns:
            list: Lista de tuplas contendo o tipo e o conteúdo.
        """
        paragraphs = re.split(r'\n\s*\n', text.strip())
        processed_content = []

        for paragraph in paragraphs:
            if re.search(r'["“”]|—|–', paragraph):
                processed_content.append(("dialogue", paragraph.strip()))
            elif re.search(r'[“”"\[\]]', paragraph):
                processed_content.append(("quote", paragraph.strip()))
            else:
                processed_content.append(("paragraph", paragraph.strip()))

        return processed_content