import json


def json_to_py(json_data, py_file):
    # Parse the JSON data
    data = json.loads(json_data)

    # Open the Python file for writing
    with open(py_file, 'w') as f:
        # Write each line to the Python file
        for line_number, value in data.items():
            f.write(f'{line_number} = "{value}"\n')