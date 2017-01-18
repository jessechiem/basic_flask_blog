"""
Separate module for running Flask project,
via app Flask object in views module.
"""
from views import app

# python run.py
if __name__ == "__main__":
    app.run(debug=True)
