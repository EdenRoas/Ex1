# Ex1
The project reprsent an ofline algorithem of a smart elevator

 first step: we will sort all the calls according to the calls' time At intervals of at most half a minute.
second step: for every section of half a minute we will split the calls for two groups according to UP calls and DOWN calls
third step: for every group from step two we'll check where to place the elevators according to the area who gets the most calls.
fourth step: for every group from step two we'll check which calls will get on to the same elevator/which calls will be ssent to the same elevator according to the source floors and the destination floor.
we will put the elevator in the most wanted area and sent the elevator to the calls who close to eachother and on the same path.
