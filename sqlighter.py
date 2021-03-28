import sqlite3


class SQLighter:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def add_subscriber(self, user_id, status=True):
        """Добавляем нового подписчика"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `userdata` (`user_id`, `status`) VALUES(?,?)",
                                       (user_id, status))

    def get_5(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT ocenka5 FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def get_4(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT ocenka4 FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def get_3(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT ocenka3 FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def get_2(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT ocenka2 FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()
    def get_ball(self, user_id):
        with self.connection:
            return self.cursor.execute('SELECT ball FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()

    def subscriber_exists(self, user_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `userdata` WHERE `user_id` = ?', (user_id,)).fetchall()
            return bool(len(result))

    def update_5(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `ocenka5` = ? WHERE `user_id` = ?",
                                       (status, user_id))

    def update_4(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `ocenka4` = ? WHERE `user_id` = ?",
                                       (status, user_id))

    def update_3(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `ocenka3` = ? WHERE `user_id` = ?",
                                       (status, user_id))

    def update_2(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `ocenka2` = ? WHERE `user_id` = ?",
                                       (status, user_id))

    def update_ball(self, user_id, status):
        with self.connection:
            return self.cursor.execute("UPDATE `userdata` SET `ball` = ? WHERE `user_id` = ?",
                                       (status, user_id))
    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()
