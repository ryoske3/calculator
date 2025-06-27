def add(x,y):
    return x + y


def subtract(x,y):
    return x - y


def multiply(x,y):
    return x * y


def divide(x,y):
    if y == 0:
        return "ゼロで割ることはできません"
    return x / y


def calculator():
    print("簡単なプログラム")
    print("演算を選択：")
    print("1.足し算")
    print("2.引き算")
    print("3.掛け算")
    print("4.割り算")

    while True:

        choice = input("演算番号を入力（1/2/3/4）：")

        num1 = float(input("最初の数値："))
        num2 = float(input("2番目の数値："))

        if choice == '1':
            print(f"結果：{num1} + {num2} = {add(num1,num2)}")
        elif choice == '2':
            print(f"結果：{num1} - {num2} = {subtract(num1,num2)}")
        elif choice == '3':
            print(f"結果：{num1} * {num2} = {multiply(num1,num2)}")
        elif choice == '4':
            print(f"結果：{num1} / {num2} = {divide(num1,num2)}")
        else:
            print("無効な入力です")

        another_calculation = input("別の計算を行いますか？（はい/いいえ）:")
        if another_calculation.lower() != 'はい':
            break

    print("電卓を終了します")

if __name__ == "__main__":
    calculator()


