from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import random


class RockPaperScissors(App):
    def build(self):
        self.choices = ['Rock', 'Paper', 'Scissors']
        self.player_score = 0
        self.computer_score = 0
        self.is_multiplayer = False
        self.player1_choice = None
        self.player2_choice = None

        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.result_label = Label(text="Choose Rock, Paper, or Scissors!", font_size=20)
        layout.add_widget(self.result_label)

        self.score_label = Label(text="Player: 0 - Computer: 0", font_size=18)
        layout.add_widget(self.score_label)

        buttons_layout = BoxLayout(spacing=10)
        for choice in self.choices:
            button = Button(text=choice, on_press=self.play)
            buttons_layout.add_widget(button)

        layout.add_widget(buttons_layout)

        bottom_buttons = BoxLayout(spacing=10)
        reset_button = Button(text="Reset Score", on_press=self.reset_score)
        bottom_buttons.add_widget(reset_button)

        multiplayer_button = Button(text="Multiplayer", on_press=self.toggle_multiplayer)
        bottom_buttons.add_widget(multiplayer_button)

        layout.add_widget(bottom_buttons)

        return layout

    def play(self, instance):
        if not self.is_multiplayer:
            self.play_vs_computer(instance.text)
        else:
            self.play_multiplayer(instance.text)

    def play_vs_computer(self, player_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(player_choice, computer_choice)

        if result == "Player wins!":
            self.player_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1

        self.result_label.text = f"You chose {player_choice}\nComputer chose {computer_choice}\n{result}"
        self.score_label.text = f"Player: {self.player_score} - Computer: {self.computer_score}"

    def play_multiplayer(self, player_choice):
        if self.player1_choice is None:
            self.player1_choice = player_choice
            self.result_label.text = "Player 1 has chosen. Player 2, make your choice!"
        else:
            self.player2_choice = player_choice
            result = self.determine_winner(self.player1_choice, self.player2_choice)

            if result == "Player wins!":
                self.result_label.text = f"Player 1 chose {self.player1_choice}\nPlayer 2 chose {self.player2_choice}\nPlayer 1 wins!"
            elif result == "Computer wins!":
                self.result_label.text = f"Player 1 chose {self.player1_choice}\nPlayer 2 chose {self.player2_choice}\nPlayer 2 wins!"
            else:
                self.result_label.text = f"Player 1 chose {self.player1_choice}\nPlayer 2 chose {self.player2_choice}\nIt's a tie!"

            self.player1_choice = None
            self.player2_choice = None

    def determine_winner(self, player, computer):
        if player == computer:
            return "It's a tie!"
        elif (
                (player == 'Rock' and computer == 'Scissors') or
                (player == 'Paper' and computer == 'Rock') or
                (player == 'Scissors' and computer == 'Paper')
        ):
            return "Player wins!"
        else:
            return "Computer wins!"

    def reset_score(self, instance):
        self.player_score = 0
        self.computer_score = 0
        self.score_label.text = "Player: 0 - Computer: 0"
        self.result_label.text = "Choose Rock, Paper, or Scissors!"

    def toggle_multiplayer(self, instance):
        self.is_multiplayer = not self.is_multiplayer
        if self.is_multiplayer:
            self.result_label.text = "Multiplayer mode: Player 1, make your choice!"
            self.score_label.text = "Multiplayer mode active"
            instance.text = "Single Player"
        else:
            self.result_label.text = "Single player mode: Choose Rock, Paper, or Scissors!"
            self.score_label.text = f"Player: {self.player_score} - Computer: {self.computer_score}"
            instance.text = "Multiplayer"
        self.player1_choice = None
        self.player2_choice = None


if __name__ == '__main__':
    RockPaperScissors().run()