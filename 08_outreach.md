---
layout: page
title: Outreach
permalink: outreach.html
---

<style type="text/css">
        #map {
        width: 100%;
        height: 400px;
        background-color: grey;
      }
</style>



<div id="map"></div>
<script>
function initMap() {
var boston = {lat: 42.3601, lng: -71.0589};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 2,
          center: boston
        });var infoWindow = new google.maps.InfoWindow(), marker, i;var service = new google.maps.places.PlacesService(map);
    // Info Window Content
    var infoWindowContent = []
infoWindowContent.push(['<div class="info_content">' +
        '<h3>Graduate Class: <a href="http://duckietown.mit.edu/">MIT 2.166</a> at <a href="http://web.mit.edu">Massachusetts Institute of Technology</a> </h3>' +
        '<p>The "Where it all started - the first class at was at MIT in 2016"</p>' + '</div>']);infoWindowContent.push(['<div class="info_content">' +
        '<h3>Graduate Class: <a href="http://duckietown.nctu.edu.tw/">ICN9005 Robotic Vision</a> at <a href="http://www.nctu.edu.tw/en">National Chiao Tung University</a> </h3>' +
        '<p>The "first branch of Duckietown" was started in 2016 in NCTU led by Prof Nick Wang</p>' + '</div>']);infoWindowContent.push(['<div class="info_content">' +
        '<h3>Undergraduate Class: <a href="http://soe.rutgers.edu/story/robotics-workshop-brings-international-students-rutgers">Robotics Summer Workshop</a> at <a href="http://www.rutgers.edu/">Rutgers University</a> </h3>' +
        '<p><a href="https://www.youtube.com/watch?v=I4NudbNBUHI">There is No Gap Between Us and the Professors</a> How is the classroom environment different in China compared with the United States? Watch our video to see what students from South China University of Technology have to say after studying robotics and engineering at Rutgers this summer.</p>' + '</div>']);infoWindowContent.push(['<div class="info_content">' +
        '<h3>Undergraduate Class: <a href="None">None</a> at <a href="http://www.tsinghua.edu.cn/publish/newthuen/">Tsinghua University</a> </h3>' +
        '<p>Class under development</p>' + '</div>']);infoWindowContent.push(['<div class="info_content">' +
        '<h3>Undergraduate Class: <a href="None">None</a> at <a href="https://rpi.edu/">Rensselaer Polytechnic Institute</a> </h3>' +
        '<p>Class under development</p>' + '</div>']);infoWindowContent.push(['<div class="info_content">' +
        '<h3>High School Class: <a href="None">Perlatecnica</a> at <a href="http://www.perlatecnica.it/">Via Napoli, 60</a> </h3>' +
        '<p>Class underway led by Mr. Mauro D`Angelo. The code for the high school class is available at <a href="https://github.com/duckietown/duckietown-hs">Duckietown HS Github page</a>.</p>' + '</div>']);infoWindowContent.push(['<div class="info_content">' +
        '<h3>Elementary School Class: <a href="None">Bruce Schwartz`s 5th grade class are building their own robots based on the Duckiebot design</a> at <a href="http://www.peckschool.org/page">The Peck School</a> </h3>' +
        '<p>The 5th graders are designing their own robots</p>' + '</div>']);infoWindowContent.push(['<div class="info_content">' +
        '<h3>Research Class: <a href="http://faculty.ucmerced.edu/scarpin">Paper under review</a> at <a href="http://www.ucmerced.edu/">University of California, Merced</a> </h3>' +
        '<p></p>' + '</div>']);var image = { 
            url: 'media/duckie2.png', 
            scaledSize: new google.maps.Size(20,20), 
            origin: new google.maps.Point(0, 0), 
            anchor: new google.maps.Point(0, 20) 
  }; 
            var request = { 
               query: 'Massachusetts Institute of Technology' 
            }; 
         service.textSearch(request, callback0); 
         function callback0(results, status) { 
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            var position = results[0].geometry.location
            var marker = new google.maps.Marker({ 
              map: map, 
              position: position,
              icon: image, 
              title: 'Massachusetts Institute of Technology \nMIT 2.166 \n(Graduate class)' 
            });
            
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[0][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 0)); 
          };};  
            var request = { 
               query: 'National Chiao Tung University' 
            }; 
         service.textSearch(request, callback1); 
         function callback1(results, status) { 
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            var position = results[0].geometry.location
            var marker = new google.maps.Marker({ 
              map: map, 
              position: position,
              icon: image, 
              title: 'National Chiao Tung University \nICN9005 Robotic Vision \n(Graduate class)' 
            });
            
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[1][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 1)); 
          };};  
            var request = { 
               query: 'Rutgers University' 
            }; 
         service.textSearch(request, callback2); 
         function callback2(results, status) { 
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            var position = results[0].geometry.location
            var marker = new google.maps.Marker({ 
              map: map, 
              position: position,
              icon: image, 
              title: 'Rutgers University \nRobotics Summer Workshop \n(Undergraduate class)' 
            });
            
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[2][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 2)); 
          };};  
            var request = { 
               query: 'Tsinghua University' 
            }; 
         service.textSearch(request, callback3); 
         function callback3(results, status) { 
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            var position = results[0].geometry.location
            var marker = new google.maps.Marker({ 
              map: map, 
              position: position,
              icon: image, 
              title: 'Tsinghua University \nNone \n(Undergraduate class)' 
            });
            
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[3][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 3)); 
          };};  
            var request = { 
               query: 'Rensselaer Polytechnic Institute' 
            }; 
         service.textSearch(request, callback4); 
         function callback4(results, status) { 
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            var position = results[0].geometry.location
            var marker = new google.maps.Marker({ 
              map: map, 
              position: position,
              icon: image, 
              title: 'Rensselaer Polytechnic Institute \nNone \n(Undergraduate class)' 
            });
            
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[4][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 4)); 
          };};  
            var request = { 
               query: 'Via Napoli, 60' 
            }; 
         service.textSearch(request, callback5); 
         function callback5(results, status) { 
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            var position = results[0].geometry.location
            var marker = new google.maps.Marker({ 
              map: map, 
              position: position,
              icon: image, 
              title: 'Via Napoli, 60 \nPerlatecnica \n(High School class)' 
            });
            
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[5][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 5)); 
          };};  
            var request = { 
               query: 'The Peck School' 
            }; 
         service.textSearch(request, callback6); 
         function callback6(results, status) { 
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            var position = results[0].geometry.location
            var marker = new google.maps.Marker({ 
              map: map, 
              position: position,
              icon: image, 
              title: 'The Peck School \nBruce Schwartz`s 5th grade class are building their own robots based on the Duckiebot design \n(Elementary School class)' 
            });
            
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[6][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 6)); 
          };};  
            var request = { 
               query: 'University of California, Merced' 
            }; 
         service.textSearch(request, callback7); 
         function callback7(results, status) { 
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            var position = results[0].geometry.location
            var marker = new google.maps.Marker({ 
              map: map, 
              position: position,
              icon: image, 
              title: 'University of California, Merced \nPaper under review \n(Research class)' 
            });
            
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[7][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 7)); 
          };}; 
      }

    </script>
