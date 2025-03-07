import streamlit as st

# UI
st.title('🌟Unit Converter App 🌟')
st.markdown('## Converts Lenght,Weight,Temperature, And Time Instantly ')
st.write('Welcome! Select a category, enter a value and get the converted result in instantly')

category = st.selectbox('Choose a category', ['Lenght','Weight','Temperature','Time'])

def convert_units(category,value,unit):
    if category == 'Lenght':
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
    elif category == 'Weight' :
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == 'Pounds to Kilograms' :
            return value / 2.20462
    elif category == 'Temperature' :
        if unit == 'Celsius to Fahrenheit':
            return (value * 9/5 ) + 32   
        elif unit == 'Fahrenheit to Celsius':
            return (value - 32) * 5/9              
    elif category == 'Time':
        if unit == 'Seconds to Minutes':
            return value / 60
        elif unit == 'Minutes to Seconds':
            return value * 60
        elif unit == 'Minutes to Hours' :
            return value / 60
        elif unit == 'Hours to Minutes':
            return value * 60  
        elif unit == 'Hours to Days':
            return value / 24
        elif unit == 'Days to Hours':
            return value * 24

if category == "Lenght":
    unit = st.selectbox('📏 Slect Conversation', ['Kilometers to Miles','Miles to Kilometers'])
elif category == "Weight":
    unit = st.selectbox('⚖ Slect Conversation', ['Kilograms to Pounds','Pounds to Kilograms']) 
elif category == 'Temperature':
    unit = st.selectbox('🌡️Slect Conversation',['Celsius to Fahrenheit','Fahrenheit to Celsius'])    
elif category == "Time":
    unit = st.selectbox ('⏲ Slect Conversation', ['Seconds to Minutes','Minutes to Seconds','Minutes to Hours','Hours to Minutes','Hours to Days','Days to Hours'])       

value = st.number_input('Enter the value') 

if st.button('Convert'):
    result = convert_units(category, value,unit)
    st.success(f'{category} {value} = {result:.2f}  {unit}')