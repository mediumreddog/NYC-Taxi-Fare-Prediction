# NYC-Taxi-Fare-Prediction

[NYC Taxi Fare Prediction on Kaggle](https://www.kaggle.com/c/new-york-city-taxi-fare-prediction)

## Preprocessing

Due to Google Maps API's high cost, we will need to locally process the road distance between each point. I am looking to use [OSRM](https://github.com/Project-OSRM/osrm-backend).

Commands below may vary by OS. Instructions are for Mac.

1. Download [NYC Map Data](https://drive.google.com/open?id=1b_J5KnmUfxXZ4v5SvyQNNesWDjTv-Rmx) and place in `preprocessing`.
2. Download Data from Kaggle link above and unzip into `data`.
3. Download OSRM backend docker container from [here](https://hub.docker.com/r/osrm/osrm-backend/).
4. Preprocesses the map data with the car profile (from the repo's main folder) with the following commands:
   1. `docker run -t -v $(pwd):/project osrm/osrm-backend osrm-extract -p /opt/car.lua /project/preprocessing/new-york-latest.osm.pbf`
   2. `docker run -t -v $(pwd):/project osrm/osrm-backend osrm-partition /project/preprocessing/new-york-latest.osrm`
   3. `docker run -t -v $(pwd):/project osrm/osrm-backend osrm-customize /project/preprocessing/new-york-latest.osrm`
5. Setup HTTP service to run requests on: `docker run -t -i -p 5000:5000 -v $(pwd):/project osrm/osrm-backend osrm-routed --algorithm mld /project/preprocessing/new-york-latest.osrm`
6. Run requests in this format: `http://127.0.0.1:5000/route/v1/driving/`Starting_lat`,`Starting_long`;`Ending_lat`,`Ending_long`?steps=false`

We are interested in two main metrics returned: distance and duration. Distance is returned in meters, and duration is number of seconds.
