import services
while True:
    a = input('what do you want (create/delete/update/get one/get all/add teacher in group/'
              'add student in group/create group) :  ')

    if a == 'create':
        tbl = input('in which table (students/teachers/autos/groups) :  ')
        if tbl == 'students':
            print(services.create_one(tbl, candidate={
                "name": "Студент Студент",
                "age": "17",
                "groups_id": 2,
                "contacts": {
                    "email": "ssssssss@example.com",
                    "phone": "+88899898998"
                }}))
        elif tbl == 'teachers':
            print(services.create_one(tbl, candidate={
                "name": "Учитель Учитель",
                "groups_id": 2,
                "contacts": {
                    "email": "yyyyyyyyy@example.com",
                    "phone": "+333333333"
                }}))
        elif tbl == 'autos':
            print(services.create_one(tbl, candidate={
                "name": "BatMobile",
                "number": "xy111z",
                "group_id": [1]
                }))
        elif tbl == 'groups':
            print(services.create_one(tbl, candidate={
                "name": "B",
                "group_teacher_id": [3],
                "students_id": [
                        1,
                        2]
                }))

    elif a == 'create group':
        db = services.get_database()
        last_teacher_id = services.get_all('teachers')[-1]["id"]
        last_group_id = services.get_all('groups')[-1]["id"]
        last_student_id = services.get_all('students')[-1]["id"]

        print(services.add_one(tbl='teachers', candidate={
            "id": last_teacher_id + 1,
            "name": "Крутой Учитель",
            "groups_id": last_group_id + 1,
            "contacts": {
                "email": "yyyyyyyyy@example.com",
                "phone": "+333333333"
            }})),
        print(services.add_one(tbl='students', candidate={
            "id": last_student_id + 1,
            "name": "Крутой Студент111",
            "age": 11,
            "groups_id": last_group_id + 1,
            "contacts": {
                "email": "ssssssss@example.com",
                "phone": "+88899898998"}
        })),
        print(services.add_one(tbl='students', candidate={
            "id": last_student_id + 2,
            "name": "Крутой Студент222",
            "groups_id": last_group_id + 1,
            "age": 22,
            "contacts": {
                "email": "ssssssss@example.com",
                "phone": "+88899898998"}
        })),
        print(services.add_one(tbl='groups', candidate={
            "id": last_group_id + 1,
            "name": "SSS",
            "group_teacher_id": [last_teacher_id],
            "students_id": [
                last_student_id + 1,
                last_student_id + 2]
        }))

    elif a == 'delete':
        print(services.delete_one_by_id(tbl=input('table (students/teachers/autos/groups) : '), id=int(input('id: '))))

    elif a == 'update':
        tbl = input('in which table (students/teachers/autos/groups) :  ')
        if tbl == 'students':
            print(services.update_one_by_id(tbl, id=int(input('id: ')), candidate={
                "name": "Обновленный Студент",
                "age": "99",
                "groups_id": 2,
                "contacts": {
                    "email": "newchellll@example.com",
                    "phone": "+7777777777"
                }}))
        elif tbl == 'teachers':
            print(services.update_one_by_id(tbl, id=int(input('id: ')), candidate={
                "name": "Обновленный Учитель",
                "groups_id": 2,
                "contacts": {
                    "email": "yyyyyyyyy@example.com",
                    "phone": "+333333333"
                }}))
        elif tbl == 'autos':
            print(services.update_one_by_id(tbl, id=int(input('id: ')), candidate={
                "name": "new lada",
                "number": "sd646s",
                "group_id": [1]
            }))
        elif tbl == 'groups':
            print(services.update_one_by_id(tbl, id=int(input('id: ')), candidate={
                "name": "B",
                "group_teacher_id": [3],
                "students_id": [
                    1,
                    2]
            }))

    elif a == 'get one':
        print(services.get_one_by_id(tbl=input('table (students/teachers/autos/groups) : '), id=int(input('id: '))))

    elif a == 'get all':
        print(services.get_all(tbl=input('table (students/teachers/autos/groups) : ')))

    elif a == 'add teacher in group':
        print(services.teacher2group(teacher_id=int(input('teacher id: ')), group_id=int(input('group id: '))))

    elif a == 'add student in group':
        print(services.student2group(student_id=int(input('student id: ')), group_id=int(input('group id: '))))

    else:
        print('error of command')