from app.models import User, Party
from app import db

db.create_all()
db.session.commit()

admin = User('tomer', 'admon', is_admin=True)
guest = User('liron', 'admon')
aa = Party('AA','https://www.am-1.org.il/wp-content/uploads/2015/03/%D7%94%D7%A2%D7%91%D7%95%D7%93%D7%94.-%D7%A6%D7%99%D7%9C%D7%95%D7%9D-%D7%99%D7%97%D7%A6.jpg')
bb = Party('BB', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Likud_Logo.svg/250px-Likud_Logo.svg.png')
db.session.add(aa)
db.session.add(bb)
db.session.add(admin)
db.session.add(guest)
db.session.commit()
users = User.query.all()
print users
