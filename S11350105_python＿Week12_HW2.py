import turtle 
per=[75.3,17.2,7]
def main():
    t=turtle.Turtle()
    t.hideturtle()
    for i in range(3):
        draw(t,-200+(120*i),0,120,per[i]*2)
    writeword(t)    
    turtle.exitonclick()    
def draw(t,x,y,w,h,colorP="black",colorF="white"):
    t.pencolor(colorP)
    t.fillcolor(colorF)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.goto(x+w,y)
    t.goto(x+w,y+h)
    t.goto(x,y+h)
    t.goto(x,y)
    t.end_fill()
    
def writeword(t):
    school=["Public","Private","Other"]
    t.pencolor("blue")
    t.up()
    for i in range(3):
        t.goto(-152+(120*i),per[i]*2)
        t.write(str(per[i])+"%",font=("Ariel",10,"normal"))
        t.goto(-152+(120*i),-2)
        t.write(school[i],align="center",font=("Ariel",10,"normal"))
    t.goto(-200,-20)
    t.write("Type of Hight School Attended by Fall 2013 College Freeshmen",font=("Ariel",12,"normal"))
main()
        