from PIL import Image

def image_to_rows(image_path):
    image = Image.open(image_path).convert('L')
    width, height = image.size
    rows = []
    for y in range(height):
        row = []
        for x in range(width):
            pixel_value = image.getpixel((x, y))
            row.append(pixel_value)
        rows.append(row)
    return rows

image_path = 'qr.png'
rows = image_to_rows(image_path)
for row in rows:
    print(row)

