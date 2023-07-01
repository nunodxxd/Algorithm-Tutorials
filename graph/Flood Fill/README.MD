# Flood Fill 

The Flood Fill algorithm has several practical applications. Here are some of its main utilities:
- Image/Fill Coloring: The Flood Fill algorithm can be used to fill closed regions or areas in an image with a specific color or pattern. 
- Image Editing: In image editing software, the Flood Fill algorithm can be used for tasks like removing backgrounds or replacing certain colors with others. 
- Boundary Detection: The Flood Fill algorithm can also be used to detect boundaries or contours within an image. 
- Maze Solving: The Flood Fill algorithm can be applied to solve mazes. By systematically exploring adjacent cells and marking visited areas, it helps in finding paths or determining the connectivity of a maze.

# Code Explanation 

In the code, we have an image represented as a 2D array. The flood_fill function takes the image, starting coordinates, and a new color as input. It calls the fill_helper function to recursively fill the connected region with the new color. The algorithm checks the boundaries and the color of neighboring pixels and updates them accordingly.

The algorithm replaces all connected cells with the same color as the starting point with the new color. It does not discriminate between different colors; it only checks if the neighboring cells have the same color as the starting point.

In the provided example, the algorithm starts at coordinates (1, 1) with a starting color of 0 and replaces all adjacent cells with the value of 0 with the new color of 2. So, in the output, all the cells within the region of connected 0's are changed to 2. Cells outside that region, remain unaffected.

