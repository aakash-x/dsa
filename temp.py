class Base:
    def __new__(cls):
        print(f"[Base.__new__] cls: {cls}")
        instance = super().__new__(cls)
        print(f"[Base.__new__] instance: {instance}")
        return instance

    def __init__(self):
        print("[Base.__init__]")

class Child(Base):
    def __new__(cls):
        print(f"[Child.__new__] cls: {cls}")
        instance = super().__new__(cls)
        print(f"[Child.__new__] instance: {instance}")
        return instance

    def __init__(self):
        print("[Child.__init__]")

obj = Child()
