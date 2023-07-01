def flood_fill(image, start_x, start_y, new_color):
    if image[start_x][start_y] == new_color:
        return

    old_color = image[start_x][start_y]
    fill_helper(image, start_x, start_y, old_color, new_color)

def fill_helper(image, x, y, old_color, new_color):
    if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] != old_color:
        return

    image[x][y] = new_color

    fill_helper(image, x + 1, y, old_color, new_color)  # Fill right neighbor
    fill_helper(image, x - 1, y, old_color, new_color)  # Fill left neighbor
    fill_helper(image, x, y + 1, old_color, new_color)  # Fill bottom neighbor
    fill_helper(image, x, y - 1, old_color, new_color)  # Fill top neighbor

# Example usage:
image = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 5, 1],
    [1, 0, 3, 0, 1],
    [1, 1, 1, 1, 1]
]

print("Original Image:")
for row in image:
    print(row)

flood_fill(image, 1, 1, 2)  # Fill the region starting at (1, 1) with the color 2

print("\nImage after Flood Fill:")
for row in image:
    print(row)
