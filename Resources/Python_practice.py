counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver': 
    print(counties[1])
if counties[1] != 'Jefferson' :
    print(counties[2])

temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

#What is the score?
score = int(input("What is your test score? "))

#Determine the grade.
if score >= 90:
    print('you grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your score is a C.')
        else:
            if score >= 60:
                print('Your score is a D.')
            else:
                print('Your grade is an F.')

#What is the score?
score = int(input("What is your test score?"))

#Determine the grade.
if score >+ 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('your grade is a C.')
elif score >= 60:
    print('Your grade is a 60.')
else:
    print('Your grade is a F.')

counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.") 
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and ElPaso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:  
    print("Arapahoe and El Paso are not in the list of counties.")
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")    
for county in counties:
    print(county)
for i in range(len(counties)):
    print(counties[i])