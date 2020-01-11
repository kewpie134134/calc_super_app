from tkinter import *
from tkinter import ttk

# 2次元配列の通りに、girdでレイアウトを作成する
LAYOUT = [
    ["(", ")", "%", "C"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

# レイアウトの行数を算出
LEN_LAYOUT_X = len(LAYOUT) + 1  # 計算窓の分を余計に1足す

# レイアウトの列数を算出
LEN_LAYOUT_Y = len(LAYOUT[0])

# 記号をまとめた定数、if char in CALC_SYMBOLS:...のように使うために定義
# CALC_SYMBOLS = ("+", "-", "*", "/", "**", "//")
CALC_SYMBOLS = ("+", "-", "*", "/")



class CalcSuperApp(ttk.Frame):
    """電卓アプリ"""

    def __init__(self, master=None):
        super().__init__(master)
        self.exp_list = ["0"]
        self.create_style()
        self.create_widgets()

    def create_style(self):
        """ボタン、ラベルのスタイルを変更"""
        style = ttk.Style()

        # ラベルのスタイルを上書き
        style.configure(
            "TLabel", font=("Meiryo UI", 20),
            background="white", foreground="black",
        )

        # ボタンのスタイルを上書き
        style.configure("TButton", font=("Meiryo UI", 20),
                        background="white", foreground="black")
        style.configure(
            "Equal.TButton", font=("Meiryo UI", 20),
            background="blue", foreground="white",
        )

    def create_widgets(self):
        """ウィジェットの作成、配置"""
        # 計算結果の表示ラベル
        self.display_var = StringVar()
        self.display_var.set("0")  # 初期値を0にする

        display_label = ttk.Label(self, textvariable=self.display_var)
        display_label.grid(
            column=0, row=0, columnspan=4, sticky=(N, S, E, W)
        )

        # レイアウトの作成
        for y, row in enumerate(LAYOUT, 1):
            for x, char in enumerate(row):
                if (char == "="):
                    button = ttk.Button(self, text=char, style="Equal.TButton")
                else:
                    button = ttk.Button(self, text=char)
                button.grid(column=x, row=y, sticky=(N, S, E, W))
                button.bind("<Button-1>", self.calc)
        # Frame自身もトップレベルウィジェットに配置
        self.grid(column=0, row=0, sticky=(N, S, E, W))

        # 横の引き伸ばし設定
        for i in range(LEN_LAYOUT_Y):
            self.columnconfigure(i, weight=1)

        # 各行の引き伸ばし設定
        for i in range(LEN_LAYOUT_X):
            self.rowconfigure(i, weight=1)

        # ウィンドウ自体の引き伸ばし設定
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

    def calc(self, event):
        # 押されたボタンのテキストを取得
        char = event.widget["text"]

        # 最後に押したボタンの内容
        last = self.exp_list[-1]

        # =ボタン(現在の式の評価)の場合
        if char == "=":
            if last in CALC_SYMBOLS:
                self.exp_list.pop()
            exp = eval("".join(self.exp_list))
            self.exp_list = [str(exp)]
        # Cボタン、内容クリア
        elif char == "C":
            self.exp_list = ["0"]
        # +,-,*,/などの記号を押した場合
        elif char in CALC_SYMBOLS:
            """
            階乗計算処理はここではコメントアウト
            """
            # if last == char == "/":
            #     self.exp_list[-1] += "/"
            # elif last == char == "*":
            #     self.exp_list[-1] += "*"
            if last in CALC_SYMBOLS:
                self.exp_list[-1] = char
            else:
                self.exp_list.append(char)
        # それ以外、数字を押した場合
        else:
            if last == "0":
                self.exp_list[-1] = char
            elif last in CALC_SYMBOLS:
                self.exp_list.append(char)
            else:
                self.exp_list[-1] += char

        # リストに格納している式を文字列にし、画面に反映
        self.display_var.set(
            " ".join(self.exp_list)
        )


def main():
    root = Tk()
    root.title("Google電卓 by Python3")
    CalcSuperApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
