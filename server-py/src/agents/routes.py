from extensions import mongo, client
from agents import agents
from flask import Flask, render_template, request, url_for, redirect


@agents.route('/agent_one', methods=('GET', 'POST'))
def index():

    if request.method=='POST':

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": request.form['content']
                }
            ]
        )

        content = completion.choices[0].message.content
        mongo.db.responses.insert_one({'content': content})
        return redirect(url_for('agents.index'))

    all_responses = mongo.db.responses.find()
    return render_template('agents.html', responses=all_responses)

@agents.route('/responses', methods=('GET', 'POST'))
def result():
    all_responses = mongo.db.responses.find()
    return render_template('agents.html', responses=all_responses)