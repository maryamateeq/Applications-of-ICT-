# Step 1: Take User Input
marks = int(input("Enter your marks"))
# Step 2: Assign grae using id/elif/else
grade = "a"
if marks>=90 and marks>=100:
 grade = "A"
elif marks>=75 and marks<90:
 grade = "B"
elif marks>=65 and marks<75:
 grade = "C"
elif marks>50 and marks<65:
 grade = "D"
elif marks<=50:
 grade = "F"
else:
 print("Invalid")
 # Step 3: Display Result
print("Grade:", grade)
                  
            