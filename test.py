import requests
import unittest 
  
class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test(self):         
        self.assertTrue(True)
        res = requests.get('http://localhost/retoibm/sumar/12/2000')
        print(res.status_code)
        print(res.text)
  
if __name__ == '__main__': 
    unittest.main() 