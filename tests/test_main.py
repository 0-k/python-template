import unittest
import pytemplate.main as main


class TestMain(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_for_valid_main(self):
        self.assertEqual(main.run(), 1)
