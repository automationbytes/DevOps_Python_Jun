import unittest

def setUpModule():
    print("Its setup module")

def tearDownModule():
    print("Its tearDown Module")

class sampleUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Its setUp class")

    def setUp(self):
        print("Its setUp test")

    def test1(self):
        print("Test1")

    def test2(self):
        print("Test2")

    def tearDown(self):
        print("Its TearDown test")

    @classmethod
    def tearDownClass(cls):
        print("Its tearDown class")

if __name__ == '__main__':
    unittest.main()