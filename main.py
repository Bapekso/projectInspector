import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QFileDialog
from checker import problems

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.selected_file_path = None

    def initUI(self):
        self.setWindowTitle('Sprawdź plik')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.select_button = QPushButton('Wybierz plik', self)
        self.select_button.clicked.connect(self.chooseFile)
        layout.addWidget(self.select_button)

        self.check_button = QPushButton('Sprawdź plik', self)
        self.check_button.clicked.connect(self.checkFile)
        layout.addWidget(self.check_button)

        self.result_area = QTextEdit(self)
        self.result_area.setReadOnly(True)
        layout.addWidget(self.result_area)

        self.setLayout(layout)

    def chooseFile(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, 'Wybierz plik', os.getenv('HOME'), "Pliki Python (*.py)")
            if file_path:
                self.selected_file_path = file_path
        except Exception as e:
            self.result_area.setText(f'Błąd: {str(e)}')

    def checkFile(self):
        try:
            if self.selected_file_path:
                self.result_area.clear()
                results = problems(self.selected_file_path)
                if isinstance(results, list):
                    self.result_area.setText('\n'.join(results))
                else:
                    self.result_area.setText(results)
            else:
                self.result_area.setText("Proszę wybrać plik przed sprawdzeniem.")
        except Exception as e:
            self.result_area.setText(f'Błąd: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
