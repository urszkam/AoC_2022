import unittest
from first_part import count_max_calories


class TestCountCalories(unittest.TestCase):
    def count_calories(self):
        data = {'function': count_max_calories(),
                'expected': 69795,
                'msg': 'incorrect result'}
        self.assertEqual(data['result'], data['expected'], data['msg'])
        
