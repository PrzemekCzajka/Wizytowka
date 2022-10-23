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
        return f'Kontaktuję się z: {self.name} {self.surname} {self.company}'
class BaseContact(Card):
    def __init__(self, name, surname, phone, email):
        super().__init__(name, surname, email)
        self.phone = phone
    def contact(self):
        return f'Wybieram numer: {self.phone} i dzwonię do: {self.name} {self.surname}'
    def label_length(self):
        return len(self.name) + len(self.surname)
class BusinessContact(Card):
    def __init__(self, name, surname, company, position, phone, email, corp_phone,*args, **kwargs):
        super().__init__(name, surname, company, position, email)
        self.phone = phone
        self.corp_phone = corp_phone
    def contact(self):
        return f'Wybieram numer: {self.corp_phone} i dzwonię do: {self.name} {self.surname}'
    def label_length(self):
        return len(self.name) + len(self.surname)
card1 = BusinessContact(name="Przemek", surname="Czajka", company="Reganta", position="Printer", phone="333905771", email="przem@google.com", corp_phone="555311221")
card2 = BusinessContact(name="Ela", surname="Czajka", company="Nordea", position="Process oficer", phone="333345672", email="ela@google.com", corp_phone="555311221")
#card3 = BaseContact(name="Basia", surname="Czajka", phone="333905771", email="basia@google.com")
#card4 = BaseContact(name="Wojtek", surname="Czajka", phone="333905771", email="wojo@google.com",)
card5 = BusinessContact(name="Tomek", surname="Kowalski", company="Maszyny", position="Lider", phone="333905771",email="tom@google.com", corp_phone="555311221")
card6 = BusinessContact(name="Remek", surname="Iksiński", company="Mosty", position="Operator", phone="333665339",email="rem@google.com", corp_phone="555311221")
card7 = BusinessContact(name="Lidka", surname="Wolska", company="Stars", position="Junior", phone="333549066",email="lid@google.com", corp_phone="555311221")
card8 = BusinessContact(name="Wiola", surname="Czabańska", company="Ruby", position="Developer", phone="333773009",email="wiola@google.com", corp_phone="555311221")
#card9 = BaseContact(name="Zbyszek", surname="Nowak", phone="333905771", email="zbych@google.com")
#cards = [card1, card2, card3, card4, card5, card6, card7, card8]
#by_name = sorted(cards, key=lambda card: card.name)
#by_company = sorted(cards, key=lambda card: card.company)

print(card1.label_length())
#print(by_age)
#print(by_name)
#print(by_company)
#print(BaseContact)

#create_contacts(BusinessContact, 1)