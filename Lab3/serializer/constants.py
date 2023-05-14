import types

BASIC_TYPES = {"int": int, "float": float, "str": str, "bool": bool, "complex": complex}

SEQUENCE_TYPES = {"list": list, "tuple": tuple }

SET_TYPES = {"set": set, "frozenset": frozenset}

BINARY_SEQUENCE_TYPES = {"bytes": bytes,"bytearray": bytearray}

MAPPING_TYPES = {"dict": dict}

SAME_SEQUENCE_TYPES = {"list": list, "tuple": tuple, "frozenset": frozenset, "set": set, "bytes": bytes,
                       "bytearray": bytearray}

ALL_COLLECTIONS_TYPES = {"list": list, "tuple": tuple, "frozenset": frozenset, "set": set, "bytes": bytes,
                         "bytearray": bytearray, "dict": dict}

