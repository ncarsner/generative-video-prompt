import ast


def remove_duplicates_from_lists(file_path):
    """
    Remove duplicates from all lists in a given Python file and overwrite the file with the updated lists.

    Args:
    - file_path (str): The path to the Python file to modify.
    """
    with open(file_path, "r") as file:
        code = file.read()

    tree = ast.parse(code)

    class ListTransformer(ast.NodeTransformer):
        def visit_Assign(self, node):
            if isinstance(node.value, ast.List):
                list_items = [item.value for item in node.value.elts if isinstance(item, ast.Constant)]
                unique_items = list(set(list_items))
                unique_items.sort(key=list_items.index)  # Preserve original order
                node.value.elts = [ast.Constant(value=item) for item in unique_items]
            return node

    transformer = ListTransformer()
    modified_tree = transformer.visit(tree)
    modified_code = ast.unparse(modified_tree)

    with open(file_path, "w") as file:
        file.write(modified_code)


if __name__ == "__main__":
    file_path = "./component_words.py"
    remove_duplicates_from_lists(file_path)
