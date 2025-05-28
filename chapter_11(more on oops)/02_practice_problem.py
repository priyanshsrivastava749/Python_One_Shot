class animal: 
  def speak():
    print("ANIMAL SPEAKS!")

class pet(animal):
  def talk():
    print("Pet animal talks!")

class dog(pet):
  def bark():
    print("DOG BARKS")



a = dog
a.speak()
a.talk()
a.bark()