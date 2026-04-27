# Sakshi – Hotel Billing with Different Facilities
# Scenario
# Enhance the hotel system to support different facilities (e.g., RoomCharge, RestaurantBill, SpaCharge) and generate a unified bill.
# OOP‑Covered
# Interface, polymorphism, composition, encapsulation
# Instructions
# Create an interface BillItem with getAmount().
# Create classes:
# RoomCharge (implements BillItem), RestaurantBill, SpaCharge.
# Create HotelBill class that holds List<BillItem> and has getTotalBill().
# In main:
# Add mixed bill items to a HotelBill.
# Call getTotalBill() and demonstrate polymorphic calls to getAmount() underneath.

from abc import ABC,abstractmethod
class BillItem(ABC):
    @abstractmethod
    def getAmount(self):
        pass

class RoomCharge(BillItem):
    def __init__(self,pricepernight,no_of_nights):
        self.pricepernight=pricepernight
        self.no_of_nights=no_of_nights

    def getAmount(self):
        return self.pricepernight*self.no_of_nights

class  RestaurantBill(BillItem):
    def __init__(self,food_price):
        self.food_price=food_price

    def getAmount(self):
        return self.food_price
    
class SpaCharge(BillItem):
    def __init__(self,fee):
        self.fee=fee
    def getAmount(self):
        return self.fee
    
class HotelBill:
    def __init__(self):
        self.items=[]

    def add_items(self,item:BillItem):
        self.items.append(item)

    def total_bill(self):
        tot=0
        for item in self.items:
            tot+=item.getAmount()
        return tot
    
bill=HotelBill()
bill.add_items(RoomCharge(1450,1))
bill.add_items(RestaurantBill(2100))

bill.add_items(SpaCharge(800))
print(f"total bill {bill.total_bill()}")
