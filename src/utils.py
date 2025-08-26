import json

def load_server_list(file_path):
    with open(file_path, "r") as f:
        return json.load(f)