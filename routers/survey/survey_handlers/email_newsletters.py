from aiogram import F, Router

from ..states import Survey
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils import markdown
from aiogram.types import ReplyKeyboardRemove

router=Router(name=__name__)

    

async def send_data(message:Message,data: dict):
    text_total=markdown.text("Your results",
                "",
                markdown.text(f"Name: {markdown.hbold(data['Name'])}"),
                markdown.text(f"Email: {markdown.hcode(data['email'])}"),
                (
                    "Cool we are send to you newsletters!!"
                     if data["news_letter"]
                     else
                     "Sorryyy, goodbye!!"
                ),
                sep="\n"
                )
    await message.answer(text=text_total,reply_markup=ReplyKeyboardRemove())

@router.message(Survey.newsletter,F.text.casefold()=="yes")
async def yes_reply(message:Message,state:FSMContext):
    data=await state.update_data(news_letter=True)
    await state.clear()
    await send_data(message,data)
    


@router.message(Survey.newsletter,F.text.casefold()=="no")
async def no_reply(message:Message,state:FSMContext):
    data=await state.update_data(news_letter=False)
    await state.clear()
    await send_data(message,data)


@router.message(Survey.newsletter)
async def check_reply(message:Message):
    await message.answer(f"Use to key {markdown.hbold('yes')} or {markdown.hbold('no')}")
    