#AIM: WAP to find students appearing for entrance exams
# Coder:Shamal 
# Date:13/02/26

print("--- Entrance Exam Students ---")
cet_students = {"Alice", "Bob", "Charlie", "Frank"}
jee_students = {"Eve", "Frank", "Bob", "Heidi"}
neet_students = {"Bob", "Charlie", "Karl", "Liam"}

print(f"List of Students:")
print(f"CET Students: {cet_students}")
print(f"JEE Students: {jee_students}")
print(f"NEET Students: {neet_students}")

# Write your code here
# TODO: Find and Print All the Students appearing for any Entrance Exam
all_students = cet_students.union(jee_students).union(neet_students)
print(f"All Students appearing for any Entrance Exam: {all_students}")

# TODO: Find and Print Students appearing for All Entrance Exams
all_exams = cet_students & jee_students & neet_students
print(f"Students appearing for All Entrance Exams: {all_exams}")

# TODO: Find and Print Students appearing for JEE but not for NEET
jee_not_neet = jee_students - neet_students
print(f"JEE but not for NEET: {jee_not_neet}")

# TODO: Find and Print Students appearing for CET and NEET but not for JEE
cet_neet_not_jee = (cet_students & neet_students) - jee_students
print(f"CET and NEET but not for JEE: {cet_neet_not_jee}")









