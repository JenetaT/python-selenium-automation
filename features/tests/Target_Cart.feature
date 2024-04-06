# Created by jeneta at 4/6/24
Feature: Target Cart
  # Enter feature description here

  Scenario: User can verify cart contents
    Given Open Target main page
    When Click on Cart icon
    Then  Verify “Your cart is empty” message is shown