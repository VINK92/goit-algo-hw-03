import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    order = int(input("Введіть глибину рекурсії (ціле число): "))

    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    snowflake = turtle.Turtle()
    snowflake.color("blue")

    snowflake.penup()
    snowflake.goto(-150, 90)
    snowflake.pendown()

    for _ in range(3):
        koch_snowflake(snowflake, order, 300)
        snowflake.right(120)

    window.mainloop()

if __name__ == "__main__":
    main()
