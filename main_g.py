import components.groups.service_g as group
import components.teachers.service_t as teacher
import components.students.service_s as student
import utils.json_service as json_service


db = json_service.get_database()
last_teacher_id = teacher.get_all()[-1]["id"]
last_group_id = group.get_all()[-1]["id"]
last_student_id = student.get_all()[-1]["id"]

print(teacher.add_one({
      "id": last_teacher_id + 1,
      "name": "Крутой Учитель",
      "groups_id": [ last_group_id + 1],
      "contacts": {
          "email": "yyyyyyyyy@example.com",
          "phone": "+333333333"
      }})),
print(student.add_one({
      "id": last_student_id + 1,
      "name": "Крутой Студент111",
      "age": 11,
      "contacts": {
          "email": "ssssssss@example.com",
          "phone": "+88899898998"},
      "group_id": last_group_id + 1
      })),
print(student.add_one({
      "id": last_student_id + 2,
      "name": "Крутой Студент222",
      "age": 22,
      "contacts": {
          "email": "ssssssss@example.com",
          "phone": "+88899898998"},
      "group_id": last_group_id + 1
      })),
print(group.add_one({
    "id": last_group_id + 1,
    "name": "SSS",
    "group_teacher_id": last_teacher_id,
    "students_id": [
        last_student_id + 1,
        last_student_id + 2]
    }))

# print(group.create_one({
#       "name": "B",
#       "group_teacher_id": 3,
#       "students_id": [
#             1,
#             2]
#       }))

#print(group.delete_one_by_id(3))

# print(group.get_all())

# print(group.get_one_by_id(2))


# print(group.update_one_by_id(2,{
#       "name": "Новая Z",
#       "group_teacher_id": 5,
#       "students_id": [
#         3]
#       }))
