# Design a program that asks the user for their biological gender and hemoglobin level (g/L).
# Based on the provided values, the program should inform the user if their hemoglobin is low, normal, or
# high. The normal ranges are:
# For adult females:117-155 g/L.
# For adult males=134-167 g/L.


gender= input("Enter the biological gender male/ female: ").lower()
hemoglobin = float(input("Enter the hemoglobin level (g/l): "))


if gender == "female":
     if hemoglobin< 117:
         print("Your hemoglobin is low.")
     elif 117<= hemoglobin <= 155:
         print("Your hemoglobin is normal.")
     else:
         print("Your hemoglobin is high. ")

elif gender == "male":
     if hemoglobin< 134:
        print("Your hemoglobin is low.")
     elif 134<= hemoglobin <= 167:
        print("Your hemoglobin is normal.")
     else:
        print("Your hemoglobin is high. ")

