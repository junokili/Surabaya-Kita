function initMap() {
            var map = new google.maps.Map(document.getElementById("map"),{
                zoom: 12,
                center: {
                    lat: -7.26550,
                    lng: 112.721825
                }
            });    

        var labels = "ABCDEFGHIJKLMNOPQPRSTUVWXYZ";

        var locations = [
            {lat: -7.281236, lng: 112.692476},
        ];

        var markers = locations.map(function(location, i){
            return new google.maps.Marker({
                position: location,
                label: labels[i % labels.length]
            });
            }); 

            var markerCluster = new MarkerClusterer(map, markers,
            {imagePath: "https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m"});
        }
