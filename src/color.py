"""
色の管理に関するクラスの定義を行う場所
"""
from collections import namedtuple
from PIL import Image

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
    
    def __init__(self) -> None:
        #行, 列 を引数にとり、matrixを初期化する。 shapeに行数と列数を記録する
        pass

    def rectangle_fill(self):
        #左上の座標, 右下の座標, RGB を引数にとり、長方形の中を全てRGBの値に更新する
        pass

    def draw_straight(self):
        #始点, 終点, RGB を引数にとり、直線上の値をRGBに置き換える
        pass



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