import unittest
from models.engine.file_storage import FileStorage
from models.state import State

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up for the tests"""
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}

    def test_all(self):
        """Test that all returns the correct dictionary of objects"""
        state = State()
        self.storage.new(state)
        self.storage.save()
        all_objects = self.storage.all()
        self.assertIn(f"State.{state.id}", all_objects)

        # Test filtering by class
        state2 = State()
        self.storage.new(state2)
        self.storage.save()
        all_states = self.storage.all(State)
        self.assertEqual(len(all_states), 2)
        self.assertIn(f"State.{state.id}", all_states)
        self.assertIn(f"State.{state2.id}", all_states)

    def test_delete(self):
        """Test that delete removes an object from storage"""
        state = State()
        self.storage.new(state)
        self.storage.save()
        self.assertIn(f"State.{state.id}", self.storage.all())
        self.storage.delete(state)
        self.assertNotIn(f"State.{state.id}", self.storage.all())

    def test_delete_none(self):
        """Test that delete does nothing if obj is None"""
        initial_objects = self.storage.all().copy()
        self.storage.delete(None)
        self.assertEqual(self.storage.all(), initial_objects)

if __name__ == '__main__':
    unittest.main()
