from turtle import Turtle,Screen
import pandas as pd

data = pd.read_csv("50_states.csv")
state_list=data["state"].to_list()
guessed=[]
screen = Screen()
pointer= Turtle()
pointer.hideturtle()
screen.title("US State Guessing Game")
screen.setup(height=491,width=725)
screen.bgpic("blank_states_img.gif")


while len(guessed) < 50:
    text = screen.textinput("Guess","Enter-State").title()
    if text in state_list:
        row = data[data.state == text]
        pointer.penup()
        pointer.goto(int(row["x"]), int(row["y"]))
        pointer.pendown()
        pointer.write(f"{text}", align="center", font=("caliber", 16, "normal"))
        guessed.append(text)
    elif text=="Exit":
        missing=[state for state in state_list if state not in guessed]
        # for state in state_list:
        #     if state not in guessed:
        #         missing.append(state)
        df = pd.DataFrame(missing)
        df.to_csv("missing_state.csv")
        break
    else:
        continue





screen.exitonclick()