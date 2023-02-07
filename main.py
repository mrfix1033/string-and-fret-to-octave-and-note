NOTES = ['ми', 'фа', 'фа#', 'соль', 'соль#', 'ля', 'ля#', 'си', "до", "до#", 'ре', 'ре#']
offset_for_prev = [0, 5, 4, 5, 5, 5]


def get(string, lad):
    return sum(offset_for_prev[string:]) + lad


while True:
    num_string = int(input("Введите номер струны: "))
    num_lad = int(input("Введите номер лада: "))
    note = get(num_string, num_lad)
    octave = (note + 4) // 12  # здесь октава используется только для обозначения перехода между октавами
    note %= 12
    print(f"Октава {octave}, нота {NOTES[note]}\n")
