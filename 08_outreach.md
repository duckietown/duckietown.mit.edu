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
infoWindowContent.push(['<div class="info_content">'+'<h3>Graduate' + ' Class'+ ': <a href="http://duckietown.mit.edu/">'+ ' MIT 2.166'+'</a>'+' at '+'<a href="http://web.mit.edu">'+'Massachusetts Institute of Technology'+'</a>'+'</h3>'+'<p>Where it all started! The first Duckietown class was at MIT in 2016</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Graduate' + ' Class'+ ': <a href="http://duckietown.nctu.edu.tw/">'+ ' ICN9005 Robotic Vision'+'</a>'+' at '+'<a href="http://www.nctu.edu.tw/en">'+'National Chiao Tung University'+'</a>'+'</h3>'+'<p>The "first branch of Duckietown" was started in 2016 in NCTU led by Prof Nick Wang</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Independent' + ': <a href="https://research.jetbrains.org/duckietown">'+ ' Independent study led by Kirill Krinkin'+'</a>'+' at '+'<a href="https://research.jetbrains.org/duckietown">'+'JetBrains Research'+'</a>'+'</h3>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Undergraduate' + ' Class'+ ': <a href="http://soe.rutgers.edu/story/robotics-workshop-brings-international-students-rutgers">'+ ' Robotics Summer Workshop'+'</a>'+' at '+'<a href="http://www.rutgers.edu/">'+'Rutgers University'+'</a>'+'</h3>'+'<p>Prof. Jingjin Yu and Prof. Qingze Zou at Rutgers led a summer workshop based on Duckietown. The focus was on comparing the differences in the classroom environment between China and the United States. Here is a  <a href="https://www.youtube.com/watch?v=I4NudbNBUHI">video</a>.</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Undergraduate' + ' Class'+ ' Under Development'+' at '+'<a href="http://www.tsinghua.edu.cn/publish/newthuen/">'+'Tsinghua University'+'</a>'+'</h3>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Undergraduate' + ' Class'+ ': <a href="https://www.facebook.com/duckietowncl/">'+ ' Facultad de Ciencias Fisicas Y Matematicas'+'</a>'+' at '+'<a href="http://www.uchile.cl/">'+'University of Chile'+'</a>'+'</h3>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Undergraduate' + ' Class'+ ' Under Development'+' at '+'<a href="https://www.cvut.cz/en">'+'Czech Technical University in Prague'+'</a>'+'</h3>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Undergraduate' + ' Class'+ ' Under Development'+' at '+'<a href="https://rpi.edu/">'+'Rensselaer Polytechnic Institute'+'</a>'+'</h3>'+'<p>The Duckietown platform was used by students in Prof. John Wen&apos;s undergraduate class. Here is a <a href="https://www.youtube.com/playlist?list=PL3qku09D5UsDIiNOpI6NKZgdSNQlhaMKm">video</a> of some of their results.</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Undergraduate' + ' Class'+ ' Under Development'+' at '+'<a href="https://permanentfuturelab.wiki/wiki/Seats2meet.com_Utrecht_CS">'+'Permanent Future Lab Utrecht'+'</a>'+'</h3>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Graduate' + ' Class'+ ' Matthew Walter&apos;s graduate class at TTIC'+' at '+'<a href="http://www.ttic.edu/">'+'Toyota Technological Institute at Chicago'+'</a>'+'</h3>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Graduate' + ' Class'+ ' Graduate class taught by Paull at U de M'+' at '+'<a href="http://www.umontreal.ca/en/">'+'Universite de Montreal'+'</a>'+'</h3>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Graduate' + ' Class'+ ' Frazzoli and Censi&apos;s graduate class at ETH Zurich'+' at '+'<a href="https://www.ethz.ch">'+'ETH Zurich'+'</a>'+'</h3>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Graduate' + ' Class'+ ' Under Development'+' at '+'<a href="https://www.u-picardie.fr/">'+'University of Picardie Jules Verne'+'</a>'+'</h3>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Research' + ': <a href="http://faculty.ucmerced.edu/scarpin">'+ ' Under Development'+'</a>'+' at '+'<a href="http://www.ucmerced.edu/">'+'University of California, Merced'+'</a>'+'</h3>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>High School' + ' Class'+ ': <a href="http://www.perlatecnica.it/">'+ ' Perlatecnica'+'</a>'+' at '+'<a href="http://www.isismarcianise.gov.it/">'+'ISIS Ferraris-Buccini Marcianise'+'</a>'+'</h3>'+'<p>Class  led by Mr. Mauro D&apos;Angelo. The code for the high school class is available at <a href="https://github.com/duckietown/duckietown-hs">Duckietown HS Github page</a>.</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>High School' + ' Class'+ ': <a href="http://www.perlatecnica.it/">'+ ' Perlatecnica'+'</a>'+' at '+'ITI E.Fermi Via Merine, 5, 73100 Lecce LE'+'</h3>'+'<p>Class  led by Mr. Mauro D&apos;Angelo. The code for the high school class is available at <a href="https://github.com/duckietown/duckietown-hs">Duckietown HS Github page</a>.</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>High School' + ' Class'+ ': <a href="http://www.perlatecnica.it/">'+ ' Perlatecnica'+'</a>'+' at '+'Istituto d&apos;istruzione superiore Baronissi'+'</h3>'+'<p>Class  led by Mr. Mauro D&apos;Angelo. The code for the high school class is available at <a href="https://github.com/duckietown/duckietown-hs">Duckietown HS Github page</a>.</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>High School' + ' Class'+ ': <a href="http://www.perlatecnica.it/">'+ ' Perlatecnica'+'</a>'+' at '+'Associazione Dambros'+'</h3>'+'<p>Class  led by Mr. Mauro D&apos;Angelo. The code for the high school class is available at <a href="https://github.com/duckietown/duckietown-hs">Duckietown HS Github page</a>.</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>High School' + ' Class'+ ': <a href="http://www.perlatecnica.it/">'+ ' Perlatecnica'+'</a>'+' at '+'ITI Dalla Chiesa Afragola - Via Sicilia 60 80021 Afragola'+'</h3>'+'<p>Class  led by Mr. Mauro D&apos;Angelo. The code for the high school class is available at <a href="https://github.com/duckietown/duckietown-hs">Duckietown HS Github page</a>.</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>High School' + ' Class'+ ': <a href="http://www.perlatecnica.it/">'+ ' Perlatecnica'+'</a>'+' at '+'Liceo Statale Gandhi - Via Aldo Moro 26 80026 Casoria (NA)'+'</h3>'+'<p>Class  led by Mr. Mauro D&apos;Angelo. The code for the high school class is available at <a href="https://github.com/duckietown/duckietown-hs">Duckietown HS Github page</a>.</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>High School' + ' Class'+ ': <a href="http://www.perlatecnica.it/">'+ ' Perlatecnica'+'</a>'+' at '+'ITI Enrico Medi Via Buongiovanni 84  80046 - San Giorgio a Cremano (NA)'+'</h3>'+'<p>Class  led by Mr. Mauro D&apos;Angelo. The code for the high school class is available at <a href="https://github.com/duckietown/duckietown-hs">Duckietown HS Github page</a>.</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>High School' + ' Class'+ ': <a href="http://www.perlatecnica.it/">'+ ' Perlatecnica'+'</a>'+' at '+'Villaggio dei ragazzi Maddaloni'+'</h3>'+'<p>Class  led by Mr. Mauro D&apos;Angelo. The code for the high school class is available at <a href="https://github.com/duckietown/duckietown-hs">Duckietown HS Github page</a>.</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>High School' + ' Class'+ ': <a href="http://www.perlatecnica.it/">'+ ' Perlatecnica'+'</a>'+' at '+'Istituto Tecnico Salvatore Citelli via Palermo, 78 - 94017 Regalbuto'+'</h3>'+'<p>Class  led by Mr. Mauro D&apos;Angelo. The code for the high school class is available at <a href="https://github.com/duckietown/duckietown-hs">Duckietown HS Github page</a>.</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>High School' + ' Class'+ ': <a href="http://www.perlatecnica.it/">'+ ' Perlatecnica'+'</a>'+' at '+'Universita Federico II - Via Claudio, 21, 80125 Napoli (NA)'+'</h3>'+'<p>Class  led by Mr. Mauro D&apos;Angelo. The code for the high school class is available at <a href="https://github.com/duckietown/duckietown-hs">Duckietown HS Github page</a>.</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>High School' + ' Class'+ ': <a href="http://www.perlatecnica.it/">'+ ' Perlatecnica'+'</a>'+' at '+'<a href="http://www.liceogandhi.gov.it/">'+'Liceo scientifico Gandhi Casoria'+'</a>'+'</h3>'+'<p>Class  led by Mr. Mauro D&apos;Angelo. The code for the high school class is available at <a href="https://github.com/duckietown/duckietown-hs">Duckietown HS Github page</a>.</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Elementary School' + ' Class'+ ' Bruce Schwartz&apos;s 5th grade class are building their own robots based on the Duckiebot design'+' at '+'<a href="http://www.peckschool.org/page">'+'The Peck School'+'</a>'+'</h3>'+'<p>The 5th graders are designing their own robots</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>High School' + ' Class'+ ': <a href="http://www.perlatecnica.it/">'+ ' Perlatecnica'+'</a>'+' at '+'Ingegneria Elettronica Napoli'+'</h3>'+'<p>Class  led by Mr. Mauro D&apos;Angelo. The code for the high school class is available at <a href="https://github.com/duckietown/duckietown-hs">Duckietown HS Github page</a>.</p>'+'</div>']);
infoWindowContent.push(['<div class="info_content">'+'<h3>Independent' + ' Independent project'+' at '+'<a href="https://www.roeper.org/">'+'Roeper School in Birmingham'+'</a>'+'</h3>'+'<p>Nathaniel Lee is a senior at the Roeper School in Birmingham, MI and is taking the Duckietown course as an independent study.</p>'+'</div>']);
var image = { 
            url: 'media/duckie2.png', 
            scaledSize: new google.maps.Size(20,20), 
            origin: new google.maps.Point(0, 0), 
            anchor: new google.maps.Point(0, 20) 
  };
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(42.360082100,-71.094279000),
         map: map,
         icon: image,
         title: 'Massachusetts Institute of Technology \nMIT 2.166 \n(Graduate Class)'
        }); 
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[0][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 0));
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(24.785945600,120.996622000),
         map: map,
         icon: image,
         title: 'National Chiao Tung University \nICN9005 Robotic Vision \n(Graduate Class)'
        }); 
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[1][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 1));
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(59.980699000,30.324098000),
         map: map,
         icon: image,
         title: 'JetBrains Research \nIndependent study led by Kirill Krinkin \n(Independent)'
        }); 
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[2][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 2));
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(40.498251400,-74.446930900),
         map: map,
         icon: image,
         title: 'Rutgers University \nRobotics Summer Workshop \n(Undergraduate Class)'
        }); 
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[3][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 3));
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(39.999717200,116.326314100),
         map: map,
         icon: image,
         title: 'Tsinghua University \nUnder Development \n(Undergraduate Class)'
        }); 
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[4][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 4));
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(-33.444576500,-70.651470300),
         map: map,
         icon: image,
         title: 'University of Chile \nFacultad de Ciencias Fisicas Y Matematicas \n(Undergraduate Class)'
        }); 
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[5][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 5));
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(50.103035900,14.391149700),
         map: map,
         icon: image,
         title: 'Czech Technical University in Prague \nUnder Development \n(Undergraduate Class)'
        }); 
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[6][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 6));
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(42.730177900,-73.678931000),
         map: map,
         icon: image,
         title: 'Rensselaer Polytechnic Institute \nUnder Development \n(Undergraduate Class)'
        }); 
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[7][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 7));
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(52.089135300,5.113237100),
         map: map,
         icon: image,
         title: 'Permanent Future Lab Utrecht \nUnder Development \n(Undergraduate Class)'
        }); 
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[8][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 8));
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(41.784751700,-87.592717900),
         map: map,
         icon: image,
         title: 'Toyota Technological Institute at Chicago \nMatthew Walter&apos;s graduate class at TTIC \n(Graduate Class)'
        }); 
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[9][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 9));
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(45.505904200,-73.613793500),
         map: map,
         icon: image,
         title: 'Universite de Montreal \nGraduate class taught by Paull at U de M \n(Graduate Class)'
        }); 
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[10][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 10));
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(47.376366100,8.547531400),
         map: map,
         icon: image,
         title: 'ETH Zurich \nFrazzoli and Censi&apos;s graduate class at ETH Zurich \n(Graduate Class)'
        }); 
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[11][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 11));
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(49.876401400,2.263670600),
         map: map,
         icon: image,
         title: 'University of Picardie Jules Verne \nUnder Development \n(Graduate Class)'
        }); 
            google.maps.event.addListener(marker, 'click', (function(marker,i) {
              return function() {
                infoWindow.setContent(infoWindowContent[12][0]);
                infoWindow.open(map, marker);
            }
        })(marker, 12));
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(37.364073300,-120.430203000),
         map: map,
         icon: image,
         title: 'University of California, Merced \nUnder Development \n(Research)'
        }); 
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(41.029723100,14.262962800),
         map: map,
         icon: image,
         title: 'ISIS Ferraris-Buccini Marcianise \nPerlatecnica \n(High School Class)'
        }); 
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(40.347443900,18.185861000),
         map: map,
         icon: image,
         title: 'ITI E.Fermi Via Merine, 5, 73100 Lecce LE \nPerlatecnica \n(High School Class)'
        }); 
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(40.736706700,14.763872800),
         map: map,
         icon: image,
         title: 'Istituto d&apos;istruzione superiore Baronissi \nPerlatecnica \n(High School Class)'
        }); 
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(40.796661500,14.600524400),
         map: map,
         icon: image,
         title: 'Associazione Dambros \nPerlatecnica \n(High School Class)'
        }); 
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(40.930284800,14.308454300),
         map: map,
         icon: image,
         title: 'ITI Dalla Chiesa Afragola - Via Sicilia 60 80021 Afragola \nPerlatecnica \n(High School Class)'
        }); 
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(40.899785200,14.282357400),
         map: map,
         icon: image,
         title: 'Liceo Statale Gandhi - Via Aldo Moro 26 80026 Casoria (NA) \nPerlatecnica \n(High School Class)'
        }); 
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(40.840506900,14.343741800),
         map: map,
         icon: image,
         title: 'ITI Enrico Medi Via Buongiovanni 84  80046 - San Giorgio a Cremano (NA) \nPerlatecnica \n(High School Class)'
        }); 
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(41.039639400,14.381165200),
         map: map,
         icon: image,
         title: 'Villaggio dei ragazzi Maddaloni \nPerlatecnica \n(High School Class)'
        }); 
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(37.648900100,14.635377500),
         map: map,
         icon: image,
         title: 'Istituto Tecnico Salvatore Citelli via Palermo, 78 - 94017 Regalbuto \nPerlatecnica \n(High School Class)'
        }); 
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(40.837002300,14.189024300),
         map: map,
         icon: image,
         title: 'Universita Federico II - Via Claudio, 21, 80125 Napoli (NA) \nPerlatecnica \n(High School Class)'
        }); 
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(40.899785200,14.282368100),
         map: map,
         icon: image,
         title: 'Liceo scientifico Gandhi Casoria \nPerlatecnica \n(High School Class)'
        }); 
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(40.786958500,-74.473032700),
         map: map,
         icon: image,
         title: 'The Peck School \nBruce Schwartz&apos;s 5th grade class are building their own robots based on the Duckiebot design \n(Elementary School Class)'
        }); 
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(40.836991700,14.188852600),
         map: map,
         icon: image,
         title: 'Ingegneria Elettronica Napoli \nPerlatecnica \n(High School Class)'
        }); 
        marker = new google.maps.Marker({
         position: new google.maps.LatLng(42.593052100,-83.254676200),
         map: map,
         icon: image,
         title: 'Roeper School in Birmingham \nIndependent project \n(Independent)'
        }); 
      }

    </script>
