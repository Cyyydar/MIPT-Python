from city.family import Family
from city.city_list import CityList
import random
from city.person import Person

class CityFamilyList(CityList):

    def __init__(self, name: str, count: int):
        super(CityList, self).__init__(name, count)
        self.__family_list = []


    def add_family(self, f: Family) -> None:
        if super(CityList, self).add_person():
            self.add_person(f.father)
            self.add_person(f.mother)
            for c in f.children:
                self.add_person(c)
            self.__family_list.append(f)

    def remove_family(self, i: int) -> None:
        if super(CityList,self).remove_person():
            i = i % len(self.__family_list)
            f: Family = self.__family_list[i]
            self.remove_person(self.__person_list.index(f.father))
            self.remove_person(self.__person_list.index(f.mother))
            for p in f.children:
                self.remove_person(self.__person_list.index(p))
            del self.__family_list[i]

    def __str__(self) -> str:
        s1 = super(CityList, self).__str__()
        s = []
        s.append(s1)
        s.append("List of families \n")

        for (i,v) in enumerate(self.__family_list):
            s.append(" - {} - {} \n".format(i,v))

        return ''.join(s)

