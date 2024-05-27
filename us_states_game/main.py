import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data_ = pandas.read_csv('50_states.csv')
all_states = data_.state.to_list()

game_on = True
correct_ = []

while len(correct_) < 50:
    answer_state = (screen.textinput(title=f'{len(correct_)}/50 States Correct', prompt="What's another state's name?")
                    .capitalize())

    if answer_state == 'Exit'.capitalize():
        missing_states = []
        for state in all_states:
            if state not in correct_:
                missing_states.append(state)
        new_doc = pandas.DataFrame(missing_states)
        new_doc.to_csv('missing_state_doc.csv')
        break
    for rows in data_.values:
        if rows[0] == answer_state:
            state_ = turtle.Turtle()
            state_.hideturtle()
            state_.penup()
            state_.goto(rows[1], rows[2])
            state_.write(rows[0])
            correct_.append(answer_state)

screen.exitonclick()
