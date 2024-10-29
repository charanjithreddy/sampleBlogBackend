from flask import Flask,render_template,request,jsonify
app=Flask(__name__)
"""
@app.route('/api/posts', methods=['POST'])
def createpost():
    data=request.get_json()
    return jsonify({"message":"Post successfully created","post":data}),201

@app.route('/api/posts',methods=['GET'])
def getpost():
    post=[{"title":"sample post","content":"this is the sample post"}]
    return jsonify(post)

"""
@app.route('/api/content',methods=['GET'])
def get_data():
    with open('data.txt','r') as f:
        content=f.read()
    return jsonify({"content": content})
    


if __name__=='__main__':
    app.run(debug=True)