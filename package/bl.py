from .dal import *


user_file_path = r"file/user.txt"
course_file_path = r"file/course.txt"
student_file_path = r"file/student.txt"
assign_course_file_path = r"file/assign.txt"


# region Dict 2 Str
def convert_dict_2_str(data: list[list]) -> list[str]:
    return list(map(lambda item: f"{item}\n", data))
# endregion Dict 2 Str


# region Str 2 Dict
def convert_str_2_dict(data: list[str]) -> list[dict]:
    return list(map(lambda item: eval(item.strip()), data))
# endregion Str 2 Dict


# region Sign Up User
def register_user_bl(fullname, email, username, password):
    
    # region Error List
    err_message = []

    if not fullname.strip():
        err_message.append("Fullname is empty!")

    if not password.strip():
        err_message.append("password is empty!")
    
    if not email.strip():
        err_message.append("Email is empty!")
        
    if not username.strip():
        err_message.append("Username is empty!")
        
    if err_message:
        return ("ERROR", "\n".join(err_message))
    # endregion Error List
    
    # region Read
    status, output = read_dal(file_path=user_file_path)

    if status == "ERROR":
        return ("ERROR", "File Error!!!")

    elif status == "SUCCESS":
        user_list = convert_str_2_dict(output)

        for user in user_list:
            if user["email"] == email:
                err_message.append("Email "f"{email} duplicate!!!")
                
            if user["username"] == username:
                err_message.append("Username " f"{username} duplicate!!!")
                

    if err_message:
        return ("ERROR", "\n".join(err_message))

    user = {
        "fullname":fullname,
        "email":email,
        "username":username,
        "password":password
    }
    # endregion Read

    # region Save
    status, output = save_dal(file_path=user_file_path, content=f"{user}\n")

    if status == "SUCCESS":
        return ("SUCCESS", "Sucess Save.")
    elif status == "ERROR":
        return ("ERROR", "Error Save!")
    # endregion Save

# endregion Sign Up User


# region Login User
def login_user_bl(username, password):
    
    # region Error List
    err_message = []

    if not password.strip():
        err_message.append("password is empty!")
        
    if not username.strip():
        err_message.append("Username is empty!")

    if err_message:
        return ("ERROR", "\n".join(err_message))
    # endregion Error List
    
    # region Read
    status, output = read_dal(file_path=user_file_path)

    if status == "ERROR":
        return ("ERROR", "Error Login")

    elif status == "SUCCESS":
        user_list = convert_str_2_dict(output)

        for user in user_list:
            if user["username"] == username and  user["password"] == password:
                return ("SUCCESS", "Sucess Login")
            
        else:
            return ("ERROR", "Username " f"{username} does not exists")
    # endregion Read

# endregion Login User


# region Get Student
def get_student_bl(username):

    status, output = read_dal(file_path=student_file_path)

    if status == "ERROR":
        return ("ERROR", "Error Get Student")

    elif status == "SUCCESS":
        student_list = convert_str_2_dict(output)
        student_list = list(filter(lambda student: student.get('owner') == username, student_list))

        return ("SUCCESS", student_list)
# endregion Get Student


# region Add Student
def add_student_bl(name, family, gender, birthDay, nationalCode, studentId, username):

    # region Error List
    err_message = []

    if not name.strip():
        err_message.append("Name is empty!")

    if not family.strip():
        err_message.append("Family is empty!")

    if not gender.strip():
        err_message.append("Gender is empty!")

    if gender not in ("male", "female", "non binary"):
        err_message.append("Gender ist valid!")

    if not birthDay.strip():
        err_message.append("Birth Day is empty!")

    if not nationalCode.strip():
        err_message.append("National Code is empty!")

    if not studentId.strip():
        err_message.append("Student ID is empty!")

    if err_message:
        return ("ERROR", "\n".join(err_message))
    # endregion Error List

    # region Read
    status, output = read_dal(file_path=student_file_path)

    if status == "ERROR":
        return ("ERROR", "Error Add!")

    elif status == "SUCCESS":
        student_list = convert_str_2_dict(output)

        for student in student_list:
            if student["nationalCode"] == nationalCode and student["owner"] == username:
                return ("ERROR", "Nationalcode " f"{nationalCode} duplicate!")

            if student["studentId"] == studentId and student["owner"] == username:
                return ("ERROR", "Student ID " f"{studentId} duplicate!")

    student = {
        "name": name,
        "family": family,
        "gender": gender,
        "birthDay": birthDay,
        "nationalCode": nationalCode,
        "studentId": studentId,
        "owner": username
    }
    # endregion Read

    # region Save
    status, output = save_dal(
        file_path=student_file_path,
        content=f"{student}\n"
    )

    if status == "SUCCESS":
        return ("SUCCESS", "Sucess Save.")

    elif status == "ERROR":
        return ("ERROR", "Error Save!")
    # endregion Save

