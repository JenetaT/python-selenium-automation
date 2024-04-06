# Created by jeneta at 4/6/24
Feature: Sign in
  # Enter feature description here

  Scenario: Logged out user can sign in
    Given Open Target main page
    When Click Sign In
    Then  Verify Sign in form opened