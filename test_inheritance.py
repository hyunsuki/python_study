#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Character:
    def __init__(self, hp=None, mp=None):
        self.hp = hp
        self.mp = mp

    def getHp(self): return self.hp

    def getMp(self): return self.mp


class Weapon:
    def __init__(self, demage=None):
        self.demage = demage

    def getDemage(self): return self.demage


class Warrior(Character):
    def __init__(self, hp, mp): pass
#        self.hp = hp
#        self.mp = mp


class Wizard(Character):
    def __init__(self, hp, mp):
        super(Wizard, self).__init__()
#        self.hp = hp
#        self.mp = mp


class Archer(Character):
    def __init__(self, hp, mp):
        super().__init__()
#        self.hp = hp
#        self.mp = mp


class Paladin(Character, Weapon):
    def __init__(self, hp, mp, weapon_demage):
        Character.__init__(hp, mp)
        Weapon.__init__(weapon_demage) 
#        self.hp = hp
#        self.mp = mp
#        self.demage = weapon_demage


class Npc(Character): pass


def main():
    # 마법사 객체 생성
    wizard = Wizard(70, 130)

    # 마법사 객체  HP, MP 확인
    print(f"\nwizard.getHp() :: {wizard.getHp()}")
    print(f"wizard.getMp() :: {wizard.getMp()}")

    # 궁수 객체 생성
    archer = Archer(80, 100)

    # 궁수  객체  HP, MP 확인
    print(f"\narcher.getHp() :: {archer.getHp()}")
    print(f"archer.getMp() :: {archer.getMp()}")

    # 팔라딘 객체 생성
    paladin = Paladin(150, 100, "sword")

    # 팔라딘 객체  HP, MP, Demage 확인
    print(f"\npaladin.getHp() :: {paladin.getHp()}")
    print(f"paladin.getMp() :: {paladin.getMp()}")
    print(f"paladin.getDemage() :: {paladin.getDemage()}")

    # NPC 객체 생성
    npc = Npc()

    # NPC  객체  HP, MP 확인
    print(f"\nnpc.getHp() :: {npc.getHp()}")
    print(f"npc.getMp() :: {npc.getMp()}")

    # 전사 객체 생성
    warrior = Warrior(180, 60)

    # 전사 객체 HP, MP 확인
    print(f"\nwarrior.getHp() :: {warrior.getHp()}")
    print(f"warrior.getMp() :: {warrior.getMp()}")


if __name__ == "__main__":
    main()
