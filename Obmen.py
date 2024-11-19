from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests

def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    currency_label.config(text=name)

def update_currency_label_1(event):
    code = base_combobox_2.get()
    name = currencies[code]
    currency_label_1.config(text=name)

def update_currency_label_2(event):
    code = base_combobox_1.get()
    name = currencies[code]
    currency_label_2.config(text=name)


def exchange():
    target_code = target_combobox.get()
    base_code_1 = base_combobox_1.get()
    base_code_2 = base_combobox_2.get()


    if target_code and base_code_1 and base_code_2:
        try:
            response_1 = requests.get(f'https://open.er-api.com/v6/latest/{base_code_1}')
            response_1.raise_for_status()
            data_1 = response_1.json()
            response_2 = requests.get(f'https://open.er-api.com/v6/latest/{base_code_2}')
            response_2.raise_for_status()

            data_2 = response_2.json()
            rates_1 = data_1['rates']
            rates_2 = data_2['rates']


            if target_code in rates_1 and target_code in rates_2:
                exchange_rate_1 = rates_1[target_code]
                exchange_rate_2 = rates_2[target_code]
                base_1 = currencies[base_code_1]
                base_2 = currencies[base_code_2]
                target = currencies[target_code]
                mb.showinfo("Курс обмена", f"Курс {exchange_rate_1:.2f} {target} за 1 {base_1}\nКурс {exchange_rate_2:.2f} {target} за 1 {base_2}")
            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Ошибка: {e}")
    else:
        mb.showwarning("Внимание", "Выберите коды валют")

# Словарь кодов валют и их полных названий
currencies = {
    "USD": "Американский доллар",
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум"
}

# Создание графического интерфейса
window = Tk()
window.title("Курс обмена валюты")
window.geometry("360x350")

Label(text="Базовая валюта:").pack(padx=10, pady=5)
base_combobox_1 = ttk.Combobox(values=list(currencies.keys()))
base_combobox_1.pack(padx=10, pady=5)
base_combobox_1.bind("<<ComboboxSelected>>", update_currency_label_2)

currency_label_2 = ttk.Label()
currency_label_2.pack(padx=10, pady=10)

Label(text="Вторая базовая валюта:").pack(padx=10, pady=5)
base_combobox_2 = ttk.Combobox(values=list(currencies.keys()))
base_combobox_2.pack(padx=10, pady=5)
base_combobox_2.bind("<<ComboboxSelected>>", update_currency_label_1)

currency_label_1 = ttk.Label()
currency_label_1.pack(padx=10, pady=10)

Label(text="Целевая валюта:").pack(padx=10, pady=5)
target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=5)
target_combobox.bind("<<ComboboxSelected>>", update_currency_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)


Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()

