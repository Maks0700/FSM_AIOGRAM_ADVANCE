from aiogram import F, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.utils import markdown
from routers.survey.states import Survey
from aiogram import Router

router=Router(name=__name__)
@router.message(Survey.full_name,F.text)
async def full_name(message:Message,state:FSMContext):
    await state.set_state(Survey.email_user)
    await state.update_data(Name=message.text)
    await message.answer(f"Great {markdown.hcode(message.text)}.Enter your email!")

@router.message(Survey.full_name,~F.text)
async def check_name(message: Message,state:FSMContext):
    await message.answer("Enter your valid name!!!")
    