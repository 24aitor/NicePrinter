# coding=utf-8

import os

class Color:
    underline = '\033[4m'
    darkcyan  = '\033[36m'
    purple    = '\033[95m'
    yellow    = '\033[93m'
    green     = '\033[92m'
    cyan      = '\033[96m'
    blue      = '\033[94m'
    bold      = '\033[1m'
    red       = '\033[91m'
    end       = '\033[0m'

def underline(string):
    return Color.underline + string + Color.end

def darkcyan(string):
    return Color.darkcyan + string + Color.end

def purple(string):
    return Color.purple + string + Color.end

def yellow(string):
    return Color.yellow + string + Color.end

def green(string):
    return Color.green + string + Color.end

def cyan(string):
    return Color.cyan + string + Color.end

def blue(string):
    return Color.blue + string + Color.end

def bold(string):
    return Color.bold + string + Color.end

def red(string):
    return Color.red + string + Color.end

def colorsChars(string):
    counter = 0
    chars = 0

    while (counter < len(string)) and (counter != -1):
        counter = string.find('\033', counter)
        if counter != -1:
            chars += len(string[counter:string.find('m', counter)]) + 1
            counter += 1

    return chars

def center(string):
    overflow = colorsChars(string)
    return string.center(os.get_terminal_size().columns + (overflow))

def hr(percentage = 75, sym = '-'):
    cols = (percentage/100) * os.get_terminal_size().columns
    return center(sym * int(cols))

def box(string, hsym = '-', vsym = '|'):
    line = (len(string) + 4 - colorsChars(string)) * hsym
    return line + '\n' + vsym + ' ' + string + ' ' + vsym + '\n' + line

def bbox(string):
    return box(string, '=', '‖')

def cbox(string, hsym = '-', vsym = '|'):
    line = center((len(string) + 4 - colorsChars(string)) * hsym)
    return line + '\n' + center(vsym + ' ' + string + ' ' + vsym) + '\n' + line

def cbbox(string):
    return cbox(string, '=', '‖')

def title(string, percentage = 75, sym = '-'):
        return '\n' + hr(percentage, sym) + '\n' + center(string) + '\n' + hr(percentage, sym) + '\n'

def listing(head, array, vsym = '|', hsym = '=', centered = False, boldHead = True):
    array.insert(0, head)
    size = 0
    export = ''
    array2 = []
    [array2.append(str(val)) for ind, val in enumerate(array)]
    array = array2

    for index, value in enumerate(array):
        if ((len(value) - colorsChars(value)) > size):
            size = len(value) - colorsChars(value)

    bar = (hsym * (size + 4))

    export += center(bar) if (centered) else (bar)

    var =  vsym
    for index, value in enumerate(array):
        var = (vsym + ' ') if (centered) else ("\n" + vsym + ' ')
        val = bold(value) if (index == 0 and boldHead) else value
        var += (val + (' ' * (size - len(value) + colorsChars(value) )) + (' ' + vsym))


        export += center(var) if (centered) else (var)

        if ((index == 0)):
            export += '\n'
            export += center(bar) if (centered) else (bar)

    export += '\n'
    export += center(bar) if (centered) else (bar)

    return export


def table(array, vsym = '|', hsym = '=', centered = False, boldHead = True):
    sizes = []
    export = ''

    [sizes.append(0) for x in array[0]]

    for subarray in array:
        for index, value in enumerate(subarray):
            if ((len(value) - colorsChars(value)) > sizes[index]):
                sizes[index] = len(value) - colorsChars(value)

    bar = (hsym * (sum(sizes) + len(sizes)*3 + 1))

    for subindex, subarray in enumerate(array):
        if subindex == 0:
            export += center(bar) if (centered) else (bar)

        export += ('\n')
        var = vsym + ' '
        for index, value in enumerate(subarray):
            val = bold(value) if (subindex == 0 and boldHead) else value
            var += (val + (' ' * (sizes[index] - len(value) + colorsChars(value) )) + (' ' + vsym + ' '))

        var = var.strip()
        export += center(var) if (centered) else (var)

        if ((subindex == 0)):
            export += '\n'
            export += center(bar) if (centered) else (bar)

    export += '\n'
    export += center(bar) if (centered) else (bar)

    return export
