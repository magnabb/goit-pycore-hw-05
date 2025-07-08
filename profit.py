import re
def generator_numbers(text):
    reg = re.compile(r'(^|\s)([\d.?]+)(\s?|$)')
    for match in reg.finditer(text):
        yield float(match.group(0).strip())

def sum_profit(text, generator):
    return sum(generator(text))

if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
