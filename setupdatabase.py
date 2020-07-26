from main import db, Student

db.create_all()

bob = Student("Bob", 90)
zaid= Student("Zaid", 84)
print(bob.id)
print(zaid.id)

db.session.add_all([zaid,bob])
db.session.commit()

print(zaid.id)
print(bob.id)
