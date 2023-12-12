import components.autos.service_a as auto


print(auto.create_one({
      "name": "new lada",
      "number": "sd646s",
      "group_id": [1]
      }))


#print(auto.delete_one_by_id(3))

# print(auto.get_all())

# print(auto.get_one_by_id(1))

print(auto.update_one_by_id(2, {
      "name": "niva",
      "number": "nn444n",
      "group_id": [2]
      }))

