import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

try:
    existing_items = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_items = []

for arg in arguments:
    existing_items.append(arg)

save_to_json_file(existing_items, "add_item.json")
