import unittest
from katas.nginx_log_parser import parse_log


class TestIsUniqueStr(unittest.TestCase):
    def test1(self):
        log = '122.176.223.47 - - [05/Feb/2024:08:29:40 +0000] "GET /index.html HTTP/1.1" 200 512 "-" "Mozilla/5.0"'
        result = parse_log(log)
        self.assertEqual(result["client_ip"], "122.176.223.47")
        self.assertEqual(result["http_method"], "GET")
        self.assertEqual(result["status"], "200")

    def test2(self):
        log = '10.0.0.1 - - [10/Jan/2023:12:00:00 +0000] "POST /submit HTTP/2.0" 404 0 "-" "curl/7.68.0"'
        result = parse_log(log)
        self.assertEqual(result["path"], "/submit")
        self.assertEqual(result["http_version"], "2.0")
        self.assertEqual(result["status"], "404")

    def test3(self):
        log = '8.8.8.8 - - [01/Mar/2025:23:59:59 +0000] "DELETE /api/v1/item/42 HTTP/1.0" 500 128 "-" "PostmanRuntime/7.26.5"'
        result = parse_log(log)
        self.assertEqual(result["http_method"], "DELETE")
        self.assertEqual(result["response_bytes"], "128")

    def test4(self):
        log = '192.168.1.1 - - [20/Dec/2022:07:07:07 +0000] "PUT /upload HTTP/1.1" 201 2048 "-" "Python-urllib/3.9"'
        result = parse_log(log)
        self.assertEqual(result["user_agent"], "Python-urllib/3.9")

    def test5(self):
        log = '1.2.3.4 - - [15/Aug/2021:00:00:01 +0000] "HEAD /health HTTP/1.1" 301 0 "-" "HealthChecker/1.0"'
        result = parse_log(log)
        self.assertEqual(result["http_method"], "HEAD")
        self.assertEqual(result["path"], "/health")

    def test6(self):
        log = '255.255.255.255 - - [31/Dec/2029:23:59:59 +0000] "OPTIONS /options HTTP/1.1" 204 0 "-" "TestAgent/0.1"'
        result = parse_log(log)
        self.assertEqual(result["status"], "204")

    def test7(self):
        invalid_log = 'INVALID LOG ENTRY'
        with self.assertRaises(ValueError):
            parse_log(invalid_log)


if __name__ == "__main__":
    unittest.main()
