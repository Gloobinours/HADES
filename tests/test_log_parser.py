import unittest
from utils.logs.log_parser import parse_logs 
from mock_files import mock_file_generator
class TestLogParser(unittest.TestCase):

    def test_parse_log(self):
        sample_log = mock_file_generator.create_mock_cowrie_log()
        
        result = list(parse_logs(sample_log))
        
        self.assertIn('ls', result)
        self.assertIn('cd /', result)
        self.assertIn('cat /etc/passwd', result)
        self.assertEqual(len(result), 3)

if __name__ == "__main__":
    unittest.main()
