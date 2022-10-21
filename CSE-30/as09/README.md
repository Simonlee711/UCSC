PROGRAM DESCRIPTION
-------------------
The international E-road network is a numbering system for roads in Europe developed by the United Nations Economic Commission for Europe (UNECE). The network is numbered from E1 up and its roads cross national borders. It also reaches Central Asian countries like Kyrgyzstan, since they are members of the UNECE.
Lovro Šubelj at the University of Ljubljana compiled a graph of significant parts of the e-road network; nodes represent cities and an edge between two nodes denotes that they are connected by an E-road.

I have re-assembled Šubelj's dataset in a slightly more friendly manner, and added geographic latitude/longitude coordinates for each city (according to Google's Geocoding API).

vertex_names.txt lists the name of each city, along with a unique integer ID (separated by a tab character) for each city. Here are the first 5 lines:

```
1	Greenock
2	Glasgow
3	Preston
4	Birmingham
5	Southampton
```

vertex_locations.txt lists a latitude and longitude coordinate for each city. Here are the first 5 lines:

```
1 55.95647599999999 -4.771983
2 55.864237 -4.251806
3 53.763201 -2.70309
4 52.48624299999999 -1.890401
5 50.90970040000001 -1.4043509
```

Note that requesting Google Maps directions between those coordinates will demonstrate that these locations represent Greenock, Glasgow, Preston, Birmingham, and Southampton:

https://www.google.com/maps/dir/55.956,-4.772/55.864,-4.252/53.763,-2.703/52.486,-1.890/50.910,-1.404

network.txt lists the edges in the graph as tuples of city ID numbers. Consider these edges to be bidirectional. 

ASSIGNMENT:
You shall write a Python program that calculates and prints the shortest path between two vertices in our e-roads graph.

Expect at least two command-line arguments as names of a starting city and an ending city, respectively.
If either city name does not exist in the dataset, or there is no path between the two cities, print an informative one-line message to standard error (sys.stderr) and exit with a nonzero exit status (sys.exit).
If only two command-line arguments are provided, print, to standard output, one per line, the name of each city along the shortest path (start to finish).
In order to determine the shortest path, assign weights to each edge that represent the great-circle distance between the two geographic coordinates as per the haversine formula. Feel free to port and cite the JavaScript code on this site (it translates almost directly to Python).
If a third command-line argument exists, print a Google Maps URL requesting directions between the vertex coordinates, instead of the names of the cities.
The format of the URL is fairly straightforward:

https://www.google.com/maps/dir/lat1,lon1/lat2,lon2/lat3,lon3/lat4,lon4/...

Round the coordinates to three digits after the decimal point to keep the URL length from getting too unwieldy, as in the example given above.
Google Maps has a limit to how many points it will accept in these directions. Don't worry about that.

HOW TO RUN PROGRAM
------------------
This assignment should be pretty cool in the sense that we are making literal Google Maps. Just put in the command line arguments 
and you should get an output to something very similar to the sample below!

```
$ python3.9 cse30_e_roads.py "Nizhny Novgorod" Munich
Nizhny Novgorod
Vladimir
Moscow
Velikiye Luki
Rēzekne
Daugavpils
Ukmergė
Kaunas
Warsaw
Piotrków Trybunalski
Wrocław
Legnica
Jelenia Góra
Harrachov
Železný Brod
Turnov
Mladá Boleslav
Prague
Plzeň
Bayerisch Eisenstein
Deggendorf
Munich
$ python3.9 cse30_e_roads.py "Nizhny Novgorod" Munich but how do we get there?
https://www.google.com/maps/dir/56.327,44.006/56.143,40.390/55.756,37.617/56.340,30.531/56.510,27.333/55.875,26.536/55.245,24.776/54.899,23.904/52.230,21.012/51.405,19.703/51.108,17.039/51.207,16.155/50.904,15.719/50.772,15.431/50.643,15.254/50.587,15.157/50.413,14.908/50.076,14.438/49.738,13.374/49.122,13.199/48.841,12.957/48.135,11.582
```
