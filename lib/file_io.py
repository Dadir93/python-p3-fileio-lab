def write_file(file_name, file_content):
    file_path = file_name.with_suffix('.txt')
    try:
        with open(file_path, 'w') as file:
            file.write(file_content)
        print(f'File "{file_path}" written successfully.')
    except Exception as e:
        print(f'Error writing file: {e}')

def append_file(file_name, file_content):
    file_path = file_name.with_suffix('.txt')
    try:
        with open(file_path, 'a') as file:
            file.write(file_content)
        print(f'Content appended to file "{file_path}" successfully.')
    except Exception as e:
        print(f'Error appending to file: {e}')

def read_file(file_name):
    file_path = file_name.with_suffix('.txt')
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
        return file_content
    except Exception as e:
        print(f'Error reading file: {e}')
        return None