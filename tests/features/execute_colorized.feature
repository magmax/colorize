Feature:
  In order to use more the console
  I want to colorize the output of any command

  Scenario: Execute another command and render the output
    When I run colorize echo FAILURE
    Then it should pass
    And output is "\x1b[1;37;41mFAILURE\x1b[m"
