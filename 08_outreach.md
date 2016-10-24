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
infoWindowContent.push(['<div class="info_content">'+'<h3>Graduate' + ' Class'+ ': <a href="http://duckietown.mit.edu/">'+ ' MIT 2.166'+'</a>'+' at '+'<a href="http://web.mit.edu">'+'Massachusetts Institute of Technology'+'</a>'+'</h3>'+'<p>Where it all started! The first Duckietown class was at MIT in 2016"</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Graduate' + ' Class'+ ': <a href="http://duckietown.nctu.edu.tw/">'+ ' ICN9005 Robotic Vision'+'</a>'+' at '+'<a href="http://www.nctu.edu.tw/en">'+'National Chiao Tung University'+'</a>'+'</h3>'+'<p>The "first branch of Duckietown" was started in 2016 in NCTU led by Prof Nick Wang</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Undergraduate' + ' Class'+ ': <a href="http://soe.rutgers.edu/story/robotics-workshop-brings-international-students-rutgers">'+ ' Robotics Summer Workshop'+'</a>'+' at '+'<a href="http://www.rutgers.edu/">'+'Rutgers University'+'</a>'+'</h3>'+'<p>Prof Jingjin Yu at Rutgers led a summer workshop based on Duckietown. The focus was on comparing the differences in the classroom environment between China and the United States. Here is a  <a href="https://www.youtube.com/watch?v=I4NudbNBUHI">video</a>.</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Undergraduate' + ' Class'+ ' Under Development'+' at '+'<a href="http://www.tsinghua.edu.cn/publish/newthuen/">'+'Tsinghua University'+'</a>'+'</h3>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Undergraduate' + ' Class'+ ' Under Development'+' at '+'<a href="https://www.cvut.cz/en">'+'Czech Technical University in Prague'+'</a>'+'</h3>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Undergraduate' + ' Class'+ ' Under Development'+' at '+'<a href="https://rpi.edu/">'+'Rensselaer Polytechnic Institute'+'</a>'+'</h3>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>High School' + ' Class'+ ': <a href="http://www.perlatecnica.it/">'+ ' Perlatecnica'+'</a>'+' at '+'<a href="http://www.isismarcianise.gov.it/">'+'I.S.I.S Marcianise'+'</a>'+'</h3>'+'<p>Class  led by Mr. Mauro D&apos;Angelo. The code for the high school class is available at <a href="https://github.com/duckietown/duckietown-hs">Duckietown HS Github page</a>.</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>High School' + ' Class'+ ': <a href="http://www.perlatecnica.it/">'+ ' Perlatecnica'+'</a>'+' at '+'<a href="http://www.liceogandhi.gov.it/">'+'Liceo scientifico Gandhi Casoria'+'</a>'+'</h3>'+'<p>Class  led by Mr. Mauro D&apos;Angelo. The code for the high school class is available at <a href="https://github.com/duckietown/duckietown-hs">Duckietown HS Github page</a>.</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Elementary School' + ' Class'+ ' Bruce Schwartz&apos;s 5th grade class are building their own robots based on the Duckiebot design'+' at '+'<a href="http://www.peckschool.org/page">'+'The Peck School'+'</a>'+'</h3>'+'<p>The 5th graders are designing their own robots</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Research' + ': <a href="http://faculty.ucmerced.edu/scarpin">'+ ' Paper under review'+'</a>'+' at '+'<a href="http://www.ucmerced.edu/">'+'University of California, Merced'+'</a>'+'</h3>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Independent' + ' Independent project'+' at '+'<a href="https://www.roeper.org/">'+'Roeper School in Birmingham'+'</a>'+'</h3>'+'<p>Nathaniel Lee is a senior at the Roeper School in Birmingham, MI and is taking the Duckietown course as an independent study.</p>'+'</div>']);
var image = { 
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
              title: 'Massachusetts Institute of Technology \nMIT 2.166 \n(Graduate Class)' 
            }); 
            
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[0][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 0));};}; 
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
              title: 'National Chiao Tung University \nICN9005 Robotic Vision \n(Graduate Class)' 
            }); 
            
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[1][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 1));};}; 
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
              title: 'Rutgers University \nRobotics Summer Workshop \n(Undergraduate Class)' 
            }); 
            
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[2][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 2));};}; 
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
              title: 'Tsinghua University \nUnder Development \n(Undergraduate Class)' 
            }); 
            
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[3][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 3));};}; 
            var request = { 
               query: 'Czech Technical University in Prague' 
            }; 
         service.textSearch(request, callback4); 
         function callback4(results, status) { 
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            var position = results[0].geometry.location
            var marker = new google.maps.Marker({ 
              map: map, 
              position: position,
              icon: image, 
              title: 'Czech Technical University in Prague \nUnder Development \n(Undergraduate Class)' 
            }); 
            
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[4][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 4));};}; 
            var request = { 
               query: 'Rensselaer Polytechnic Institute' 
            }; 
         service.textSearch(request, callback5); 
         function callback5(results, status) { 
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            var position = results[0].geometry.location
            var marker = new google.maps.Marker({ 
              map: map, 
              position: position,
              icon: image, 
              title: 'Rensselaer Polytechnic Institute \nUnder Development \n(Undergraduate Class)' 
            }); 
            
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[5][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 5));};}; 
            var request = { 
               query: 'I.S.I.S Marcianise' 
            }; 
         service.textSearch(request, callback6); 
         function callback6(results, status) { 
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            var position = results[0].geometry.location
            var marker = new google.maps.Marker({ 
              map: map, 
              position: position,
              icon: image, 
              title: 'I.S.I.S Marcianise \nPerlatecnica \n(High School Class)' 
            }); };}; 
            var request = { 
               query: 'Liceo scientifico Gandhi Casoria' 
            }; 
         service.textSearch(request, callback7); 
         function callback7(results, status) { 
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            var position = results[0].geometry.location
            var marker = new google.maps.Marker({ 
              map: map, 
              position: position,
              icon: image, 
              title: 'Liceo scientifico Gandhi Casoria \nPerlatecnica \n(High School Class)' 
            }); };}; 
            var request = { 
               query: 'The Peck School' 
            }; 
         service.textSearch(request, callback8); 
         function callback8(results, status) { 
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            var position = results[0].geometry.location
            var marker = new google.maps.Marker({ 
              map: map, 
              position: position,
              icon: image, 
              title: 'The Peck School \nBruce Schwartz&apos;s 5th grade class are building their own robots based on the Duckiebot design \n(Elementary School Class)' 
            }); };}; 
            var request = { 
               query: 'University of California, Merced' 
            }; 
         service.textSearch(request, callback9); 
         function callback9(results, status) { 
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            var position = results[0].geometry.location
            var marker = new google.maps.Marker({ 
              map: map, 
              position: position,
              icon: image, 
              title: 'University of California, Merced \nPaper under review \n(Research)' 
            }); };}; 
            var request = { 
               query: 'Roeper School in Birmingham' 
            }; 
         service.textSearch(request, callback10); 
         function callback10(results, status) { 
          if (status === google.maps.places.PlacesServiceStatus.OK) {
            var position = results[0].geometry.location
            var marker = new google.maps.Marker({ 
              map: map, 
              position: position,
              icon: image, 
              title: 'Roeper School in Birmingham \nIndependent project \n(Independent)' 
            }); };};
      }

    </script>
