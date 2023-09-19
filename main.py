#maruf_bro
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog

class VCFGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('VCF File Generator')
        self.setGeometry(100, 100, 400, 200)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()

        self.names_label = QLabel('Enter names (comma-separated):')
        self.names_entry = QLineEdit()
        layout.addWidget(self.names_label)
        layout.addWidget(self.names_entry)

        self.emails_label = QLabel('Enter emails (comma-separated):')
        self.emails_entry = QLineEdit()
        layout.addWidget(self.emails_label)
        layout.addWidget(self.emails_entry)

        self.phones_label = QLabel('Enter phone numbers (comma-separated):')
        self.phones_entry = QLineEdit()
        layout.addWidget(self.phones_label)
        layout.addWidget(self.phones_entry)

        generate_button = QPushButton('Generate VCF File')
        layout.addWidget(generate_button)
        generate_button.clicked.connect(self.generate_vcf)

        main_widget.setLayout(layout)

    def generate_vcf(self):
        names = self.names_entry.text().split(',')
        emails = self.emails_entry.text().split(',')
        phones = self.phones_entry.text().split(',')

        if not names or not emails or not phones:
            return

        vcf_file_name, _ = QFileDialog.getSaveFileName(self, 'Save VCF File', '', 'VCF Files (*.vcf)')

        if vcf_file_name:
            with open(vcf_file_name, 'w') as vcf_file:
                for name, email, phone in zip(names, emails, phones):
                    vcf_file.write('BEGIN:VCARD\n')
                    vcf_file.write('VERSION:3.0\n')
                    vcf_file.write(f'FN:{name}\n')
                    vcf_file.write(f'EMAIL;TYPE=INTERNET:{email}\n')
                    vcf_file.write(f'TEL;TYPE=CELL:{phone}\n')
                    vcf_file.write('END:VCARD\n')

            self.names_entry.clear()
            self.emails_entry.clear()
            self.phones_entry.clear()

            self.statusBar().showMessage(f'VCF file "{vcf_file_name}" generated successfully.')

def main():
    app = QApplication(sys.argv)
    window = VCFGeneratorApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