# endregion Add Student


# region Edit Student
def edit_student_bl(old_name, old_family, old_gender, old_birthDay, old_nationalCode, old_studentId, name, family, gender, birthDay, nationalCode, studentId, username):

    # region Erro List
    err_message = []

    if not name.strip():
        err_message.append("Name is empty!")

    if not family.strip():
        err_message.append("Family is empty!")

    if not gender.strip():
        err_message.append("Gender is empty!")

    if gender not in ("male", "female", "non binary"):
        err_message.append("Gender is not valid!")

    if not birthDay.strip():
        err_message.append("Birth Day is empty!")

    if not nationalCode.strip():
        err_message.append("National Code is empty!")

    if not studentId.strip():
        err_message.append("Student ID is empty!")

    if err_message:
        return ("ERROR", "\n".join(err_message))
    # endregion Erro List

    # region Read
    status, output = read_dal(file_path=student_file_path)

    if status == "ERROR":
        return ("ERROR", "Error Edit!")

    elif status == "SUCCESS":
        student_list = convert_str_2_dict(output)

        for student in student_list:

            if student["nationalCode"] == nationalCode and student["owner"] == username:
                return ("ERROR", "Nationalcode " f"{nationalCode} duplicate!")

            if student["studentId"] == studentId and student["owner"] == username:
                return ("ERROR", "Student ID " f"{studentId} duplicate!")

        select_student = {
            "name": old_name,
            "family": old_family,
            "gender": old_gender,
            "birthDay": old_birthDay,
            "nationalCode": old_nationalCode,
            "studentId": old_studentId,
            "owner": username,
        }

        select_index = student_list.index(select_student)
        student = student_list[select_index]
        
        student["name"] = name
        student["family"] = family
        student["nationalCode"] = nationalCode
        student["gender"] = gender
        student["birthDay"] = birthDay
        student["studentId"] = studentId

        student_list = convert_dict_2_str(student_list)
    # endregion Read

    # region Save
    status, output = save_dal(

        file_path=student_file_path,
        content=student_list,
        mode="w",
        write_state="wl"
    )

    if status == "SUCCESS":
        return ("SUCCESS", "Success Save.")

    elif status == "ERROR":
        return ("ERROR", "Error Save!")
    # endregion Save

# endregion Edit Student


# region Remove Student
def remove_student_bl(remove_list):

    status, output = read_dal(file_path=student_file_path)

    if status == "ERROR":
        return ("ERROR", "Error Remove Student")

    elif status == "SUCCESS":
        student_list = convert_str_2_dict(output)

        for remove_item in remove_list:
            student = {
                "name": remove_item[0],
                "family": remove_item[1],
                "gender": remove_item[2],
                "birthDay": remove_item[3],
                "nationalCode": remove_item[4],
                "studentId": remove_item[5],
                "owner": remove_item[6],
            }
            student_list.remove(student)

        student_list = convert_dict_2_str(student_list)

        # region Save
        status, output = save_dal(
            file_path=student_file_path,
            content=student_list,
            mode="w",
            write_state="wl"
        )

        if status == "SUCCESS":
            return ("SUCCESS", "Sucess Save.")

        elif status == "ERROR":
            return ("ERROR", "Error Save!")
        # endregion Save

# endregion Remove Student


# region Get Course
def get_course_bl(username):

    status, output = read_dal(file_path=course_file_path)

    if status == "ERROR":
        return ("ERROR", "Error Get Course!")

    elif status == "SUCCESS":

        course_list = convert_str_2_dict(output)
        course_list = list(filter(lambda course: course.get('owner') == username, course_list))

        return ("SUCCESS", course_list)
# endregion Get Course


# region Remove Course
def remove_course_bl(remove_list):
    status, output = read_dal(file_path=course_file_path)

    if status == "ERROR":
        return ("ERROR", "Error Remove Course!")

    elif status == "SUCCESS":
        course_list = convert_str_2_dict(output)

        for remove_item in remove_list:

            course = {
                "title": remove_item[0],
                "courseCode": remove_item[1],
                "price": remove_item[2],
                "owner": remove_item[3]
            }
            course_list.remove(course)

        course_list = convert_dict_2_str(course_list)

        # region Save
        status, output = save_dal(
            file_path=course_file_path,
            content=course_list,
            mode="w",
            write_state="wl"
        )

        if status == "SUCCESS":
            return ("SUCCESS", "Sucess Save.")

        elif status == "ERROR":
            return ("ERROR", "Error Save!")
        # endregion Save

