print("Hello World")

number =10
print (number)


age=27
max=90.5

name="Brian Kitonyi"


def print_tree(height):
    """
    Prints a simple ASCII tree with the given height.
    """
    # Print the tree
    for i in range(height):
        # Print spaces before the tree branches
        spaces = height - i - 1
        # Print stars for the tree branches
        stars = 2 * i + 1
        
        print(" " * spaces + "*" * stars)
    
    # Print the tree trunk
    trunk_width = 3
    trunk_height = 2
    for i in range(trunk_height):
        trunk_spaces = height - trunk_width // 2 - 1
        print(" " * trunk_spaces + "#" * trunk_width)

# Call the function to print a tree with height 5
if __name__ == "__main__":
    tree_height = 5
    print_tree(tree_height)







    