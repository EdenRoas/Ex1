# Ex1
The project reprsent an ofline algorithem of a smart elevator

Submissions:
Eden Roas- 318356599
Hadar Bitan- 318463882

We looked for a sources of a smart elevator and a algorithm of an elevator\smart elevator, we found a few articals on the subjec that helped understand the projrct better.
Here are the articals:

First artical- https://www.researchgate.net/publication/268237626_Optimization_of_waiting_and_journey_time_in_group_elevator_system_using_genetic_algorithm  
Second artical- https://www.sciencedirect.com/science/article/pii/S2405896316302671   
Third artical- https://www.hellocodeclub.com/design-elevator-system-java/

For this project we used an offline algorithm, a little explanation about offline algorithm:  
Offline algorithm gets all the problem data from the beginning and required to produce an answer that solve the giving problem(the explanation from Wikipedia).
In simple words in offline algorithm all the inputs is available to us in advance, and according to that we can write an algorithm that fits for all the inputs, meaning, because we gets all the input in advance we can write an algorithm more affective. 

The algorithm:   
First step- we'll receive the json and csv files which contains the data of the building and the sorted array of calls,
and create a new building and a new array of calls(each cell in the array contains a new call) containing the data we received from the files. 
Second step- we'll performe a basic tests in cases of zero elevators and only one elevator.
Third step- in a cases of 2 elevatos or more we'll check which elevator is the optimal one for this specific call according to the time it takes the elevator to get to the call, considering all the floors it has to stop in.
Fourth step- after we'll find the right elevator we'll update the number of elevator in the right variable of the call and add the call to the list of calls of the elevator.
Fifth step- we'll take the updated array of calls and create a new csv file from it.


the project's UML:

![image](https://user-images.githubusercontent.com/86705118/142629166-9451e9c3-c3f5-4881-9b4e-2e2aad7f9c53.png)
