""" All Query Operators """

from .base import OperationRegistry, Operator, Q
from .inopr import InOperator
from .gt import GTEOperator, GTOperator
from .lt import LTEOperator, LTOperator

OperationRegistry.register("in", InOperator)
OperationRegistry.register("gte", GTEOperator)
OperationRegistry.register("gt", GTOperator)
OperationRegistry.register("lte", LTEOperator)
OperationRegistry.register("lt", LTOperator)