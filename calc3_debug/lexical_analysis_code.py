class AdvancedCalculator:
    def __init__(self):
        #演算子の優先順位
        self.precedence = {
            '+':1,
            '-':1,
            '*':2,
            '/':2,
            '^':3 #べき乗
        }


    def tokenize(self,expression):
            """
            数式を字句解析してトークンに分解
            スペースを無視し、数値と演算子を分離
            """
            tokens = []
            i = 0
            while i < len(expression):
                char = expression[i]
                
                #数値の処理
                if char.isdigit() or char == '.':
                    num = char
                    while(i + 1 < len(expression) and (expression[i+1].isdigit() or expression[i+1] == '.')):
                        i += 1
                        num += expression[i]
                    tokens.append(float(num))

                #演算子とかっこの処理
                elif char in '+-*/^()':
                    tokens.append(char)
                
                #スペースは無視
                elif not char.isspace():
                    raise ValueError(f"不正な文字: {char}")

                i += 1

            return tokens


    def calculate(self,expression):
        """
        メイン計算メソッド
        """
        #字句解析
        tokens = self.tokenize(expression)
        
        return tokens




def main():
    calculator = AdvancedCalculator()

    print("高度な電卓")
    print("数式を入力してください（例: 3 + (4 * 2) - 1）")
    print("サポートされる演算: +, -, *, /, ^")
    print("終了するには 'q' を入力")


    user_input = input("数式を入力: ")


    result = calculator.calculate(user_input)
    #result = calculator.tokenize(user_input)
    print(result)
    print("字句解析結果のトークン表示")
    print(f"結果：{result}")
   


if __name__ == "__main__":
    main()


                
