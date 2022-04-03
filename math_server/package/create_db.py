import mathematical_logic
from structure_of_table import MathExpression
from database_for_server import Session


def processing_to_query(data: str) -> str:
    if data.split()[0] == 'get':
        offset, limit = data.split()[1:]
        query = output(int(offset), int(limit))
        return '\n'.join(map(str, query))
    else:
        return get_answer(data)


def fill_db(name_operator: str, num1: str, num2: str, result: str) -> None:
    with Session() as session:
        if result != '':
            math_expression = MathExpression(name_operator, float(num1), float(num2), float(result))
            session.add(math_expression)
            session.commit()


def get_answer(data: str) -> str:
    name_operator, num1, num2 = data.split(' ')
    result = mathematical_logic.multi_func(data)
    fill_db(name_operator, num1, num2, result)
    return result


def output(offset, limit) -> list:
    expression = Session().query(MathExpression).all()
    for i in expression:
        if not offset:
            if limit:
                yield i.operator_ex
                limit -= 1
        else:
            offset -= 1
