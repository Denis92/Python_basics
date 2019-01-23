import re

str_in = """    Заменить           
группы пробелов одиночными,         крайние пробелы удалить. 
"""


def format_str(input_str):
    input_str = input_str.lower()
    template = r'(\s{2,}|\n)'
    input_str = re.sub(template, " ", input_str)
    list_srt = input_str.split(" ")
    return (" ".join(list_srt[1:-1]).capitalize())


print(format_str(str_in))
