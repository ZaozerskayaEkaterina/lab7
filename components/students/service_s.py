import utils.json_service as json_service


def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["students"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["students"]


def update_one_by_id(id, student):
    db = json_service.get_database()

    for i, elem in enumerate(db["students"]):
        if elem["id"] == id:
            elem["name"] = student["name"]
            elem["age"] = student["age"]
            elem["contacts"] = student["contacts"]
            elem["group_id"] = student["group_id"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["students"]):
        if elem["id"] == id:
            candidate = db["students"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(student):  # создает новый id
    db = json_service.get_database()

    last_student_id = get_all()[-1]["id"]
    return add_one({"id": last_student_id + 1, **student})


def add_one(student):  # дабвляет нового студента по созданному выше id
    db = json_service.get_database()

    db["students"].append(student)

    json_service.set_database(db)
    return student
