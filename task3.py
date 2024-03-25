import timeit
from tabulate import tabulate

import algo


test_fn = {
    "Boyer-Moore Algorithm": algo.boyer_moore_search,
    "Knut-Morris-Pratt Algorithm": algo.kmp_search,
    "Rabin-Karp Algorithm": algo.rabin_karp_search,
}

fake_text = "The quick brown fox jumps over the lazy dog"
files = [
    ("\nFirst file", "Рішення: Жадібний алгоритм у цьому випадку", "./files/one.txt"),
    (
        "\nSecond file",
        "Крок 2. Для кожного агента випадковим чином генерується від 1 до n вподобань.",
        "./files/two.txt",
    ),
]


def benchmark(sub, file):
    pattern = []
    with open(file, "r") as f:
        text = f.read()

        for name, fn in test_fn.items():
            pattern.append([
                name,
                timeit.timeit(lambda: fn(text, sub), number=30),
                timeit.timeit(lambda: fn(text, fake_text), number=30),
            ])
    return pattern


if __name__ == "__main__":
    headers = ["Algorithm", "Real text", "Fake"]

    for title, sub, file in files:
        print(title)
        print(tabulate(benchmark(sub, file), headers, tablefmt="pipe"))
