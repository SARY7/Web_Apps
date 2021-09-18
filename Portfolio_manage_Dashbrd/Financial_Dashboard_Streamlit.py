import streamlit as st
# import yfinance as yf
import pandas as pd

# st.set_page_config(layout="centered")
#
# def Signinpage():
#     st.title("Welcome back, please Log In")
#
#     signin_menu = ["SignIn", "SignUp"]
#     signin_select = st.sidebar.selectbox("SignIn menu", signin_menu)
#
#     if signin_select == "SignIn":
#         st.sidebar.subheader("SignIn to your account:")
#
#         username = st.sidebar.text_input("User Name")
#         password = st.sidebar.text_input("Password", type='password')
#         if st.sidebar.button("SignIn"):
#             if password == "12345":
#                 st.success("Hi {}, its great to have you back :)".format(username))
#             else:
#                 st.warning("Oops, the username/password is incorrect :( , try again.")
#
#     elif signin_select == "SignUp":
#         st.subheader("Create your new account:")
#
#
# # if __name__ == '__Signinpage__':
# Signinpage()

# st.title("Let's create a table!")
# for i in range(1, 10):
#     cols = st.beta_columns(4)
#     cols[0].write(f'{i}')
#     cols[1].write(f'{i * i}')
#     cols[2].write(f'{i * i * i}')
#     cols[3].write('x' * i)

col1, col2, col3, col4 = st.columns(4)
# You can use a column just like st.sidebar:
col1.button('Press me!')
col1.button('Press again')

col2.checkbox('Press me')




# col1, col2 = st.beta_columns(2)
# original = Image.open("https://static.dw.com/image/51817152_303.jpg")
# col1.header("Original")
# col1.image(original, use_column_width=True)
# grayscale = original.convert('LA')
# col2.header("Grayscale")
# col2.image(grayscale, use_column_width=True)

# with col2:
#    something in row1..
#
# with col1:
#   something in row2..
#
# with col2:
#    something in row2..

# st.title('Portfolio Management Dashboard')
#
# ticker = ('BTC-USD', 'ETH-USD')
#
# dropdown = st.multiselect('Pick your assets', ticker)
#
# start = st.date_input('Start', value=pd.to_datetime('2021-09-09'))
# end = st.date_input('End', value=pd.to_datetime('today'))
#
# # if len(dropdown) > 0:
# #     df = yf.download(dropdown, start, end)['Adlj Close']
# #     st.line_chart(df)
#
# """
# # header
# """
#
# options = st.selectbox("which", ("hi", "car"))
#
# if options == "car":
#     st.image("https://static.dw.com/image/51817152_303.jpg")
#
# st.sidebar.title("t")
# choose = st.sidebar.write("test")
#
# sidechoose = st.sidebar.selectbox("which", ("hi", "car", "selecr"))
#
# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)
#
