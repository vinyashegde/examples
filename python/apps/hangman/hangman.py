import random

import flet
from flet import (
    Column,
    Container,
    Page,
    Row,
    Text,
    UserControl,
    alignment,
    border,
    border_radius,
    colors,
)


class GameData:
    def __init__(self, attempts) -> None:
        self.attempts = attempts


def main(page: Page):
    page.title = "Hangman"
    page.vertical_alignment = "center"

    game_data = GameData(10)
    lives = Text(value=f"Lives: {game_data.attempts}", text_align="center", size=30)
    words = ["dog", "helicopter", "flower", "apple"]
    i = random.randint(0, len(words) - 1)
    word = words[i]
    word_letters = list(word.upper())

    display_word_letters = Row()
    alphabet_letters = Row(wrap=True)

    for letter in word_letters:
        display_word_letters.controls.append(
            Container(
                content=Text(letter, visible=True),
                border=border.all(1),
                width=20,
            )
        )

    def letter_clicked(e):
        found = False
        for letter in word_letters:
            if e.control.data == letter:
                e.control.bgcolor = colors.GREEN_100
                found = True
        if not found:
            game_data.attempts = game_data.attempts - 1
            lives.value = f"Lives: {game_data.attempts}"
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
                Container(content=lives, width=300),
            ],
        )
    )


flet.app(target=main)