<script async defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDCdYZ3gHK80cDg8NKT8g24JQJVLyUYqc8&callback=initMap&libraries=places">
    </script>



## Education
    
    


### Graduate




<p id="MIT" class=""> <a class="title" href="http://web.mit.edu">Massachusetts Institute of Technology</a> - <a class="title" href="http://duckietown.mit.edu/"> MIT 2.166</a>: Where it all started! The first Duckietown class was at MIT in 2016</p>



<p id="NCTU" class=""> <a class="title" href="http://www.nctu.edu.tw/en">National Chiao Tung University</a> - <a class="title" href="http://duckietown.nctu.edu.tw/"> ICN9005 Robotic Vision</a>: The "first branch of Duckietown" was started in 2016 in NCTU led by Prof Nick Wang</p>



<p id="TTIC" class=""> <a class="title" href="http://www.ttic.edu/">Toyota Technological Institute at Chicago</a> - Matthew Walter&apos;s graduate class at TTIC</p>



<p id="UdM" class=""> <a class="title" href="http://www.umontreal.ca/en/">Universite de Montreal</a> - Graduate class taught by Paull at U de M</p>



<p id="ETHZ" class=""> <a class="title" href="https://www.ethz.ch">ETH Zurich</a> - Frazzoli and Censi&apos;s graduate class at ETH Zurich</p>



