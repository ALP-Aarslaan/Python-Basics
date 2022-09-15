class Phone:

    def call(self):
        print("you can call")

    def message(self):
        print("you can message")


class OnePlus (Phone):
    # def call(self):
    #     print("you can call good")
    def picture(self):
        print("you can take picture")


ph1 = Phone()
ph1.call()
ph1.message()
print("\n\n")
ph2 = OnePlus()
ph2.call()
ph2.message()
ph2.picture()