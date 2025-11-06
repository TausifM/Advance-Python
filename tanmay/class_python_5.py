#class
class Tanmay:
    def __init__(self, name, aadhar):
        self.name = name
        self.aadhar = aadhar

    def validation(self):
        if len(self.aadhar) ==12 and self.aadhar.is_digit():
            return f"aadhar is valid"
        else:
            return f"aadhar is invalid"
        
print(Tanmay("name",1234))
print(Tanmay.validation())
        