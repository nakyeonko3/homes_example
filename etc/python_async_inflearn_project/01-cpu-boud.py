import sys

sys.set_int_max_str_digits(0)


def cpu_boud_func(number: int):
    total = 1
    arrange = range(1, number + 1)
    for i in arrange:
        for j in arrange:
            for k in arrange:
                total *= i * j * k
    return total


if __name__ == "__main__":
    result = cpu_boud_func(30)
    print(int(result))
