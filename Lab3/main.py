from pprint import pprint
from serializer_factory.serializer_factory import Serializer_Factory
import argparse
import configparser


def test(sep=" "):
    def inside(string: str):
        return string.strip(sep)

    return inside



def parse_config_file(config_file):
    """
         parse_config_file, a function that reads arguments from the provided configuration file.

         :param config_file: config_file file whose format is ini.
         :type config_file: config_file.ini
     """
    config = configparser.ConfigParser()
    config.read(config_file)

    if 'config' in config:
        config_section = config['config']
        if all(param in config_section
               for param in ['source_file', 'source_format', 'destination_file', 'destination_format']):
            return (config_section['source_file'], config_section['source_format'],
                    config_section['destination_file'], config_section['destination_format'])

    return None


def parse_cli():
    """
         parse_cli, a function that reads arguments from the CMD.
     """
    parser = argparse.ArgumentParser(description='JSON / XML serializer')
    parser.add_argument('source_file', type=str, help='Path to source file')
    parser.add_argument('source_format', type=str, choices=['json', 'xml'], help='Format of source file')
    parser.add_argument('destination_file', type=str, help='Path to destination file')
    parser.add_argument('destination_format', type=str, choices=['json', 'xml'], help='Format of destination file')
    args = parser.parse_args()

    return args.source_file, args.source_format, args.destination_file, args.destination_format


def main():
    config_file = 'config.ini'
    config_values = parse_config_file(config_file)

    source_file, source_format, destination_file, destination_format = config_values if config_values else parse_cli()

    source_serializer = Serializer_Factory.create_serializer(source_format)
    destination_serializer = Serializer_Factory.create_serializer(destination_format)

    with open(source_file, "r") as file:
        obj = source_serializer.load(file)

    with open(destination_file, "w") as file:
        destination_serializer.dump(obj, file)


if __name__ == '__main__':
    main()

# if __name__ == '__main__':
#     factory = Serializer_Factory()
#     json_ser = factory.create_serializer("json")
#     xml_ser = factory.create_serializer("xml")
#     data = test
#     file = "default_files/source.txt"
#
#     # pprint(data("Jeka HOLLLA            "))
#     with open(file, 'w') as f:
#         json_ser.dump(data, f)
#
#     with open(file, 'r') as f:
#         result = json_ser.load(f)
#
#     pprint(open(file, "r").read())
#     pprint(type(result))
#
#     test = result()
#     pprint(test("Jeak sdfs f      "))

# import math
# from pprint import pprint
#
# from json_serializer.json_serializer import JSON_Serializer
#
#
# class A:
#     def my_method(self):
#         return 5
#
#
# class B:
#     def another_method(self):
#         return 6
#
#
# class C(A, B):
#     pass
#
#
# x = 10
#
#
# def my_func(a):
#     return math.sin(x * a)
#
#
# json_ser = JSON_Serializer()
# obj = C()
# ser_obj = json_ser.dumps(obj)
# deser_obj = json_ser.loads(ser_obj)
# pprint(deser_obj.my_method())  # returns 5
# pprint(deser_obj.another_method())  # returns 6
#
# ser_class = json_ser.dumps(C)
# deser_class = json_ser.loads(ser_class)
# obj = deser_class()
# pprint(obj.my_method())   # returns 5
# pprint(obj.another_method())   # returns 6
#
# ser_func = json_ser.dumps(my_func)
# deser_func = json_ser.loads(ser_func)
# pprint(deser_func(20))   # returns sin(10 * 20)
