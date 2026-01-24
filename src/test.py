from color import ImageWork, RGB
from ImageOutput import image_output
from file_manage import PathManagement

path_manage = PathManagement()
save_path = path_manage.connect_path("movie")
path_manage.make_dir(save_path)

shape = (500, 700)
image_matrix = [[RGB(0, 0, 0) for i in range(shape[1])] for j in range(shape[0])]

image = ImageWork(image_matrix, shape)
image = image.rectangle_fill((100,100), (300,300), RGB(225, 225, 225))
image = image.draw_straight((100,400), (400, 600), RGB(255, 0, 0))

save_name = save_path / "test.png"
print("書き込み開始")
image_output(image, str(save_name))
print("処理終了")