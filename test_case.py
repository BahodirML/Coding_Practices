import unittest
from last import kattar_harf_qaytar

# class Test(unittest.TestCase):
#     def test_case(self):
#         self.assertTrue(katta_son_qaytar(6,8,25), 25)
# unittest.main()




class Test(unittest.TestCase):
    def get_letter(self):
        self.assertEqual(kattar_harf_qaytar(),['Ism', 'Famikiya', 'Nimadier', 'Olma', 'Uzum', 'Shaftoli'] )

unittest.main()