PROBLEM STATEMENT


Pizza Trent' is a famous Pizza shop. The shop is becoming increasingly known, and the number of
daily customers is increasing dramatically. Therefore, the shop manager asks you to help them by
developing an application to calculate every customer's purchase price. You need to write a PYTHON
program that computes the cost of purchasing pizza at Pizza Trent shop according to the following
purchasing rules.
The cost, of course, depends on the number of pizzas you buy. Suppose that the shop has
only four sizes of pizza; the following table gives the breakdown of the prices per pizza
depending on the number of pizzas purchased:
Cost

A customer can save on the HST (13%) if they buy 10 or more pizzas, so only charge HST
(use a constant) if they purchase less than 10 pizzas. That is, if the number of pizzas is 10
or more, there will be no tax.
There is also a cover charge for the luxury of purchasing one of Pizza Trent's special pizzas.
The cover charge (also a constant) is $0.50 (before HST), which is added to the total
irrespective of the number of pizzas purchased. That is, the $0.50 must be added to all
orders.
The program should do the following:

1.Input the Customer's Last Name , the size of the pizza , and the number of
pizzas purchased.

2.The pizza size inputs could be 'S' for small, 'M' for medium, ‘L' for large, or 'XL' for X-
large.

3.The program should output (neatly with properly formatted currency) the customer's last
Name, Number of Pizzas Purchased, and Total Cost. After printing the total cost, sign it by
printing your first and last name. You must use a single "WriteLine" statement to print this
output.

4.The program should also validate the user's input:

5.if the user enters 0 (or fewer) for the number of pizzas, an error message should be
printed indicating that at least one pizza needs to be ordered.
 Also, if the user enters a letter other than 'S', 'M', 'L', or 'XL' for the pizza size, an
