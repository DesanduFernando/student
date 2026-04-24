if __name__ == "__main__":
    print("Welcome to Student Record Management System")

    try:
        with open("students.txt", "r") as f:
            list = []
            for line in f:
                list.append(eval(line))
    except:
        list = []

    while True:
        print("\n1. Add a student")
        print("2. View all students")
        print("3. Search for a student")
        print("4. Update student details")
        print("5. Delete a student")
        print("6. Save and Exit")

        initial_request = input("What do you want to do: ")

        if initial_request == "1":
            print("Enter student details")
            student_id = input("Enter ID: ")
            student_name = input("Enter Name: ")
            age = input("Enter Age: ")
            course = input("Enter Course: ")

            students = {
                "student_id": student_id,
                "student_name": student_name,
                "age": age,
                "course": course,
            }

            list.append(students)
            print("Student added:", students)

        elif initial_request == "2":
            print(list)

        elif initial_request == "3":
            search_id = input("Enter ID to search: ")

            for i in list:
                if i["student_id"] == search_id:
                    print("Student found:", i)
                    break
            else:
                print("Student not found")

        elif initial_request == "4":
            update_id = input("Enter ID to update: ")

            for i in list:
                if i["student_id"] == update_id:
                    name = input("Enter new name: ")
                    age = input("Enter new age: ")
                    course = input("Enter new course: ")

                    if name != "":
                        i["student_name"] = name
                    if age != "":
                        i["age"] = age
                    if course != "":
                        i["course"] = course

                    print("Updated:", i)
                    break
            else:
                print("Student not found")

        elif initial_request == "5":
            delete_id = input("Enter ID to delete: ")

            for i in list:
                if i["student_id"] == delete_id:
                    list.remove(i)
                    print("Student Deleted")
                    break
            else:
                print("Student not found")

        elif initial_request == "6":
            with open("students.txt", "w") as f:
                for i in list:
                    f.write(str(i) + "\n")
            print("Saved")        
            break

        else:
            print("Invalid request")
        