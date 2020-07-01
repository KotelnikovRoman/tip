from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title("Чаевые")
# Англия 10-15%
# Франция 15%
# Италия, Испания, Португалия 5-10%
# Греция 10%
# Чехия 10-15%
# Германия, Австрия 5-10%
# Нидерланды, Швейцария 3-5
country_all = [
    # 0
    "Англия",
    # 1
    "Франция",
    # 2
    "Италия",
    # 3
    "Германия",
    # 4
    "Греция",
    # 5
    "Германия",
    # 6
    "Испания",
    # 7
    "Нидерланды",
    # 8
    "Португалия",
    # 9
    "Чехия",
    # 10
    "Австрия"
]

place_all = [
    # 0
    "кафе",
    # 1
    "ресторан",
    # 2
    "доставка",
    # 3
    "пабы и бары",
    # 4
    "отель",
    # 5
    "спа-услуги",
    # 6
    "такси",
    # 7
    "гиды и экскурсоводы",
    # 8
    "театры и кинотеатры"
]

percent = 0
min_percent = 0
max_percent = 0


def clicked():
    if country.get() == country_all[0]:
        if place.get() == place_all[0]:
            res = "Можно оставить 1-2 фунта (необязательно)"
        elif place.get() == place_all[1]:
            res = "В недорогих 1-2 фунта (необязательно)\n В более дорогих 10-15% чаевых"
        elif place.get() == place_all[2]:
            res = ""
        elif place.get() == place_all[3]:
            res = "Принято угощать бармена, оставляя сумму на напиток"
        elif place.get() == place_all[4]:
            res = "Считается вежливым тоном оставлять горничным 10-20 фунтов за неделю"
        elif place.get() == place_all[5]:
            res = "2 фунта"
        elif place.get() == place_all[6]:
            res = "10% от поездки если водитель был вежлив, помог с богажём"
        elif place.get() == place_all[7]:
            res = "10% от экскурсии"
        else:
            res = "Неизвестно"
    elif country.get() == country_all[1]:
        if place.get() == place_all[0]:
            res = "В некоторых туристических городах принято давать щедрые чаевые"
        elif place.get() == place_all[1]:
            res = "Не смотря на то что 15% от заказа уже включены в счёт\n"
            res += "Хорошим тоном считается оставлять 1-2 евро\n"
            res += "1 евро принято оставлять гардеробщику за каждый предмет\n"
            res += "Шфейцару и сотруднику театра проводившего вас к месту, пологается 1 евро"
        elif place.get() == place_all[2]:
            res = "Неизвестно"
        elif place.get() == place_all[3]:
            res = "Неизвестно"
        elif place.get() == place_all[4]:
            res = "Неизвестно"
        elif place.get() == place_all[5]:
            res = "Неизвестно"
        elif place.get() == place_all[6]:
            res = "Неизвестно"
        elif place.get() == place_all[7]:
            res = "Неизвестно"
        else:
            res = "Неизвестно"
    elif country.get() == country_all[2]:
        if place.get() == place_all[0]:
            res = "включены в чек 5-10% от суммы"
        elif place.get() == place_all[1]:
            res = "включены в чек 5-10% от суммы"
        elif place.get() == place_all[2]:
            res = "неизвестно"
        elif place.get() == place_all[3]:
            res = "неизвестно"
        elif place.get() == place_all[4]:
            res = "неизвестно"
        elif place.get() == place_all[5]:
            res = "Горничным 1-2 евро, в 5и звездочных отелях 5 евро\n"
            res = "Носильщику 1-2 евро за единицу богажа"
        elif place.get() == place_all[6]:
            res = "неизвестно"
        elif place.get() == place_all[7]:
            res = "неизвестно"
        elif place.get() == place_all[8]:
            res = "Сопровождающему в театре или кинозале от 0.5 до 1 евро"
        else:
            res = "Неизвестно"
    elif country.get() == country_all[3]:
        if place.get() == place_all[0]:
            res = "5-10%"
        elif place.get() == place_all[1]:
            res = "5-10%"
        elif place.get() == place_all[2]:
            res = "неизвестно"
        elif place.get() == place_all[3]:
            res = "неизвестно"
        elif place.get() == place_all[4]:
            res = "неизвестно"
        elif place.get() == place_all[5]:
            res = "неизвестно"
        elif place.get() == place_all[6]:
            res = "неизвестно"
        elif place.get() == place_all[7]:
            res = "неизвестно"
        else:
            res = "Неизвестно"
    elif country.get() == country_all[4]:
        if place.get() == place_all[0]:
            res = "10% от суммы"
        elif place.get() == place_all[1]:
            res = "10% в обычных\n"
            res += "в более дорогих 15%"
        elif place.get() == place_all[2]:
            res = "неизвестно"
        elif place.get() == place_all[3]:
            res = "неизвестно"
        elif place.get() == place_all[4]:
            res = "горничные, носильщики будут рады 1-2 евро"
        elif place.get() == place_all[5]:
            res = "неизвестно"
        elif place.get() == place_all[6]:
            res = "5-10% от поездки"
        elif place.get() == place_all[7]:
            res = "неизвестно"
        else:
            res = "Неизвестно"
    elif country.get() == country_all[5]:
        if place.get() == place_all[0]:
            res = "неизвестно"
        elif place.get() == place_all[1]:
            res = "неизвестно"
        elif place.get() == place_all[2]:
            res = "неизвестно"
        elif place.get() == place_all[3]:
            res = "неизвестно"
        elif place.get() == place_all[4]:
            res = "неизвестно"
        elif place.get() == place_all[5]:
            res = "неизвестно"
        elif place.get() == place_all[6]:
            res = "неизвестно"
        elif place.get() == place_all[7]:
            res = "неизвестно"
        else:
            res = "Неизвестно"
    elif country.get() == country_all[6]:
        if place.get() == place_all[0]:
            res = "включены в чек 5-10% от суммы"
        elif place.get() == place_all[1]:
            res = "включены в чек 5-10% от суммы"
        elif place.get() == place_all[2]:
            res = "неизвестно"
        elif place.get() == place_all[3]:
            res = "неизвестно"
        elif place.get() == place_all[4]:
            res = "неизвестно"
        elif place.get() == place_all[5]:
            res = "Горничным 1-2 евро, в 5и звездочных отелях 5 евро\n"
            res = "Носильщику 1-2 евро за единицу богажа"
        elif place.get() == place_all[6]:
            res = "неизвестно"
        elif place.get() == place_all[7]:
            res = "неизвестно"
        elif place.get() == place_all[8]:
            res = "Сопровождающему в театре или кинозале от 0.5 до 1 евро"
        else:
            res = "Неизвестно"
    elif country.get() == country_all[7]:
        if place.get() == place_all[0]:
            res = "3-5%"
        elif place.get() == place_all[1]:
            res = "3-5%"
        elif place.get() == place_all[2]:
            res = "неизвестно"
        elif place.get() == place_all[3]:
            res = "неизвестно"
        elif place.get() == place_all[4]:
            res = "неизвестно"
        elif place.get() == place_all[5]:
            res = "неизвестно"
        elif place.get() == place_all[6]:
            res = "неизвестно"
        elif place.get() == place_all[7]:
            res = "неизвестно"
        else:
            res = "Неизвестно"
    elif country.get() == country_all[8]:
        if place.get() == place_all[0]:
            res = "включены в чек 5-10% от суммы"
        elif place.get() == place_all[1]:
            res = "включены в чек 5-10% от суммы"
        elif place.get() == place_all[2]:
            res = "неизвестно"
        elif place.get() == place_all[3]:
            res = "неизвестно"
        elif place.get() == place_all[4]:
            res = "неизвестно"
        elif place.get() == place_all[5]:
            res = "Горничным 1-2 евро, в 5и звездочных отелях 5 евро\n"
            res = "Носильщику 1-2 евро за единицу богажа"
        elif place.get() == place_all[6]:
            res = "неизвестно"
        elif place.get() == place_all[7]:
            res = "неизвестно"
        elif place.get() == place_all[8]:
            res = "Сопровождающему в театре или кинозале от 0.5 до 1 евро"
        else:
            res = "Неизвестно"
    elif country.get() == country_all[9]:
        if place.get() == place_all[0]:
            res = "10-15%"
        elif place.get() == place_all[1]:
            res = "10-15%"
        elif place.get() == place_all[2]:
            res = "неизвестно"
        elif place.get() == place_all[3]:
            res = "неизвестно"
        elif place.get() == place_all[4]:
            res = "неизвестно"
        elif place.get() == place_all[5]:
            res = "неизвестно"
        elif place.get() == place_all[6]:
            res = "неизвестно"
        elif place.get() == place_all[7]:
            res = "неизвестно"
        else:
            res = "Неизвестно"
    elif country.get() == country_all[10]:
        if place.get() == place_all[0]:
            res = "5-10%"
        elif place.get() == place_all[1]:
            res = "5-10%"
        elif place.get() == place_all[2]:
            res = "неизвестно"
        elif place.get() == place_all[3]:
            res = "неизвестно"
        elif place.get() == place_all[4]:
            res = "неизвестно"
        elif place.get() == place_all[5]:
            res = "неизвестно"
        elif place.get() == place_all[6]:
            res = "неизвестно"
        elif place.get() == place_all[7]:
            res = "неизвестно"
        else:
            res = "Неизвестно"
        res += '\nПопрасили счёт 3-и недождались?. Можете уходить'
    tip.configure(text=res)


    # список стран
country_title = Label(window, text="Выбрать страну")
country_title.grid(column=0, row=0)

country = Combobox(window)
country['values'] = (country_all)
country.current(0)
country.grid(column=1, row=0)

# список мест
place_title = Label(window, text="Место")
place_title.grid(column=0, row=1)

place = Combobox(window)
place['values'] = (place_all)
place.current(0)
place.grid(column=1, row=1)

# кнопка
btn = Button(window, text="Проверить", command=clicked)
btn.grid(column=0, row=2)

# показать ответ
tip = Label(window, text="")
tip.grid(column=0, row=3)
window.geometry('500x300')
window.mainloop()
