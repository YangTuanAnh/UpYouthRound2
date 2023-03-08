import openai

summary = """Write a 1000-word summary: 
---
{input}
---
This is the summary: """

quiz = """Generate 3 multiple-choice questions for the content below.

The response must be returned with each answer being in a seperate line, and each answer for every question is also its own seperate line. Remember to add a space before the line break character.

There should be one correct answer and 3 incorrect answers. The incorrect answers should be response options that a candidate with incomplete knowledge or skill might choose. 

Provide an explanation for the answer to each question as well. The question must be about a scenario, and not a simple definition question such as What type of storage is Amazon S3. 

The answers must also be action-oriented and not just the name of a concept.

The content:
---
{input}
---
This is the quiz:"""

def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key

class GeneralModel:
    def __init__(self):
        print("Model Intilization--->")
        # set_openai_key(API_KEY)

    def query(self, prompt, myKwargs={}):
        """
        wrapper for the API to save the prompt and the result
        """

        # arguments to send the API
        kwargs = {
            "engine": "text-davinci-002",
            "temperature": 0.85,
            "max_tokens": 600,
            "best_of": 1,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            "stop": ["###"],
        }


        for kwarg in myKwargs:
            kwargs[kwarg] = myKwargs[kwarg]


        r = openai.Completion.create(prompt=prompt, **kwargs)["choices"][0][
            "text"
        ].strip()
        return r

    def model_prediction(self, input, api_key):
        """
        wrapper for the API to save the prompt and the result
        """
        # Setting the OpenAI API key got from the OpenAI dashboard
        set_openai_key(api_key)
        output = (self.query(summary.format(input = input)), self.query(quiz.format(input = input)))
        return output