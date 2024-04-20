Feature: Target Cart

  Scenario: User can verify cart contents
    Given Open Target main page
    When Click on Cart icon
    Then  Verify “Your cart is empty” message is shown

  Scenario: User can add product into cart
    Given Open Target main page
    When Search for towels
    And Click on Add to Cart button
    And store product name
    And Confirm Add to cart button from side nav
    Then Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product
