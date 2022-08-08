import random

import flet
from flet import (
    Column,
    Container,
    Image,
    Page,
    Row,
    Text,
    UserControl,
    alignment,
    border,
    border_radius,
    colors,
)


class GameProgress(UserControl):
    def __init__(self, attempts) -> None:
        super().__init__()
        self.attempts = attempts
        self.letters_guessed = 0
        self.attempts_failed = 0
        self.lives = Text(value=f"Lives: {self.attempts}", text_align="center", size=30)
        self.img = Image(src=f"/hangman-0.png", width=500, fit="cover")

    def attempt_failed(self):
        self.attempts = self.attempts - 1
        self.attempts_failed = self.attempts_failed + 1
        self.lives.value = f"Lives: {self.attempts}"
        file_name = "/hangman-" + str(self.attempts_failed) + ".png"

        self.img.src = f"{file_name}"
        if self.attempts < 0:
            self.lives.value = "You lost!"
        self.update()

    def build(self):
        return Column(
            controls=[
                Container(content=self.lives),
                Container(content=self.img),
            ]
        )


class WordLetter(UserControl):
    def __init__(self, letter) -> None:
        super().__init__()
        self.letter = letter

    def reveal(self):
        self.txt.visible = True
        self.cont.border = None
        self.update()

    def build(self):
        self.txt = Text(self.letter, visible=False, size=20)
        self.cont = Container(
            content=self.txt,
            border=border.all(1),
            width=20,
        )
        return self.cont


def main(page: Page):
    page.title = "Hangman"
    page.vertical_alignment = "center"

    game_data = GameProgress(9)
    lives = Text(value=f"Lives: {game_data.attempts}", text_align="center", size=30)
    words = [
        "dog",
        "helicopter",
        "flower",
        "apple",
        "refrigerator",
        "hangman",
        "stranger",
        "boat",
    ]
    i = random.randint(0, len(words) - 1)
    word = words[i]
    word_letters = list(word.upper())

    display_word_letters = Row()
    alphabet_letters = Row(wrap=True)

    for letter in word_letters:
        display_word_letters.controls.append(WordLetter(letter))

    def letter_clicked(e):
        found = False
        for word_letter in display_word_letters.controls:
            if e.control.data == word_letter.letter:
                e.control.bgcolor = colors.GREEN_100
                word_letter.reveal()
                game_data.letters_guessed = game_data.letters_guessed + 1
                found = True
        if not found:
            game_data.attempt_failed()
            # lives.value = f"Lives: {game_data.attempts}"
            e.control.bgcolor = colors.BLUE_GREY_100

            # e.control.disabled = True
        if game_data.letters_guessed == len(display_word_letters.controls):
            game_data.lives.value = "You won!"

        page.update()

    for letter in [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]:
        alphabet_letters.controls.append(
            Container(
                content=Text(letter, size=20),
                bgcolor=colors.BLUE_100,
                padding=5,
                border=border.all(2),
                border_radius=border_radius.all(5),
                on_click=letter_clicked,
                data=letter,
                width=30,
                alignment=alignment.center,
            )
        )

    page.add(
        Row(
            controls=[
                Column(
                    width=500,
                    controls=[
                        Container(content=display_word_letters),
                        alphabet_letters,
                    ],
                ),
                # Column(
                #     controls=[
                #         Container(content=lives),
                #         Container(content=game_data.img),
                #     ]
                # ),
                game_data,
            ],
        )
    )


flet.app(target=main, assets_dir="images")
