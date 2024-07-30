students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
    'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}


def get_student_info():
    student = input("Entrez le nom de l'étudiant : ")
    if student in students:
        print(f"\nNotes de {student} : \n")
        grades = students[student]
        for subject, grade in grades.items():
            print(f"{subject} : {grade}")

        average = calculate_average(grades.values())
        print(f"\nMoyenne de {student} : {average}")

    else:
        print(f"\nL'étudiant {student} n'existe pas dans la liste.")


def calculate_average(grades):
    if not grades:
        print("Aucune note n'a été trouvée")
        return
    return sum(grades) / len(grades)


get_student_info()
