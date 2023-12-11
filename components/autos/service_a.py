import utils.json_service as json_service

def get_one_by_id(id):
    db = json_service.get_database()

    for elem in db["autos"]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент с {id} не найден"}


def get_all():
    db = json_service.get_database()

    return db["autos"]


def update_one_by_id(id, auto):
    db = json_service.get_database()

    for i, elem in enumerate(db["autos"]):
        if elem["id"] == id:

            elem["name"] = auto["name"]
            elem["number"] = auto["number"]
            elem["group_id"] = auto["group_id"]

            json_service.set_database(db)
            return elem

    return {"message": f"Элемент с {id} не найден"}


def delete_one_by_id(id):
    db = json_service.get_database()

    for i, elem in enumerate(db["autos"]):
        if elem["id"] == id:

            candidate = db["autos"].pop(i)
            json_service.set_database(db)

            return candidate

    return {"message": f"Элемент с {id} не найден"}


def create_one(auto):
    db = json_service.get_database()

    last_auto_id = get_all()[-1]["id"]
    db["autos"].append({"id": last_auto_id + 1, **auto})

    json_service.set_database(db)
