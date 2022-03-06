"""Other fun functions! :D"""





def get_dict_attr(obj):
    """Gets attributes of an object then returns it as a dict."""
    def check_if_has_dict(obj):
        return hasattr(obj, "__dict__")

    dictionary = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, list):
            value_list = []
            for value_item in value:
                if not check_if_has_dict(value_item):
                    value_list.append(value_item)
                else:
                    value_list.append(get_dict_attr(value_item))
            dictionary[attr] = value_list
        elif not check_if_has_dict(value):
            dictionary[attr] = value
        else:
            dictionary[attr] = get_dict_attr(value)
    return dictionary
