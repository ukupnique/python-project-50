import pytest
import ast
from gendiff.modules.formatters import stylish, plain, json


@pytest.fixture
def diff_example():
    with open('tests/fixtures/diff_result.txt', 'r') as result:
        diff_result = ast.literal_eval(result.read())
        return diff_result


def test_build_string():
    assert stylish.build_string({'key': 'hexlet', 'another': 44},
                                'key', 1) == '    hexlet: hexlet'


def test_stylish_format(diff_example):
    with open('tests/fixtures/result_stylish.txt', 'r') as result:
        assert stylish.stylish_format(diff_example) == result.read()


def test_plain_format(diff_example):
    with open('tests/fixtures/result_plain.txt', 'r') as result:
        assert plain.plain_format(diff_example) == result.read()


def test_json_format(diff_example):
    with open('tests/fixtures/result_json.txt', 'r') as result:
        assert json.json_format(diff_example) == result.read()
