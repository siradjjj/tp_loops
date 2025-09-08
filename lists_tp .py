
# math = ["charlie", "kevin", "alise", "bob", "leo"]
# physics = ["jack", "paolo", "alex", "bob", "charlie"]


# new_math_student = input("Enter a new student for Math: ")
# math.append(new_math_student)
# print(math)


# new_physics_student = input("Enter a new student for Physics (will be inserted at index 2): ")
# physics.insert(2, new_physics_student)


# math.sort()
# physics.sort()
# print(math)
# print(physics)

# remove_student = input("Enter a student name to remove from Physics: ")
# physics.remove(remove_student)

# print( math) 
# print( physics)




import turtle

side_length = int(input("Enter the size of each side: "))

mbappe = turtle.Turtle()
mbappe.color("yellow")
mbappe.pensize(5)
mbappe.shape("turtle")
mbappe.speed(1)
colors = ["red" , "blue" , "black" , "purple" "pink" , "green" ]
mbappe.fillcolor("bleu")
mbappe.begin_fill()
for i in range (6):
    mbappe.color(color[i])
    mbappe.forward(side_length)
    mbappe.right(60)
mbappe.end_fill()
turtle.done()