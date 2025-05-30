from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql import operators
from sqlalchemy.sql.expression import BinaryExpression
from sqlalchemy.types import Boolean

# Register the % operator (pg_trgm's similarity match operator)
class SimilarityOp(BinaryExpression):
    pass

@compiles(SimilarityOp)
def compile_similarity_op(element, compiler, **kw):
    left = compiler.process(element.left, **kw)
    right = compiler.process(element.right, **kw)
    return f"{left} % {right}"

def similarity_match(left, right):
    return SimilarityOp(left, right, operator=operators.custom_op('%'), type_=Boolean)
