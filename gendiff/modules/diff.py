def common_and_different(dict1, dict2):
    common = dict1.keys() & dict2.keys()
    removed = dict1.keys() - dict2.keys()
    added = dict2.keys() - dict1.keys()
    return common, removed, added


def diff(dict1, dict2):
    keys = sorted(dict1.keys() | dict2.keys())
    common, removed, added = common_and_different(dict1, dict2)
    result = {}
    for k in keys:
        if k in removed:
            result[f'- {k}'] = dict1[k]
        elif k in added:
            result[f'+ {k}'] = dict2[k]
        elif k in common:
            if dict1[k] == dict2[k]:
                result[f'  {k}'] = dict1[k]
            else:
                result[f'- {k}'] = dict1[k]
                result[f'+ {k}'] = dict2[k]
    res = [f"{key}: {value}" for key, value in result.items()]
    return '\n'.join(res)
