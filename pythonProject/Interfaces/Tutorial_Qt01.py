import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel("<font color=red size=40>Hello World! Olá Mundo!</font>")
label.show()
app.exec_()


