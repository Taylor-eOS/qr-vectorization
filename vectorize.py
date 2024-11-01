from PIL import Image

def process_image_to_matrix(image_path):
    image = Image.open(image_path).convert('L')  # Convert image to grayscale
    width, height = image.size
    threshold = 128  # You can adjust this threshold to make the "fuzzy logic" more forgiving
    matrix = []

    for y in range(height):
        row = []
        for x in range(width):
            pixel_value = image.getpixel((x, y))
            row.append(1 if pixel_value < threshold else 0)  # Closer to black (1) or white (0)
        matrix.append(row)

    for row in matrix:
        print(row)

process_image_to_matrix('qr.png')

