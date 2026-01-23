from PIL import Image
import pathlib
import random

current = pathlib.Path(__file__).resolve().parent

movie_dir = current / "movie"

width, height = 500, 500
size = width * height

def random_3list(border=255):
    ret = [random.randint(0, border) for i in range(3)]
    return (ret[0], ret[1], ret[2])


def generat(path, widht, height, number):
    size = widht * height
    color_data = [random_3list() for i in range(size)]
    color_img = Image.new('RGB', (width, height))
    color_img.putdata(color_data)
    color_img.save(str(path / f"{number:03}.png"), format="PNG")


num = 5

num = 60

num = 5
for i in range(num):
    generat(movie_dir, width, height, i)
    print(i+1,num)

print("終了")