from behave import *
from TDD_test import *

@given("Technic_Builder")
def first_step(context):
    context.a = Technic_Builder_Test()

@when("test_Mvideo_builder return OK")
def test_Mvideo_builder(context):
    context.a.test_Mvideo_builder()

@when("test_DNS_builder return OK")
def test_DNS_builder(context):
    context.a.test_DNS_builder()

@then("Good job")
def last_step(context):
    pass