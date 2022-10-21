from flask import Flask
app = Flask(__name__)
contact = [{
    'id': tasks[-1]['id']+1,
    'name':request.json['Name'],
    'Contact': request.json.get('Contact',""),
    'done': False
}]

@app.route('/add-data', methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'PLease provide the data!'
        },400)

if(__name__=='__main__'):
    app.run(debug=True)        