import math
import image_processing.main as im

def fill_with_circles(data):
    circles = []
    while data:
        _, color = data[0]
        pixels = [coord for coord, c in data if c == color]

        min_x, min_y = min(pixels)
        max_x, max_y = max(pixels)
        radius = min((max_x - min_x) // 2, (max_y - min_y) // 2)

        center_x = min_x + radius
        center_y = min_y + radius

        circles.append([(center_x, center_y), radius])

        new_data = []
        for coord, c in data:
            dx = center_x - coord[0]
            dy = center_y - coord[1]
            if dx**2 + dy**2 > radius**2 or c != color:
                new_data.append([coord, c])
        data = new_data

    return circles


print(fill_with_circles(im.image_to_vector(
    "C:/Users/Али/PycharmProjects/colors/image_processing/moon.png"))) #Сюда абсолютный path
