from gendiff.modules.open_file import open_file
from gendiff.modules.parser import parser
from gendiff.modules.diff import diff
from gendiff.modules.formatters.apply_format import apply_format


def generate_diff(path1, path2, format='stylish'):
    data1, format1 = open_file(path1)
    data2, format2 = open_file(path2)
    dict1 = parser(data1, format1)
    dict2 = parser(data2, format2)
    diff_result = diff(dict1, dict2)
    return apply_format(diff_result, format)
