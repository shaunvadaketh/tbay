

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    bids = relationship("Bid", backref = "bid")
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    items = relationship("Item", backref = "users")
    bids = relationship("Bid", backref = "bids")
    
class Bid(Base):
    
    __tablename__ = "bids"
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    bidder_id = Column(Integer, ForeignKey('users.id'),nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'),nullable=False)
Base.metadata.create_all(engine)

# shaun = User(username="shaun",password="thinkful")
# brian = User(username="brian", password="thinkful")
# jake = User(username="jake", password="thinkful")

# baseball = Item(name="baseball", description="A ball that is used in the sport of baseball", owner_id=shaun.id)
# tennisball = Item(name = "tennisball", description="A ball that is used in tennis", owner_id=shaun.id)

# brian_bid = Bid(bidder_id=brian.id, price=100.0, item_id=baseball.id)
# jake_bid = Bid(bidder_id=jake.id, price=50.0, item_id=baseball.id)

# session.add_all([shaun, brian, jake, baseball, brian_bid, jake_bid])
# session.commit()



