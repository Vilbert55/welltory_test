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
                return messages
        except json.decoder.JSONDecodeError as error:
            messages.append("Invalid JSON, needs to be corrected: %s" % error)
            return messages

    schema_name = json_object.get("event")

    if not schema_name:
        messages.append(
            "required key 'event' is missing, check the key in the JSON file")
        return messages

    try:
        with open(f"schema/{schema_name}.schema", "r", encoding="utf-8") as schema:
            schema_obj = json.load(schema)
    except FileNotFoundError:
        messages.append(
            f"No such schema with name '{schema_name}', check the key 'event' value")
        return messages

    validator = Draft7Validator(schema_obj)
    if validator.is_valid(json_object["data"]):
        messages.append("Validate successful!")
        return messages
    else:
        messages.append("ERRORS:")

    errors = validator.iter_errors(json_object["data"])
    for error in errors:
        messages.append("---------------")
        messages.append(error.message)
        messages.append(help_text(error))

    return messages


if __name__ == "__main__":
    json_files = os.listdir("event/")
    with open('log.txt', 'w') as f:
        for json_file in json_files:
            result = json_file_validation(json_file)
            for msg in result:
                print(msg, file=f)
            print("\n================================\n", file=f)
