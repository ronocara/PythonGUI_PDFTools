from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()


layout = QVBoxLayout();
layout.addWidget(QLabel('PDF Tools'))
layout.addWidget(QPushButton('Overlay'))
layout.addWidget(QPushButton('Merge'))
layout.addWidget(QPushButton('Split'))
layout.addWidget(QPushButton('Convert'))
layout.addWidget(QPushButton('Compress'))
window.setLayout(layout)
window.show()

app.exec() #run app until user closes it
