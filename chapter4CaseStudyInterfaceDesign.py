# import turtle
# bob = turtle.Turtle()



# # def square(t):
# #     for i in range(4):
# #         t.fd(100)
# #         t.lt(90)
# # square(bob)


# # def polygon(t, n, length):
# #     angle = 360 / n
# #     for i in range(n):
# #         t.fd(length)
# #         t.lt(angle)

# # polygon(bob, 8, 50)

# # Tạo đối tượng turtle
# pen = turtle.Turtle()
# pen.speed(3)  # Tốc độ vẽ
# pen.color("red")
# pen.pensize(3)

# # Bắt đầu vẽ trái tim
# pen.begin_fill()
# pen.fillcolor("red")

# pen.left(50)
# pen.forward(133)
# pen.circle(50, 200)
# pen.right(140)
# pen.circle(50, 200)
# pen.forward(133)

# pen.end_fill()

# # Viết chữ lên trái tim
# pen.penup()
# pen.goto(-30, 120)
# pen.pendown()
# pen.color("white")
# pen.write("Love", font=("Arial", 18, "bold"))
# pen.hideturtle()
# turtle.mainloop()


import turtle
import numpy as np

# Khởi tạo Turtle
screen = turtle.Screen()
screen.bgcolor("black")  # Đặt màu nền
pen = turtle.Turtle()
pen.speed(0)  # Tốc độ vẽ nhanh nhất
pen.width(2)
pen.color("red")

# Tạo danh sách điểm theo phương trình trái tim
t = np.linspace(0, 2 * np.pi, 200)  # Chia nhỏ khoảng từ 0 đến 2π
x = 16 * np.sin(t) ** 3  # Tính giá trị x
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)  # Tính y

# Dịch trái tim về trung tâm màn hình
scale = 10  # Phóng to hình
x = x * scale
y = y * scale

# Di chuyển Turtle đến điểm đầu tiên
pen.penup()
pen.goto(x[0], y[0])
pen.pendown()

# Vẽ trái tim theo danh sách điểm
pen.begin_fill()
pen.fillcolor("red")
for i in range(len(x)):
    pen.goto(x[i], y[i])
pen.end_fill()


pen.hideturtle()

# Giữ cửa sổ không bị đóng ngay lập tức
turtle.done()
