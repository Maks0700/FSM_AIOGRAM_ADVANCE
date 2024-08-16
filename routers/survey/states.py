from aiogram.fsm.state import State,StatesGroup
from enum import Enum

class Survey(StatesGroup):
    full_name=State()
    email_user=State()
    sport=State()
    newsletter=State()


class SurveySports(StatesGroup):
    Tennis=State()
    Football=State()
    Formula_One=State()
    
    

class Sports(str,Enum):
    Tennis="Tennis"
    Football="Football"
    Formula_One="Formula_One"
    


class TrackFormulaone(str,Enum):
    monaco="Monaco"
    spa="Spa"
    suzuka="Suzuka"
    monzo="Monzo"

    