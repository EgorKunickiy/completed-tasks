import mathematical_logic
from database_for_server import Base
from sqlalchemy import Column, Integer, Numeric, Enum
import enum


class MathExpression(Base):
    __tablename__ = 'math_expression'
    id = Column(Integer, primary_key=True)
    operator_ex = Column('operator', Enum(enum.Enum('Operator', mathematical_logic.LIST_OF_OPERATOR),
                                          name='operators', create_type=False))
    number1 = Column('number1', Numeric)
    number2 = Column('number2', Numeric)
    result = Column('result', Numeric)

    def __init__(self, operator, number1, number2, result):
        self.operator_ex = operator
        self.number1 = number1
        self.number2 = number2
        self.result = result