<script async defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDCdYZ3gHK80cDg8NKT8g24JQJVLyUYqc8&callback=initMap&libraries=places">
    </script>



## Education
    
    


### Graduate




<p id="MIT" class=""> <a class="title" href="http://web.mit.edu">Massachusetts Institute of Technology</a> - <a class="title" href="http://duckietown.mit.edu/"> MIT 2.166</a>: Where it all started! The first Duckietown class was at MIT in 2016"</p>



<p id="NCTU" class=""> <a class="title" href="http://www.nctu.edu.tw/en">National Chiao Tung University</a> - <a class="title" href="http://duckietown.nctu.edu.tw/"> ICN9005 Robotic Vision</a>: The "first branch of Duckietown" was started in 2016 in NCTU led by Prof Nick Wang</p>




### Undergraduate




<p id="Rutgers" class=""> <a class="title" href="http://www.rutgers.edu/">Rutgers University</a> - <a class="title" href="http://soe.rutgers.edu/story/robotics-workshop-brings-international-students-rutgers"> Robotics Summer Workshop</a>: Prof Jingjin Yu at Rutgers led a summer workshop based on Duckietown. The focus was on comparing the differences in the classroom environment between China and the United States. Here is a  <a href="https://www.youtube.com/watch?v=I4NudbNBUHI">video</a>.</p>



<p id="Tsinghua" class=""> <a class="title" href="http://www.tsinghua.edu.cn/publish/newthuen/">Tsinghua University</a> - Under development</p>



<p id="CTU" class=""> <a class="title" href="https://www.cvut.cz/en">Czech Technical University in Prague</a> - Under development</p>



<p id="RPI" class=""> <a class="title" href="https://rpi.edu/">Rensselaer Polytechnic Institute</a> - Under development</p>




## Media Coverage
    
    


<p id="projectm" class=""> <a class="title" href="http://projectm-online.com/">Project M</a> - <a class="title" href="http://projectm-online.com/risk/what-do-autonomous-cars-mean-for-the-future-mobility-of-the-elderly/"> Follow the ducks to road safety</a>: Computer-supported driving is still in its infancy, but auto researchers are working hard to avoid accidents such as the fatal crash of a Tesla Model S. Some scientists are even playing with rubber ducks, but only in the interests of our safety</p>



<p id="boston.com" class=""> <a class="title" href="http://www.boston.com">www.boston.com</a> - <a class="title" href="http://www.boston.com/cars/news-and-reviews/2016/06/02/why-mits-duckietown-uses-adorable-rubber-toys-to-research-self-driving-cars"> Why MITs Duckietown uses adorable rubber toys to research self-driving cars</a></p>



<p id="popsci" class=""> <a class="title" href="http://www.popsci.com/">Popular Science</a> - <a class="title" href="http://www.popsci.com/meet-self-driving-rubber-duckie-taxis-duckietown"> MEET THE SELF-DRIVING RUBBER DUCKIE TAXIS OF DUCKIETOWN</a></p>



<p id="csail" class=""> <a class="title" href="http://www.csail.mit.edu">CSAIL</a> - <a class="title" href="http://www.csail.mit.edu/Self_driving_cars_meet_rubber_duckies"> SELF-DRIVING CARS, MEET RUBBER DUCKIES</a></p>



<p id="quartz" class=""> <a class="title" href="http://qz.com">Quartz</a> - <a class="title" href="http://qz.com/672992/a-tiny-town-of-rubber-ducks-is-laying-the-groundwork-for-the-next-generation-of-self-driving-cars/"> A tiny town of rubber ducks is laying the groundwork for the next generation of self-driving cars</a></p>



<p id="techtimes" class=""> <a class="title" href="http://www.techtimes.com">Tech Times</a> - <a class="title" href="http://www.techtimes.com/articles/152328/20160421/cruisin-in-duckietown-mits-rubber-duckie-taxis-can-self-drive.htm"> Cruisin&apos; In Duckietown: MIT&apos;s Rubber Duckie Taxis Can Self-drive</a></p>





