from src.app import create_app
if __name__ == '__main__':
    db = create_app()
    db.run()