import pytest

from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientFundsException


@pytest.fixture
def zero_bank_account():
    return BankAccount()


@pytest.fixture
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (7, 1, 8),
    (-10, 12, 2),
])
def test_add(num1, num2, expected):
    assert expected == add(num1, num2)


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 1),
    (7, 1, 6),
    (-10, 12, -22),
])
def test_subtract(num1, num2, expected):
    assert expected == subtract(num1, num2)


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 6),
    (7, 4, 28),
    (-10, 12, -120),
])
def test_multiply(num1, num2, expected):
    assert expected == multiply(num1, num2)


@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 1.5),
    (7, 1, 7),
    (-10, 2, -5),
])
def test_divide(num1, num2, expected):
    assert expected == divide(num1, num2)


def test_bank_default(zero_bank_account):
    assert 0 == zero_bank_account.balance


def test_bank_set_initial_amount(bank_account):
    assert 50 == bank_account.balance


def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert 30 == bank_account.balance


def test_deposit(bank_account):
    bank_account.deposit(20)
    assert 70 == bank_account.balance


def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert 55 == round(bank_account.balance)


@pytest.mark.parametrize("deposited, withdrew, expected", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000),
])
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert expected == zero_bank_account.balance


@pytest.mark.parametrize("withdrew", [50.01, 51, 100, 200])
def test_insufficient_funds(bank_account, withdrew):
    with pytest.raises(InsufficientFundsException):
        bank_account.withdraw(withdrew)
