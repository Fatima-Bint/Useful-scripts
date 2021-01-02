import unittest


class IDHashingCollisionTest(unittest.TestCase):

    def test_that_no_hash_collisions_for_1000_stones_with_given_fields(self):
        """
        Test that no hash collision occurs for 1000 stones with the given model
        fields
        :return:
        """