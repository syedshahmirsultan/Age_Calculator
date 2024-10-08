import streamlit as st

st.title("Shahmir Age Calculator")
st.write("     ")
#userAge is responsible for getting user age in years
userAge:int = st.number_input("Enter your age in years",step=1,min_value=1,max_value=150)
ageInMonths =  userAge*12
ageInDays =  userAge*365
ageInHours = userAge*365*24
ageInMins = userAge*365*24*60
ageInSecs = userAge*365*24*60*60

st.write("  ")
# When the user click on this it will give the result
if(st.button("Calculate")):
    
    st.success(f"""
               Your age in the following units : \n
               Years = {userAge} years \n
                Months = {ageInMonths} months \n
                 Days = {ageInDays} days \n
                 Hours = {ageInHours} hours \n
                 Minutes = {ageInMins} mins \n
                 Seconds = {ageInSecs} seconds""")