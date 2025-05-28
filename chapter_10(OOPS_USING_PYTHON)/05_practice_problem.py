class Train:
  def __init__(self,seat,fare,name):
    self.seat = seat
    self.name = name
    self.fare = fare
  def get_status(self):
    print(f"THE AVAILABLE SEATS IN THIS TRAIN IS: {self.seat}")
  def book_ticket(self):
    print("THANKS FOR TRAVELING WITH US SUBH JOURNEY!")
    self.seat -= 1
  def get_fare(self):
    print(f"THE FARE OF THIS TRAIN {self.name} IS: {self.fare}")

vardman = Train(4,45,"vardman")
vardman.get_fare()
vardman.get_status()
