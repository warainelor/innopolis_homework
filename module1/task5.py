def is_cat(word):
    return word in ["Кот", "КОТ", "кот"]


text = input("Введите строку: ")

cat_amount = 0
word = ""
for ch in text:
    if ch == ' ':
        if is_cat(word):
            cat_amount += 1
        word = ""
    else:
        word += ch

print(f"Количество котов: {cat_amount}")
