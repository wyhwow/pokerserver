from .models import db

def get_all(model):
    data = model.query.all()
    return data

# kwargs for passing uknown number argurments
def add_instance(model, **kwargs):
    instance = model(**kwargs)
    db.session.add(instance)
    commit_changes()

def commit_changes():
    db.session.commit()
