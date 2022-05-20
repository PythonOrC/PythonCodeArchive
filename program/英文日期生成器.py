#英文日期生成器
months=[
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December']
    
endings=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']

year = input('year:')
month=input('mouth(1-12):')
day=input('day(1-31):')

month_number = int(month)
day_number=int(day)

month_name= months[month_number]
ordinal = day + endings[day_number]

print('英文日期表达为'+month_name+''+ordinal+','+year)