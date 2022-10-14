#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "square", "triangle", "classic"]
horiz_colors = ["blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50
for s in turtle_shapes:

  # create horizontal turtles
  ht = trtl.Turtle(shape=s)
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)

  # create vertical turtles
  
  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions

step = 1
for step in range(50):
	# do something
  if (step % 5 == 0):
    step += 1

  for ht in horiz_turtles:
    destx = ht.xcor() + 5
    desty = ht.ycor()
    ht.pd()

    collision = False

    for vt in vert_turtles:
      if ((abs(ht.xcor() - vt.ycor()) < 20) and (abs(ht.xcor() - vt.xcor()) < 20)):
        ht.shape("circle")
        ht.turtlecolor("red")
        collision = True
        break

    if ht.xcor() < 250:
      ht.forward(step)


  for vt in vert_turtles:
    destx = vt.xcor()
    desty = vt.ycor() - 5
    vt.pd()

    collision = False

    for ht in horiz_turtles:
      if ((abs(vt.ycor() - ht.ycor()) < 20) and (abs(vt.xcor() - ht.xcor()) < 20)):
        vt.shape("circle")
        vt.color("red")
        collision = True
        break

    if (vt.ycor() > -250) and not collision:
      vt.forward(step)

for turt in (vert_turtles + horiz_turtles):
  turt.color("blue")
  turt.shape("triangle")

wn = trtl.Screen()
wn.mainloop()
