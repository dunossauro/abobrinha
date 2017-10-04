from behave import given, then
from project.calc import add


@given('que somo "{n1:g}" e "{n2:g}"')
def execute_add(context, n1, n2):
    context.result = add(n1, n2)


@given('que somo "{n1:g}" e "{n2:w}"')
def execute_add(context, n1, n2):
    context.result = add(n1, n2)


@then('o resultado deve ser "{r:g}"')
def compare_result(context, r):
    assert context.result == r, \
           'Esperado: {}\nRecebido{}'.format(r, context.result)


@then('o resultado deve ser "{r}"')
def compare_result(context, r):
    assert context.result == r, \
           'Esperado: {}\nRecebido{}'.format(r, context.result)
