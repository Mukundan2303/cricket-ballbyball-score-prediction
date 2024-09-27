import streamlit as st
import pickle
import numpy as np

# Load the Random Forest Classifier model from the .sav file
filename = 'first-innings-score-lr-model.sav'
with open(filename, 'rb') as file:
    regressor = pickle.load(file)

# Streamlit app
st.title('IPL Score Predictor')

# User inputs
batting_team = st.selectbox('Select Batting Team', 
                            ['Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 
                             'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals', 
                             'Royal Challengers Bangalore', 'Sunrisers Hyderabad'])

bowling_team = st.selectbox('Select Bowling Team', 
                            ['Chennai Super Kings', 'Delhi Daredevils', 'Kings XI Punjab', 
                             'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals', 
                             'Royal Challengers Bangalore', 'Sunrisers Hyderabad'])

overs = st.number_input('Overs Completed', min_value=0.0, max_value=20.0, step=0.1)
runs = st.number_input('Runs Scored', min_value=0)
wickets = st.number_input('Wickets Lost', min_value=0, max_value=10)
runs_in_prev_5 = st.number_input('Runs Scored in Previous 5 Overs', min_value=0)
wickets_in_prev_5 = st.number_input('Wickets Lost in Previous 5 Overs', min_value=0, max_value=10)

# Encoding the inputs similar to how it was done in the Flask app
temp_array = []

if batting_team == 'Chennai Super Kings':
    temp_array = [1,0,0,0,0,0,0,0]
elif batting_team == 'Delhi Daredevils':
    temp_array = [0,1,0,0,0,0,0,0]
elif batting_team == 'Kings XI Punjab':
    temp_array = [0,0,1,0,0,0,0,0]
elif batting_team == 'Kolkata Knight Riders':
    temp_array = [0,0,0,1,0,0,0,0]
elif batting_team == 'Mumbai Indians':
    temp_array = [0,0,0,0,1,0,0,0]
elif batting_team == 'Rajasthan Royals':
    temp_array = [0,0,0,0,0,1,0,0]
elif batting_team == 'Royal Challengers Bangalore':
    temp_array = [0,0,0,0,0,0,1,0]
elif batting_team == 'Sunrisers Hyderabad':
    temp_array = [0,0,0,0,0,0,0,1]

if bowling_team == 'Chennai Super Kings':
    temp_array += [1,0,0,0,0,0,0,0]
elif bowling_team == 'Delhi Daredevils':
    temp_array += [0,1,0,0,0,0,0,0]
elif bowling_team == 'Kings XI Punjab':
    temp_array += [0,0,1,0,0,0,0,0]
elif bowling_team == 'Kolkata Knight Riders':
    temp_array += [0,0,0,1,0,0,0,0]
elif bowling_team == 'Mumbai Indians':
    temp_array += [0,0,0,0,1,0,0,0]
elif bowling_team == 'Rajasthan Royals':
    temp_array += [0,0,0,0,0,1,0,0]
elif bowling_team == 'Royal Challengers Bangalore':
    temp_array += [0,0,0,0,0,0,1,0]
elif bowling_team == 'Sunrisers Hyderabad':
    temp_array += [0,0,0,0,0,0,0,1]

temp_array += [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]

# Convert list to numpy array
data = np.array([temp_array])

# Predict and display the result
if st.button('Predict Score'):
    my_prediction = int(regressor.predict(data)[0])
    st.write(f"Predicted Score Range: {my_prediction-10} to {my_prediction+5}")