from PIL import Image

def image_to_vector(image_path):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size
    data = []
    for y in range(height):
        for x in range(width):
            coord = (x, y)
            color = pixels[x, y]
            if color != (255, 255, 255):
                pixel_data = [coord, color]
                data.append(pixel_data)
    return data

print(image_to_vector("moon.png")) #Сюда путь к имеджу