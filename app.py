import flask
import pickle
import pandas as pd
# Use pickle to load in the pre-trained model.
with open(f'model/mlp_model.pkl', 'rb') as f:
    model = pickle.load(f)
app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main.html'))

    if flask.request.method == 'POST':
        # Extract the input
        temperature_max = flask.request.form['temperature_max']
        temperature_min = flask.request.form['temperature_min']
        avg_humidity = flask.request.form['avg_humidity']
        ss = flask.request.form['ss']

        # Make DataFrame for model
        input_variables = pd.DataFrame([[temperature_max, temperature_min, avg_humidity, ss]],
                                       columns=['Tx', 'Tn',
                                                'RH_avg', 'ss'],
                                       dtype=float,
                                       index=['input'])

        # Get the model's prediction
        prediction = model.predict(input_variables)[0]

        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('main.html',
                                     original_input={'Temperature Maximum': temperature_max,
                                                     'Temperature Minimum': temperature_min,
                                                     'Average Humidity': avg_humidity,
                                                     'ss': ss},
                                     result=prediction,
                                     )


if __name__ == '__main__':
    app.run()
