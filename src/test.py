from color import ImageWork, RGB
from ImageOutput import image_output
from file_manage import PathManagement

path_manage = PathManagement()
save_path = path_manage.connect_path("movie")
path_manage.make_dir(save_path)

shape = (500, 700)
image_matrix = [[RGB(0, 0, 0) for i in range(shape[1])] for j in range(shape[0])]

image = ImageWork(image_matrix, shape)
image = image.rectangle_fill((30,30), (200,200), RGB(225, 225, 225))

save_name = save_path / "test(1).png"
print("書き込み開始")
image_output(image, str(save_name))
print("処理終了")