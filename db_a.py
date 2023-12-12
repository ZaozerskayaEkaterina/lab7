db = {
  "auto_school_name": "АвтоШкола №1",
  "address": "ул. Дорожная, 45",
  "students": [
    {
      "id": 1,
      "name": "Попов Арсений",
      "age": 30,
      "contacts":
        {
          "email": "popov@example.com",
          "phone": "+1234567890"
        },
      "group_id": 1
    },
    {
      "id": 2,
      "name": "Шавухич Антон",
      "age": 20,
      "contacts":
        {
          "email": "hasnuts@example.com",
          "phone": "+0987654321"
        },
      "group_id": 2
    },
    {
      "id": 3,
      "name": "Мартов Сергей",
      "age": 21,
      "contacts":
        {
          "email": "sergey@example.com",
          "phone": "+8664565466"
       },
      "group_id": 1
    },
    {
      "id": 4,
      "name": "Петров Дмитрий",
      "age": 28,
      "contacts":
        {
            "email": "petpet@example.com",
            "phone": "+5678901234"
        },
      "group_id": 2
    }
  ],
  "groups": [
    {
      "id": 1,
      "name": "A",
      "group_teacher_id": [
        1
      ],
      "students_id": [
        1,
        3
      ]
    },
    {
      "id": 2,
      "name": "B",
      "group_teacher_id": [
        2
      ],
      "students_id": [
        2,
        4
      ]
    }
  ],
  "teachers": [
    {
      "id": 1,
      "name": "Смирнова Екатерина",
      "groups_id": [
        1,
        2
      ],
      "contacts": {
        "email": "smirnova@example.com",
        "phone": "+1122334455"
      }
    },
    {
      "id": 2,
      "name": "Иванова Ольга",
      "groups_id": [
        3
      ],
      "contacts": {
        "email": "ivanova@example.com",
        "phone": "+9988776655"
      }
    },
    {
      "id": 3,
      "name": "Петров Иван",
      "groups_id": [
        1
      ],
      "contacts": {
        "email": "petrov@example.com",
        "phone": "+3344556677"
      }
    }
  ],
  "autos": [
    {
      "id": 1,
      "name": "mercedes",
      "number": "bb666b",
      "group_id": [
        1
      ]
    },
    {
      "id": 2,
      "name": "lada",
      "number": "aa123a",
      "group_id": [
        2
      ]
    }
  ]
}