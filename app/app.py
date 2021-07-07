from flask import Flask
from flask import request
from flask import render_template
from models.models import WorkorderContent

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def root(name = [i + 1 for i in range(30)]):
  # get all workorder from database
  all_wo = WorkorderContent.query.all()
  return render_template('index.html', all_wo = all_wo)

@app.route('/index', methods=['post'])
def search():
  # get all workorder from database 
  all_wo = WorkorderContent.query.all()
  # get text from input form
  try:
    target_wo = int(request.form.get("target_wo"))
  except:
    target_wo = 0
  
  print("Log Message:")
  print(target_wo)

  # content = WorkorderContent(title, body, datetime.now())
  # db_session.add(content)
  # db_session.commit()

  return render_template('index.html', all_wo = all_wo)

#rendering the HTML page which has the button
#@app.route('/json')
#def json():
#    return render_template('index.html')

#background process happening without any refreshing
@app.route('/background_process_test', methods=['post'])
def background_process_test():
  # get all workorder from database 
  all_wo = WorkorderContent.query.all()

  pos = request.get_data()
  print (pos)

  return render_template('index.html', all_wo = all_wo)

if __name__ == "__main__":
  app.run(debug=True, port=8888)