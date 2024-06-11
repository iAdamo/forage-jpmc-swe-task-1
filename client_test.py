""" This module tests the client3.py module
"""
import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  """ Test for client3.py
  """
  def test_getDataPoint_calculatePrice(self):
    """ The price should be (bid_price + ask_price) / 2
    """
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual(price, (bid_price + ask_price) / 2)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    """ The price should be (bid_price + ask_price) / 2
    """
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual(price, (bid_price + ask_price) / 2)

  def test_getRatio(self):
    """ The ratio should be price_a / price_b
    """
    price_a = 120.48
    price_b = 121.68
    self.assertEqual(getRatio(price_a, price_b), price_a / price_b)

  def test_getRatio_priceBisZero(self):
    """ The ratio should be None when price_b is zero
    """
    price_a = 120.48
    price_b = 0
    self.assertIsNone(getRatio(price_a, price_b))

if __name__ == '__main__':
  """ Run the tests
  """
  unittest.main()
