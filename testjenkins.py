import unittest
import jenkinstest

jenkinsTest = jenkinstest.jenkins_test()

class Testjenkins(unittest.TestCase):
    def test_addtwo(self):
        self.assertEqual(jenkinsTest.add_two(10,5), 15)

    def test_split(self):
        self.assertEqual(jenkinsTest.hello_world(), 'Hello World')

if __name__ == '__main__':
    unittest.main() lakes
    
