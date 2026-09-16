from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class ChessBoard(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 8

        pieces = [
            "♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜",
            "♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟",
            "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "",
            "♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙",
            "♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"
        ]

        for piece in pieces:
            button = Button(
                text=piece,
                font_size="32sp"
            )
            self.add_widget(button)


class ChessApp(App):
    def build(self):
        return ChessBoard()


if __name__ == "__main__":
    ChessApp().run()