<p id="PJV" class=""> <a class="title" href="https://www.u-picardie.fr/">University of Picardie Jules Verne</a> - Under development</p>




### Undergraduate




<p id="Rutgers" class=""> <a class="title" href="http://www.rutgers.edu/">Rutgers University</a> - <a class="title" href="http://soe.rutgers.edu/story/robotics-workshop-brings-international-students-rutgers"> Robotics Summer Workshop</a>: Prof. Jingjin Yu and Prof. Qingze Zou at Rutgers led a summer workshop based on Duckietown. The focus was on comparing the differences in the classroom environment between China and the United States. Here is a  <a href="https://www.youtube.com/watch?v=I4NudbNBUHI">video</a>.</p>



<p id="Tsinghua" class=""> <a class="title" href="http://www.tsinghua.edu.cn/publish/newthuen/">Tsinghua University</a> - Under development</p>



<p id="Chile" class=""> <a class="title" href="http://www.uchile.cl/">University of Chile</a> - <a class="title" href="https://www.facebook.com/duckietowncl/"> Facultad de Ciencias Fisicas Y Matematicas</a></p>



<p id="CTU" class=""> <a class="title" href="https://www.cvut.cz/en">Czech Technical University in Prague</a> - Under development</p>



<p id="RPI" class=""> <a class="title" href="https://rpi.edu/">Rensselaer Polytechnic Institute</a> - Under development: The Duckietown platform was used by students in Prof. John Wen&apos;s undergraduate class. Here is a <a href="https://www.youtube.com/playlist?list=PL3qku09D5UsDIiNOpI6NKZgdSNQlhaMKm">video</a> of some of their results.</p>



