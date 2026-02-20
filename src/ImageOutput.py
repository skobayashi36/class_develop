from PIL import Image
from color import ImageWork, RGB

def image_output(imageWorkObject:ImageWork, path:str): # (1.
    matrix = imageWorkObject.matrix # (2.
    shape = imageWorkObject.shape

    #shapeは(行数, 列数)でデータを保存するが、Pillowのnew関数は(幅, 高さ)を期待するので順番を入れ替えた
    img = Image.new("RGB", (shape[1], shape[0])) # (3.

    # height = len(matrix)
    # width = len(matrix[0])
    # size = height * width
    # img = Image.new("RGB", (width, height))

    array = [] # 2次元配列を1次元に開く(4.
    for i in matrix:
        array += i
    
    img.putdata(array) # (5.

    img.save(path, format="PNG") # (6.
    