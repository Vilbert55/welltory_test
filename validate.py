import json
import os
from jsonschema import validate, Draft7Validator


def help_text(error):
    key_obj = error.message.split("'")[1]
    if error.validator == "type":
        key = " ".join(list(error.path))
        return f"Invalid data type in key '{key}', data type expected '{error.validator_value}'"

    if error.validator == "required":
        return f"Required key '{key_obj}' is missing, the required keys are:\n{error.validator_value}"


def json_file_validation(file_name):

    messages = [f"Validate '{file_name}'", ]

    with open(f"event/{file_name}", "r", encoding="utf-8") as myjson:
        try:
            json_object = json.load(myjson)
            if not isinstance(json_object, dict):
                messages.append(f"File '{file_name}' is not JSON-file")
                return False, messages
            if not json_object:
                messages.append(f"File '{file_name}' is empty")
                return False, messages

        except json.decoder.JSONDecodeError as error:
            messages.append("Invalid JSON, needs to be corrected: %s" % error)
            return False, messages

    schema_name = json_object.get("event")
    data = json_object.get("data")

    if not schema_name:
        messages.append(
            "Required key 'event' is missing, check the key in the JSON file")
    if not data:
        messages.append(
            "Required key 'data' is missing, check the key in the JSON file")

    if not (schema_name and data):
        return False, messages

    try:
        with open(f"schema/{schema_name}.schema", "r", encoding="utf-8") as schema:
            schema_obj = json.load(schema)
    except FileNotFoundError:
        messages.append(
            f"No such schema with name '{schema_name}', check the key 'event' value")
        return False, messages

    validator = Draft7Validator(schema_obj)

    if validator.is_valid(data):
        messages.append("Validate successful!")
        return True, messages
    else:
        messages.append("ERRORS:")

    errors = validator.iter_errors(json_object["data"])
    for error in errors:
        messages.append("---------------")
        messages.append(error.message)
        messages.append(help_text(error))

    return False, messages


if __name__ == "__main__":
    json_files = os.listdir("event/")
    with open('log.txt', 'w') as f:
        data = []
        count = len(json_files)
        err_count = 0
        for json_file in json_files:
            result, messages = json_file_validation(json_file)
            data.append(messages)
            if not result:
                err_count += 1
        print(
            f"Total: {count}, Fails: {err_count}, Passed: {count - err_count}\n", file=f)
        for file_msgs in data:
            for msg in file_msgs:
                print(msg, file=f)
            print("\n================================\n", file=f)
