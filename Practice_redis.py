from redis import Redis


class MuseumApp:
    def __init__(self):
        self.server = Redis(
            host="localhost",
            port=6379,
            db=0,
            decode_responses=True,
        )

    def _get_exhibit_key(self, ex_id):
        return f"exhibit:{ex_id}"

    def _get_people_key(self, ex_id):
        return f"exhibit_people:{ex_id}"

    def _get_exhibits_by_person_key(self, person_name):
        return f"person_exhibits:{person_name}"

    def _get_type_key(self, ex_type):
        return f"type:{ex_type}"

    def add_exhibit(self, ex_id, title, ex_type, description):
        key = self._get_exhibit_key(ex_id)

        if self.server.exists(key):
            print("Експонат з таким ID вже існує.")
            return

        data = {"title": title, "type": ex_type, "description": description}
        self.server.hset(key, mapping=data)

        self.server.sadd(self._get_type_key(ex_type), ex_id)
        print("Експонат додано.")

    def delete_exhibit(self, ex_id):
        key = self._get_exhibit_key(ex_id)
        if not self.server.exists(key):
            print("Експонат не знайдено.")
            return

        ex_type = self.server.hget(key, "type")
        self.server.delete(key)
        self.server.srem(self._get_type_key(ex_type), ex_id)
        print("Експонат видалено.")

    def edit_exhibit(self, ex_id, title=None, description=None):
        key = self._get_exhibit_key(ex_id)
        if not self.server.exists(key):
            print("Експонат не знайдено.")
            return

        if title: self.server.hset(key, "title", title)
        if description: self.server.hset(key, "description", description)
        print("Інформацію оновлено.")

    def get_exhibit_info(self, ex_id):
        key = self._get_exhibit_key(ex_id)
        data = self.server.hgetall(key)
        print(f"Інформація: {data}" if data else "Експонат не знайдено.")

    def link_person_to_exhibit(self, person_name, ex_id):
        self.server.sadd(self._get_people_key(ex_id), person_name)
        self.server.sadd(self._get_exhibits_by_person_key(person_name), ex_id)
        print(f"Особу {person_name} додано до експонату {ex_id}.")

    def get_exhibits_by_type(self, ex_type):
        ex_ids = self.server.smembers(self._get_type_key(ex_type))
        print(f"Експонати типу {ex_type}: {ex_ids}")


museum = MuseumApp()
museum.add_exhibit("101", "Кобзар", "книга", "Видання 1840 року")
museum.get_exhibit_info("101")
