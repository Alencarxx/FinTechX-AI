# tests/test_read_sql_query.py

import unittest
from unittest.mock import patch, MagicMock
from app.main import read_sql_query
import pandas as pd

class TestReadSqlQuery(unittest.TestCase):
    @patch('app.main.mysql.connector.connect')
    def test_read_sql_query(self, mock_connect):
        mock_conn = MagicMock()
        mock_cursor = mock_conn.cursor()
        mock_connect.return_value = mock_conn
        mock_cursor.fetchall.return_value = [(1, 'Test')]
        mock_cursor.description = (('id',), ('name',))

        sql_query = "SELECT * FROM test_table;"
        df = read_sql_query(sql_query)

        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)
        self.assertEqual(df.iloc[0]['id'], 1)
        self.assertEqual(df.iloc[0]['name'], 'Test')

if __name__ == '__main__':
    unittest.main()
