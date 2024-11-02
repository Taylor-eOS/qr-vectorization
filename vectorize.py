from PIL import Image

def image_to_matrix(image_path):
    image = Image.open(image_path).convert('L')
    width, height = image.size
    threshold = 128
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel_value = image.getpixel((x, y))
            row.append(1 if pixel_value < threshold else 0)
        matrix.append(row)
    for row in matrix:
        print(row)
    print()
    return matrix

def best_grid(matrix):
    max_size = min(len(matrix), len(matrix[0])) // 2
    best_score = 0
    best_grid_size = 1
    for grid_size in range(2, max_size + 1):
        score = 0
        for i in range(grid_size, len(matrix), grid_size):
            for j in range(len(matrix[0])):
                if matrix[i - 1][j] != matrix[i][j]:
                    score += 1
        for j in range(grid_size, len(matrix[0]), grid_size):
            for i in range(len(matrix)):
                if matrix[i][j - 1] != matrix[i][j]:
                    score += 1
        print(f'Grid size {grid_size}: transition score {score / len(matrix)}')
        if score > best_score:
            best_score = score
            best_grid_size = grid_size
    return best_grid_size

def uniformity(matrix, grid_size):
    rows = len(matrix)
    cols = len(matrix[0])
    total_uniformity = 0
    cell_count = 0
    for i in range(0, rows, grid_size):
        for j in range(0, cols, grid_size):
            cell_pixels = []
            for x in range(i, min(i + grid_size, rows)):
                for y in range(j, min(j + grid_size, cols)):
                    cell_pixels.append(matrix[x][y])
            majority_color = max(set(cell_pixels), key=cell_pixels.count)
            uniformity = cell_pixels.count(majority_color) / len(cell_pixels)
            total_uniformity += uniformity
            cell_count += 1
    return total_uniformity / cell_count

def transitions_per_grid_size(matrix):
    max_size = min(len(matrix), len(matrix[0])) // 2
    best_uniformity = 0
    best_grid_size = 1
    for grid_size in range(2, max_size + 1):
        uniformity = uniformity(matrix, grid_size)
        print(f'Grid size {grid_size}: uniformity {uniformity}')
        if uniformity > best_uniformity:
            best_uniformity = uniformity
            best_grid_size = grid_size
    return best_grid_size, best_uniformity

def transitions_per_line(matrix, grid_size):
    rows = len(matrix)
    cols = len(matrix[0])
    transitions_per_line = []
    for i in range(grid_size, rows, grid_size):
        horizontal_transitions = 0
        for j in range(cols):
            if matrix[i - 1][j] != matrix[i][j]:
                horizontal_transitions += 1
        transitions_per_line.append(horizontal_transitions)
    for j in range(grid_size, cols, grid_size):
        vertical_transitions = 0
        for i in range(rows):
            if matrix[i][j - 1] != matrix[i][j]:
                vertical_transitions += 1
        transitions_per_line.append(vertical_transitions)
    return transitions_per_line

def determine_grid_size(matrix):
    max_size = min(len(matrix), len(matrix[0])) // 2
    grid_scores = {}
    for grid_size in range(2, max_size + 1):
        transitions = transitions_per_line(matrix, grid_size)
        median = sorted(transitions)[len(transitions) // 2]
        high_transition_count = sum(1 for t in transitions if t >= median)
        if median > 1: #this needs to be more general
            grid_scores[grid_size] = high_transition_count
        print(f'Grid {grid_size}: median {median}, high transitions {high_transition_count}')
    print(f'Grid size scores: {grid_scores}')
    best_grid_size = max(grid_scores, key=grid_scores.get)
    return best_grid_size

MATRIX1 = image_to_matrix('qr.png')
#best_grid(MATRIX1)
#transitions_per_grid_size(MATRIX1)
best_grid_size = determine_grid_size(MATRIX1)
print(f'best grid size: {best_grid_size}')

