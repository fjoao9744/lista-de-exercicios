'''day = int(input(''))
month = int(input(''))
year = int(input(''))
'''
'''print('hoje é', day, '/', month, '/', year)'''

'''print('hoje é dia {} / {} / {}'.format(day, month, year))'''

'''print(f'hoje é dia {day} / {month} / {year}')'''

def date_convert(day, month, year):
    date = f'{day} / {month} / {year}'
    return date

print(f'hoje é dia {date_convert(input(), input(), input())}')

