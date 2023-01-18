# import the streamlit library
import streamlit

#adding a title to the page
streamlit.title('My Parents New Healthy Diner')

# adding a header to the page
streamlit.header('Breakfast Menu')
# adding text under the heading
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

# adding another header to the page
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# importing the pandas library
import pandas
# defining a variable my_fruit_list and reading csv using pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# setting variable index to the field in csv fruit
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
# define variable fruits_selected , multiselect option added and list
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# loc function label-based specifies the field to be filtered by (based on a selection)
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# new section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")

# importing the python requests library
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# tabulate the pandas response & stored it as a variable 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# push it out as a dataframe in a table
streamlit.dataframe(fruityvice_normalized)
