class Person:
    def __init__(self,names,weights):
        self.name = names
        self.weight = weights
    def eat(self,g):
        self.weight += g / 1000
    def diet(self,h):
        self.weight -= h / 100
        
kim = Person('kim',78.1)
print(kim.name+'さんの体重は'+str(kim.weight)+'kgです')
kim.eat(400)
print(kim.name+'さんの体重は'+str(kim.weight)+'kgです')
kim.diet(3)
print(kim.name+'さんの体重は'+str(kim.weight)+'kgです')
        
        