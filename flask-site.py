""" Serverside script that: controlls the database,
                            handels post from user,
                            prints out score on website"""

from flask import Flask, request
import sqlite3

app = Flask(__name__)


DATABASE = "mysite/testdb.db"


def create_table():
    """ create the table
        THIS CODE SHALL ONLY WHEN THE TABLE NEEDS TO BE MADE!"""
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        cursor.execute("SELECT NAME FROM SQLITE_MASTER WHERE NAME=?", ("highscore",))


        cursor.execute("""CREATE TABLE highscore(
                        id INTEGER NOT NULL,
                        score INTEGER,
                        PRIMARY KEY(id)
                        )""")

        db.commit()

    return "table created"

def set_up_highscore():
    """ this function creates 10 elements to the database with the value 0"""
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()

        #add all the 10 different scores to the database
        for n in range(10):
            cursor.execute("INSERT INTO highscore(id,score) values (?,?)", (n,0))

        db.commit()

    return "Highscore set up complete"

def clear_highscore():
    """ this function resets the highscore"""
    highscore = []

    for n in range(10):
        highscore.append(0)

    set_new_highscore(highscore)

    return "highscore cleared"

def get_highscore():
    """ this function return the highscore from the database"""

    highscore = []

    with sqlite3.connect(DATABASE) as db:

        cursor = db.cursor()
        cursor.execute("SELECT * FROM highscore")
        everything = cursor.fetchall()


        # add score from db to the highscore list
        for n in everything:
            highscore.append(n[1])


    return highscore

def set_new_highscore(highscore):
    """ take a list of highscores and set the values in the database to these values"""
    with sqlite3.connect(DATABASE) as db:

        cursor = db.cursor()

        for n in range(10):
            cursor.execute("UPDATE highscore SET score=? WHERE id=?",(highscore[n],n))

        db.commit()

    return "Highscore updated successfully"

@app.route("/hub/", methods=["POST"])
def post_stuff():
    """ this function is called by the local script"""


    command = request.form.get('command')

    # create the highscore table
    if(command == "create_table"):
        return create_table()

    # create the elements in the database
    elif(command == "set_up"):
        return set_up_highscore()

    # set all highscores to 0
    elif(command == "clear_highscore"):
        return clear_highscore()

    # check if a new score beats a highscore
    elif(command == "highscore"):

        # get current highscore
        highscore = get_highscore()

        # get the score
        score = int(request.form.get('score'))

        # check for a lower highscore
        for n in range(10):
            if(score > highscore[n]):




                # lower position of everyone else
                for m in range(9,n,-1):
                    highscore[m] = highscore[m-1]

                # add the new score
                highscore[n] = score

                # save the new highscore to database
                return set_new_highscore(highscore)

                break


    return "post succesfull"

@app.route("/")
def main_page():
    """ this function is called when a user enters the website
        it prints out the list of highscore on the webpage"""
    highscore = get_highscore()

    score_list = ""

    # add all the lines to the list
    for n in range(10):
        score_list += str(n+1) + ": " + str(highscore[n]) + "<br>"

    # print it out
    return score_list

if(__name__ == "__main__"):
    # run the application
    app.secret_key = "super mega secret"
    app.run()
