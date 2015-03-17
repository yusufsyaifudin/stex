# Stex

Stex is a python framework based on [Flask](http://flask.pocoo.org/)


## Installation
To install just using `pip`

```
pip install -r requirements.txt
```

## Running application

```
python manage.py runserver
```


## Migrations
Stex using [Flask-Migrate](https://flask-migrate.readthedocs.org/en/latest/) for migration support. Please read official documentation for more info.


To run migration
`python manage.py db upgrade`


## Eloquent database
Stex using [Active-SQLAlchemy](https://github.com/mardix/active-sqlalchemy) for ORM interface. It makes you to easy communicate with your database. [See docs for usage](/docs/active_sqlalchemy.md)

## Modules
Stex support module. All you need is create your own module and import in `/app/modules.py` such as `from app.home_module.controllers import mod_home` and then register it to the blueprint `app.register_blueprint(mod_home)`. Done!


## Commands
Sometimes we need console interface to communicate with our python application. You can make your own command in `/app/commands/`. Create file `yourcommand.py`, `from app import manager` define your function like:

```
from app import manager


@manager.command
def hello(name):
    "Just say hello"
    print "hello", name

```

then in `/app/console.py` register your command. How?

import using `from app.commands import yourcommand` where `yourcommand` is yourcommad filename


## Templates
Flask leverages Jinja2 as template engine. So, Stex too.



## License

The MIT License (MIT)

Copyright (c) [2015] [Yusuf Syaifudin]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
