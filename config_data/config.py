from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str  # Токен для доступа к боту
    admins_id: list[int]  # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot


# Создаём экземпляр класса Config и наполняем его данными из переменных окружения
def load_config(path: str | None = None) -> Config:
    # Создаём экземпляр класса Env
    env: Env = Env()

    # Добавляем в окружение данные прочитанные из файла .env
    env.read_env()

    return Config(tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admins_id=list(map(int, env.list('ADMINS_ID')))))
