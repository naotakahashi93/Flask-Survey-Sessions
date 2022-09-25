from crypt import methods
from dis import Instruction
from distutils.log import debug, error
from urllib import response
from flask import Flask, request, render_template, redirect, flash, session
# from flask_debugtoolbar import DebugToolbarExtension
from random import choice, sample
from surveys import satisfaction_survey

app = Flask(__name__)
# app.debug = True 
# app.config['SECRET_KEY'] = 'secrettttkeyyy'
# debug = DebugToolbarExtension(app)

responses = []
app.config["SECRET_KEY"] = "secret session keyyyy" ## setting a secret key to enable session 

@app.route("/")
def home():
    """ Home page that lists the title and instructions of the survey """
    title = satisfaction_survey.title # the variable that gives us the title of the survey
    instructions = satisfaction_survey.instructions #the variable that gives us the instructions of the survey
    session["responses"] =[] # setting the sessions dictionary with key of responses to an empty list
    return render_template("home.html", title = title, instructions = instructions)

@app.route("/questions/<int:q>")
def questions(q):
    """ The page that gives you each question and options to select answers """
    question = satisfaction_survey.questions[q].question 
    choices = satisfaction_survey.questions[q].choices

    # if (responses is None):
    #     # trying to access question page too soon
    #     return redirect("/")

    # if (len(responses) == len(satisfaction_survey.questions)):
    #     # They've answered all the questions! Thank them.
    #     return redirect("/complete")

    # if (len(responses) != q):
    #     # Trying to access questions out of order.
    #     flash("Invalid question id")
    #     return redirect(f"/questions/{len(responses)}")

    return render_template("questions.html", question = question, choices = choices)  


@app.route("/answers", methods=["POST"])
def log_answer():
    """ In this page we are listening for the post request from the /questions/<int:q> route and we log the answers"""
    userselection = request.form["answer"] ## we are grabbing the "answer" key in the request.form which is going to give us what the user answered
    # print("userselectionnN2", userselection)
    
    ## we need to bind the "responses" list into the session 
    responses = session["responses"] ## the "responses" list = the valyes in the responses key in session
    responses.append(userselection) ## then we are going to add the userselection (the selected answers) to the response list 
    # print("responses---", responses)
    session["responses"] = responses # then we are binding that values of the responses key to the "responses" list 
    print("sessionresponsesss ", session["responses"]) ## printing the list with teh responses to the questions 

    if (len(responses) == len(satisfaction_survey.questions)): ## this is to trigger the complete page - so if the length of the responses (should be 4) is the same as the number of questions in the survey questions we end the survey 
        return redirect("/complete") 
    else:
        return redirect(f"/questions/{len(responses)}") ## we can increment the value of the page with the length of response, each time the user answers a question it adds to the response list so we can use the length of that list to go to the next page


@app.route("/complete")
def complete():
    return render_template("complete.html")