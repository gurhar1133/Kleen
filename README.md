# Kleen
- Based on the circut modeling project from runestone's adaptation of Problem Solving with Algorithms and Data Structures using Python By Brad Miller and David Ranum, Luther College. (see https://www.amazon.com/Problem-Solving-Algorithms-Structures-Python/dp/1590282574/ref=sr_1_1?crid=2BBIE0R5C59HI&keywords=problem+solving+with+algorithms+and+data+structures+using+python&qid=1572490645&sprefix=problem+sol%2Caps%2C205&sr=8-1) 

- logicClass.py has minimal modifications to the original project from the book and contains 
the LogicGate parent class as well as logic gate class definitions based on traditional binary logic. 

- kleen_logic.py introduces trinary logic gates and has a main function that walks the user through some implications of trinary logic values. Some modifications to getPin() methods were made for easier customization of circuits. Such non-traditional logics have been devised by philosophers. One example is Kleen's K3 logic.(see https://en.wikipedia.org/wiki/Three-valued_logic) 

- taut_circ.py and excluded_mid.py both model the logic of the law of excluded middle. Using trinary logic, they demonstrate how the law of excluded middle is not tautological if we add a third truth valuation. taut_circ.py uses assignment to build the circuit, whereas excluded_mid.py uses the connector class to creat composite circuits

- non_con.py will do something similar to what taut_circ.py and excluded_mid.py do, but for the principle of non-contradiction.

Objective:
The main purpose of this project is to get a better grasp on object oriented programming in general by modeling
something that interests me with it. Setting up user defined classes, methods and inheritance schemes helped
me get a better understanding of how OOP works.