<script async defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDCdYZ3gHK80cDg8NKT8g24JQJVLyUYqc8&callback=initMap&libraries=places">
    </script>



## Education
    
    


### Graduate




<p id="MIT" class=""><a class="title" href="None">Massachusetts Institute of Technology</a> - <a class="title" href="http://duckietown.mit.edu/">MIT 2.166</a>: The "Where it all started - the first class at was at MIT in 2016"</p>



<p id="NCTU" class=""><a class="title" href="None">National Chiao Tung University</a> - <a class="title" href="http://duckietown.nctu.edu.tw/">ICN9005 Robotic Vision</a>: The "first branch of Duckietown" was started in 2016 in NCTU led by Prof Nick Wang</p>




### Undergraduate




<p id="Rutgers" class=""><a class="title" href="None">Rutgers University</a> - <a class="title" href="http://soe.rutgers.edu/story/robotics-workshop-brings-international-students-rutgers">Robotics Summer Workshop</a>: <a href="https://www.youtube.com/watch?v=I4NudbNBUHI">There is No Gap Between Us and the Professors</a> How is the classroom environment different in China compared with the United States? Watch our video to see what students from South China University of Technology have to say after studying robotics and engineering at Rutgers this summer.</p>



<p id="Tsinghua" class="missing"><a class="title" href="None">Tsinghua University</a> - <a class="title" href="None">Missing title</a>: Class under development</p>



<p id="RPI" class="missing"><a class="title" href="None">Rensselaer Polytechnic Institute</a> - <a class="title" href="None">Missing title</a>: Class under development</p>




### High School




<p id="Perlatecnica" class=""><a class="title" href="None">Via Napoli, 60</a> - <a class="title" href="None">Perlatecnica</a>: Class underway led by Mr. Mauro D`Angelo. The code for the high school class is available at <a href="https://github.com/duckietown/duckietown-hs">Duckietown HS Github page</a>.</p>




### Elementary School




<p id="Peck" class=""><a class="title" href="None">The Peck School</a> - <a class="title" href="None">Bruce Schwartz`s 5th grade class are building their own robots based on the Duckiebot design</a>: The 5th graders are designing their own robots</p>




## Research
    
    


<p id="Carpin" class=""><a class="title" href="None">University of California, Merced</a> - <a class="title" href="http://faculty.ucmerced.edu/scarpin">Paper under review</a>: <span class="missing">Missing description</span></p>




## Media Coverage
    
    


<p id="projectm" class=""><a class="title" href="None">Project M</a> - <a class="title" href="http://projectm-online.com/risk/what-do-autonomous-cars-mean-for-the-future-mobility-of-the-elderly/">Follow the ducks to road safety</a>: Computer-supported driving is still in its infancy, but auto researchers are working hard to avoid accidents such as the fatal crash of a Tesla Model S. Some scientists are even playing with rubber ducks, but only in the interests of our safety</p>



<p id="boston.com" class=""><a class="title" href="None">www.boston.com</a> - <a class="title" href="http://www.boston.com/cars/news-and-reviews/2016/06/02/why-mits-duckietown-uses-adorable-rubber-toys-to-research-self-driving-cars">Why MITs Duckietown uses adorable rubber toys to research self-driving cars</a>: <span class="missing">Missing description</span></p>



<p id="popsci" class=""><a class="title" href="None">Popular Science</a> - <a class="title" href="http://www.popsci.com/meet-self-driving-rubber-duckie-taxis-duckietown">MEET THE SELF-DRIVING RUBBER DUCKIE TAXIS OF DUCKIETOWN</a>: <span class="missing">Missing description</span></p>



<p id="csail" class=""><a class="title" href="None">CSAIL</a> - <a class="title" href="http://www.csail.mit.edu/Self_driving_cars_meet_rubber_duckies">SELF-DRIVING CARS, MEET RUBBER DUCKIES</a>: <span class="missing">Missing description</span></p>



<p id="quartz" class=""><a class="title" href="None">Quartz</a> - <a class="title" href="http://qz.com/672992/a-tiny-town-of-rubber-ducks-is-laying-the-groundwork-for-the-next-generation-of-self-driving-cars/">A tiny town of rubber ducks is laying the groundwork for the next generation of self-driving cars</a>: <span class="missing">Missing description</span></p>





