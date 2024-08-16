from aiogram import Router,F
from aiogram.types import Message,ReplyKeyboardRemove
from keyboards.common_keyboards import build_keyboard_select
from routers.survey.states import Sports, Survey,SurveySports,TrackFormulaone
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State

router=Router(name=__name__)


known_sport_to_next:dict[Sports|str,tuple[State,str]]={
    Sports.Tennis:(SurveySports.Tennis,"Who are you favorite player"),
    Sports.Football:(SurveySports.Football,"What is your favourite football team?"),
    Sports.Formula_One:(SurveySports.Formula_One,"What is your favourite track?")
}
known_sport_to_kb={
    Sports.Formula_One:build_keyboard_select(TrackFormulaone)
}

@router.message(Survey.sport,F.text.cast(Sports))
async def sport_handle(message:Message,state:FSMContext):
    
    await state.update_data(sport=message.text)
    next_state,question_next=known_sport_to_next[message.text]
    
    await state.set_state(next_state)
    kb=ReplyKeyboardRemove()
    if message.text in known_sport_to_kb:
        kb=known_sport_to_kb[message.text]
    await message.answer(
        text=question_next,
        reply_markup=kb
    )
    

@router.message(Survey.sport)
async def select_sport(message:Message):
    await message.answer(
        text="Uknown sport, please tap the following below!!",
        reply_markup=build_keyboard_select(Sports)
        
    )
    
    