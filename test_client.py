import unittest
from unittest.mock import patch
from client import Client


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client_1 = Client('Masayoshi', 'Son')
        self.client_2 = Client('Lisa', 'Sue')

    def test_trades_for_month(self):
        with patch('client.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'AMD'

            trades = self.client_1.trades_for_month('October')
            mocked_get.assert_called_with('http://trades.cs.com/Son/October')
            self.assertEqual(trades, 'AMD')

            mocked_get.return_value.ok = False

            trades = self.client_2.trades_for_month('March')
            mocked_get.assert_called_with('http://trades.cs.com/Sue/March')
            self.assertEqual(trades, 'Bad Response!')

    def test_db_select(self):
        with patch('client.mysql.connector.connect') as mocked_conn:
            mocked_cursor = mocked_conn.return_value.cursor.return_value
            test_result = [{'name': 'masa', 'company': 'softbank'}]
            mocked_cursor.fetchall.return_value = test_result
            returned_val = self.client_1.get_val_from_db()
            self.assertEqual(returned_val,test_result)



    def test_get_email(self):
        self.assertEqual(self.client_2.get_email(),'lisa.sue@credit-suisse.com')

if __name__ == '__main__':
    unittest.main()