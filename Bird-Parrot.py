class Parrot:
  species = "Bird"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def sing(self, song):
    return "{} sings {}".format(self.name, song)
  def dance(self):
    return "{} is now dancing.format(self.name)

Twink = Parrot("Twink", 10)
Wubba = Parrot("Wubba", 15)

print(Twink.sing("Your Idol"))
print(Wubba.sing("Ocean man"))

print(Twink.dance())
print(Wubba.dance())
