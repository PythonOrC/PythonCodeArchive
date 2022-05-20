import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import json

class Ui_potion(object):
    def setupUi(self, potion):
        potion.setObjectName("potion")
        potion.resize(291, 131)
        self.centralwidget = QWidget(potion)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(16, 10, 261, 51))
        self.label.setObjectName("label")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QRect(20, 70, 261, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QRect(20, 100, 261, 21))
        self.pushButton.setObjectName("pushButton")
        potion.setCentralWidget(self.centralwidget)

        self.retranslateUi(potion)
        QMetaObject.connectSlotsByName(potion)

    def retranslateUi(self, potion):
        potion.setWindowTitle(QApplication.translate("potion", "Potion Ingredients", None, -1))
        self.label.setText(QApplication.translate("potion", "TextLabel", None, -1))
        self.pushButton.setText(QApplication.translate("potion", "PushButton", None, -1))

class Potion(QMainWindow, Ui_potion):
    def __init__(self):
        super().__init__()
        self.potions = {
            "swiftness": ["Nether Wart + Sugar", "Awkward Potion + Sugar\n"],
            "slowness": [
                "Nether Wart + Sugar + Fermented Spider Eye\n",
                "Nether Wart + Rabbit's Foot + Fermented Spider Eye\n",
                "Potion of Swiftness + Fermented Spider Eye\n",
                "Potion of Leaping + Fermented Spider Eye\n"
            ],
            "strength": ["Nether Wart + Blaze Powder\n"],
            "weakness": ["Fermented Spider Eye\n"],
            "healing": ["Nether Wart + Glistering Melon\n"],
            "harming": [
                "Nether Wart + Glistering Melon + Fermented Spider Eye\n",
                "Nether Wart + Spider Eye + Fermented Spider Eye\n",
                "Potion of Healing + Fermented Spider Eye\n",
                "potion of Poison + Fermented Spider Eye\n"
            ],
            "regeneration": ["Nether Wart + Ghast Tear\n"],
            "fire resistance": ["Nether Wart + Magma Cream\n"],
            "water breathing": ["Nether Wart + Pufferfish\n"],
            "poison": ["Nether Wart + Spider Eye\n"],
            "night vision": ["Nether Wart + Golden Carrot\n"],
            "invisibility": [
                "Nether Wart + Golden Carrot + Fermented Spider Eye\n",
                "Potion of Night Vision + Fermented Spider Eye\n"
            ],
            "leaping ": ["Nether Wart + Rabbit's Foot\n"],
            "slow falling": ["Nether Wart + Phantom Membrane\n"],
            "turtle master": ["Nether Wart + Turtle Shell\n"],
            "splash potion": ["Gunpowder\n"],
            "lingering potion": ["Gunpowder + Dragon's breath\n"],
            "mundane potion": [
                "Spider Eye\n",
                "Ghast Tear\n",
                "Rabbit's Foot\n",
                "Blaze Powder\n",
                "Glistering Melon\n",
                "Sugar\n",
                "Magma Cream\n",
                "Redstone\n"
            ],
            "thick potion": ["Glowstone\n"],
            "awkward potion": ["Nether Wart\n"]
        }

        self.setupUi(self)
        self.setup()
        self.show()

    def setup(self):
        self.label.setText('Ingredients List')
        self.pushButton.setText('Search')
        self.pushButton.clicked.connect(self.check)

    def check(self):
        self.name = self.lineEdit.text().lower()
        if self.name:
            if self.name in self.potions.keys():
                self.ingredients = self.potions[self.name]
                self.display_text = ""
                for procedure in self.ingredients:
                    self.display_text += procedure
                self.label.setText(self.display_text)
            else:
                self.label.setText("Invalid potion name!")
        else:
            self.label.setText("Please enter the name of the potion!")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Potion()
    sys.exit(app.exec_())
