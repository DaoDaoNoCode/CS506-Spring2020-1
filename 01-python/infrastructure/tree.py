def draw_tree(height=5):
    if height<=0:
        print("tree not found")
    else:
        for i in range(height):
            print(' ' * (height - i) + '*' * (2 * i + 1))
        print(' ' * height + "|")
    return
