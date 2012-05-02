Feature:
  In order to use more the console
  I want to colorize the output of any command

  Scenario Outline: Basic execution
    When I use as stdin "<input>"
    Then it should pass
    And output is "<output>"

    Examples:
    | input        | output    |
    | example      | example   |
    | failure      | failure   |
    | FAILURE      | \x1b[0;37;41mFAILURE\x1b[m   |
