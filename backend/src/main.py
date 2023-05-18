from flask.cli import FlaskGroup
from app import app, db

cli = FlaskGroup(app)

# Registers CLI command for recreating db 
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    cli()