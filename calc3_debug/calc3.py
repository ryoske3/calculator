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


    def infix_to_postfix(self,tokens):
                """
                中置記法（通常の数式）から後置記法（逆ポーランド記法）への変換
                """
                output = []
                operator_stack = []

                for token in tokens:
                    #数値はそのまま出力
                    if isinstance(token, float):
                        output.append(token)

                    #左括弧はスタックに追加
                    elif token == '(':
                        operator_stack.append(token)
                    
                    #右括弧が来たら、左括弧まで演算子を出力
                    elif token == ')':
                        while operator_stack and operator_stack[-1] != '(': 
                            output.append(operator_stack.pop())
                    
                        #左括弧を取り除く
                        if operator_stack and operator_stack[-1] == '(':
                            operator_stack.pop()
                        else:
                            raise ValueError("括弧の対応が不正です")
                
                    #演算子の処理
                    elif token in self.precedence:
                        #優先順位の高い演算子を先に出力
                        while(operator_stack and self.precedence.get(operator_stack[-1], 0) >= self.precedence[token]):
                            output.append(operator_stack.pop())
                        operator_stack.append(token)


                #残りの演算子を出力
                while operator_stack:
                    if operator_stack[-1] == '(':
                        raise ValueError("括弧の対応が不正です")
                    output.append(operator_stack.pop())

                return output


    def evaluate_postfix(self,postfix):
        """
        後置記法の式を計算
        """
        stack = []

        for token in postfix:
            if isinstance(token,float):
                stack.append(token)
            else:
                #二項演算子
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        raise ValueError("ゼロ除算エラー")
                    stack.apend(a / b)
                elif token == '^':
                    stack.append(a ** b)

        return stack[0]


    def calculate(self,expression):
        """
        メイン計算メソッド
        """
        #字句解析
        tokens = self.tokenize(expression)

        #中間記法から後置記法への変換
        postfix = self.infix_to_postfix(tokens)

        #後置記法の式を計算
        return self.evaluate_postfix(postfix)


def main():
    calculator = AdvancedCalculator()

    print("高度な電卓")
    print("数式を入力してください（例: 3 + (4 * 2) - 1）")
    print("サポートされる演算: +, -, *, /, ^")
    print("終了するには 'q' を入力")

    while True:
        try:
            user_input = input("数式を入力: ").replace(' ','')

            if user_input.lower() == 'q':
                break

            result = calculator.calculate(user_input)
            print(f"結果：{result}")

        except Exception as e:
            print(f"エラー: {e}")

if __name__ == "__main__":
    main()

