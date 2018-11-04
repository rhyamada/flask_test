import sqlalchemy
from sqlalchemy.ext.associationproxy import association_proxy
from app import db
from wtforms import validators

class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer(),primary_key=True)

class Product(Base):
    name = db.Column(db.String())
    def __str__(self):
        return self.name


class User(Base):
    name = db.Column(db.String(),default='Noname')
    products = db.relationship(Product, secondary=db.Table('association', db.metadata,
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('product_id', db.Integer(), db.ForeignKey('product.id'))
    ))
    keywords = association_proxy('user_keywords', 'keyword')
    keywords_values = association_proxy('user_keywords', 'keyword_value')

    def __str__(self):
        return self.name



class UserKeyword(db.Model):
    __tablename__ = 'user_keyword'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    user = db.relationship(User, backref=db.backref("user_keywords", cascade="all, delete-orphan"))

    keyword_id = db.Column(db.Integer, db.ForeignKey('keyword.id'), primary_key=True)
    keyword = db.relationship("Keyword")

    special_key = db.Column(db.String(50))

    keyword_value = association_proxy('keyword', 'keyword')

    def __init__(self, keyword=None, user=None, special_key=None):
        self.user = user
        self.keyword = keyword
        self.special_key = special_key


class Keyword(Base):
    keyword = db.Column('keyword', db.String(64))
    def __init__(self, keyword=None):
        self.keyword = keyword

    def __repr__(self):
        return 'Keyword(%s)' % repr(self.keyword)


@sqlalchemy.event.listens_for(User, 'before_insert')
@sqlalchemy.event.listens_for(User, 'before_update')
def bf(m,c,t):
    if hasattr(t,'_data'):
        print(t._data)

@sqlalchemy.event.listens_for(User.products,'bulk_replace')
def br(t,v,i):
    for p in Product.query.all():
        if not p in v:
            v.append(p)

@sqlalchemy.event.listens_for(User.products,'append')
def a(t,v,i):
    t._data = (v,)

@sqlalchemy.event.listens_for(User.products,'remove')
def r(t,v,i):
    pass 
