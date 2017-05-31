from niceprinter import *

if __name__ == '__main__':
    print(title("Welcome To NICEPRINTER Demo", 90, '='))
    print()
    print(title('Boxes'))
    print(box("My nice box!"))
    print()
    print(box("My nice box modified!", '_', '*'))
    print()
    print(bbox("My nice bbox!"))
    print()
    print(cbox("My nice centered box!"))
    print()
    print(cbbox("My nice centered bbox"))
    users = [
        [ '#', underline(red('Name')), 'Email', yellow('Created At') ],
        [ '1', 'Aitor Riba', 'contact@aitorriba.com', purple('2017-05-18 08:54:46') ],
        [ '2', 'Giovanny Hudson', 'jermey56@example.net', purple('2017-05-22 18:32:48') ],
        [ '3', 'Dolores Mertz', 'lola67@example.net', purple('2017-05-22 20:22:35') ],
        [ '4', 'Earnestine Klein', 'koepp.nettie@example.com', purple('2017-05-22 21:42:43') ],
        [ '5', 'Valentina Altenwerth', 'zula86@example.com', purple('2017-05-23 10:53:15') ]
    ]
    print(title('Tables'))
    print(table(users, boldHead = False))
    print(title("Centered table"))
    print(table(users, centered=True))
    print(title("Custom table"))
    print(table(users, '‖', '*'))
    print(title("Colors"))
    print(red("My bussy text"))
    print(center(yellow(bold(underline("My bussy text")))))
    print()
    print(cbox(yellow(bold(underline("My bussy text"))), red("="), red("‖")))
    print(cbox(blue(bold(underline("My bussy text"))), purple("="), purple("‖")))
    print(cbox(red(bold(underline("My bussy text"))), cyan("="), cyan("‖")))
    print(title('Lists'))
    print(listing('Numbers', [1,2,4]))
    print(listing(red('Numbers'), [1,2,4], centered=True))
