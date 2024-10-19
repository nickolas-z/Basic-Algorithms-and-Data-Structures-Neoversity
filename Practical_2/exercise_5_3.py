import timeit
import time
import re

# start = time.time()
# ### Code here
# print(time.time() - start)

#
# Імплементацію алгоритмів взято з матеріалів, куди рекомендую заглянути за хорошим поясненням роботи самих алгоритмів
# Алгоритми повертають перший знайдений індекст шуканого підрядку в тексті

def polynomial_hash(s, base=256, modulus=101):
    """
    Повертає поліноміальний хеш рядка s.
    """
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(main_string, substring):
    # Довжини основного рядка та підрядка пошуку
    substring_length = len(substring)
    main_string_length = len(main_string)

    # Базове число для хешування та модуль
    base = 256
    modulus = 101

    # Хеш-значення для підрядка пошуку та поточного відрізка в основному рядку
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    # Попереднє значення для перерахунку хешу
    h_multiplier = pow(base, substring_length - 1) % modulus

    # Проходимо крізь основний рядок
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i + substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


def build_shift_table(pattern):
    """Створити таблицю зсувів для алгоритму Боєра-Мура."""
    table = {}
    length = len(pattern)
    # Для кожного символу в підрядку встановлюємо зсув рівний довжині підрядка
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    # Якщо символу немає в таблиці, зсув буде дорівнювати довжині підрядка
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            return i  # Підрядок знайдено, повертаємо перший знайдений індекс

        # Зсув індексу i
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return -1


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1  # якщо підрядок не знайдено

#
# Імплементацію алгоритмів взято з матеріалів, куди рекомендую заглянути за хорошим поясненням роботи самих алгоритмів
# 


def regex_search(main_string, pattern):
    match = re.search(pattern, main_string)
    if match:
        return match.start()
    else:
        return -1


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def measure_time(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=100)

if __name__ == "__main__":
    text1 = read_file('article_1.txt')
    text2 = read_file('article_2.txt')

    patterns = {
        "existing": "алгоритм",
        "non_existing": "вимишленийпідрядок"
    }

    results = []

    for pattern_type, pattern in patterns.items():
        for i, text in enumerate([text1, text2], 1):
            bm_time = measure_time(boyer_moore_search, text, pattern)
            kmp_time = measure_time(kmp_search, text, pattern)
            rk_time = measure_time(rabin_karp_search, text, pattern)

            results.append((f"Article {i} - {pattern_type}", bm_time, kmp_time, rk_time))

    for result in results:
        article, bm_time, kmp_time, rk_time = result
        print(f"{article}: Boyer-Moore = {bm_time:.6f}s, KMP = {kmp_time:.6f}s, Rabin-Karp = {rk_time:.6f}s")