from app import manager


@manager.command
def hello(name):
    "Just say hello"
    greeting = "hello %s" % name
    print(greeting)
