
Feature: Sign In Tests

Scenario: open Login Page
  Given user is on "MainPage"
  When user clicks on "SignIn"
  Then user checks he is on "SigninPage"
  And user sees element "SignIn button"

Scenario: user fails to sign in
  Given user is on "SigninPage"
  When user types "test_username" in "Username"
  And user types "test_password" in "Password"
  And user clicks on "SignIn button"
  Then user sees text "Incorrect username or password." in "Error message"