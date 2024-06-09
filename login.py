import streamlit as st

username = "test"
password = "123"

def validate_login(user, pwd):
  """Dummy function to accept user input (not recommended for real-world use)"""
  return user == username and pwd == password

def main():
  """Displays the login form and handles user interaction."""
  st.title("Login Page")

  form = st.form(key="login_form")
  username = form.text_input(label="Username")
  password = form.text_input(label="Password", type="password")
  submit_button = form.form_submit_button(label="Login")

  if submit_button:
    if validate_login(username, password):
      st.success("Login successful!")
      # Add logic to redirect to a different page after successful login
    else:
      st.error("Invalid username or password.")

if __name__ == "__main__":
  main()
