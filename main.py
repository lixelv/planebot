from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from utils import calculate_plane2

from dotenv import env

bot = Bot(token=env("TELEGRAM"))
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\nЭтот бот создан для того, чтобы считать уравнение плоскости на основании 3 точек, лежащих в этой плоскости.\n\nТак вот, для того, чтобы посчитать уранение матрицы просто введите координаты 3 точек через пробел, вот как это должно выглядеть:")
    await message.answer("2 6 0\n-8 3 1\n-7 6 2")

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Введите 3 точки в следующем виде и я вам посчитаю уранение плоскости.")
    await message.answer("2 1 0\n-40 3 2\n-2 6 -5")

@dp.message()
async def echo(message: types.Message):
    await message.answer(calculate_plane2(message.text))
    

if __name__ == "__main__":
    dp.run_polling(bot)