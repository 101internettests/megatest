import pytest
from config import bot, chat_id


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    bot.send_message(chat_id, "Тест по канониклам прошел, а результат в дженкинсе")
