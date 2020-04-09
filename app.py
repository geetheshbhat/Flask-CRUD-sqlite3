import sqlite3
from flask import Flask, request
from flask_restful import Resource, reqparse

app=Flask(__name__)
@app.route('/create', methods=['GET'])
def create_table():
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()
    query="CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, movie_name text)"
    cursor.execute(query)
    connection.commit()
    connection.close()
    return {'message':'table created successfully'},200

@app.route('/create/<string:name>',methods=['POST'])
def add_item(name):
    rd=find_one(name)
    if rd is None:
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="INSERT INTO movies VALUES(NULL,?)"
        cursor.execute(query,(name,))
        connection.commit()
        connection.close()
        return {'message':'Movies added successfully'},200
    return {'Message':"Movie already exists"},400

@app.route('/read',methods=['GET'])
def show_movies():
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()
    query="SELECT * FROM movies"
    rows=cursor.execute(query)
    item=[]
    if rows:
        for row in rows:
            item.append({"id":row[0],"Movie Name":row[1]})
        return {'movies':item}
    return {'Message':'The Database is empty'},400

@app.route('/read/<string:name>',methods=['GET'])
def find_one(name):
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()
    query="SELECT * FROM movies where movie_name=?"
    rows=cursor.execute(query,(name,))
    rd=rows.fetchone()
    try:
        if rd:
            return {"Movie":rd[1]},201
    except:
        return {"Message":"Movie Not Found"},404 
@app.route('/update',methods=['PUT'])
def movie_update():
    data=request.get_json()
    rd=find_one(data['old_name'])
    if rd:
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="UPDATE movies SET movie_name=? where movie_name=?"
        row=cursor.execute(query,(data['new_name'],data['old_name']))
        connection.commit()
        connection.close()
        return {'message':'Movie renamed from {} to {}'.format(data['old_name'],data['new_name'])},201
    add_item(data['old_name'])
    return {'message':"Movie doesn't exist, a new movie has been created"},201

@app.route('/delete/<string:name>',methods=['DELETE'])
def delete_movie(name):
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()
    query="DELETE FROM movies where movie_name=?"
    row=cursor.execute(query,(name,))
    connection.commit()
    connection.close()
    return {"Message":"Movie {} deleted successfully".format(name)},200
if __name__ == '__main__':
    app.run(debug=True)