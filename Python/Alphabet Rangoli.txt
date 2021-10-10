import string

def print_rangoli(size):
    alphabets = list(string.ascii_lowercase)
    width = 2*(2*size-1) -1
    list_ = alphabets[:size]
    list_.reverse()
    for i in range(size):
        front_text_list = list_[:i+1]
        back_text_list = list_[:i]
        back_text_list.reverse()
        text = ("-".join(front_text_list) + "-" + "-".join(back_text_list)).strip("-")
        rangoli = text.center(width, "-")
        print(rangoli)
    for i in range(size-1, 0, -1):
        front_text_list = list_[:i]
        back_text_list = list_[:i-1]
        back_text_list.reverse()
        text = ("-".join(front_text_list) + "-" + "-".join(back_text_list)).strip("-")
        rangoli = text.center(width, "-")
        print(rangoli)


###########################################################################################

import string

def print_rangoli(size):
    alphabets = string.ascii_lowercase
    width = 2*(2*size-1) -1
    reverse_heap = []
    for i in range(size):
        line_in_heap = ("-".join((alphabets[i:size])[::-1]) + "-" + "-".join((alphabets[i:size])[1:])).strip("-")
        reverse_heap.append(line_in_heap.center(width, "-"))
    rangoli = reverse_heap[::-1] + reverse_heap[1:]
    print("\n".join(rangoli))
