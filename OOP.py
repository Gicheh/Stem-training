class Dog:
    def __init__(self,no_of_eyes, color,no_of_legs,tail,no_of_ears):
        self.no_of_eyes=no_of_eyes
        self.color=color
        self.no_of_legs=no_of_legs
        self.tail=tail
        self.no_of_ears=no_of_ears
    def barking(self):
        print("woof woof!")
    def movement(self):
        print("running")
german_shepherd=Dog(no_of_eyes=2,color="black",no_of_legs=4,tail="short",no_of_ears=2)
dodger=Dog(color="white",no_of_eyes=2,no_of_legs=4,tail="long",no_of_ears=2)
Dobberman=Dog(2,"brown",4,"short",2)

print(german_shepherd.no_of_eyes,german_shepherd.color,german_shepherd.tail)
print(dodger.color,dodger.no_of_legs,dodger.no_of_ears)

Dobberman.color="dark brown"
print(Dobberman.color)
Dobberman.movement()
dodger.barking()