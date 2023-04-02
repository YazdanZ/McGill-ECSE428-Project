# Feature: Re-use previously created locations as starting points or destinations for trips

# Scenario Outline: User creates trip with previously created locations
# Given The user has an account with mcgill_id 1 already in the database
# And The user has already created one or more trips
# When The create trip page is opened with the user's mcgill_id parameter passed as a URL parameter
# Then two dropdown menus are displayed
# And the possible values for the dropdowns include the addresses associated with the user's previously created trips
# When the user selects two different previously created addresses for both dropoff and pickup
# And the user enters a valid value into the total distance field
# And The user presses the submit button
# Then The user gets a notification message stating a new trip was created

# Scenario Outline: User attempts to create trip with one or more invalid location selections
# Given The user has an account with mcgill_id 1 already in the database
# When The create trip page is opened with the user's mcgill_id parameter passed as a URL parameter
# Then two dropdown menus are displayed
# And the possible values for the dropdowns include the addresses associated with the user's previously created trips
# When the user does not make a valid selection for at least one of pickup and dropoff addresses
# And the user enters a valid value into the total distance field
# And The user presses the submit button
# Then The user gets a notification message stating one of the locations was not selected

# Scenario Outline: User attempts to create trip with the same location selections for dropoff and pickup
# Given The user has an account with mcgill_id 1 already in the database
# And The user has already created one or more trips
# When The create trip page is opened with the user's mcgill_id parameter passed as a URL parameter
# Then two dropdown menus are displayed
# And the possible values for the dropdowns include the addresses associated with the user's previously created trips
# When the user selects the same previously created address for both dropoff and pickup
# And the user enters a valid value into the total distance field
# And The user presses the submit button
# Then The user gets a notification message stating the pickup and dropoff addresses must be different