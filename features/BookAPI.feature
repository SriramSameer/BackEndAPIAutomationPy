# Created by vtadimet at 04-08-2023
Feature: Verify if books are added and deleted using Library API

  @library
  Scenario: Verify AddBook API functionality
    Given the Book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then the book is successfully installed
    And  status code of response should be 200


  @library
  Scenario Outline: Verify AddBook API functionality
    Given the Book details with <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then the book is successfully installed
    Examples:
      |isbn  |aisle|
      |fdfee |8948
      |powr  |76333
