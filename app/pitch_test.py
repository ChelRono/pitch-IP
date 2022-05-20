import unittest
from models import pitch
Pitch = pitch.Pitch

class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Pitch class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_pitch = Pitch('Valarie Rono','pickup-lines','I must be in a museum, because you truly are a work of art.','September 3rd, 2020')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))


if __name__ == '__main__':
    unittest.main()