# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_contact(app):
    app.session.login("admin", "secret")
    app.contact.create_new(Contact("Masha", "Ivanovna", "Ivanova", "IP Maria", "Main", "Mary27", "Russian Federation",
                            "738412", "89092154315", "745640", "222351", "maria27@mail.ru", "maria28@mail.ru",
                            "mariaiv27@mail.ru", "www.masha27.ru", "10", "August", "1999", "12", "June", "2010",
                            "dddd", "dfgs", "12345"))
    app.session.logout()