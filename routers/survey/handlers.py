from aiogram import Router,F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from .states import Survey
from .survey_handlers.email_newsletters import router as email_newsletter_router
from .survey_handlers.user_email_handlers import router as user_email_router
from .survey_handlers.full_name_user_handlers import router as full_name_user
from aiogram.fsm.state import default_state,any_state
from .survey_handlers.sport_handlers import router as sport_router



router=Router(name=__name__)

router.include_router(full_name_user)
router.include_router(user_email_router)
router.include_router(sport_router)
router.include_router(email_newsletter_router)

@router.message(Command("survey",prefix="!/"),default_state)#default state in start State()
async def greeting(message: Message,state:FSMContext):
    await message.answer(f"Hello my dear friend.Glad to see u. Let's go!!!")
    await state.set_state(Survey.full_name)
    

@router.message(Command("cancel"),Survey())
@router.message(F.text.casefold()=="cancel",Survey())
async def cancel_button(message:Message,state:FSMContext):
    current_state=await state.get_state()# Gain current state for cancel poll
    if current_state is None:
        await message.reply(text="OK, but nothing was going on.Start survey: /survey",reply_markup=ReplyKeyboardRemove())
        return
    await state.clear()
    await message.answer(
        text=f"Cancelled state {current_state}. Start again: /survey",
        reply_markup=ReplyKeyboardRemove()
    ) 




    
    
    

    

                
    

    






















