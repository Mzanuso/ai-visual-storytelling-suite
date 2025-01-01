from PySide6.QtWidgets import QMainWindow, QDockWidget, QTabWidget, QMenuBar
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('AI Visual Storytelling Suite')
        self.resize(1600, 900)
        self.init_ui()

    def init_ui(self):
        # Central widget with tabs
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Initialize dock widgets
        self.init_docks()

        # Create menu bar
        self.create_menu_bar()

    def init_docks(self):
        # Explorer dock
        self.explorer_dock = QDockWidget('SREF Explorer', self)
        self.explorer_dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.explorer_dock)

        # Properties dock
        self.properties_dock = QDockWidget('Properties', self)
        self.properties_dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.addDockWidget(Qt.RightDockWidgetArea, self.properties_dock)

        # Timeline dock
        self.timeline_dock = QDockWidget('Timeline', self)
        self.timeline_dock.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.timeline_dock)

    def create_menu_bar(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        # File menu
        file_menu = menu_bar.addMenu('File')
        # Add menu items