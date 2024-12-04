rom Flask import Flask

app = Flask(name)

app.route('/')

def hello_world():

    return 'gymbattlebot'

if  __name__ == "__main__":

  app.run()
