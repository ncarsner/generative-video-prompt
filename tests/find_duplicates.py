import ast


def find_duplicates(lst):
    """
    Find duplicate items in a list and return a list of duplicate items.

    Args:
    - lst (list): The input list to examine for duplicate items.

    Returns:
    - list: A list containing the duplicate items found in the input list.
    """
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)


def examine_lists_in_file(file_path):
    """
    Examine all lists in a given Python file and print any duplicate items found.

    Args:
    - file_path (str): The path to the Python file to examine.
    """
    with open(file_path, "r") as file:
        code = file.read()

    tree = ast.parse(code)

    for node in ast.walk(tree):
        if isinstance(node, ast.List):
            list_items = [item.s for item in node.elts if isinstance(item, ast.Str)]
            duplicates = find_duplicates(list_items)
            if duplicates:
                print("Duplicate items found in list:")
                print(list_items)
                print("Duplicate items:", duplicates)
                print()


# Example usage
examine_lists_in_file("component_words.py")
