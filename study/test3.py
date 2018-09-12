#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Field(object):
    """docstring for Filed"""

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __getattr__(self, name):
        pass

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    """docstring for StringField"""

    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    """docstring for IntegerField"""

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if (name == 'Model'):
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    """docstring for Model"""

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except Exception as e:
            raise
        else:
            pass
        finally:
            pass


class User(Model):
    name = StringField('name')
    email = StringField('email')
    address = StringField('address')
    id = IntegerField('id')


u = User(id=1, name='张三', email='731097245@qq.com', address='北京市')
u.save()
