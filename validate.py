import json
import os
from jsonschema import validate, Draft7Validator


class JsonValidator:
    def __init__(self):
        self.files_count = 0
        self.passed = 0
        self.messages = []

    def help_text(self, error):
        key_obj = error.message.split("'")[1]
        instance = ""
        value = error.validator_value
        if error.instance:
            instnse_fr = str(error.instance)[:100]
            instance = f"Instanse: {instnse_fr}\n"
        if error.validator == "type":
            key = " ".join(list(error.path))
            return f"{instance}Invalid data type in key '{key}', data type expected '{value}'"

        if error.validator == "required":
            return f"{instance}Required key '{key_obj}' is missing, the required keys are: \n{value}"
        return ""

    def json_file_validation(self, file_name):
        messages = []

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
                messages.append(
                    "Invalid JSON, needs to be corrected:\n %s" % error)
                return False, messages

        schema_name = json_object.get("event")
        data = json_object.get("data")

        if not (schema_name and data):
            if not schema_name:
                messages.append(
                    "Required key 'event' is missing, check the key in the JSON file")
            if not data:
                messages.append(
                    "Required key 'data' is missing, check the key in the JSON file")
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
            messages.append(self.help_text(error))

        return False, messages

    def add_file(self, file_name):
        self.messages.append(f"Validate '{file_name}'")
        self.files_count += 1
        valid, messages = self.json_file_validation(file_name)
        if valid:
            self.passed += 1
        self.messages += messages
        self.messages.append("\n================================\n")


if __name__ == "__main__":
    json_files = os.listdir("event/")
    validator = JsonValidator()
    for json_file in json_files:
        validator.add_file(json_file)

    with open('log.txt', 'w') as f:
        total = validator.files_count
        fails = validator.files_count - validator.passed
        passed = validator.passed
        print(f"Total:{total} Fails:{fails} Passed:{passed}\n", file=f)

        for msg in validator.messages:
            print(msg, file=f)
