# securin-project
Part A: Solution Documentation - The Doomed Dice Challenge

Introduction
Welcome to our solution for the Doomed Dice Challenge! Imagine you have two regular dice with numbers 1 through 6 on each side. Ever wondered what happens when you roll them together? That's exactly what we're exploring here! We'll see what combinations pop up and how often certain results occur. Let's roll the dice and find out! I used Flask, Python, HTML, and CSS to make a fun web app for the Doomed Dice Challenge. Flask handles the behind-the-scenes work, HTML shows our calculations like total combinations, CSS makes it look nice, and everything updates instantly as you interact with it. It's a cool way to explore how rolling two dice can lead to different outcomes!
 
Problem Statement
The challenge involves working with two six-sided dice, labeled Die A and Die B, each numbered from 1 to 6. When both dice are rolled simultaneously, their totals can range from 2 to 12, depending on the sum of their faces. The task is to analyze the various aspects of these dice rolls:
1. Total Combinations:
   Calculate the total number of combinations possible when rolling both Die A and Die B together.
2. Distribution of Combinations:
   Generate a 6x6 matrix representing all possible combinations of rolls from Die A and Die B.
3. Frequency of Sums:
   Determine the frequency of each possible sum that can result from rolling both dice.
4. Probability of Sums
   Calculate the probability of each sum occurring, based on the frequency of each sum and the total number of combinations.

 Solution Overview
To address the Doomed Dice Challenge, we will proceed with the following approach:

1. Total Combinations:
   We will first calculate the total number of combinations possible when rolling both Die A and Die B together. This will be achieved by multiplying the number of faces on each die.
2. Distribution of Combinations:
   Next, we will generate a 6x6 matrix representing all possible combinations of rolls from Die A and Die B. Each cell in the matrix will contain a tuple representing a combination of results from both dice.
3. Frequency of Sums:
   After establishing the distribution of combinations, we will determine the frequency of each possible sum that can result from rolling both dice. This will involve iterating over each combination in the matrix and updating the frequency of the corresponding sum.
4. Probability of Sums:
   With the frequency of sums identified, we will proceed to calculate the probability of each sum occurring. This will be accomplished by dividing the frequency of each sum by the total number of combinations.
By following this approach, we aim to gain insights into the distribution of outcomes and the likelihood of various sums when rolling two dice together. This comprehensive analysis will provide a deeper understanding of the probabilities associated with the Doomed Dice Challenge.
Mathematical Analysis
1. Total Combinations
   The total number of combinations possible when rolling both Die A and Die B together can be calculated by multiplying the number of faces on each die. Since each die has 6 faces, the total combinations will be 
6*6=36
2. Distribution of Combinations:
   To generate the distribution of combinations, we create a 6x6 matrix where each cell represents a combination of results from Die A and Die B. This matrix will have 36 cells in total, covering all possible combinations.

3.  Frequency of Sums
   After generating the combinations matrix, we iterate over each cell to calculate the sum of the results from Die A and Die B. By tallying the frequency of each sum, we determine how often each possible sum occurs when rolling both dice.
4. Probability of Sums
   The probability of each sum occurring is calculated by dividing the frequency of each sum by the total number of combinations. This provides insight into the likelihood of obtaining each sum when rolling two dice together.
By performing this mathematical analysis, we gain a quantitative understanding of the distribution of outcomes and the probabilities associated with the Doomed Dice Challenge. These calculations enable us to draw meaningful conclusions and make informed decisions based on the results.
Implementation
•	Total Combinations Calculation (totalcomb()):  This function calculates the total number of combinations when rolling two six-sided dice. It returns the result of multiplying 6 (the number of faces on each die) by 6.
•	Combinations Matrix Generation (combmat()): Here, we generate a matrix representing all possible combinations of rolling Die A and Die B together. Each cell in the matrix contains a pair of numbers representing a possible outcome from rolling both dice.
•	Frequency of Sums Calculation (cal(combm)): In this function, we determine how often each possible sum appears when rolling both dice. We go through each combination in the matrix, calculate the sum of the numbers on the dice, and count how many times each sum occurs.
•	Probability of Sums Calculation (prob(f, total)):  This function calculates the probability of each sum occurring. By dividing the frequency of each sum by the total number of combinations, we get the probability of rolling each sum.
•	Main Function Execution (main()): The main function puts everything together. It calculates the total combinations, generates the combinations matrix, calculates the frequency of sums, determines the probability of each sum, and prints out the results.

 

Result 


 
 

Conclusion
In summary, our web app built with Flask, Python, HTML, and CSS offers a fun way to explore rolling two dice. It's easy to use and shows the chances of getting different outcomes. With real-time updates and a user-friendly design, it's a great tool for understanding dice probabilities.











 Part B: Solution Documentation – Transform Dice Challenge
