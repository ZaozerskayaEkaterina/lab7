import utils.json_service as json_service

def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["groups"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["groups"]


def update_one_by_id(id, group):
    db = json_service.get_database()

    for i, elem in enumerate(db["groups"]):
        if elem["id"] == id:

            elem["name"] = group["name"]
            elem["group_teacher_id"] = group["group_teacher_id"]
            elem["students_id"] = group["students_id"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["groups"]):
        if elem["id"] == id:

            candidate = db["groups"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(group): #создает новый id
    db = json_service.get_database()

    last_group_id = get_all()[-1]["id"]
    return add_one({"id": last_group_id + 1, **group})


def add_one(group): #дабвляет новую группу по созданному выше id
    db = json_service.get_database()

    db["groups"].append(group)

    json_service.set_database(db)
    return student
