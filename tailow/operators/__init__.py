""" All Query Operators """

from .base import OperationRegistry, Operator
from .inopr import InOperator

OperationRegistry.register("in", InOperator)