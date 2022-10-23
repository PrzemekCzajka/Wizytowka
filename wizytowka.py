#Wizytówka
from faker import Faker
def create_contacts(type, amount):
    fake = Faker()
    if type == BaseContact:
        for i in range(amount):
            return(f"Osoba:",fake.name(),"Email:",fake.email(),"Telefon:",fake.phone_number())
    elif type == BusinessContact:
        for i in range(amount):
            return(f"Osoba:",fake.name(),"Email: ",fake.email(),"Telefon służbowy:",fake.phone_number(),"Firma:",fake.company(),"Stanowisko:",fake.job(),)
class Card:
    def __init__(self, name, surname, company, position, email):
        self.name = name
        self.surname = surname
        self.company = company
        self.position = position
        self.email = email
    def __str__(self):
        return f'{self.name} {self.surname} {self.company}'
    def __repr__(self):
        return f'{self.name} {self.surname} {self.company}'
    def contact(self):
        return f'Kontaktuję się z: {self.name} {self.surname} {self.company} {self.company}'
class BaseContact(Card):
    def __init__(self, phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.phone = phone
    def contact(self):
        return f'Wybieram numer: {self.phone} i dzwonię do: {self.name} {self.surname}'
    def label_length(self):
        return len({self.name} + {self.surname})
class BusinessContact(Card):
    def __init__(self, phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.phone = phone
    def contact(self):
        return f'Wybieram numer: {self.phone} i dzwonię do: {self.name} {self.surname}'
    def label_length(self):
        return len({self.name} + {self.surname})
card1 = Card(name="Przemek", surname="Czajka", company="Reganta", position="Printer",  email="przem@google.com")
#card2 = Card(name="Ela", surname="Czajka", company="Nordea", position="Process oficer", phone="333345672", email="ela@google.com")
card3 = Card(name="Basia", surname="Czajka", company="Szkoła", position="Uczeń", email="basia@google.com")
card4 = Card(name="Wojtek", surname="Czajka", company="Szkoła", position="Uczeń", email="wojo@google.com")
#card5 = Card(name="Tomek", surname="Kowalski", company="Maszyny", position="Lider", phone="333905771",email="tom@google.com")
#card6 = Card(name="Remek", surname="Iksiński", company="Mosty", position="Operator", phone="333665339",email="rem@google.com")
#card7 = Card(name="Lidka", surname="Wolska", company="Stars", position="Junior", phone="333549066",email="lid@google.com")
#card8 = Card(name="Wiola", surname="Czabańska", company="Ruby", position="Developer", phone="333773009",email="wiola@google.com")
#card9 = Card(name="Zbyszek", surname="Nowak", position="Senior", email="zbych@google.com")
#cards = [card1, card2, card3, card4, card5, card6, card7, card8]
#by_name = sorted(cards, key=lambda card: card.name)
#by_company = sorted(cards, key=lambda card: card.company)

#print(card1)
#print(by_age)
#print(by_name)
#print(by_company)
#print(BaseContact)
create_contacts(BusinessContact, 1)