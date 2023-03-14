import unittest
from my_url.my_url import make_request


class TestUrl(unittest.TestCase):
    """
    Test a url.
    """
    def test_url(self):
        response = make_request('https://example.com')
        self.assertEqual(int(response.status_code), 200, 'The request returned a non-200 response.')

if __name__ == '__main__':
    unittest.main()