
class UserProfileSerializer(object):
    def __init__(self,name,surname,phone,street,city,state,postal_code,country, created=None):
        self.name=name
        self.surname=surname
        self.phone=phone
        self.street=street
        self.city=city
        self.state=state
        self.postal_code=postal_code
        self.country=country

class CreditCardSerializer(object):
    def __init__(self,credit_card_number,cardholder_name,expration_date,cvv, created=None):
        self.credit_card_number = credit_card_number
        self.cardholder_name = cardholder_name
        self.expration_date =expration_date
        self.cvv =cvv