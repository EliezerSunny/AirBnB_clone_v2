import unittest
from console import HBNBCommand
from models import storage
from models.state import State
from models.place import Place
from io import StringIO
import sys

class TestHBNBCommandCreate(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def test_create_state_with_name(self):
        output = StringIO()
        sys.stdout = output
        self.console.onecmd('create State name="California"')
        sys.stdout = sys.__stdout__
        state_id = output.getvalue().strip()
        self.assertIn(state_id, storage.all(State).keys())
        self.assertEqual(storage.all(State)[state_id].name, "California")

    def test_create_place_with_parameters(self):
        output = StringIO()
        sys.stdout = output
        self.console.onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
        sys.stdout = sys.__stdout__
        place_id = output.getvalue().strip()
        place = storage.all(Place)[place_id]
        self.assertEqual(place.city_id, "0001")
        self.assertEqual(place.user_id, "0001")
        self.assertEqual(place.name, "My little house")
        self.assertEqual(place.number_rooms, 4)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 10)
        self.assertEqual(place.price_by_night, 300)
        self.assertEqual(place.latitude, 37.773972)
        self.assertEqual(place.longitude, -122.431297)

if __name__ == '__main__':
    unittest.main()
