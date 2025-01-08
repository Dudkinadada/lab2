import unittest


class MyTestCase(unittest.TestCase):
    def test_valid_ipv4_addresses(self):
        valid_ips = [
            "192.168.0.1",
            "255.255.255.255",
            "0.0.0.0",
            "127.0.0.1"
        ]
        for ip in valid_ips:
            with self.subTest(ip=ip):
                self.assertTrue(re.fullmatch(IPV4_REGEX, ip))
    def test_invalid_ipv4_addresses(self):
        invalid_ips = [
            "256.256.256.256",
            "192.168.1",
            "192.168.0.0.1",
            "192.168.0.-1",
            "abc.def.ghi.jkl"
        ]
        for ip in invalid_ips:
            with self.subTest(ip=ip):
                self.assertFalse(re.fullmatch(IPV4_REGEX, ip))


if __name__ == '__main__':
    unittest.main()
