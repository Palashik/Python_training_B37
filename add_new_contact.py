# -*- coding: utf-8 -*-
from contact import Contact
from application2 import Application2
import pytest

@pytest.fixture
def app(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_contact(app):
    app.login("admin", "secret")
    app.create_new_contact(Contact("Masha", "Ivanovna", "Ivanova", "IP Maria", "Main", "Mary27", "Russian Federation",
                            "738412", "89092154315", "745640", "222351", "maria27@mail.ru", "maria28@mail.ru",
                            "mariaiv27@mail.ru", "www.masha27.ru", "10", "August", "1999", "12", "June", "2010",
                            "dddd", "dfgs", "12345"))
    app.logout()