<p id="Utrecht" class=""> <a class="title" href="https://permanentfuturelab.wiki/wiki/Seats2meet.com_Utrecht_CS">Permanent Future Lab Utrecht</a> - Under development</p>




### Independent Study




<p id="jetbrains" class=""> <a class="title" href="https://research.jetbrains.org/duckietown">JetBrains Research</a> - <a class="title" href="https://research.jetbrains.org/duckietown"> Independent study led by Kirill Krinkin</a></p>




## Media Coverage
    
    


<p id="projectm" class=""> <a class="title" href="http://projectm-online.com/">Project M</a> - <a class="title" href="http://projectm-online.com/risk/what-do-autonomous-cars-mean-for-the-future-mobility-of-the-elderly/"> Follow the ducks to road safety</a>: Computer-supported driving is still in its infancy, but auto researchers are working hard to avoid accidents such as the fatal crash of a Tesla Model S. Some scientists are even playing with rubber ducks, but only in the interests of our safety</p>



<p id="boston.com" class=""> <a class="title" href="http://www.boston.com">www.boston.com</a> - <a class="title" href="http://www.boston.com/cars/news-and-reviews/2016/06/02/why-mits-duckietown-uses-adorable-rubber-toys-to-research-self-driving-cars"> Why MITs Duckietown uses adorable rubber toys to research self-driving cars</a></p>



