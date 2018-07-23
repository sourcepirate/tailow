## Tailow
[![Build Status](https://travis-ci.org/sourcepirate/tailow.svg?branch=master)](https://travis-ci.org/sourcepirate/tailow)
[![Documentation Status](https://readthedocs.org/projects/tailow/badge/?version=latest)](https://tailow.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/tailow.svg)](https://badge.fury.io/py/tailow)

A ORM wrapper around motor

## Usage

```python
import asyncio
from tailow.fields import *
from pymongo import ASCENDING
from tailow.document import Document

class Address(Document):

    address = StringField(required=True)


class Student(Document):

    name = StringField(required=True)
    age = IntegerField(required=True)
    std = IntegerField(required=True)
    address = ReferenceField(Address)

    class Meta:
        name = "students"
        indexes = [(age, ASCENDING)]


async def get_all_students():
    values = await Student.objects.filter(name="sathya").limit(10).skip(2).find()
    print(values)

evloop = asyncio.get_event_loop()
evloop.run_until_complete(get_all_students())

```

## Provides

* Querying via Q objects.
* Special Operators.
* Index Support.

## License
MIT.

