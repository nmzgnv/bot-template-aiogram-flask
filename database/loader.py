from gino import Gino

# TODO change db to async

db = Gino()

if __name__ == '__main__':
    pass
    # # db.drop_all()
    # db.create_all()
    # db.session.commit()
