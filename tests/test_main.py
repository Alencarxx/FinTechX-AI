# tests/test_main.py

import unittest
from unittest.mock import patch
from dotenv import load_dotenv
import os
import app.main as main_app

class TestMainApp(unittest.TestCase):
    @patch('app.main.st')
    def test_streamlit_initialization(self, mock_streamlit):
        # Testa se o título do Streamlit é definido corretamente
        main_app.st.title("FinTechX AI")
        mock_streamlit.title.assert_called_once_with("FinTechX AI")

    def test_load_dotenv(self):
        # Testa se as variáveis de ambiente são carregadas corretamente
        load_dotenv()
        self.assertIsNotNone(os.getenv("GOOGLE_API_KEY"))
        self.assertIsNotNone(os.getenv("DB_HOST"))
        self.assertIsNotNone(os.getenv("DB_USER"))
        self.assertIsNotNone(os.getenv("DB_PASSWORD"))
        self.assertIsNotNone(os.getenv("DB_NAME"))

if __name__ == '__main__':
    unittest.main()
