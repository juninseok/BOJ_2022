# cafe 클래스를 만들고 재고 관리 이동하기

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

    def move_goods_in_stock(self, cafe, coffee_bean=0, milk=0, cookie=0, cake=0):
        self.coffee_bean = self.coffee_bean - coffee_bean
        self.milk = self.milk - milk
        self.cookie = self.cookie - cookie
        self.cake = self.cake - cake
        cafe.coffee_bean = cafe.coffee_bean + coffee_bean
        cafe.milk = cafe.milk + milk
        cafe.cookie = cafe.cookie + cookie
        cafe.cake = cafe.cake + cake


cafe_1 = Cafe(2,2,2,2)
cafe_2 = Cafe(3,3,3,3)

cafe_1.show_goods_in_stock()
cafe_2.show_goods_in_stock()

cafe_1.move_goods_in_stock(cafe_2, coffee_bean=1, cookie=1)

cafe_1.show_goods_in_stock()
cafe_2.show_goods_in_stock()