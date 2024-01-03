import json
import os
from config import ROOT_DIR

OPERATION_PATH = os.path.join(ROOT_DIR, 'src', 'operations.json')


def load_json_operations():
    with open(OPERATION_PATH) as file:
        operation_files = json.load(file)
    return operation_files


