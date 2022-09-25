class Question:
    """Question on a questionnaire."""

    def __init__(self, question, choices=None, allow_text=False):
        """Create question (assume Yes/No for choices."""

        if not choices:
            choices = ["Yes", "No"]

        self.question = question
        self.choices = choices
        self.allow_text = allow_text

# to access the choices and 
# In : satisfaction_survey.questions[1].choices
# Out: ['Yes', 'No']


class Survey:
    """Questionnaire."""

    def __init__(self, title, instructions, questions):
        """Create questionnaire."""

        self.title = title
        self.instructions = instructions
        self.questions = questions


satisfaction_survey = Survey( ##satisfaction_survey is an instance of the Survey class
    "Customer Satisfaction Survey",
    "Please fill out a survey about your experience with us.",
    [
        Question("Have you shopped here before?"),
        Question("Did someone else shop with you today?"),
        Question("On average, how much do you spend a month on frisbees?", 
                ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to shop here again?"),
    ])

    #In: satisfaction_survey.title 
    #Out: 'Customer Satisfaction Survey'

    #In: satisfaction_survey.instructions
    #Out: 'Please fill out a survey about your experience with us.'

    #In: satisfaction_survey.questions
    #Out: [<__main__.Question at 0x10bbb3e80>,
    # <__main__.Question at 0x10bbb3d90>,
    # <__main__.Question at 0x10bbb3e20>,
    # <__main__.Question at 0x10bbb3dc0>]

    #In: satisfaction_survey.questions[0]
    #Out: <__main__.Question at 0x10bbb3e80>

    #In: satisfaction_survey.questions[0].question
    #Out: 'Have you shopped here before?'




personality_quiz = Survey(
    "Rithm Personality Test",
    "Learn more about yourself with our personality quiz!",
    [
        Question("Do you ever dream about code?"),
        Question("Do you ever have nightmares about code?"),
        Question("Do you prefer porcupines or hedgehogs?",
                 ["Porcupines", "Hedgehogs"]),
        Question("Which is the worst function name, and why?",
                 ["do_stuff()", "run_me()", "wtf()"],
                 allow_text=True),
    ]
)

surveys = {
    "satisfaction": satisfaction_survey,
    "personality": personality_quiz,
}