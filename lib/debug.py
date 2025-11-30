#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev, Freebie

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    
    # Create a session to query the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Test 1: Freebie.dev and Freebie.company
    print("\nTEST 1: Freebie Relationships")
    freebie = session.query(Freebie).first()
    print(f"Freebie.dev: {freebie.dev}")  # Should return Dev instance
    print(f"Freebie.company: {freebie.company}")  # Should return Company instance  

    # Test 2: Company.freebies and Company.devs
    print("\nTEST 2: Company Relationships")
    company = session.query(Company).first()
    print(f"Company: {company.name}")
    print(f"Company.freebies: {company.freebies}")  # Should return collection of Freebie instances
    print(f"Company.devs: {company.devs}")  # Should return collection of Dev instances

    # Test 3: Dev.freebies and Dev.companies
    print("\nTEST 3: Dev Relationships")
    dev = session.query(Dev).filter_by(name="Dan").first()
    print(f"Dev: {dev.name}")
    print(f"Dev.freebies: {dev.freebies}")  # Should return collection of Freebie instances
    print(f"Dev.companies: {dev.companies}")  # Should return collection of Company instances

    # Test 4: Freebie.print_details()
    print("\nTEST 4: Freebie.print_details()")
    freebie = session.query(Freebie).first()
    print(f"freebie.print_details(): {freebie.print_details()}")
    # Should return: "DevName owns a ItemName from CompanyName"

    # Test 5: Company.give_freebie()
    print("\nTEST 5: Company.give_freebie()")
    company = session.query(Company).first()
    dev = session.query(Dev).first()
    new_freebie = company.give_freebie(dev, "Wireless Mouse", 45, session)
    print(f"New freebie: {new_freebie}")
    print(f"New freebie details: {new_freebie.print_details()}")
    # Verify it's associated with the right company and dev
    print(f"Freebie company: {new_freebie.company.name}")
    print(f"Freebie dev: {new_freebie.dev.name}")

    # Test 6: Company.oldest_company()
    print("\nTEST 6: Company.oldest_company()")
    oldest = Company.oldest_company(session)
    print(f"Oldest company instance: {oldest}")
    print(f"Oldest company name: {oldest.name}")
    print(f"Oldest company founding year: {oldest.founding_year}")

    # Test 7: Dev.received_one()
    print("\nTEST 7: Dev.received_one()")
    dev = session.query(Dev).filter_by(name="Dan").first()
    print(f"Dan's freebies: {[f.item_name for f in dev.freebies]}")
    print(f"Dan received 'Coffee Mug': {dev.received_one('Coffee Mug')}")  # Should be True
    print(f"Dan received 'Jetpack': {dev.received_one('Jetpack')}")  # Should be False

    # Test 8: Dev.give_away()
    print("\nTEST 8: Dev.give_away()")
    dan = session.query(Dev).filter_by(name="Dan").first()  
    newton = session.query(Dev).filter_by(name="Newton").first()
    freebie = session.query(Freebie).filter_by(dev_id=dan.id).first()
    
    if freebie:
        print(f"Before: {freebie.print_details()}")
        success = dan.give_away(newton, freebie, session)
        print(f"Give away successful: {success}")
        print(f"After: {freebie.print_details()}")
    else:
        print("Dan has no freebies to give away")
    
    import ipdb; ipdb.set_trace()

