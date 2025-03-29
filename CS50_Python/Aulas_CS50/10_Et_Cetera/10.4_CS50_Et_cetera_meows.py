class Cat:
    MEOWS = 3 # Constant variable

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()  # Output: meow meow meow