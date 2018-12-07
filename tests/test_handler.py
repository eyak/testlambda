import unittest
import index

class TestHandlerCase(unittest.TestCase):
    
    def test_PIL(self):
        try:
            import PIL
            print('PIL', PIL.VERSION)
        except:
            print('PIL failed')

        
    def test_response(self):
        print("testing response.")
        result = index.handler({}, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('Hello World', result['body'])


if __name__ == '__main__':
    unittest.main()
