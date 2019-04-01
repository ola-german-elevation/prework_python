from workers.person import Person, StreetAddress, Phone, PobAddress

import unittest


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        print("setup")


    def test_create_person(self):
        # make sure the shuffled sequence does not lose any elements
        p1 = Person("Ola", "German", 1983, "ola@elevetion.ac.hwltd.com", ["+547266673"], "hakneset hagdola")
        self.assertEqual(p1.first_name, "Ola")
        self.assertEqual(p1.id, 1)
        self.assertEqual(Person._id, 1)



if __name__ == '__main__':
    unittest.main()
