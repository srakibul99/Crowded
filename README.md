# Crowded

Struggling to move the folders to be more readable/organized, but the goal is to have 2 folders:
1. website
    - website.py
    - .idea
    - templates
    - static
    - venv
    - .DS_Store
  
2. ios app
    - Crowded
    - CrowdedUITests
    - CrowdedTests
    - Crowded.xcodeproj
    
###

Our website is built with Python (and Flask), HTML, and CSS. It's a basic website that takes in user input on Location/query, as well the user's time and weekday that they are using the application, in order to make Foursquare API calls to find venues nearby that match the query. The user will then see the crowdedness/business of that venue.

Our ios app is in an earlier stage of development. It uses Swift in order to similarly take user input for Location/query and makes Foursquare API calls to find 3 venues nearby that match the input. The crowdedness of the venue is still in development, as well as other features we may add to the iOS app (such as a map view).
