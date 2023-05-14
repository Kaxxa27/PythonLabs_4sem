import types
import inspect
import re
from serializer.constants import BASIC_TYPES, SET_TYPES, SEQUENCE_TYPES, \
    BINARY_SEQUENCE_TYPES, SAME_SEQUENCE_TYPES, MAPPING_TYPES, ALL_COLLECTIONS_TYPES, \
    CODE_PROPERTIES, CLASS_PROPERTIES, TYPES, DECORATOR_METHODS


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

        # Serialization class.
        elif inspect.isclass(obj):
            return self.serialize_class(obj)

        else:
            return self.serialize_object(obj)

    def serialize_basic_types(self, obj):
        serialize_result = dict()
        serialize_result["type"] = self.get_object_type(obj)
        serialize_result["value"] = obj
        return serialize_result

    def serialize_none_type(self):
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

    def serialize_class(self, obj):
        serialize_result = dict()
        serialize_result["type"] = "class"
        serialize_result["value"] = self.total_class_serialize(obj)
        return serialize_result

    def total_class_serialize(self, obj):
        serialize_result = dict()
        serialize_result["__name__"] = self.serialize(obj.__name__)

        for key, value in obj.__dict__.items():

            if key in CLASS_PROPERTIES or type(value) in TYPES:
                continue

            if isinstance(obj.__dict__[key], staticmethod):
                serialize_result[key] = dict()
                serialize_result[key]["type"] = "staticmethod"
                serialize_result[key]["value"] = {
                    "type": "function", "value": self.total_function_serialize(value.__func__, obj)
                }

            elif isinstance(obj.__dict__[key], classmethod):
                serialize_result[key] = dict()
                serialize_result[key]["type"] = "classmethod"
                serialize_result[key]["value"] = {
                    "type": "function", "value": self.total_function_serialize(value.__func__, obj)
                }

            elif inspect.ismethod(value):
                serialize_result[key] = self.total_function_serialize(value.__func__, obj)

            elif inspect.isfunction(value):
                serialize_result[key] = dict()
                serialize_result[key]["type"] = "function"
                serialize_result[key]["value"] = self.total_function_serialize(value, obj)

            else:
                serialize_result[key] = self.serialize(value)

        serialize_result["__bases__"] = dict()
        serialize_result["__bases__"]["type"] = "tuple"
        serialize_result["__bases__"]["value"] = [self.serialize(base) for base in obj.__bases__ if base != object]

        return serialize_result

    def serialize_object(self, obj):
        serialize_result = dict()
        serialize_result["type"] = "object"
        serialize_result["value"] = self.total_object_serialization(obj)
        return serialize_result

    def total_object_serialization(self, obj):
        value = dict()
        value["__class__"] = self.serialize(obj.__class__)
        value["__members__"] = {key: self.serialize(value) for key, value in inspect.getmembers(obj)
                                if not (key.startswith("__") or inspect.isfunction(value) or inspect.ismethod(value))}
        return value

    def deserialize(self, obj):

        if obj["type"] in self.extract_keys(str(BASIC_TYPES.keys())):
            return self.deserialize_basic_types(obj)

        elif obj["type"] in str(SAME_SEQUENCE_TYPES.keys()):
            return self.deserialize_collections(obj)

        elif obj["type"] == "code":
            return self.deserialize_code(obj["value"])

        elif obj["type"] == "function":
            return self.deserialize_function(obj["value"])

        elif obj["type"] == "cell":
            return self.deserialize_cell(obj)

        elif obj["type"] == "class":
            return self.deserialize_class(obj["value"])

        elif obj["type"] in DECORATOR_METHODS:
            return DECORATOR_METHODS[obj["type"]](self.deserialize(obj["value"]))

        elif obj["type"] == "object":
            return self.deserialize_object(obj["value"])

    def deserialize_basic_types(self, obj):
        return BASIC_TYPES[obj["type"]](obj["value"])

    def deserialize_collections(self, obj):
        collection_type = obj["type"]

        if collection_type in SAME_SEQUENCE_TYPES.keys():
            return SAME_SEQUENCE_TYPES[collection_type](self.deserialize(item) for item in obj["value"])

        elif collection_type in ALL_COLLECTIONS_TYPES.keys():
            return ALL_COLLECTIONS_TYPES[collection_type](
                {self.deserialize(item[0]): self.deserialize(item[1]) for item in obj["value"]})

    def deserialize_code(self, code):
        return types.CodeType(*(self.deserialize(code[prop]) for prop in CODE_PROPERTIES))

    def deserialize_function(self, func):
        code = func["__code__"]
        globs = func["__globals__"]
        func_closure = func["__closure__"]
        des_globals = self.deserialize_globals(globs, func)

        cl = self.deserialize(func_closure)
        if cl:
            closure = tuple(cl)
        else:
            closure = tuple()
        codeType = self.deserialize_code(code)

        des_globals["__builtins__"] = __import__("builtins")
        des_function = types.FunctionType(code=codeType, globals=des_globals, closure=closure)
        des_function.__globals__.update({des_function.__name__: des_function})

        return des_function

    def deserialize_globals(self, globs, func):
        des_globals = dict()

        for glob in globs:
            if "module" in glob:
                des_globals[globs[glob]["value"]] = __import__(globs[glob]["value"])

            elif globs[glob] != func["__name__"]:
                des_globals[glob] = self.deserialize(globs[glob])

        return des_globals

    def deserialize_cell(self, obj):
        return types.CellType(self.deserialize(obj["value"]))

    def deserialize_class(self, obj):
        bases = self.deserialize(obj["__bases__"])

        members = {member: self.deserialize(value) for member, value in obj.items()}

        cls = type(self.deserialize(obj["__name__"]), bases, members)

        for k, member in members.items():
            if inspect.isfunction(member):
                member.__globals__.update({cls.__name__: cls})
            elif isinstance(member, (staticmethod, classmethod)):
                member.__func__.__globals__.update({cls.__name__: cls})

        return cls

    def deserialize_object(self, obj):
        cls = self.deserialize(obj["__class__"])
        des = object.__new__(cls)
        des.__dict__ = {key: self.deserialize(value) for key, value in obj["__members__"].items()}
        return des

    # def(BASIC_TYPES) -> return  str: [ int, float, complex, ... ]
    def extract_keys(self, string) -> str:
        return re.search(r"\[.*\]", string).group()
