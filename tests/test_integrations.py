import math_server.package.mathematical_http_server as http_server
import math_server.package.mathematical_socket_server as socket_server
import math_server.package.mat_socket_client as socket_client
import json
import unittest


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.app = http_server.app
        http_server.app.config['TESTING'] = True
        self.client = http_server.app.test_client()

    def test(self):
        server = socket_server.Server()
        server.processing()
        client = socket_client.Client()
        result = client.send(('add', '44', '66'))
        assert result == '110.0'

    def test_2(self):
        response = self.client.post("/", data={})

        resp_json = response.data
        resp_dict = json.loads(resp_json)

        self.assertIn("code", resp_dict)


if __name__ == '__main__':
    unittest.main()
