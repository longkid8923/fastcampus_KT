# -*- coding: utf-8 -*-
import sqlite3

## 데이터베이스를 연결하는 코드
conn = sqlite3.connect('D:/python_basic/fastcampus_KT/shoppingmall.db', isolation_level=None)
c1 = conn.cursor()

# 상품과 주문 테이블을 생성하는 코드
# c1.execute(
#     "CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY, name TEXT, price INTEGER)"
# )

# c1.execute(
#     "DELETE FROM orders"
#     #"CREATE TABLE IF NOT EXISTS orders(id INTEGER, name TEXT, price INTEGER, number INTEGER, total_price INTEGER)"
# )

## 상품 데이터를 추가하는 코드
# productList = (
#     (1, 'noodle', '1000'),
#     (2, 'milk', '3000'),
#     (3, 'bread', '2000'),
#     (4, 'salt', '5000'),
#     (5, 'yogurt', '3500')
# )

# c1.executemany("INSERT INTO products(id, name, price) VALUES(?, ?, ?)", productList)

## 상품 목록을 표시하는 코드
# c1.execute("SELECT * FROM products")
# product_lst = c1.fetchall()
# for p in product_lst:
#     print(p)




## 상품 번호와 주문 수량을 입력받는 코드
while True:
    print('')
    id = input("구매하실 상품의 번호를 입력해주세요: ")

    print('')
    number = input("구매할 수량을 입력해주세요: ")
    c1.execute("SELECT * FROM products WHERE id = ?", (id))
    id, name, price = c1.fetchone()

    total_price = int(number) * int(price)

    ## 주문 데이터를 db에 추가하는 코드
    c1.execute("INSERT INTO orders(id, name, price, number, total_price) VALUES(?, ?, ?, ?, ?)", (id, name, price, number, total_price))

    is_cont = input("계속 하시겠습니까?(y/n)")
    if is_cont == 'n' or is_cont == 'N':
        break
        




# 현재까지 주문 내역을 출력하는 코드
print('')
print("현재까지 구매한 내역 보기")
print('')
c1.execute("SELECT * FROM orders")
for row in c1.fetchall():
    print(row)


conn.close()