class Builder(object):
    def build_body(self):
        raise NotImplementedError()

    def build_lamp(self):
        raise NotImplementedError()

    def build_battery(self):
        raise NotImplementedError()

    def create_flashlight(self):
        raise NotImplementedError()


class Flashlight(object):
    """Карманный фонарик"""

    def __init__(self, body, lamp, battery):
        self._shine = False  # излучать свет
        self._body = body
        self._lamp = lamp
        self._battery = battery

    def on(self):
        self._shine = True

    def off(self):
        self._shine = False

    def __str__(self):
        shine = 'on' if self._shine else 'off'
        return 'Flashlight [%s]' % shine


class Lamp(object):
    """Лампочка"""


class Body(object):
    """Корпус"""


class Battery(object):
    """Батарея"""


class FlashlightBuilder(Builder):
    def build_body(self):
        return Body()

    def build_battery(self):
        return Battery()

    def build_lamp(self):
        return Lamp()

    def create_flashlight(self):
        body = self.build_body()
        lamp = self.build_lamp()
        battery = self.build_battery()
        return Flashlight(body, lamp, battery)

class A:
    a = 222


class MyClass:

    @classmethod
    def method(cls, arg):
        print('%s classmethod. %d' % (cls.__name__, arg))

    @classmethod
    def call_original_method(cls):
        cls.method(5)

    def call_class_method(self):
        self.method(10)


class MySubclass():

    def call_original_method(self):
        self.method(6)



if __name__ == "__main__":

    a = MySubclass
    a.call_original_method()

    def removeDuplicates(nums) -> int:
        resp = []
        resp.append(nums[0])
        length = len(nums)
        i = 1
        while i < len(nums):
            print(i)
            if nums[i - 1] != nums[i]:
                resp.append(nums[i])
            elif i == length - 1 and nums[i-1] != nums[i]:
                resp.append(nums[i])
            i = i + 1
        return len(resp)

    a=[1,1,2]


    # print(removeDuplicates(a))