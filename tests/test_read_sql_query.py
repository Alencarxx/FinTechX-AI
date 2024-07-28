# tests/test_clean_sql_query.py

import unittest
from app.main import clean_sql_query

class TestCleanSqlQuery(unittest.TestCase):
    def test_clean_sql_query(self):
        raw_sql = "```SELECT * FROM orders;```"
        cleaned_sql = clean_sql_query(raw_sql)
        self.assertEqual(cleaned_sql, "SELECT * FROM orders;")
        self.assertNotIn('```', cleaned_sql)

if __name__ == '__main__':
    unittest.main()
