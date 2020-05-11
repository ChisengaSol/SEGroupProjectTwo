# SEGroupProjectTwo
This is the online food ordering system which meets the following functional requirements:

1)It enables customers of a restaurant to browse the menu 

2)The customers can choose and order the dishes they prefer.

3)The chefs in the kitchen are able to receive the orders as they are made. 

4)The customer is able to see the bill for the orders made. 

5)The system provides payment options for the customer.

One data structure used in this project is the dictionary. This is because its key-value characteristic 
has helped in the easy and efficient storage and retrieval of data in the system. For instance, the data structure facilitates the storing 
of a meal as a key and its attributes such as the price as the value.

The methods in which this data structure is used include getMenu, and Orderform. In the getMenu, the dictionaries
are used to store the availabe meals that are then displayed to the user. In the Orderform, the data structure is used to
to store the orders made by the customer.

In building this system, the python django framework has been used for the backend and bootstrap for the frontend. One of the 
reasons of using the django franework is that it supports major operating systems and hence enhances the accessibility of web applications.
It also makes it easier to work with different databases. Django also has built-in security features which protect the web applications 
attacks by malicious users. In addition, Django supports model-view-controller (MVC) design. Postgresql has been used for the database.

To meet the online payment functionality, the Rave Payment API has been used. The API facilitates payment for meals through 
various payment options including mobile money and credit card.
