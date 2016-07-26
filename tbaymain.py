from tbay import Item, User, Bid
from sqlalchemy import create_engine
engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

import pdb; pdb.set_trace()
shaun = User(username="shaun",password="thinkful")
brian = User(username="brian", password="thinkful")
jake = User(username="jake", password="thinkful")



baseball = Item(name="baseball", description="A ball that is used in the sport of baseball")
session.add_all([baseball, shaun, brian, jake])
session.commit()
shaun.items.append(baseball)
# tennisball = Item(name = "tennisball", description="A ball that is used in tennis", owner_id=shaun.id)



brian_bid = Bid(price=100.0, item_id = baseball.id)
jake_bid = Bid(price=50.0, item_id = baseball.id)

# baseball.bids.append(brian_bid, jake_bid)
brian.bids.append(brian_bid)
jake.bids.append(jake_bid)

# session.add_all([brian_bid, jake_bid])
session.add_all([brian_bid, jake_bid])

session.commit()