from app import manager


@manager.command
def hello(name):
    "Just say hello"
    print("hello", name)
