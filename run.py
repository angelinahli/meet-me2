#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app, db
from app.models import User, Event

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Event": Event}

if __name__ == "__main__":
    app.run(debug=True)