from PIL import Image

img = Image.open("Il Palazzo dei Papi ad Avignone.png")

result = ""

width, height = img.size
for y in range(height):
    for x in range(width):
        r, g, _, _ = img.getpixel((x,y))
        result += f"{r},"
    result += "\n"
    for x in range(width):
        _, g, _, _ = img.getpixel((x,y))
        result += f"{g},"
    result += "\n"
    for x in range(width):
        _, _, b, _ = img.getpixel((x,y))
        result += f"{b},"
    result += "\n"

with open("image_to_rgb_pixel_rows_output.txt", "w") as out:
    out.write(result)