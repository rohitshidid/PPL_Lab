

flight(pune, mumbai,2500).
flight(mumbai, delhi,6700).
flight(pune, mumbai,3000).
flight(pune, nashik,4500).
flight(delhi, mumbai,7000).
flight(delhi, nashik,6400).
flight(pune, delhi,6500).
flight(delhi, pune,6300).
flight(pune, nashik,3900).
flight(pune, mumbai,2100).
flight(delhi, mumbai,5500).
flight(nashik, mumbai,2500).
flight(delhi, pune,8000).


check_min(X, Y,Z) :-
  	flight(X,Y,Z).
    


