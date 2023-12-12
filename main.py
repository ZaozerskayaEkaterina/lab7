import components.teachers.service_t as teacher


print(teacher.create_one({
      "name": "Учитель Учитель",
      "groups_id": [
          1,
          2
      ],
      "contacts": {
          "email": "yyyyyyyyy@example.com",
          "phone": "+333333333"
      }}))


#print(teacher.delete_one_by_id(4))

# print(teacher.get_all())

# print(teacher.get_one_by_id(1))

# print(teacher.update_one_by_id(4, {
#       "name": "Новый Учитель",
#       "contacts": {
#           "email": "нет@example.com",
#           "phone": "+1111111111"
#       }}))

