# определим ф-ю-генератор all_variants, кот. прин. строку text
def all_variants(text):
    # опред-м длину строки
    n = len(text)
    # пройдем по всем возм. длинам подпослед-ей от 1 до n
    for length in range(1, n + 1):
        # пройдем по всем возм. нач. позициям подстроки для тек. длины
        for start in range(n - length + 1):
            # вычислим конеч. позицию для тек. подстроки
            end = start + length
            # возврат тек. подстроки с использованием оператора yield
            yield text[start:end]
# пример
a = all_variants("abc")
for i in a:
    print(i)