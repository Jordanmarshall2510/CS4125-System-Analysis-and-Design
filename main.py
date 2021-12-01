from server.session import Session 
from client.app import App
import sys

def main(args):
    
    if args == ['session']:
        session = Session()
        session.init()

    if args == ['app']:
        app = App()
        app.init()
        app.run()

    if args == []:
        session = Session()
        session.init()
        app = App()
        app.init()
        app.run()


if __name__ == '__main__':
    main(sys.argv[1:])