from model import Base, Test


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///database.db?check_same_thread=False')
 
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_test(input_subject, input_grade, input_picture, input_description, input_solution, input_username):
    print("tring to add!!!!!!!!!!!!!!!!!!!!!!!!!")
    
    
    test_object = Test(
        subject=input_subject,
        grade=input_grade,
        picture=input_picture,
        solution = input_solution,
        username = input_username,
        description = input_description)
    session.add(test_object)
    session.commit()


def test_by_id(id):
  test1 = session.query(
       Test).filter_by(
       id=id).first()
  return test1


def query_all():
  tests = session.query(Test).all()
  return tests
'''

def isExistTest(testname):
  test_object = session.query(Test).filter_by(picture=testname).scalar()

  if(test_object != None):
    return True
  return False
'''


