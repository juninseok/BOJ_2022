# cafe 클래스를 만들고 재고 관리하기

class Cafe:

    def __init__(self, coffee_bean, milk, cookie, cake):
        self.coffee_bean = coffee_bean * 2
        self.milk = milk * 2
        self.cookie = cookie * 2
        self.cake = cake * 2

    def show_goods_in_stock(self):
        print("========================")
        print("coffee_bean : {}".format(self.coffee_bean))
        print("milk : {}".format(self.milk))
        print("cookie : {}".format(self.cookie))
        print("cake : {}".format(self.cake))
        print("========================")

cafe_1 = Cafe(coffee_bean=3, milk=2, cookie=5, cake=1)

cafe_1.show_goods_in_stock()
