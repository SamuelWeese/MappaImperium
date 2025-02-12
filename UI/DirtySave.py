import json, importlib

# Ok, so the whole idea about this is that we:
# - look at an object, check if we can serialize
# - iterate through its members
# - find all sub members
# - turn all sub member into pickle or json
# - nest inside parent object
# finally, write to file
# So thinking ahead, we should write once
# and we can iterate through each object, calling the recurions on each child
# not sure we can optimize via dp, as all objects should by definition be different
def jsonify_object(an_object):
    try:
        json.dumps(an_object)
        return an_object
    except (TypeError, OverflowError):
        pass

    if isinstance(an_object, dict):
        return {key: jsonify_object(value) for key, value in an_object.items()}

    if isinstance(an_object, (list, tuple, set)):
        return [jsonify_object(item) for item in an_object]

    if hasattr(an_object, '__dict__'):
        return {
            "__class__": an_object.__class__.__name__,
            "__module__": an_object.__module__,
            "attributes": {key: jsonify_object(value) for key, value in vars(an_object).items()}
        }

    return str(an_object)

# Ok, for loading we want this to check the type
# And then just cast to the type, regardless of type
# We do have json list and json dict
# So two options for that
# And both should probably be recursive
# So we:
# - check which type of json it is, list/dict
# - check what type of module it is, and import it
# - get the attributes
# - check if it has children
# - populate those children, recursively
# - if no children, just populate it.
# We need to add DP so shared objects are recreated TODO
# Not an issue currently

def load_object(json_obj):
    if isinstance(json_obj, dict):
        if "__class__" in json_obj and "__module__" in json_obj:
            class_name = json_obj["__class__"]
            module_name = json_obj["__module__"]
            attributes = json_obj["attributes"]

            module = importlib.import_module(module_name)
            cls_type = getattr(module, class_name)

            obj = cls_type.__new__(cls_type)

            for key, value in attributes.items():
                setattr(obj, key, load_object(value))
            return obj
        else:
            return {key: load_object(value) for key, value in json_obj.items()}

    if isinstance(json_obj, list):
        return [load_object(item) for item in json_obj]

    return json_obj