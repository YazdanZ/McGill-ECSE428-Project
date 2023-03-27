Feature: Create Trip as a Driver with pick-up and drop-off address

  Scenario Outline: Create New Trip as a Driver with valid information (Normal Flow)
    Given The Driver is logged in to their drivers account with <email> and <password>
     When The Driver enters their <pick-up-address-line-1>
      And The Driver enters their <pick-up-address-city>
      And The Driver enters their <pick-up-address-postal-code>
      And The Driver enters their <drop-off-address-line-1>
      And The Driver enters their <drop-off-address-city>
      And The Driver enters their <drop-off-address-postal-code>
      And The Driver enters their total <distance> covered in their trip
     Then The Driver gets a notification message stating "New Trip Created"
    Examples:
      | email                      | password  | pick-up-address-line-1 | pick-up-address-city | pick-up-address-postal-code | drop-off-address-line-1 | drop-off-address-city | drop-off-address-postal-code | distance |
      | mihir.kumar@mail.mcgill.ca | anshul123 | 5678 Stanley Street    | Montreal             | H2FC7T                      | 3440 Parc Avenue        | Laval              | H2XB3B                       | 30       |
     # | mihiranshul@gmail.com      | mihir1234 | 3100 Peel Street       | Montreal             | H2XB3A                      | 1221 Drummond           | Montreal              | H1B6C5                       | 20       |

  Scenario Outline: Crete New Trip as a Driver with no distance covered information (Error Flow)
    Given The Driver is logged in to their drivers account with <email> and <password>
     When The Driver enters their <pick-up-address-line-1>
      And The Driver enters their <pick-up-address-city>
      And The Driver enters their <pick-up-address-postal-code>
      And The Driver enters their <drop-off-address-line-1>
      And The Driver enters their <drop-off-address-city>
      And The Driver enters their <drop-off-address-postal-code>
      And The Driver does not enter their total distance covered in their trip
     Then The Driver gets a notification message stating "Set a total distance."
    Examples:
      | email                      | password  | pick-up-address-line-1 | pick-up-address-city | pick-up-address-postal-code | drop-off-address-line-1 | drop-off-address-city | drop-off-address-postal-code |
      | mihir.kumar@mail.mcgill.ca | anshul123 | 5678 Stanley Street    | Montreal             | H2FC7T                      | 3440 Parc Avenue        | Laval              | H2XB3B                       |
     # | mihiranshul@gmail.com      | mihir1234 | 3440 Parc Avenue       | Montreal             | H2XB3A                      | 1221 Drummond           | Montreal              | H1B6C5                       |

  Scenario Outline: Crete New Trip as a Driver with no pick up address line 1 information (Error Flow)
    Given The Driver is logged in to their drivers account with <email> and <password>
     When The Driver does not enter their pick up address line 1
      And The Driver enters their <pick-up-address-city>
      And The Driver enters their <pick-up-address-postal-code>
      And The Driver enters their <drop-off-address-line-1>
      And The Driver enters their <drop-off-address-city>
      And The Driver enters their <drop-off-address-postal-code>
      And The Driver enters their total <distance> covered in their trip
     Then The Driver gets a notification message stating "Add Pick up Address Line"
    Examples:
      | email                      | password  | pick-up-address-city | pick-up-address-postal-code | drop-off-address-line-1 | drop-off-address-city | drop-off-address-postal-code | distance |
      | mihir.kumar@mail.mcgill.ca | anshul123 | Montreal             | H2FC7T                      | 3440 Parc Avenue        | Laval              | H2XB3B                       | 30       |
  #    | mihiranshul@gmail.com      | mihir1234 | Montreal             | H2XB3A                      | 1221 Drummond           | Montreal              | H1B6C5                       | 20       |

  Scenario Outline: Crete New Trip as a Driver with no pick up address city information (Error Flow)
    Given The Driver is logged in to their drivers account with <email> and <password>
     When The Driver enters their <pick-up-address-line-1>
      And The Driver does not enter their pick up address city
      And The Driver enters their <pick-up-address-postal-code>
      And The Driver enters their <drop-off-address-line-1>
      And The Driver enters their <drop-off-address-city>
      And The Driver enters their <drop-off-address-postal-code>
      And The Driver enters their total <distance> covered in their trip
     Then The Driver gets a notification message stating "Add Pick up City"
    Examples:
      | email                      | password  | pick-up-address-line-1 | pick-up-address-postal-code | drop-off-address-line-1 | drop-off-address-city | drop-off-address-postal-code | distance |
      | mihir.kumar@mail.mcgill.ca | anshul123 | 5678 Stanley Street    | H2FC7T                      | 3440 Parc Avenue        | Laval              | H2XB3B                       | 30       |
   #   | mihiranshul@gmail.com      | mihir1234 | 3440 Parc Avenue       | H2XB3A                      | 1221 Drummond           | Montreal              | H1B6C5                       | 20       |

  Scenario Outline: Crete New Trip as a Driver with no pick up address postal code information (Error Flow)
    Given The Driver is logged in to their drivers account with <email> and <password>
     When The Driver enters their <pick-up-address-line-1>
      And The Driver enters their <pick-up-address-city>
      And The Driver does not enter their pick up address postal code
      And The Driver enters their <drop-off-address-line-1>
      And The Driver enters their <drop-off-address-city>
      And The Driver enters their <drop-off-address-postal-code>
      And The Driver enters their total <distance> covered in their trip
     Then The Driver gets a notification message stating "Add Pick up Postal Code"
    Examples:
      | email                      | password  | pick-up-address-line-1 | pick-up-address-city | drop-off-address-line-1 | drop-off-address-city | drop-off-address-postal-code | distance |
      | mihir.kumar@mail.mcgill.ca | anshul123 | 5678 Stanley Street    | Montreal             | 3440 Parc Avenue        | Laval              | H2XB3B                       | 30       |
  #    | mihiranshul@gmail.com      | mihir1234 | 3440 Parc Avenue       | Montreal             | 1221 Drummond           | Montreal              | H1B6C5                       | 20       |

  Scenario Outline: Crete New Trip as a Driver with no drop off address line 1 information (Error Flow)
    Given The Driver is logged in to their drivers account with <email> and <password>
     When The Driver enters their <pick-up-address-line-1>
      And The Driver enters their <pick-up-address-city>
      And The Driver enters their <pick-up-address-postal-code>
      And The Driver does not enter their drop off address line 1
      And The Driver enters their <drop-off-address-city>
      And The Driver enters their <drop-off-address-postal-code>
      And The Driver enters their total <distance> covered in their trip
     Then The Driver gets a notification message stating "Add Drop off Address Line"
    Examples:
      | email                      | password  | pick-up-address-line-1 | pick-up-address-city | pick-up-address-postal-code | drop-off-address-city | drop-off-address-postal-code | distance |
      | mihir.kumar@mail.mcgill.ca | anshul123 | 5678 Stanley Street    | Montreal             | H2FC7T                      | Laval              | H2XB3B                       | 30       |
  #    | mihiranshul@gmail.com      | mihir1234 | 3440 Parc Avenue       | Montreal             | H2XB3A                      | Montreal              | H1B6C5                       | 20       |

  Scenario Outline: Crete New Trip as a Driver with no drop off address city information (Error Flow)
    Given The Driver is logged in to their drivers account with <email> and <password>
     When The Driver enters their <pick-up-address-line-1>
      And The Driver enters their <pick-up-address-city>
      And The Driver enters their <pick-up-address-postal-code>
      And The Driver enters their <drop-off-address-line-1>
      And The Driver does not enter their drop off address city
      And The Driver enters their <drop-off-address-postal-code>
      And The Driver enters their total <distance> covered in their trip
     Then The Driver gets a notification message stating "Add Drop off City"
    Examples:
      | email                      | password  | pick-up-address-line-1 | pick-up-address-city | pick-up-address-postal-code | drop-off-address-line-1 | drop-off-address-postal-code | distance |
      | mihir.kumar@mail.mcgill.ca | anshul123 | 5678 Stanley Street    | Montreal             | H2FC7T                      | 3440 Parc Avenue        | H2XB3B                       | 30       |
   #   | mihiranshul@gmail.com      | mihir1234 | 3440 Parc Avenue       | Montreal             | H2XB3A                      | 1221 Drummond           | H1B6C5                       | 20       |

  Scenario Outline: Crete New Trip as a Driver with no drop off address postal code information (Error Flow)
    Given The Driver is logged in to their drivers account with <email> and <password>
     When The Driver enters their <pick-up-address-line-1>
      And The Driver enters their <pick-up-address-city>
      And The Driver enters their <pick-up-address-postal-code>
      And The Driver enters their <drop-off-address-line-1>
      And The Driver enters their <drop-off-address-city>
      And The Driver does not enter their drop off address postal code
      And The Driver enters their total <distance> covered in their trip
     Then The Driver gets a notification message stating "Add Drop off Postal Code"
    Examples:
      | email                      | password  | pick-up-address-line-1 | pick-up-address-city | pick-up-address-postal-code | drop-off-address-line-1 | drop-off-address-city | distance |
      | mihir.kumar@mail.mcgill.ca | anshul123 | 5678 Stanley Street    | Montreal             | H2FC7T                      | 3440 Parc Avenue        | Laval              | 30       |
  #    | mihiranshul@gmail.com      | mihir1234 | 3440 Parc Avenue       | Montreal             | H2XB3A                      | 1221 Drummond           | Montreal              | 20       |


