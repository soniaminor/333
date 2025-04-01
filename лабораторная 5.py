matpimport tkinter as tk
import numpy as np
import lotlib.pyplot as plt
from scipy.interpolate import lagrange

def plot_lagrange_interpolation():
    x_values = [float(x1_entry.get()), float(x2_entry.get()), float(x3_entry.get()), float(x4_entry.get())]
    y_values = [float(y1_entry.get()), float(y2_entry.get()), float(y3_entry.get()), float(y4_entry.get())]

    poly = lagrange(x_values, y_values)
    x_interp = np.linspace(min(x_values), max(x_values), 1000)
    y_interp = poly(x_interp)

    plt.figure()
    plt.plot(x_interp, y_interp, label='Интерполяция')
    plt.scatter(x_values, y_values, color='red', label='Заданные точки')
    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Интерполяционный полином Лагранжа')
    plt.grid(True)
    plt.show()

# Создание графического интерфейса с использованием tkinter
root = tk.Tk()
root.title("Интерполяция Лагранжа")

root.configure(bg = '#5C2D91')

# Создание и размещение виджетов
label_points = tk.Label(root, text="Введите координаты точек (x1,y1), (x2,y2), (x3,y3), (x4,y4):")
label_points.pack()

x1_label = tk.Label(root, text="x1:") 
x1_label.pack()
x1_entry = tk.Entry(root)
x1_entry.insert(0, "1.0")  # Значение по умолчанию
x1_entry.pack()
y1_label = tk.Label(root, text="y1:") 
y1_label.pack()
y1_entry = tk.Entry(root)
y1_entry.insert(0, "2.0")  # Значение по умолчанию
y1_entry.pack()


x2_label = tk.Label(root, text="x2:") 
x2_label.pack()
x2_entry = tk.Entry(root)
x2_entry.insert(0, "3.0")  # Значение по умолчанию
x2_entry.pack()
y2_label = tk.Label(root, text="y2:") 
y2_label.pack()
y2_entry = tk.Entry(root)
y2_entry.insert(0, "4.0")  # Значение по умолчанию
y2_entry.pack()


x3_label = tk.Label(root, text="x3:") 
x3_label.pack()
x3_entry = tk.Entry(root)
x3_entry.insert(0, "5.0")  # Значение по умолчанию
x3_entry.pack()
y3_label = tk.Label(root, text="y3:") 
y3_label.pack()
y3_entry = tk.Entry(root)
y3_entry.insert(0, "6.0")  # Значение по умолчанию
y3_entry.pack()


x4_label = tk.Label(root, text="x4:") 
x4_label.pack()
x4_entry = tk.Entry(root)
x4_entry.insert(0, "7.0")  # Значение по умолчанию
x4_entry.pack()
y4_label = tk.Label(root, text="y4:") 
y4_label.pack()
y4_entry = tk.Entry(root)
y4_entry.insert(0, "8.0")  # Значение по умолчанию
y4_entry.pack()


plot_button = tk.Button(root, text="Интерполяция графика", command=plot_lagrange_interpolation)
plot_button.pack()

root.mainloop()