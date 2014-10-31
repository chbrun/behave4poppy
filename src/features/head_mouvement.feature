# language: en
Feature: Head mouvements

    Scenario: Move the head
        Given Poppy initialisation
        When Poppy turns head to the left "45"
        Then waiting 2s
        When Poppy turns head to the right "45"
        Then waiting 2s

