from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

class RockPaperScissors(App):
    def build(self):
        self.choices = ['Rock', 'Paper', 'Scissors']
        self.player_score = 0
        self.computer_score = 0

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

        reset_button = Button(text="Reset Score", on_press=self.reset_score)
        layout.add_widget(reset_button)

        return layout

    def play(self, instance):
        player_choice = instance.text
        computer_choice = random.choice(self.choices)

        result = self.determine_winner(player_choice, computer_choice)

        if result == "Player wins!":
            self.player_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1

        self.result_label.text = f"You chose {player_choice}\nComputer chose {computer_choice}\n{result}"
        self.score_label.text = f"Player: {self.player_score} - Computer: {self.computer_score}"

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

if __name__ == '__main__':
    RockPaperScissors().run()