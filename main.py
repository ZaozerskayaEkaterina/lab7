import services

a = input('what do you want:  ')

if a == 'create':
    print(services.create_one(tbl=input('table: '), candidate={
        "name": "Студент Студент",
        "age": "тт",
        "contacts": {
            "email": "ssssssss@example.com",
            "phone": "+88899898998",
        "groups_id": [
                3
            ]
        }}))

if a == 'delete':
    print(services.delete_one_by_id(tbl=input('table: '), id=int(input('id: '))))

if a == 'upload':
    print(services.update_one_by_id(tbl=input('table: '), candidate={
        "name": "Новый Чел",
        "age": "99",
        "contacts": {
          "email": "newchellll@example.com",
          "phone": "+7777777777",
        "group_id": [
          1
        ]
        }}))

if a == 'get one':
    print(services.update_one_by_id(tbl=input('table: '), id=int(input('id: '))))

if a == 'get all':
    print(services.get_all(tbl=input('table: ')))

if a == 'new teacher':
    print(services.teacher2group(teacher_id=int(input('teacher id: ')), group_id=int(input('group id: '))))

if a == 'new student':
    print(services.student2group(student_id=int(input('student id: ')), group_id=int(input('group id: '))))

else:
    print('error of command')