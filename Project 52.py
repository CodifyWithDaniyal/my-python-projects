class Car:
    color="Red"
    body="Sexy"
    front="Two lights"
    back="Two lights"
    def info(self):
        print(f"{self.color} should be the color of my car")
a=Car()
a.body
a.front
a.back="Three lights"
a.body="good"
a.bay()