import random

from combat import Combat


class Character(Combat):
    attack_limit = 10
    experiance = 0
    base_hit_points = 10

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        if self.weapon = 'sword':
            roll += 1
        elif self.weapon = 'axe':
            roll += 2
        return roll > 4

    def get_weapon(self):
        weapon.choice = input("Pick a weapon [S]word [A]xe [B]ow").lower()
        if weapon.choice in 'sab':
            if weapon.choice == 's':
                return 'sword'
        elif weapon.choice == 'a':
            return 'axe'
        else:
            return 'bow'
            return self.get_weapon()


    def __init__(self, **kwarges):
        self.name = input("Name: ")
        self.weapon = self.get_weapon()
        self.hit_points = self.base_hit_points()

        for key, value in kwarges.items():
            setattr(self, key, value)

    def __str__(self):
        if self.hit_points < self.base_hit_points:
            self.hit_points +=1

    def leveled_up(self):
        return self.experiance >= 5
