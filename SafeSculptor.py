#Author
#Illyrian






import itertools
import os

banner = '''
  @@@@@@  @@@@@@  @@@@@@@@ @@@@@@@@  @@@@@@  @@@@@@@ @@@  @@@ @@@      @@@@@@@  @@@@@@@  @@@@@@  @@@@@@@ 
 !@@     @@!  @@@ @@!      @@!      !@@     !@@      @@!  @@@ @@!      @@!  @@@   @@!   @@!  @@@ @@!  @@@
  !@@!!  @!@!@!@! @!!!:!   @!!!:!    !@@!!  !@!      @!@  !@! @!!      @!@@!@!    @!!   @!@  !@! @!@!!@! 
     !:! !!:  !!! !!:      !!:          !:! :!!      !!:  !!! !!:      !!:        !!:   !!:  !!! !!: :!! 
 ::.: :   :   : :  :       : :: ::: ::.: :   :: :: :  :.:: :  : ::.: :  :          :     : :. :   :   : :

Answer the questions to get the passwords generated.



'''

print(banner)

name = input(">Name ")
surname = input(">surname? ")
middlename = input(">middle name? ")
day = input(">day of birth? ")
month = input(">month of birth? ")
year = input(">year of birth? ")
pets = input(">pet name? ")
kids = input(">kids' name? ")
team = input(">favorite team? ")
dob_kids_day = input(">day of birth of kids? ")
dob_kids_month = input(">the month of birth of kids? ")
dob_kids_year = input(">the year of birth of kids? ")


def generate_password_lists(name, surname, middlename, day, month, year, pets, kids, team, dob_kids_day, dob_kids_month, dob_kids_year):
    password_lists = []

    
    basic_components = [name, surname, middlename, day, month, year , pets, kids, team, dob_kids_day, dob_kids_month, dob_kids_year]

    
    separator_combinations = [
        name + dob_kids_day,
        name + dob_kids_month,
        name + dob_kids_year,
        surname + dob_kids_day,
        surname + dob_kids_month,
        surname + dob_kids_year,
        name + day,
        name + month,
        name + year,
        surname + day,
        surname + month,
        surname + year,
        name + pets,
        surname + pets,
        team + dob_kids_day,
        name + surname + day,
        name + pets + year,
        name + surname + month,
        name + surname + year,
        name + surname + pets,
    ]

    
    date_month_year_combinations = [
        name + day,
        surname + month,
        year + name,
        year + surname,
        pets + day,
        team + dob_kids_month,
    ]

    
    pattern_combinations = [
        name + '123',
        surname + '123',
        year + name,
        year + surname,
        pets + '123',
        team + year,
    ]

    
    unique_combinations = set(itertools.chain(basic_components, separator_combinations, date_month_year_combinations, pattern_combinations))
    password_lists.extend(unique_combinations)

    return password_lists


passwords = generate_password_lists(name, surname, middlename, day, month, year , pets, kids, team, dob_kids_day, dob_kids_month, dob_kids_year)

for i in range(1, 101):
    modified_name = f"{name}{i}"
    modified_surname = f"{surname}{i}"
    modified_passwords = generate_password_lists(modified_name, modified_surname, middlename, day, month, year, pets, kids, team, dob_kids_day, dob_kids_month, dob_kids_year)
    passwords.extend(modified_passwords)

output_file_path = "generated_passwords.txt"
counter = 1
while os.path.exists(output_file_path):
    output_file_path = f"generated_passwords{counter}.txt"
    counter += 1

with open(output_file_path, "w") as output_file:
    output_file.write("\nGenerated Passwords:\n")
    for password in passwords:
        output_file.write(password + "\n")

print(f"\nGenerated passwords have been written to: {output_file_path}")