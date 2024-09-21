from Address import Address
from Mailing import Mailing

to_address = Address("123456", "Москва", "Ленина", "15", "12")
from_address = Address("654321", "Санкт-Петербург", "Невский пр.", "7", "5")

mailing = Mailing(to_address, from_address, 300, "TRK123456")

print(mailing)
