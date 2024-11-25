import colorgram

# Extract 30 colors from an image.
colors = colorgram.extract('image.jpg', 30)

rgb_color = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    t_rgb = (r, g, b)
    rgb_color.append(t_rgb)
    