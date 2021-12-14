Feature: Test
    Scenario: Test Builder
      Given Technic_Builder
      When test_Mvideo_builder return OK
      And test_DNS_builder return OK
      Then Good job