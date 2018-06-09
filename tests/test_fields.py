from datetime import datetime
from unittest import TestCase
from bson.objectid import ObjectId
from tailow.fields import BaseField, IntegerField, ReferenceField
from tailow.document import Document


class TestBaseField(TestCase):

    def setUp(self):
        self.field = BaseField(required=True)
        self.value = 2
    
    def test_base_get_value(self):
        self.assertEqual(self.field.get_value(self.value), self.value)
    
    def test_base_to_son(self):
        self.assertEqual(self.field.to_son(self.value), self.value)
    
    def test_base_from_son(self):
        self.assertEqual(self.field.from_son(self.value), self.value)
    
    def test_base_to_query(self):
        self.assertEqual(self.field.to_query(self.value), self.value)
    
    def test_base_validate(self):
        self.assertTrue(self.field.validate(self.value))

class TestIntegerField(TestCase):

    def setUp(self):
        self.field = IntegerField(max_value=20, min_value=10, default=5)
        self.test_value = "12"
        self.act_value = 12
    
    def test_field_get_value_for_none(self):
        self.assertEqual(self.field.to_son(None), self.field.default)

    def test_field_get_value_to_son(self):
        self.assertEqual(self.field.to_son(self.test_value), self.act_value)

    def test_field_get_value_from_son(self):
        self.assertEqual(self.field.from_son(self.test_value), self.act_value)
    
    def test_field_get_value_to_query(self):
        self.assertEqual(self.field.to_query(self.test_value), self.act_value)

    def test_field_validation_ok_case(self):
        self.assertTrue(self.field.validate(self.test_value))
    
    def test_field_validation_failure_case(self):
        self.assertFalse(self.field.validate("24"))

class TestReferenceField(TestCase):

    def setUp(self):
        class PsyDuck(Document):
            pass
        self.field = ReferenceField(PsyDuck)
        self._id = ObjectId.from_datetime(datetime.now())
        self.test_value = PsyDuck(id=self._id)
        self.test_value._id = self._id

    def test_field_valdiation_true_case(self):
        self.assertTrue(self.field.validate(self.test_value))
    
    def test_field_validation_false_case(self):
        self.assertFalse(self.field.validate(None))
    
    def test_field_to_son_case(self):
        self.assertEqual(self.field.to_son(self._id), self._id)
    
    def test_field_from_son_case(self):
        self.assertEqual(self.field.from_son(self._id), self._id)