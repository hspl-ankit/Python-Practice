'''Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given
range 0 and n.
Consider use yield'''

class DivisibleBySeven:
    def __init__(self, n):
        self.n = n
    
    def generate(self):
        for i in range(self.n):
            if i % 7 == 0:
                yield i

divisible_by_seven = DivisibleBySeven(50)
for num in divisible_by_seven.generate():
    print(num)

