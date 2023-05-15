from serializer.serializer import Serializer
from json_serializer.json_serializer import JSON_Serializer


class Serializer_Factory:
    """This factory for creating serializer {json/xml}"""
    @staticmethod
    def create_serializer(serializer_frmt: str) -> Serializer:
        """
        Return json_serializer if str: json
        Return xml_serializer if str: xml
        """
        serializer_frmt = serializer_frmt.lower()

        if serializer_frmt == "json":
            return JSON_Serializer()
        # elif serializer_frmt == "xml":
        #     return




