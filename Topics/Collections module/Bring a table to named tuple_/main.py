from collections import namedtuple

person_template = namedtuple('Student', ['name', 'age', 'department'])

people = (person_template('Alina', '22', 'linguistics'),
          person_template('Alex', '25', 'programming'),
          person_template('Kate', '19', 'art'))

print(*people, sep='\n')
