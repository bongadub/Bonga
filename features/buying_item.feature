@order
Feature: Buying an item

  Scenario: Process of buying an item
    Given the log in page is open
     When the user logs in with username "bongadubula@gmail.com" and password "bonga"
     Then the user hovers over women section

    Given the user clicks on Tops
     When the user add an item to a shopping cart
     Then the user clicks proceed to checkout

    Given the user goes to shopping summary page
     When the user goes to address verification page
     Then the user clicks agree on terms check button

    Given the user goes to shipping page
     When the user must choose payment method
     Then the user must confirm order