# endregion Remove Course


# region Add Course
def add_course_bl(title, courseCode, price, username):

    # region Error List
    err_message = []

    if not title.strip():
        err_message.append("Title is empty!")

    if not courseCode.strip():
        err_message.append("Course Code is empty!")

    if not price.strip():
        err_message.append("Price is empty!")

    if err_message:
        return ("ERROR", "\n".join(err_message))
    # endregion Error List

    # region Read
    status, output = read_dal(file_path=course_file_path)

    if status == "ERROR":
        return ("ERROR", "Error Add Course!")

    elif status == "SUCCESS":
        course_list = convert_str_2_dict(output)

        for course in course_list:
            if course["title"] == title and course["owner"] == username:
                return ("ERROR", "Title " f"{title} duplicate!!!")

            if course["courseCode"] == courseCode and course["owner"] == username:
                return ("ERROR", "Course Code " f"{courseCode} duplicate!!!")

    course = {
        "title": title,
        "courseCode": courseCode,
        "price": price,
        "owner": username,
    }
    # endregion Read

    # region Save
    status, output = save_dal(
        file_path=course_file_path,
        content=f"{course}\n"
    )

    if status == "SUCCESS":
        return ("SUCCESS", "Sucess Save.")

    elif status == "ERROR":
        return ("ERROR", "Error Save!")
    # endregion Save

# endregion Add Course


# region Edit Course
def edit_course_bl(old_title, old_courseCode, old_price, title, courseCode, price, username):

    # region Error List
    err_message = []

    if not title.strip():
        err_message.append("Title is empty!")

    if not courseCode.strip():
        err_message.append("Course Code is empty!")

    if not price.strip():
        err_message.append("price is empty!")

    if err_message:
        return ("ERROR", "\n".join(err_message))
    # endregion Error List

    # region Read
    status, output = read_dal(file_path=course_file_path)

    if status == "ERROR":
        return ("ERROR", "Error Edit Course!")

    elif status == "SUCCESS":
        course_list = convert_str_2_dict(output)

        for course in course_list:
            if course["title"] == title and course["owner"] == username:
                return ("ERROR", f"{title} duplicate!!!")

            if course["courseCode"] == courseCode and course["owner"] == username:
                return ("ERROR", f"{courseCode} duplicate!!!")

        select_course = {
            "title": old_title,
            "courseCode": old_courseCode,
            "price": old_price,
            "owner": username,
        }

        select_index = course_list.index(select_course)

        course = course_list[select_index]
        course["title"] = title
        course["courseCode"] = courseCode

        course_list = convert_dict_2_str(course_list)
    # endregion Read

    # region Read
    status, output = save_dal(
        file_path=course_file_path,
        content=course_list,
        mode="w",
        write_state="wl"
    )

    if status == "SUCCESS":
        return ("SUCCESS", "Sucess Save.")

    elif status == "ERROR":
        return ("ERROR", "Error Save!")
    # endregion Read

# endregion Edit Course


# region Assign Course
def get_assign_course_bl(username):

    status, output = read_dal(file_path=assign_course_file_path)
    
    if status == "ERROR":
        return ("ERROR", "Errro Assign Course!")

    elif status == "SUCCESS":
        assign_course_list = convert_str_2_dict(output)
        assign_course_list = list(filter(lambda item: item.get('owner') == username, assign_course_list))

        return ("SUCCESS", assign_course_list)
# endregion Assign Course


#region Add Student Course
def add_student_course_bl(select_student, course, username):

    status, output = read_dal(file_path=assign_course_file_path)

    if status == "ERROR":
        return ("ERROR", "Error Add Course!")

    elif status == "SUCCESS":
        assign_course_list = convert_str_2_dict(output)
    
        for item in assign_course_list:

            if item["studentId"] == select_student[3] and item["courseCode"] == course[1] and item["owner"] == username:
                return ("ERROR", "This Student has taken this course already")
        
    assign_course = {
        "name":select_student[0],
        "family":select_student[1],
        "nationalCode":select_student[2],
        "studentId":select_student[3],
        "course_title":course[0],
        "courseCode":course[1],
        "owner":username,
    }

    #region Save
    status, output = save_dal(
        file_path=assign_course_file_path, 
        content=f"{assign_course}\n"
    )

    if status == "SUCCESS":
        return ("SUCCESS", "Sucess Save.")

    elif status == "ERROR":
        return ("ERROR", "Error Save!")
    #endregion Save

#endregion Add Student Course

