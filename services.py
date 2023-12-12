import json


def get_database():
    with open("db.json", encoding="utf-8") as db_file:
        return json.load(db_file)


def set_database(db):
    with open("db.json", "w", encoding="utf-8") as db_file:
        json.dump(db, db_file, ensure_ascii=False, indent=2)


def get_one_by_id(tbl, id):
    db = get_database()

    for elem in db[tbl]:
        if elem["id"] == id:
            return elem

    return {"message": f"Элемент {id} в таблице  {tbl} не найден"}


def get_all(tbl):
    db = get_database()

    return db[tbl]


def update_one_by_id(tbl, id, candidate):
    db = get_database()

    for i, elem in enumerate(db[tbl]):
        if elem["id"] == id:
            db[tbl].pop(i)
            db[tbl].append({"id": id, **candidate})

            set_database(db)
            return elem

    return {"message": f"Элемент {id} в таблице  {tbl} не найден"}


def delete_one_by_id(tbl, id):
    db = get_database()

    for i, elem in enumerate(db[tbl]):
        if elem["id"] == id:

            candidate = db[tbl].pop(i)
            if tbl == 'teachers':  # если удаляем учителя, то надо удалить его из всех групп
                for gr in db['groups']:
                    for k, tea in enumerate(gr['teachers_id']):
                        if tea == id:
                            gr['teachers_id'].pop(k)
                            break

            if tbl == 'students':  # если удаляем ученика, то надо удалить его из всех групп
                for gr in db['groups']:
                    for j, st in enumerate(gr['students_id']):
                        if st == id:
                            gr['students_id'].pop(j)
                            break

            set_database(db)

            return candidate

    return {"message": f"Элемент {id} в таблице  {tbl} не найден"}


def create_one(tbl, candidate):
    db = get_database()

    last_id = get_all(tbl)[-1]["id"]
    return add_one(tbl, {"id": last_id + 1, **candidate})


def add_one(tbl, candidate):
    db = get_database()

    db[tbl].append(candidate)

    set_database(db)
    return candidate


def teacher2group(teacher_id, group_id):
    db = get_database()

    for gr in db['groups']:
        if gr["id"] == group_id:
            for tea in gr['teachers_id']:
                if tea == teacher_id:
                    return {"message": f"Учитель {teacher_id} уже есть в группе {group_id}"}
            gr['teachers_id'].append(teacher_id)
            set_database(db)
            return gr

    return {"message": f"Группа {group_id} не найдена"}


def student2group(student_id, group_id):
    db = get_database()

    for gr in db['groups']:
        if gr["id"] == group_id:
            for st in gr['students_id']:
                if st == student_id:
                    return {"message": f"Студент {student_id} уже есть в группе {group_id}"}
            gr['students_id'].append(student_id)
            set_database(db)
            return gr

    return {"message": f"Группа {group_id} не найдена"}
