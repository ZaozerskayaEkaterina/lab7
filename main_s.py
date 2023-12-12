import services as student


print(student.create_one(student, {
      "name": "Студент Студент",
      "age": "тт",
      "contacts": {
          "email": "ssssssss@example.com",
          "phone": "+88899898998",
      "groups_id": [
          3
      ],
      }}))


#print(student.delete_one_by_id(4))

# print(student.get_all())

# print(student.get_one_by_id(2))

# print(student.update_one_by_id(5, {
#       "name": "Новый Чел",
#       "age": "99"
#       "contacts": {
#           "email": "newchellll@example.com",
#           "phone": "+7777777777"
#       "group_id": [
#           1
#       ],
#       }}))
