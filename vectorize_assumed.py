from PIL import Image

def process_qr_image(input_path='qr.png', output_path='processed_qr.svg', grid_size=83, square_size=10):
    try:
        img = Image.open(input_path).convert('RGB')
    except FileNotFoundError:
        print(f"Error: The file '{input_path}' was not found.")
        return
    except Exception as e:
        print(f"Error opening image: {e}")
        return
    resized_img = img.resize((grid_size, grid_size), Image.Resampling.LANCZOS)
    svg_elements = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{grid_size * square_size}" height="{grid_size * square_size}">']
    for y in range(grid_size):
        for x in range(grid_size):
            r, g, b = resized_img.getpixel((x, y))
            grayscale = (r + g + b) / 3
            if grayscale < 128:
                svg_elements.append(f'<rect x="{x * square_size}" y="{y * square_size}" width="{square_size}" height="{square_size}" fill="black" />')
    svg_elements.append('</svg>')
    with open(output_path, 'w') as f:
        f.write('\n'.join(svg_elements))
    print(f"Processed SVG image saved as '{output_path}'.")

if __name__ == '__main__':
    process_qr_image()

