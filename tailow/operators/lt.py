from tailow.operators.base import Operator


class LTOperator(Operator):
    """ Greater than operator """

    def to_query(self, field_name, value):

        return {"$lt": value}

    def get_value(self, field, value):
        return field.to_son(value)


class LTEOperator(Operator):
    def to_query(self, field_name, value):
        return {"$lte": value}

    def get_value(self, field, value):
        return field.to_son(value)
