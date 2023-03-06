import module


year_level = ['First Year', 'Second Year', 'Third Year', 'Fourth Year']
per_unit = 1000

ge_courses = [
    {'EnviSci': 3, 'Algebra': 3}, {'Cal2': 3, 'Linear': 3, 'Physics1': 3},
    {'PolSci1': 3, 'Anthro1': 3, 'Psych1': 3}, {'Acctg1': 3, 'Rizal': 3}]

professional_courses = [
    {'Eng1': 3, 'Fil 1': 3, 'PE1': 3}, {'Eng3': 3, 'Fil3': 3, 'PE3': 3},
    {'Writing1': 3, 'DataSci1': 3}, {'Writing3': 3, 'DataSci3': 3}]

core_courses = [
    {'CC1': 3, 'CC2': 3}, {'CC4': 3, 'CC5': 3},
    {'CC6': 3, 'CC10': 3, 'Thesis1': 3}, {'Elect1': 3, 'Elect2': 3, 'Thesis2': 3}]

miscellaneous_and_devt_fee = [2000, 2500, 3000, 3500]


def login():
    username = input('Enter Username : ')
    password = input('Enter Password : ')
    admin_username = 'PSUAdmin'
    admin_password = 'Systematic08'
    while True:
        if username == admin_username and password == admin_password:
            return
        print('Login Failed')


def dictionary_subjects(year):
    year -= 1
    return {
        'Year Level': year_level[year], 'GE Courses': ge_courses[year],
        'Professional Courses': professional_courses[year],
        'Core Courses': core_courses[year], 'Misc and Devt Fee': miscellaneous_and_devt_fee[year]}


master_dictionary = {
    'dictionary1': dictionary_subjects(1), 'dictionary2': dictionary_subjects(2),
    'dictionary3': dictionary_subjects(3), 'dictionary4': dictionary_subjects(4)
}

login()
print('\n')

dict__ = {'Surname': str, 'First Name': str, 'Middle Initial': str, 'Course': str, 'Year': int}

student_dictionary = (lambda a, b, c: {x[0]: (
    lambda x, y: y(b(x, b)) if y == str else c(c, x, y, b))(x[0], x[1]) for (x) in a.items()}
             )(dict__, lambda x, s: (lambda i_: i_ if i_ != '' else s(x, s))(input(f'Enter {x} : ').strip()),
               lambda s, x, y, b: (lambda b_: y(b_) if b_.isdigit() else s(s, x, y, b))(b(x, b)), )

print('\n')
# print(dictionary1)
# print(dictionary2)
# print(dictionary3)
# print(dictionary4)
year_level2_ = student_dictionary['Year']
master_access = f'dictionary{year_level2_}'
units = module.compute(master_dictionary[master_access])
number_of_subjects = module.number_subjects(master_dictionary[master_access])
misc_fee = master_dictionary[master_access]['Misc and Devt Fee']
# print(number_of_subjects)
# print(units)
# print(misc_fee)


def payment_mode1():
    global units
    global number_of_subjects
    global misc_fee
    return ((units * per_unit) * (1 - 0.05)) + misc_fee


def payment_mode2():
    global units
    global number_of_subjects
    global misc_fee
    return ((units * per_unit) * (1 - 0.03)) + misc_fee


def payment_mode3():
    global units
    global number_of_subjects
    global misc_fee
    return ((units * per_unit) * 1) + misc_fee


def tuition_total():
    while True:

        try:
            mode_payment = int(input('1 : Full Payment , 2 : Two Installments , 3 : Partial Payment     |     '))
            if mode_payment == 1:
                return payment_mode1()
            if mode_payment == 2:
                return payment_mode2()
            if mode_payment == 3:
                return payment_mode3()
        except ValueError:
            print('Invalid Input')


tuition = tuition_total()

print('\n')
module.display_subs(master_dictionary[master_access])
surname = student_dictionary['Surname']
firstname = student_dictionary['First Name']
mid_name = student_dictionary['Middle Initial']
course = student_dictionary['Course']
year__1 = student_dictionary['Year']

print(f'{surname}, {firstname} {mid_name}. | Course : {course} | Year : {year__1} | Tuition : {tuition}')

print(student_dictionary)
