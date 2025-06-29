class RPNCalculator:
    def __init__(self):
        self.stack = []

    def push(self,value):
        """スタックに値をプッシュする"""
        self.stack.append(value)

    def pop(self):
        """スタックから値をポップする"""
        if not self.stack:
            raise ValueError('スタックが空です')
        return self.stack.pop()

    def add(self):
        """足し算"""
        b = self.pop()
        a = self.pop()
        self.push(a + b)

    def subtract(self):
        """引き算"""
        b = self.pop()
        a = self.pop()
        self.push(a - b)

    def multiply(self):
        """掛け算"""
        b = self.pop()
        a = self.pop()
        self.push(a * b)

    def divide(self):
        """割り算"""
        b = self.pop()
        a = self.pop()
        if b == 0:
            raise ValueError("ゼロで割ることはできません")
        self.push(a / b)

    def calculate(self,tokens):
        """トークンを処理して計算を行う"""
        for token in tokens:
            if isinstance(token,(int,float)):
                self.push(token)
            elif token == '+':
                self.add()
            elif token == '-':
                self.subtract()
            elif token == '*':
                self.multiply()
            elif token == '/':
                self.divide()
            else:
                raise ValueError(f"無効な演算子: {token}")

        return self.stack[-1] if self.stack else None



def main():
    calculator = RPNCalculator()
    
    print("逆ポーランド記法電卓")
    print("数値と演算子を空白区切りで入力してください")
    print("例: 3 4 + (3 + 4)") 
    print("終了するには 'q' を入力")

    while True:
        try:
            user_input = input("入力:")

            if user_input.lower() == 'q':
                break

            # 入力を解析
            tokens = []
            for item in user_input.split():
                try:
                    # 数値に変換できるか試みる
                    tokens.append(float(item))
                except ValueError:
                    # 数値でない場合は演算子
                    tokens.append(item)
            
            result = calculator.calculate(tokens)
            print(f"結果: {result}")
        
        except Exception as e:
            print(f"エラー: {e}")


if __name__ == "__main__":
    main()


