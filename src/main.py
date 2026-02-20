"""メイン処理をここに記述していく"""
from color import ImageWork, RGB
from ImageOutput import image_output
from file_manage import PathManagement

path_manage = PathManagement()
save_path = path_manage.connect_path("movie")
path_manage.make_dir(save_path)
shape = (700,1000)
image_matrix = [[RGB(0, 0, 0) for i in range(shape[1])] for j in range(shape[0])]
image = ImageWork(image_matrix, shape)

for i in range(0,300,10):
    flame = image.rectangle_fill((200,i), (500,i+300), RGB((i)%225, (i+100)%225, (i+200)%225))

    save_name = save_path / f"{i:4}.png"
    image_output(flame, str(save_name))
    print(i)


