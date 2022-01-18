## Phillies Questionnaire

This repo contains my responses to the Phillies' questionnaire for their 2021 internship.

### Question 1

The following Python function checks whether a string is a palindrome. Please explain, in 250 words or less, how you'd improve this code and why. We’re not looking for a simple one-line rewrite here - submissions will be graded based on the clarity by which you describe what the improvements are, and also WHY they should be made.

### Answer 1

Response can be found in ./palindrome.py

### Question 2

In baseball, a team can provide a departing free agent player with a qualifying offer: a one-year contract whose monetary value is the average of the 125 highest salaries from the past season. The player is free to reject it and sign with any other team, but his new team will have to forfeit a draft pick.

Use the provided dataset to write a program or application that determines the monetary value of the upcoming qualifying offer and displays the amount along with any other relevant information or visualizations to the user. Note that while the URL and general format of the data will be consistent, the data itself can change slightly with each page load, so make sure your code pulls the data each time it is run and expect the final result to change each time.

You should submit a link or file containing your response to the question, including all source code. The link or file should contain a README that contains clear, step-by-step instructions for how to run or access your response.

Submissions will be graded on accuracy, readability, reproducibility, error handling and presentation of the result to the user. Use of online resources such as Stack Overflow is encouraged, but please cite (by including a comment in your code with a link to the resource) any answers used and provide comments on your particular implementation if appropriate. Use of open-source/third-party libraries is encouraged.

Data: https://questionnaire-148920.appspot.com/swe/data.html

Tip: As is often the case, the data sometimes contains corrupted or malformed values. Do your best to handle these and feel free to ignore missing values, but make sure they don’t interfere with the calculation or presentation of the final result.

### Answer 2

To run my code and view my answer:

1. open this repository
2. install npm if not already installed
3. run `cd repo/qualifying-offer`
4. run `npm i`
5. run `npm run serve`
6. open up which ever localhost it starts on, usually: localhost:8080
7. click the `load data` button

Technologies used:

- [VueJS](https://cli.vuejs.org/)
- [Buefy](https://buefy.org/) for CSS
- [axios](https://axios-http.com/) and [cors-anywhere](https://www.npmjs.com/package/cors-anywhere#client) for web scrapping
- [vuex](https://vuex.vuejs.org/) for state management
