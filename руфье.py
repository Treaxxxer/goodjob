import tkinter as tk
from tkinter import messagebox

class RuffierTestApp:
    def __init__(self, master):
        self.master = master
        master.title("Программа по определению состояния здоровья")

        self.welcome_message = tk.Label(master, text="Добро пожаловать в программу по определению состояния здоровья!\n\n"
                                                      "Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n\n"
                                                      "Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n"
                                                      "Измеряют пульс в положении сидя, затем спортсмен выполняет 30 глубоких приседаний в течение 30 с.\n"
                                                      "После этого подсчитывают пульс стоя, а затем — через минуту отдыха.\n\n"
                                                      "Индекс оценивается: < 0 — отлично, 1—5 — хорошо, 6—10 — удовлетворительно, 11—15 слабо, > 15 — неудовлетворительно.\n\n"
                                                      "Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.",
                                        justify="left")
        self.welcome_message.pack()

        self.start_button = tk.Button(master, text="Начать тест", command=self.start_test)
        self.start_button.pack()

    def start_test(self):
        self.master.destroy()  # Закрыть окно приветствия
        root = tk.Tk()
        app = RuffierTest(root)
        root.mainloop()

class RuffierTest:
    def __init__(self, master):
        self.master = master
        master.title("Тест Руфье")

        self.full_name_label = tk.Label(master, text="Введите Ф.И.О.:")
        self.full_name_label.pack()
        self.full_name_entry = tk.Entry(master)
        self.full_name_entry.pack()

        self.age_label = tk.Label(master, text="Полных лет:")
        self.age_label.pack()
        self.age_entry = tk.Entry(master)
        self.age_entry.pack()

        self.pulse1_label = tk.Label(master, text="Пульс в положении сидя:")
        self.pulse1_label.pack()
        self.pulse1_entry = tk.Entry(master)
        self.pulse1_entry.pack()

        self.start_squats_button = tk.Button(master, text="Начать приседания", command=self.start_squats)
        self.start_squats_button.pack()

        self.pulse2_label = tk.Label(master, text="Пульс после приседаний:")
        self.pulse2_label.pack()
        self.pulse2_entry = tk.Entry(master)
        self.pulse2_entry.pack()

        self.pulse3_label = tk.Label(master, text="Пульс через минуту после приседаний:")
        self.pulse3_label.pack()
        self.pulse3_entry = tk.Entry(master)
        self.pulse3_entry.pack()

        self.submit_button = tk.Button(master, text="Отправить результаты", command=self.submit_results)
        self.submit_button.pack()

    def start_squats(self):
        messagebox.showinfo("Инструкция", "Выполните 30 приседаний в течение 30 секунд.")
        self.start_timer()

    def start_timer(self):
        self.master.after(30000, self.measure_pulse2)

    def measure_pulse2(self):
        messagebox.showinfo("Инструкция", "Измерьте пульс после приседаний.")
        self.start_timer2()

    def start_timer2(self):
        self.master.after(60000, self.measure_pulse3)

    def measure_pulse3(self):
        messagebox.showinfo("Инструкция", "Измерьте пульс через минуту после приседаний.")

    def submit_results(self):
        full_name = self.full_name_entry.get()
        age = int(self.age_entry.get())
        pulse1 = int(self.pulse1_entry.get())
        pulse2 = int(self.pulse2_entry.get())
        pulse3 = int(self.pulse3_entry.get())

        ruffier_index = ((pulse1 + pulse2 + pulse3) - 200) / 10

        if ruffier_index < 0:
            interpretation = "Отлично"
        elif 0 <= ruffier_index <= 5:
            interpretation = "Хорошо"
        elif 6 <= ruffier_index <= 10:
            interpretation = "Удовлетворительно"
        elif 11 <= ruffier_index <= 15:
            interpretation = "Слабо"
        else:
            interpretation = "Неудовлетворительно"

        messagebox.showinfo("Результаты",
                            f"Ф.И.О.: {full_name}\nПолных лет: {age}\nПульс в положении сидя: {pulse1}\nПульс после приседаний: {pulse2}\nПульс через минуту после приседаний: {pulse3}\nИндекс Руфье: {ruffier_index}\nОценка: {interpretation}")

root = tk.Tk()
app = RuffierTestApp(root)
root.mainloop()