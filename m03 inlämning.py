
salary = int(input("Hur mycket tjänar du i månaden i kr?"))

#jag gör en input för variabeln salary och gör den till en intergear

StateTax= 0
CommunalTax = salary*0.2136
CouncilTax = salary*0.1148
SalaryNetto = salary - CommunalTax - CouncilTax
YearlySalary = 12*salary

#Ger värden till alla mina variabler

if YearlySalary < 19247:
    CommunalTax = 0
    CouncilTax = 0
    SalaryNetto = salary - CommunalTax - CouncilTax

if YearlySalary > 468700 and YearlySalary < 675700:
    StateTax = salary*0.2
    SalaryNetto = salary - CommunalTax - CouncilTax - StateTax
    print(f"Din Statligaskatt är {round(StateTax)} kr")

if YearlySalary > 675700:
    StateTax = salary*0.25
    SalaryNetto = salary - CommunalTax - CouncilTax - StateTax
    print(f"Din Statligaskatt är {round(StateTax)} kr")

#skriver argument som sker beroende på angiven lön
    
TotalTax = CommunalTax + CouncilTax + StateTax
TaxProcent = TotalTax/salary*100

#Den totala skatten räknas utifrån vilket argument som stämde in med den givna inputen

print(f"Din lön är {round(salary)} kr i månaden")
print(f"Din kommunalskatt är {round(CommunalTax)}  kr")
print(f"Din Landstingskatt är {round(CouncilTax)} kr")
print(f"Din nettolön är {round(SalaryNetto)} kr")
print(f"Din totala skatt är {round(TotalTax)} kr")
print(f"Din totala procent skatt är {round(TaxProcent,2)}%")

#printar alla beräkningar med hjälp av f-string samt avrundar de



