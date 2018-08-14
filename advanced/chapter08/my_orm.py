import numbers
# 一种是
class IntField:
    def __init__(self, db_column,min_value=None, max_value=None):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        self.db_column = db_column
        if min_value is not None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError("min_value must be int")
            elif min_value < 0:
                raise ValueError("min_value must be positive int")
        if max_value is not None:
            if not isinstance(max_value, numbers.Integral):
                raise ValueError("max_value must be int")
            elif max_value < 0:
                raise ValueError("max_value must be positive int")

        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError("min_value must be smaller than max_value")


    def __get__(self, instance, value):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        if value < self.min_value or value > self.max_value:
            raise ValueError("value must between min_value and max_value")
        self.value = value

        pass

class CharField:
    def __init__(self, db_column, max_length=None):
        self._value = None
        self.db_column = db_column
        if max_length is None:
            raise ValueError("must specify max_length for charfield")
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("str value need")
        if len(value) > self.max_length:
            raise ValueError("value len excess len of max_length")
        self.value = value

class ModelMetaClass(type):
    #def __new__(cls, *args, **kwargs):
    # 拆包
    def __new__(cls, name, bases, attrs, **kwargs):
        for key, values in attrs.items():
            pass


class User(metaclass=ModelMetaClass):
    name = CharField(db_column="", max_length=10)
    age = IntField(db_column="", min_value=0, max_value=100)

    class Meta:
        db_table = ""

if __name__ == "__main__":
    user = User()
    user.name = "ajioy" # 数值报错
    user.age = 26 # 字符串报错
    user.save() # 将数据写入数据库中
