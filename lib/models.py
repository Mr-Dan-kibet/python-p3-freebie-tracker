from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())

    # Relationship that shows which dev recived a freebie from the company
    @property
    def devs(self):
        return list({freebie.dev for freebie in self.freebies})

    def __repr__(self):
        return f'<Company {self.name}>'

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    # Relationship attribute between devs and companies that gave them freebies
    @property
    def companies(self):
        return list({freebie.company for freebie in self.freebies})

    def __repr__(self):
        return f'<Dev {self.name}>'
    
class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer(), primary_key=True)
    item_name = Column(String())
    value = Column(Integer())
    company_id = Column(Integer, ForeignKey('companies.id'))

    dev_id = Column(Integer, ForeignKey('devs.id'))


    company = relationship('Company', backref=backref('freebies', cascade='all, delete-orphan')) 
    dev = relationship('Dev', backref=backref('freebies', cascade='all, delete-orphan'))

    def __repr__(self):
        return f"<Freebie {self.item_name} from {self.company.name} to {self.dev.name}>"    
