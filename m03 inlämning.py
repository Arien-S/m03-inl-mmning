
salary = int(input("Hur mycket tjänar du i månaden i kr?"))
StateTax= 0
CommunalTax = salary*0.2136
CouncilTax = salary*0.1148
SalaryNetto = salary - CommunalTax - CouncilTax
TotalTax = CommunalTax + CouncilTax + StateTax
TaxProcent = TotalTax/salary*100

YearlySalary = 12*salary

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
    
    
    

print(f"Din lön är {round(salary)} kr i månaden")
print(f"Din kommunalskatt är {round(CommunalTax)}  kr")
print(f"Din Landstingskatt är {round(CouncilTax)} kr")
print(f"Din nettolön är {round(SalaryNetto)} kr")
print(f"Din totala skatt är {round(TotalTax)} kr")
print(f"Din totala procent skatt är {round(TaxProcent,2)}%")



