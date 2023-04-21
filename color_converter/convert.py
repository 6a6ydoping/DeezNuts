def bits_to_rgb(color):
    red = (color >> 16) & 0xFF
    green = (color >> 8) & 0xFF
    blue = color & 0xFF
    return red, green, blue

# print(bits_to_rgb(9927659))