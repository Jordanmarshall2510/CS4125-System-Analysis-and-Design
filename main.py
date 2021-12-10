from server.session import Session 
from client.app import App
import argparse
import sys
from getpass import getpass

# sqlite bool true or false, hostname, username, password, database

def main():

    # Instantiate the parser
    parser = argparse.ArgumentParser(description='A Smart City Simulation')

    parser.add_argument('-a', '--all', action='store_true', help='Run both session and client. Also works using -r, --remote features.')
    parser.add_argument('-c', '--client', action='store_true', help='Run client. Also works using -r, --remote features.')
    parser.add_argument('-r', '--remote', action='store_true', help='Use remote feature for SQLite or MySQL. Only works using -s, --session, -c, --client, or -a, --all.')
    parser.add_argument('-s', '--session', action='store_true', help='Run session. Also works using -r, --remote features.')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0', help='Get version of program.')

    args = parser.parse_args()
    
    if args.session:
        session = Session()
        session.init()

    if args.client:
        app = App()
        app.init()
        app.run()

    if args.all:
        session = Session()
        session.init()
        app = App()
        app.init()
        app.run()

    if args.remote:
        print("mySQL Login")
        print("----------------------")
        input('Username: ')
        val = getpass('Password: ')

if __name__ == '__main__':
    main()