# tests/test_get_gemini_response.py

import unittest
from app.main import get_gemini_response

class TestGetGeminiResponse(unittest.TestCase):
    def setUp(self):
        self.prompt = [
            """
            You are an expert in converting English questions into SQL queries for a MySQL database.
            Please ensure the SQL query is valid and does not include any additional explanations, comments, or characters that could cause a syntax error.
            """
        ]

    def test_get_gemini_response(self):
        question = "What is the total sales for the year 2023?"
        response = get_gemini_response(question, self.prompt)
        self.assertIsInstance(response, str)
        self.assertNotIn('```', response)

if __name__ == '__main__':
    unittest.main()
