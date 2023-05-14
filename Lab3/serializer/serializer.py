import types
import inspect
import re
from serializer.constants import BASIC_TYPES, SET_TYPES, SEQUENCE_TYPES, \
    BINARY_SEQUENCE_TYPES, SAME_SEQUENCE_TYPES, MAPPING_TYPES, ALL_COLLECTIONS_TYPES, CODE_PROPERTIES


class Serializer:

    @staticmethod
    def get_object_type(obj) -> str:
        return re.search(r"\'(\w+)\'", str(type(obj)))[1]

    def serialize(self, obj):
        # Serialization of basic types.
        if isinstance(obj, tuple(BASIC_TYPES.values())):
            return self.serialize_basic_types(obj)

        # Serialization None type.
        elif isinstance(obj, types.NoneType):
            return self.serialize_none_type()

        # Serialization of same sequence types.
        # [ list, tuple, frozenset, set, bytes, bytearray ].
        elif isinstance(obj, tuple(SAME_SEQUENCE_TYPES.values())):
            return self.serialize_same_sequence_types(obj)

        # Serialization of mapping types.
        # [ dict ]
        elif isinstance(obj, tuple(MAPPING_TYPES.values())):
            return self.serialize_mapping_types(obj)

        # Serialization function.
        elif inspect.isfunction(obj):
            return self.serialize_function(obj)

        # Serialization code.
        elif inspect.iscode(obj):
            return self.serialize_code(obj)

        # Serialization cell.
        elif isinstance(obj, types.CellType):
            return self.serialize_cell(obj)



    def serialize_basic_types(self, obj):
        serialize_result = dict()
        serialize_result["type"] = self.get_object_type(obj)
        serialize_result["value"] = obj
        return serialize_result

    def serialize_none_type(self, obj):
        serialize_result = dict()
        serialize_result["type"] = "NoneType"
        # serialize_result["value"] = "definitely none"
        serialize_result["value"] = "None"
        return serialize_result

    def serialize_same_sequence_types(self, obj):
        serialize_result = dict()
        serialize_result["type"] = self.get_obj_type(obj)
        serialize_result["value"] = [self.serialize(item) for item in obj]
        return serialize_result

    def serialize_mapping_types(self, obj):
        serialize_result = dict()
        serialize_result["type"] = self.get_obj_type(obj)
        serialize_result["value"] = [[self.serialize(key), self.serialize(value)] for (key, value) in obj.items()]
        return serialize_result

    def serialize_function(self, obj):
        serialize_result = dict()
        serialize_result["type"] = "function"
        serialize_result["value"] = self.total_func_serialize(obj)
        return serialize_result

    def total_func_serialize(self, obj, cls=None):
        value = dict()
        value["__name__"] = obj.__name__
        value["__globals__"] = self.get_globals(obj, cls)
        value["__closure__"] = self.serialize(obj.__closure__)
        value["__code__"] = {key: self.serialize(value) for key, value in inspect.getmembers(obj.__code__)
                             if key in CODE_PROPERTIES}
        return value

    def get_globals(self, obj, cls=None):
        """Work with __globals__ and __code__"""

        globs = dict()
        for global_variable in obj.__code__.co_names:

            if global_variable in obj.__globals__:

                # That prop is module.
                if isinstance(obj.__globals__[global_variable], types.ModuleType):
                    globs[" ".join(["module", global_variable])] = self.serialize(
                        obj.__globals__[global_variable].__name__)

                # That prop is class.
                elif inspect.isclass(obj.__globals__[global_variable]):

                    if cls and obj.__globals__[global_variable] != cls or not cls:
                        globs[global_variable] = self.serialize(obj.__globals__[global_variable])

                elif global_variable != obj.__code__.co_name:
                    globs[global_variable] = self.serialize(obj.__globals__[global_variable])

                # It works out once in order to avoid recursion (serialization of itself).
                else:
                    globs[global_variable] = self.serialize(obj.__name__)

        return globs

    def serialize_code(self, obj):
        serialize_result = dict()
        serialize_result["type"] = "code"
        serialize_result["value"] = {key: self.serialize(value) for key, value in inspect.getmembers(obj)
                                     if key in CODE_PROPERTIES}
        return serialize_result

    def serialize_cell(self, obj):
        serialize_result = dict()
        serialize_result["type"] = "cell"
        serialize_result["value"] = self.serialize(obj.cell_contents)
        return serialize_result
