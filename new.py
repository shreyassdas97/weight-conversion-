pound_to_kg=0.45
kg_to_pound=2.20
x=float(input("what is your weight? "))
unit=input("is it in 'p'ounds or 'k'ilograms ").lower()
if unit == 'p':
    a= pound_to_kg * (x)
    print(a)
elif unit == 'k':
    b=x *kg_to_pound
    print(b )
if x < 100 :
    print("normal weight")
else :
    print("decrease your weight " )
