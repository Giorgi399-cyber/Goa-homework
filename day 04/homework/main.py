#Debugging-არის კოდის გასწორება.

#ინტაქსური შეცდომები (Syntax Errors)
#ეს შეცდომები წარმოიქმნება მაშინ, როცა კოდი არ შეესაბამება ენის გრამატიკას.
# მაგალითი:
#python
#Copy
#Edit
#if True
#    print("Hello")
# აქ : აკლია if კონსტრუქციის ბოლოს.

#2. გამონაკლისები (Exceptions)
#ეს შეცდომები წარმოიქმნება პროგრამის შესრულებისას, ანუ როცა კოდი სინტაქსურად სწორია, მაგრამ შესრულებისას წარმოიქმნება პრობლემა.

# ყველაზე გავრცელებული გამონაკლისების (exceptions) ტიპები:
#შეცდომის ტიპი	ახსნა
#NameError	ცვლადი ან სახელი არ არის განსაზღვრული
#TypeError	ტიპებს შორის არასწორი ოპერაცია (მაგ. რიცხვის + სტრიქონი)
#ValueError	სწორი ტიპი, მაგრამ არასწორი მნიშვნელობა (მაგ. int("abc"))
#IndexError	სიის არარსებული ინდექსი
#KeyError	ლექსიკონში არარსებული გასაღები
#AttributeError	ობიექტს არ აქვს მოთხოვნილი ატრიბუტი
#ZeroDivisionError	რიცხვის გაყოფა ნულზე
#ImportError	მოდულის იმპორტის შეცდომა
#FileNotFoundError	ფაილის არ არსებობა

# გამონაკლისების დამუშავება (try/except)
#python
#Copy
#Edit
#try:
#    x = 5 / 0
#except ZeroDivisionError:
#    print("ნულზე გაყოფა არ შეიძლება")

name =("Giorgi")
print(name)


number=5
text="apples"
number = 5
text = " apples"
result = str(number) + text
print(result)







name = "liKa"
name2 = name + "4"
print(name2)



#name = "liKa"         # ვქმნით სტრიქონის ტიპის ცვლადს სახელად name და ვანიჭებთ მნიშვნელობას "liKa"
#name2 = name + "4"    # ვქმნით ახალ ცვლადს name2 და ვანიჭებთ name-ს მნიშვნელობას ("liKa") დამატებულს "4"-სთან
#print(name2)          # დაიბეჭდება name2-ს მნიშვნელობა — ანუ "liKa4"
