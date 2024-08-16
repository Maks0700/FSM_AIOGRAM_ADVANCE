from aiogram import Router
from validators.validator import valid_email_filter,valid_email,validate_email
from aiogram.types import Message
from ..states import Sports, Survey
from aiogram.fsm.context import FSMContext
from aiogram.utils import markdown
from keyboards.common_keyboards import build_keyboard_select, keyboard_balidator_yes
from aiogram import F

router=Router(name=__name__)

@router.message(
    Survey.email_user,F.text.cast(validate_email).normalized.as_("email"))
async def record_email(message:Message,state:FSMContext,email:str,):
    await state.set_state(Survey.sport)
    await state.update_data(email=email)
    await message.answer(f"Cool, very good. Your email is {markdown.hcode(email)}.Which your favourite sport?"
                         ,reply_markup=build_keyboard_select(Sports))
    
@router.message(Survey.email_user)

async def check_record_email(message: Message,state:FSMContext):
    await message.reply(f"Invalid email, please try again!! Cancel survey? Tap here: /cancel")
    
    