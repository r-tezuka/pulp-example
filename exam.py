#ライブラリのインポート
import pulp

#目的関数の設定と変数の設定
problem = pulp.LpProblem('sample', pulp.LpMaximize)
a = pulp.LpVariable('a',0,10)
b = pulp.LpVariable('b',0,5)

#制約条件の記述
problem += a >= 2
problem += b >= 1
problem += 700000*a + 650000*b <= 5000000

status = problem.solve()
print("Status", pulp.LpStatus[status])

print(problem)

print("result")
print("a",a.value())
print("b",b.value())

## 結果 a=2.5 b=5.0になります。