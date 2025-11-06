#class
class Tanmay:
    def __init__(self, name, aadhar):
        self.name = name
        self.aadhar = aadhar
        print(f"name: {self.name}, aadhar: {self.aadhar}")

    def validation(self):
        if len(str(self.aadhar)) == 12 and str(self.aadhar).isdigit():
            return f"aadhar is valid"
        else:
            return f"aadhar is invalid"
        
print(Tanmay("name",1234).validation()) 
# to solve below error we used str() function
# TypeError: object of type 'int' has no len()
print(Tanmay("tanmay", "123456789012").validation())
# Thats why we are passing aadhar as string
#print(Tanmay("tanmay", "12345678901").validation())
        