from tailow.operators.base import Operator

class SizeOperator(Operator):
    """ 
        operator to query for arrays by number of elements 
    """

    def to_query(self, field_name, value):

        return {
            "$size": value
        }

    def get_value(self, field, value):
        return field.to_son(value)