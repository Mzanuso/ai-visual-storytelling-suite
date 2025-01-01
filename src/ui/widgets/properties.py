from PySide6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit

class PropertiesWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        layout.addLayout(form_layout)

        # Properties fields
        self.sref_id = QLineEdit()
        form_layout.addRow('SREF ID:', self.sref_id)

        self.category = QLineEdit()
        form_layout.addRow('Category:', self.category)