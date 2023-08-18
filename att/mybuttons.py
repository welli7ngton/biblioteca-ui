from PySide6.QtWidgets import QPushButton


class MyButtons(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        font = self.font()
        font.setPixelSize(40)
        font.setBold(True)
        self.setFont(font)
        self.setFixedSize(500, 100)
