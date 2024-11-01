from PIL import Image

def process_image_to_matrix(image_path):
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
    return matrix

def find_best_grid(matrix):
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
        print(f'Grid size: {grid_size}: {score}')
        if score > best_score:
            best_score = score
            best_grid_size = grid_size
    return best_grid_size

matrix = process_image_to_matrix('qr.png')
print(find_best_grid(matrix))

