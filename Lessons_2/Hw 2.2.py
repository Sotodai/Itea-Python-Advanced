# 2. Давайте представим, что мы занимаемся проектированием CRM для сервисного центра по обслуживанию и ремонту техники.
# Реализуйте класс Заявка. Каждая заявка должна иметь следующие поля: уникальный идентификатор (присваивается в момент)
# создания заявки автоматически, дата и время создания заявки (автоматически), имя пользователя, серийный номер
# оборудования, статус (активная заявка или закрытая например, статусов может быть больше). Id заявки сделать приватным
# полем.
# У заявки должны быть следующие методы:
# - метод, возвращающий, сколько заявка находится в активном статусе (если она в нём)
# - метод, изменяющий статус заявки
# - метод, возвращающий id заявки
import uuid
from datetime import datetime
class Request:

    def __init__(self, name, serial_number, status='active'):
        self.name = name
        self.serial_number = serial_number
        self.identificator = uuid.uuid4()
        self.status = status
        self.creation_time = datetime.now()

    def get_id(self):
        return f'Id: {self.identificator}'

    def get_status(self):
        return f'Status: {self.status}'

    def set_status(self, status: str):
        self.status = status

    def get_time(self):
        return self.creation_time

req0 = Request('Yaroslav', 150102, 'Active')
req1 = Request('Max', 120722, 'Active')