import utils.json_service as json_service


def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["teachers"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["teachers"]


def update_one_by_id(id, teacher):
    db = json_service.get_database()

    for i, elem in enumerate(db["teachers"]):
        if elem["id"] == id:

            elem["name"] = teacher["name"]
            elem["contacts"] = teacher["contacts"]
            elem["groups_id"] = teacher["groups_id"]
            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["teachers"]):
        if elem["id"] == id:

            candidate = db["teachers"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(teacher): #создает новый id
    db = json_service.get_database()

    last_teacher_id = get_all()[-1]["id"]
    return add_one({"id": last_teacher_id + 1, **teacher})


def add_one(teacher): #дабвляет нового учителя по созданному выше id
    db = json_service.get_database()

    db["teachers"].append(teacher)

    json_service.set_database(db)
    return teacher