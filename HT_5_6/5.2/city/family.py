from city.person import Person

class Family:
    def __init__(self, father: Person, mother: Person, surname: str):
        self.father = father
        self.mother = mother
        self.surname = surname
        self.children = []

    def get_size(self):
        return 2 + len(self.children)

    def add_child(self, child_first_name):
        middle_name = self.self.father._name
        child = Person(_name = child_first_name, _surname = self.surname, _midname = middle_name)
        self.children.append(child)
        return child
    
    def __str__(self) -> str:
        str = ''
        for key,val in self.__dict__.items():
            str = str + '{} = {} \n'.format(key, val)
        return str

    def _generate_middle_name(self, fathers_name):
        return fathers_name