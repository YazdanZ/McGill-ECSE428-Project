# # -- FILE: features/Create_Trip.feature

# Feature: Create Trip as a Driver

#   Scenario Outline: Create New Trip as a Driver with valid information (Normal Flow)
#     Given The Driver is logged in to their drivers account with <email> and <password>
#     When The Driver enters their total <distance> covered in their trip
#     Then The Driver gets a notification message stating "New Trip Created"
#     Examples:
#       | email | password | distance |
#     |mihiranshul@gmail.com|name123|20|
#     |mihir.kumar@yahoo.com|age456 |30|
#     |kumarsingh56@hotmail.com|animal22|10|

#   Scenario Outline: Crete New Trip as a Driver with no distance covered information (Error Flow)
#     Given The Driver is logged in to their drivers account with <email> and <password>
#     When The Driver does not enter their total distance covered in their trip
#     Then The Driver gets a notification message stating "Add Distance covered"
#     Examples:
#       | email | password |
#     |mihiranshul@gmail.com|name123|
#     |mihir.kumar@yahoo.com|age456 |


