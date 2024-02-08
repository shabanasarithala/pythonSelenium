# same method name with different parameters - method overloading
#


class Bank:
    def RateOfInterest(self):
        return 0


class IciciBank(Bank):
    def RateOfInterest(self):
        return 8


class HdfcBank(Bank):
    def RateOfInterest(self):
        return 9


obj_icici = IciciBank()
obj_hdfc = HdfcBank()

print(obj_icici.RateOfInterest())
print(obj_hdfc.RateOfInterest())
