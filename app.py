rom Flask import Flask

app = Flask(name)

app.route('/')

def hello_world():

    return 'gymbattlebot'

if  name == "main":

  app.run()
