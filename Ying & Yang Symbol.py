from turtle import *



def ying_yang_func(radius,color1,color2):

    width(3)
    color("black",color1)
    begin_fill()

    circle(radius/2.0,180)
    circle(radius,180)
    left(180)
    circle(-radius/2.0,180)
    end_fill()

    left(90)

    up()

    forward(radius*0.35)
    right(90)

    down()

    color(color1,color2)
    begin_fill()

    circle(radius*0.15)
    end_fill()

    left(90)

    up()
    backward(radius*0.35)
    down()
    left(90)


def main():

    reset()
    ying_yang_func(200,"black","white")
    ying_yang_func(200,"white","black")
    ht()

    return "Ying-Yang Generated"

if __name__ == '__main__':

    main()
    mainloop()





