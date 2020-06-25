from pkg.main.all import Application
from pkg.config.all import Config


if __name__=='__main__':
    app = Application('5m-fast-120p.mov', Config.loadFromFile('config.json'))
    app.run()
