from redis import Redis

host = 'localhost'
port = 6379

server = Redis(
    host="localhost",
    port=6379,
    db=0,  # індекс бази даних
    decode_responses=True,  # щоб повертало не сирі байти
)


server.set("name", "Alice")

user_name = server.get("name")
print(user_name)


server.set("name", "John Doe")
server.get("name")

server.rpush("fruits", "apple", "banana", "orange")
server.lrange("fruits", 0, -1)

server.hset("user:1", mapping={"name": "Alice", "age": 25})
server.hgetall("user:1")

server.sadd("tags", "red", "green", "blue")
server.smembers("tags")

server.incr("counter")
server.get("counter")

server.delete("name")
server.exists("name")

server.setex("message", 60, "Hello, Redis!")
