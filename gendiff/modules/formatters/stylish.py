import itertools


def stylish_value(value, depth):
    if isinstance(value, dict):
        string = ''
        for k, v in value.items():
            space = '    ' * (depth + 1)
            string += f"\n{space}{k}: {stylish_value(v, depth + 1)}"
        s = itertools.chain('{', string, '\n', ['    ' * depth, '}'])
        return ''.join(s)
    else:
        if isinstance(value, bool):
            return str(value).lower()
        elif value is None:
            return 'null'
        else:
            return str(value)


def build_string(dictionary, key, depth, sign='  '):
    string = f"{'  ' * depth}{sign}{dictionary['key']}: " \
             f"{stylish_value(dictionary[key], depth + 1)}"
    return string


def stylish_format(diff_result):  # noqa C901

    def walk(node, depth, replacer='  '):
        space = replacer * (depth + 1)
        strings = ''
        for k, v in node.items():
            if v['operation'] == 'nested':
                strings += (f"\n{space * 2}{v['key']}: "
                            f"{walk((v['value']), depth + 1)}")
            elif v['operation'] == 'unchanged':
                strings += (f"\n{space}"
                            f"{build_string(v, 'value', depth)}").rstrip()
            elif v['operation'] == 'changed':
                strings += (f"\n{space}"
                            f"{build_string(v, 'old', depth, '- ')}").rstrip()
                strings += (f"\n{space}"
                            f"{build_string(v, 'new', depth, '+ ')}").rstrip()
            elif v['operation'] == 'removed':
                strings += (f"\n{space}"
                            f"{build_string(v, 'value', depth, '- ')}").rstrip()
            elif v['operation'] == 'added':
                strings += (f"\n{space}"
                            f"{build_string(v, 'value', depth, '+ ')}").rstrip()
        result = itertools.chain('{', strings, '\n', ['    ' * depth + '}'])
        return ''.join(result)

    return walk(diff_result, 0)
