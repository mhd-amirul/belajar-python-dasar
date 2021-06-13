# ==== Class 1

# == Catatan:

# Apa itu Class?
#    Jawab :
#    cth case dari game :
#                      / Player1(HP, Atk, Block) \
#        Instances <--|  Player2(HP, Atk, Block)  |-->  Template/Blueprint ----> Classs
#                      \ Player3(HP, Atk, Block) /
#
#              Class =    <----------|
#        /       |      \            |
# Instances Instances Instances  ----|

class Enemy():
    Name = 'name'
    HP = 100
    Atk = 5

class Ally():
    Name = 'name'
    HP = 100
    Atk = 50

Enemy1 = Enemy()
Enemy1.Name = 'Hilicurl'
Ally1 = Ally()
Ally1.Name = 'Eula'
print('============================')
print('Nama   :',Ally1.Name,
        '\nAttack :',Ally1.Atk,
        '\nHP     :',Ally1.HP)
print('============================')
print('Nama   :',Enemy1.Name,
        '\nAttack :',Enemy1.Atk,
        '\nHP     :',Enemy1.HP)