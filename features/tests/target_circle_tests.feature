Feature: Tests for target Circle page

  Scenario: Open Target Circle page
    Given Open Target Circle page
    Then  Verify circle page opened

  Scenario: Verify correct benefit cells
    Given Open Target Circle Page
    Then Verify page has 10 benefit cells

