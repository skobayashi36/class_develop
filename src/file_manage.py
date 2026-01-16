import pathlib

class PathManagement:
    def __init__(self) -> None:

        #実行されたファイルのあるディレクトリの絶対パス
        self.current = pathlib.Path(__file__).resolve().parent

    def connect_path(self, *pathes:str) -> pathlib.Path:
        new_path = self.current
        for next_path in pathes: #引数を一つずつ取り出す
            new_path = new_path / next_path #pathlibのオブジェクトは / 演算子で接続が可能
        
        return new_path
    
    def make_dir(self, path):
        # pathを引数にディレクトリを作成する(既に存在する場合は作成しない)
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)



#===========以下デバッグ用===================
if __name__ == "__main__":
    print("\n直接実行した時のみこのスコープ内の処理が実行されます。")

    #パスの管理のためのインスタンスを作成する
    path_manage_obj = PathManagement()


    #3つの文字列を引数として新たなパスを作る

    new_path = path_manage_obj.connect_path("next_path", "next_next_path", "debug.txt")
    #typeはpathlib.WindowsPathとなっており、柔軟な操作が可能だがそのまま他のライブラリが利用することはできない
    print(new_path, type(new_path))

    str_new_path = str(new_path)
    #typeがstrとなっており、柔軟な操作ができない代わりに様々なライブラリがこの変数をPCのパスとして読み込むことができる
    print(str_new_path, type(str_new_path))

    #ディレクトリ(フォルダ)作成
    path_manage_obj.make_dir()