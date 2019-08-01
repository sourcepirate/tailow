from unittest import TestCase

from tailow.operators.base import Q, transform_query
from tailow.fields import StringField, IntegerField
from tailow.operators.inopr import InOperator


class TestOperators(TestCase):
    def setUp(self):
        self._fields = {"username": StringField(), "age": IntegerField()}
        self.operator = InOperator()

    def test_operator_behaviours(self):
        """ test operator behaviour """
        val = self.operator.to_query("username", [1, 2, 3, 4])
        self.assertDictEqual(val, {"$in": [1, 2, 3, 4]})

    def test_transform_query(self):
        """ test query transformation by operator """
        val = transform_query(self._fields, age__in=[1, 2, 3])
        self.assertDictEqual(val, {"age": {"$in": [1, 2, 3]}})


class TestQObjects(TestCase):
    def setUp(self):
        self._fields = {"username": StringField(), "age": IntegerField()}

    def test_q_object_query_transformation(self):
        val = Q(age__in=[1, 2, 3])
        self.assertDictEqual(
            val.query(self._fields), {"age": {"$in": [1, 2, 3]}}
        )

    def test_q_object_query_conjugation(self):
        val = Q(age__in=[1, 2, 3]) & Q(age__in=[4, 6, 7])
        self.assertDictEqual(
            val.query(self._fields),
            {
                "$and": [
                    {"age": {"$in": [1, 2, 3]}},
                    {"age": {"$in": [4, 6, 7]}},
                ]
            },
        )

    def test_q_object_query_combination(self):
        val = Q(age__in=[1, 2, 3]) | Q(age__in=[4, 6, 7])
        self.assertDictEqual(
            val.query(self._fields),
            {
                "$or": [
                    {"age": {"$in": [1, 2, 3]}},
                    {"age": {"$in": [4, 6, 7]}},
                ]
            },
        )
