from PySide6.QtWidgets import QPushButton


class MyButtons(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        font = self.font()
        font.setPixelSize(30)
        self.setFont(font)
        self.setFixedHeight(80)
        self.setFixedWidth(1200)
