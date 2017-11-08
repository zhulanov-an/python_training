from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact(first_name="AAA", middle_name="BBB", lastname="CCC", mobile_phone="890263366554"))