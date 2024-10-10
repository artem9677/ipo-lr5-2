string_1 = str(input("Введите первую строку: "))
string_2 = str(input("Введите вторую строку: "))

if string_1 == string_2:
    print("Строки не являются анаграммами.")
    quit()

elif len(string_1)!=len(string_2):
    print("Строки не являются анаграммами.")
    quit()

is_anagr = 0

for i in string_1:
    for j in string_2:
        if i == j:
            is_anagr+=1
            break

if is_anagr == len(string_1):
    print("Строки являются анаграммами.")
else:
    print("Строки не явлются анаграммами.")