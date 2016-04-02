import unittest

def compress(value_to_compress):
  return value_to_compress

class RunLengthTests(unittest.TestCase):
  def test_given_a_input_we_expect_a_given_output(self):

    compressed_value = compress("AAABBZXA")

    self.assertEqual(compressed_value,"3A2B1Z1X1A")

if __name__ == "__main__":
  unittest.main()
