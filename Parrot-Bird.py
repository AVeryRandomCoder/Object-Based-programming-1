class Parrot:
  species = "Bird"
  def __init__(self, name, age):
    self.name = name
    self.age = age

Twink = Parrot("Twink", 10)
Wubba = Parrot("Wubba", 15)

print("Twink is a {}".format(Twink.species))
print("Wubba is also a {}".format(Wubba.species))

print("{} is {} years old".format(Twink.age))
print("{} is {} years old".format(Wubba.aage))
