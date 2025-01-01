from PySide6.QtWidgets import QWidget, QHBoxLayout, QGraphicsView, QGraphicsScene

class TimelineWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout(self)

        # Graphics view for timeline
        self.view = QGraphicsView()
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)
        layout.addWidget(self.view)