Introduction
Welcome to the Doomed Dice Challenge, a thrilling journey where we confront the whimsical antics of the Norse God Loki! Picture yourself leisurely enjoying a board game afternoon, rolling dice with excitement, when suddenly, Loki appears with a mischievous grin. In a playful twist, he strips the dice of their spots, leaving you in a predicament. But fear not! Armed with Python, Flask, HTML, and CSS, we're equipped to tackle Loki's challenge head-on.
 
Problem Statement
In the Doomed Dice Challenge, two regular dice, Die A and Die B, have had their spots removed by Loki. Our task is to reattach the spots while ensuring:
1. Die A has no more than 4 spots per face.
2. Die B can have any number of spots on a face.
3. The probabilities of different sums when rolling the dice remain unchanged.
Objective
Develop a function, undoom_dice, that takes initial configurations of Die A and Die B and outputs updated configurations meeting Loki's conditions while preserving sum probabilities.
Input
Initial configurations of Die A (Die_A) and Die B (Die_B): Lists of integers representing spot counts on each face.

Output
Updated configurations of Die A (New_Die_A) and Die B (New_Die_B) satisfying the conditions.
Constraints
•	Die_A and Die_B are both of length 6.
•	Each element in Die_A and Die_B is an integer (1 to 6).
This challenge tests our ability to balance constraints and probabilities to restore the dice to their original state, thwarting Loki's mischief.
 Solution Overview
This solution explores different combinations of spots for two dice, A and B, to find a transformation that satisfies Loki's conditions and preserves the original probabilities of obtaining different sums when rolling the dice.
1. Finding Probabilities
   Calculate how likely it is to get each sum when rolling the original dice A and B together.
2. Checking Combinations
   Generate all possible combinations of spots for dice A and B, making sure that dice A has no more than 4 spots on any face.
3. Main Logic
Go through each combination of spots for dice A and B. If a combination preserves the original probabilities, print the transformed configurations for dice A and B.
4. Output
   Find a suitable transformation and print the new configurations for dice A and B. If not, indicate that no transformations were found. 
This approach systematically explores combinations to solve the Doomed Dice Challenge, demonstrating a methodical way to handle complex problems.
Mathematical Analysis
In the approach to the Doomed Dice Challenge, reliance is placed on several key mathematical principles. Here's a simplified breakdown:



1. Counting Possibilities
   The initial step involves determining the various ways to achieve each possible total when rolling two dice. This encompasses examining all potential combinations of spots on each die.
2. Checking Combinations
   Subsequently, experimentation with different spot configurations for the two dice is conducted. Adherence to Loki's rule, limiting one die to no more than 4 spots on any face, is ensured.
3. Comparing Probabilities
   Each attempted combination is evaluated to ascertain whether it maintains the original probabilities. The objective is to retain the likelihood of rolling each total, notwithstanding alterations to the dice spots.
4. Considering Complexity
   Assessment of the solution's computational complexity is imperative. This evaluation hinges on the number of combinations requiring scrutiny and the dice's side count.
5. Improving Efficiency
   Strategies for enhancing solution efficiency are explored to minimize unnecessary computations. The aim is to expedite the identification of the optimal spot combination.
Implementation
The implementation part of the solution involves putting the defined functions into action. It includes:
1. Calculating Probabilities
   Utilizing the `findprobs` function to determine the probabilities of obtaining different sums when rolling two dice. This function takes the spot configurations of dice A and B as input and returns a dictionary containing the probabilities of each sum.
2. Checking Combination Preservation
   Employing the `check` function to verify whether a combination of spots for dice A and B preserves the original probabilities. This function compares the probabilities of a given combination with the probabilities of the original dice configuration.
 
3. Generating Combinations
   Using the `combb`   and  `comba`  function to generate all possible combinations of spots for dice B. This function takes a list of spots for dice B and the number of sides on dice B as input and returns a list of all possible combinations.
 
4. Transformation part
The `partb` function seeks a valid transformation for both dice A and B while maintaining the original probabilities. It begins by setting up initial configurations for the dice and generating all possible combinations of spots. Subsequently, it calculates the probabilities for different sums based on the initial dice setups. The function then systematically examines each combination, ensuring it preserves the original probabilities. Upon finding a suitable transformation, it prepares the altered configurations for presentation in an HTML template. This meticulous process ensures the integrity of the dice transformations by upholding the original probabilities.
 
This comprehensive approach guarantees the reliability of the dice transformation process, maintaining the integrity of the original probabilities.

Result
 
Conclusion
In conclusion, our solution ensures that dice A and B can be transformed while keeping the original probabilities intact. This means you can modify the dice configurations without changing the likelihood of getting different sums when rolling them together. It's a reliable and accurate way to handle dice transformations, ensuring fair gameplay.
