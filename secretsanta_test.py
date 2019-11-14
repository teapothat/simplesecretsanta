import unittest
from secretsanta import create_santa_list_random, create_santa_list_chain, verify_not_same

class TestStringMethods(unittest.TestCase):

    def test_create_santa_list_random(self):
        names = {"a": "x@x", "b": "z@z"}
        result = create_santa_list_random(names)
        self.assertEquals(result["a"], "b")
        self.assertEquals(result["b"], "a")

    def test_create_santa_list_random_one_entry(self):
        names = {"a": "x@x"}
        result = create_santa_list_random(names)
        self.assertEquals(result["a"], "a")

    def test_create_santa_list_random_none(self):
        names = {}
        result = create_santa_list_random(names)
        self.assertEquals(len(result), 0)

    def test_create_santa_list_chain(self):
        names = {"a": "x@x", "b": "z@z"}
        result = create_santa_list_chain(names)
        self.assertEquals(result["a"], "b")
        self.assertEquals(result["b"], "a")

    def test_verify_not_same(self):
        org = ["a", "b", "c"]
        new = ["a", "b", "c"]
        verify_not_same(org, new)
        self.assertEquals(new, ["b", "c", "a"])

    def test_verify_not_same_one(self):
        org = ["a"]
        new = ["a"]
        verify_not_same(org, new)
        self.assertEquals(new, ["a"])


if __name__ == '__main__':
    unittest.main()