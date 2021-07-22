import pytest
# import pytest_mock
from kissaas_app.app import choice, kindness
from pytest_mock import MockerFixture, mocker


def test_kindness_should_call_random_choice(mocker: MockerFixture) -> None:
    test_string = "Hello, World!"
    choice_spy = mocker.patch('kissaas_app.app.choice', return_value=test_string)

    result = kindness()

    choice_spy.assert_called_once()
    assert result is test_string
