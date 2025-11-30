#!/usr/bin/env python3

# Script goes here!


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Company, Dev, Freebie 





# Create Companies

facebook = Company(name="Facebook", founding_year=2001)
openAI = Company(name="OpenAI", founding_year=2005)
andela = Company(name="Andela", founding_year=1996)


# Create Devs

dan = Dev(name="Dan")
newton = Dev(name="Newton")
bill = Dev(name="Bill")


# Create Freebies

freebie1 = Freebie(
    item_name="Mouse Pad",
    value=15,
    company=openAI,
    dev=newton
)

freebie2 = Freebie(
    item_name="T-Shirt",
    value=30,
    company=facebook,
    dev=bill
)

freebie3 = Freebie(
    item_name="Coffee Mug",
    value=25,
    company=andela,
    dev=dan
)

# Database connection

engine = create_engine('sqlite:///freebies.db')  
Session = sessionmaker(bind=engine)
session = Session()

# Save to database
session.add_all([
    facebook, openAI, andela,
    dan, newton, bill,
    freebie1, freebie2, freebie3
])

session.commit()
