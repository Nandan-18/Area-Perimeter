
def area_rect(l, b):
    print("The area of the rectangle = ", l * b)
    print("The perimeter of the rectangle = ", 2 * (l + b))


def area_sqr(side):
    print("The area of the square = ", side * side)
    print("The perimeter of the square = ", 4 * side)


def area_circle(rad):
    print("The area of the circle = ", 3.14 * rad * rad)
    print("The perimeter of the circle = ", 2 * 3.14 * rad)


print(""" 
           ---------------------------------
          | LET'S FIND AREA AND PERIMETER ! |
           ---------------------------------
          |  1. Rectangle   ▭               |
          |  2. Square      ▢               |
          |  3. Circle      O               |
          |  4. EXIT        X               |
          -----------------------------------
      """)

while True:

    ch = int(input("Enter your choice: "))

    if ch == 1:
        length = int(input("Enter length of the rectangle: "))
        b = int(input("Enter breadth of the rectangle: "))
        area_rect(length, b)
    elif ch == 2:
        side = int(input("Enter the side: "))
        area_sqr(side)
    elif ch == 3:
        rad = int(input("Enter the radius: "))
        area_circle(rad)
    elif ch == 4:
        break
    else:
        print("INVALID INPUT !")
