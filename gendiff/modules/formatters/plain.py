def plain_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return str(value)
    return f"'{value}'"


def plain_format(diff_result):
    def format_change(current_path, old_value, new_value):
        return (f"Property '{current_path}' was updated. "
                f"From {plain_value(old_value)} to {plain_value(new_value)}\n")

    def format_removal(current_path):
        return f"Property '{current_path}' was removed\n"

    def format_addition(current_path, value):
        return f"Property '{current_path}' was added with value: {plain_value(value)}\n"

    operations = {
        'changed': format_change,
        'removed': format_removal,
        'added': format_addition,
        'nested': lambda path, value: walk(value, path + '.')
    }

    def walk(node, path):
        result = []
        for k, v in node.items():
            current_path = f"{path}{v['key']}"
            operation_func = operations.get(v['operation'])
            if v['operation'] in operations:
                result.append(operation_func(current_path, *(v.get('old'), v.get('new', v.get('value')))))
        return ''.join(result)

    return walk(diff_result, '')
