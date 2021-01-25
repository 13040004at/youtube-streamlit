def adder(a):
    def inner(x):
        # xは関数内関数の引数、aはadder呼び出し時の引数
        return x + a
    return inner

# クロージャを作成し、add3,add5に代入する
add3 = adder(3)
add5 = adder(5)

# add3,add5に代入されたクロージャを呼び出す
print(add3(10))
print(add5(10))