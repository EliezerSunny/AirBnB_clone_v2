import unittest
from models.engine.file_storage import FileStorage
from models.state import State
from models.place import Place

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()
        self.storage.reload()  # Ensure we start with an empty storage

    def test_all_with_cls(self):
        new_state = State()
        new_state.name = "California"
        self.storage.new(new_state)
        new_place = Place()
        new_place.name = "My little house"
        self.storage.new(new_place)
        self.storage.save()

        all_states = self.storage.all(State)
        all_places = self.storage.all(Place)
        
        self.assertIn(new_state, all_states.values())
        self.assertNotIn(new_place, all_states.values())
        self.assertIn(new_place, all_places.values())

    def test_delete(self):
        new_state = State()
        new_state.name = "California"
        self.storage.new(new_state)
        self.storage.save()
        
        state_id = new_state.id
        self.assertIn("State.{}".format(state_id), self.storage.all().keys())

        self.storage.delete(new_state)
        self.assertNotIn("State.{}".format(state_id), self.storage.all().keys())

if __name__ == '__main__':
    unittest.main()
