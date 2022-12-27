from aiogram.utils import executor
from commands import dp
import handlers


async def bot_start(_):
    print('Бот запущен')


if __name__ == '__main__':
    handlers.registred_handlers(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=bot_start)
