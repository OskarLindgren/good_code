def small_alpha(int:int) -> int:
    return int+26

# 26 + 26 = 52
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '!']

# H8 e5 l12 l12 o15 space-2 W23 o15 r18 l12 d4 !-1
large_to_print = [8, 23]
small_to_print = [5, 12, 12, 15, 15, 18, 12, 4]
special_chars = [-2, -1]
order = [0, 1, 1, 1, 1, 2, 0, 1, 1, 1, 1, 2]

small_count = 0
large_count = 0
special_count = 0
base_count = 0

while True:
    type = order[base_count]
    match type:
        case 0:
            print(alphabet[large_to_print[large_count]-1], end='')
            large_count += 1
        case 1:
            print(alphabet[small_alpha(small_to_print[small_count])-1], end='')
            small_count += 1
        case 2:
            print(alphabet[special_chars[special_count]], end='')
            special_count += 1
        case _:
            print("Error!")
    base_count += 1
    if base_count >= len(order):
        print()
        break