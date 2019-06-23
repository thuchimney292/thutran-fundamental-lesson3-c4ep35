from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
color(colors[0],colors[0])
for i in range(5):
    color(colors[i],colors[i])
    begin_fill()
    for v in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()
mainloop()
