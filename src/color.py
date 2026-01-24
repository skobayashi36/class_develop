"""
色の管理に関するクラスの定義を行う場所
"""
from collections import namedtuple
from PIL import Image
import math, copy

class RGB(namedtuple('RGB', ['r', 'g', 'b'], defaults=[0, 0, 0])):

    """ここにRGB型に実装するメソッド等を書いていく"""

    def _sum(self, *other):
        #クラスの内部処理で使用する。RGB型同士で各値を合計する 内部での計算のため、各値の最大値は無制限
        for i in other:
            if not isinstance(i, RGB):
                raise ValueError("RGB型には直接RGB型以外の値を加算することはできません")
        v1 = self.r
        v2 = self.g
        v3 = self.b
        for rgb in other:
            v1 += rgb[0]
            v2 += rgb[1]
            v3 += rgb[2]
        return (v1, v2, v3)


class ImageWork:
    def __init__(self,matrix, shape) -> None:
        self.matrix = matrix
        self.shape = shape #shapeは(行, 列)

    def rectangle_fill(self, start, end, color:RGB):
        #左上の座標, 右下の座標, RGB を引数にとり、長方形の中を全てRGBの値に更新する
        new_matrix = copy.deepcopy(self.matrix)
        row_start = min(start[0], end[0])
        row_end = max(start[0], end[0])
        col_start = min(start[1], end[1])
        col_end = max(start[1], end[1])
        for row in range(row_start, row_end+1):
            new_matrix[row][col_start:col_end+1] = [color for i in range(col_start, col_end+1)]
        
        return ImageWork(new_matrix, self.shape)

    def draw_straight(self, start, end, color:RGB):
        #始点, 終点, RGB を引数にとり、直線上の値をRGBに置き換える
        new_matrix = copy.deepcopy(self.matrix)
        row_start = min(start[0], end[0])
        row_end = max(start[0], end[0])
        col_start = min(start[1], end[1])
        col_end = max(start[1], end[1])
        row_distance = row_end+1 - row_end
        col_distance = col_end+1 - col_start

        if row_distance < col_distance:
            col_idx = float(col_start)
            for row in range(row_start, row_end+1):
                draw_range = col_idx + (col_distance / row_distance)
                for col in range(int(col_idx), math.ceil(draw_range)):
                    new_matrix[row][col] = color
                col_idx = draw_range

        elif row_distance == col_distance:
            for row in range(row_start, row_end+1):
                for col in range(col_start, col_end+1):
                    new_matrix[row][col] = color

        else:
            row_idx = float(row_start)
            for col in range(col_start, col_end+1):
                draw_range = row_idx + (row_distance / col_distance)
                for row in range(int(row_idx), math.ceil(draw_range)):
                    new_matrix[row][col] = color
                row_idx = draw_range

        return new_matrix



#===========以下デバッグ用===================
if __name__ == "__main__":
    print("直接実行した時のみこのスコープ内の処理が実行されます。")

    color1 = RGB(10, 5, 8)
    print("変数colorの内容",color1)
    print("type = ",type(color1))
    print("計算にも使えます。\ncolor[0] * 5 = ",color1[0] * 5)

    color2 = RGB(4, 6, 2)
    print(f"color1 + color2 = {color1} + {color2} = ", color1 + color2)

    color3 = RGB(7, 3, 5)
    print(f"color1 + color2 + color3 = {color1} + {color2} + {color3} = ",color1 + color2 + color3 )