<p id="popsci" class=""> <a class="title" href="http://www.popsci.com/">Popular Science</a> - <a class="title" href="http://www.popsci.com/meet-self-driving-rubber-duckie-taxis-duckietown"> MEET THE SELF-DRIVING RUBBER DUCKIE TAXIS OF DUCKIETOWN</a></p>



<p id="csail" class=""> <a class="title" href="http://www.csail.mit.edu">CSAIL</a> - <a class="title" href="http://www.csail.mit.edu/Self_driving_cars_meet_rubber_duckies"> SELF-DRIVING CARS, MEET RUBBER DUCKIES</a></p>



<p id="quartz" class=""> <a class="title" href="http://qz.com">Quartz</a> - <a class="title" href="http://qz.com/672992/a-tiny-town-of-rubber-ducks-is-laying-the-groundwork-for-the-next-generation-of-self-driving-cars/"> A tiny town of rubber ducks is laying the groundwork for the next generation of self-driving cars</a></p>



<p id="techtimes" class=""> <a class="title" href="http://www.techtimes.com">Tech Times</a> - <a class="title" href="http://www.techtimes.com/articles/152328/20160421/cruisin-in-duckietown-mits-rubber-duckie-taxis-can-self-drive.htm"> Cruisin&apos; In Duckietown: MIT&apos;s Rubber Duckie Taxis Can Self-drive</a></p>





