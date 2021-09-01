from unittest import TestCase


class Test(TestCase):
    def test_is_prime(self):
        # self.fail()
        from pycharmTest import is_prime
        self.assertTrue(is_prime(5))
