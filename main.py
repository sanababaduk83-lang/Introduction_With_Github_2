import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.energy = 30
        self.hungry = 50
        self.alive = True

    def eat(self):
        print("😺 Мням-мням, котик поїв!")
        self.hungry -= 15
        self.energy += 5
        if self.hungry < 0:
            self.hungry = 0

    def sleep(self):
        print("💤 Котик спить...")
        self.energy += 10
        self.hungry += 5

    def play(self):
        print("🐾 Котик грається з клубком ниток!")
        self.happiness += 10
        self.energy -= 5
        self.hungry += 5

    def scratch(self):
        print("😼 Котик дряпає меблі!")
        self.happiness += 5
        self.energy -= 3
        self.hungry += 3

    def is_alive(self):
        if self.hungry >= 100:
            print("☠️Чучмек, ти був сильним, прощавай...")
            self.alive = False
        elif self.energy <= 0:
            print("☠️ Мені було дуже грустно писати це...")
            self.alive = False
        elif self.happiness <= 0:
            print("☠️ Котик впав у депресію, потім його нікто не бачив...")
            self.alive = False

    def end_of_day(self):
        print(f"Щастя = {self.happiness}")
        print(f"Енергія = {self.energy}")
        print(f"Голод = {self.hungry}")

    def live(self, day):
        day = "День " + str(day) + " з життя котика " + self.name
        print(f"{day:=^50}")
        action = random.randint(1, 4)
        if action == 1:
            self.eat()
        elif action == 2:
            self.sleep()
        elif action == 3:
            self.play()
        elif action == 4:
            self.scratch()
        self.end_of_day()
        self.is_alive()


chuchmek = Cat(name="Чучмек")

for day in range(1, 366):
    if not chuchmek.alive:
        break
    chuchmek.live(day)
