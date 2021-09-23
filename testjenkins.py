import unittest
import jenkinstest

x = jenkinstest.jenkins_test()

class Testjenkins(unittest.TestCase):
    def test_addtwo(self):
        result = x.add_two(10,5)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()