import mathematical_logic
from database_for_server import Base, Session, engine
from sqlalchemy import Column, Integer, Numeric, Enum
import enum


class Operators(enum.Enum):
    add = 'add',
    floordiv = 'floordiv',
    mod = 'mod',
    mul = 'mul',
    lt = 'lt',
    le = 'le',
    eq = 'eq',
    ne = 'ne',
    ge = 'ge',
    gt = 'gt',
    pow = 'pow',
    sub = 'sub',
    truediv = 'truediv'


class MathExpression(Base):
    __tablename__ = 'math_expression'
    id = Column(Integer, primary_key=True)
    operator_ex = Column('operator', Enum(Operators, name='operators', create_type=False))
    number1 = Column('number1', Numeric)
    number2 = Column('number2', Numeric)
    result = Column('result', Numeric)

    def __init__(self, operator, number1, number2, result):
        self.operator_ex = operator
        self.number1 = number1
        self.number2 = number2
        self.result = result


def processing_to_query(data: str):
    if data.split()[0] == 'get':
        offset, limit = data.split()[1:]
        query = output(int(offset), int(limit))
        return '\n'.join(map(str, query))
    else:
        return fill_db(data)


def fill_db(data: str) -> str:
    name_operator, num1, num2 = data.split(' ')
    with Session() as session:
        result = mathematical_logic.multi_func(data)
        if result == '':
            return result
        else:
            Base.metadata.create_all(engine)
            math_expression = MathExpression(name_operator, float(num1), float(num2), float(result))
            session.add(math_expression)
            session.commit()
        return result


def output(offset, limit):
    expression = Session().query(MathExpression).all()
    for i in expression:
        if not offset:
            if limit:
                yield i.operator_ex
                limit -= 1
        else:
            offset -= 1


if __name__ == '__main__':
    output(5, 5)
