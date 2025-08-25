from datetime import datetime

from db.database import get_db
from models.card import Card
import random
from dateutil.relativedelta import relativedelta


def create_card(user_id: int, is_credit: bool):

    with get_db() as db:

        new_card = Card(

            number = str(random.randint(1000_0000_0000_0000, 9999_9999_9999_9999)),
            exp_date = datetime.now() + relativedelta(years=5),
            cvv = str(random.randint(100, 999)),
            is_credit = is_credit,
            user_id = user_id

        )

        db.add(new_card)
        db.commit()
        db.refresh(new_card)

        return new_card