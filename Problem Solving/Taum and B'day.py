def taumBday(b, w, bc, wc, z):
    if bc+z <= wc:
        wc = bc+z
    if wc+z <= bc:
        bc = wc+z
    total = b*bc + w*wc
    return total