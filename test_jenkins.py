import unittest
import jenkinstest

class Testjenkins(unittest.TestCase):
    def test_addtwo(self):
        self.assertEqual(jenkinstest.addTwo(10,5), 15)

    def test_helloworld(self):
        self.assertEqual(jenkinstest.helloWorld(), 'Hello World')

if __name__ == '__main__':
    unittest.main()
    
