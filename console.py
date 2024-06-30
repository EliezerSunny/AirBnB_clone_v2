import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    # Existing code...

    def do_create(self, arg):
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        new_instance = storage.classes()[class_name]()
        
        for param in args[1:]:
            key_value = param.split("=")
            if len(key_value) != 2:
                continue
            key, value = key_value
            value = self.parse_value(value)
            if value is not None:
                setattr(new_instance, key, value)

        new_instance.save()
        print(new_instance.id)

    def parse_value(self, value):
        """Parse a value from the command line to the correct type."""
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1].replace('_', ' ').replace('\\"', '"')
            return value
        elif '.' in value:
            try:
                return float(value)
            except ValueError:
                return None
        else:
            try:
                return int(value)
            except ValueError:
                return None

    # Existing code...

if __name__ == '__main__':
    HBNBCommand().cmdloop()
