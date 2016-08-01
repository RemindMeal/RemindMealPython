from app import app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_security.script import AddRoleCommand, CreateUserCommand, CreateRoleCommand, RemoveRoleCommand, \
    ActivateUserCommand, DeactivateUserCommand

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('grant', AddRoleCommand)
manager.add_command('create_user', CreateUserCommand)
manager.add_command('create_role', CreateRoleCommand)
manager.add_command('remove_role', RemoveRoleCommand)
manager.add_command('activate', ActivateUserCommand)
manager.add_command('deactivate', DeactivateUserCommand)

if __name__ == '__main__':
    manager.run()
