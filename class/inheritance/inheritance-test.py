

class Human():
    def __init__(self) -> None:
        print('インスタンス化しました')
        self.hp = 100

class WizardClass(Human):
    def __init__(self) -> None:
        super().__init__()
        print('ウィザードを継承')

class SwordFighterClass(Human):
        # イニシャライザを省略した時、自動的に親クラスのイニシャライザを実行
    def __init__(self) -> None:
        super().__init__()  #   親クラスのイニシャライザを実行


# 多重継承の場合はsuper().__init__で最初に継承したクラスのイニシャライザが実行される
class MagicSwordFiterClass(WizardClass, SwordFighterClass):
    def __init__(self) -> None:
        super().__init__()

h = Human()
w = WizardClass()
print(w.hp)
ms = MagicSwordFiterClass()