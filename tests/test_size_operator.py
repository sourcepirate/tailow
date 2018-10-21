from unittest import TestCase

from tailow.operators.base import Q, transform_query
from tailow.fields import ListField, IntegerField
from tailow.operators.size import SizeOperator


class TestOperators(TestCase):

    def setUp(self):
        self._fields = {
            "tags": ListField(sub_field=IntegerField())
        }
        self.size = SizeOperator()

    def test_operator_behaviours(self):
        """ test operator behaviour """
        val = self.size.to_query("tags", [1,2,3,4])
        self.assertDictEqual(val, {
            "$size": [1,2,3,4]
        })