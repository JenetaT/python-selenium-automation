Feature: Target Cart

  Scenario: User can verify cart contents
    Given Open Target main page
    When Click on Cart icon
    Then  Verify “Your cart is empty” message is shown

  Scenario: User can add product into cart
    Given Open Target main page
    When Search for towels
    When Add item to cart
    Then Navigate to cart page
    Then Verify item in cart
