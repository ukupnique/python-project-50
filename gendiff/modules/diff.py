def common_and_different(dict1, dict2):
    common = dict1.keys() & dict2.keys()
    removed = dict1.keys() - dict2.keys()
    added = dict2.keys() - dict1.keys()
    return common, removed, added


def diff(dict1, dict2):
    keys = sorted(dict1.keys() | dict2.keys())
    common, removed, added = common_and_different(dict1, dict2)
    result = {}
    for key in keys:
        if key in removed:
            description = {
                'key': key, 'operation': 'removed', 'value': dict1[key]}
        elif key in added:
            description = {'key': key,
                           'operation': 'added',
                           'value': dict2[key]}
        elif key in common and dict1[key] == dict2[key]:
            description = {
                'key': key,
                'operation': 'unchanged',
                'value': dict1[key]}
        elif all(
            [key in common,
             dict1[key] != dict2[key],
             isinstance(dict1[key], dict),
             isinstance(dict2[key], dict)]
        ):
            description = {
                'key': key,
                'operation': 'nested',
                'value': diff(dict1[key], dict2[key])}
        else:
            description = {
                'key': key,
                'operation': 'changed',
                'old': dict1[key],
                'new': dict2[key]}
        result[key] = description
    return result
