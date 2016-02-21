// Docs at http://simpleweatherjs.com

/* Does your browser support geolocation? */
if ("geolocation" in navigator) {
  $('.js-geolocation').show(); 
} else {
  $('.js-geolocation').hide();
}

/* Where in the world are you? */
$('.js-geolocation').on('click', function() {
  navigator.geolocation.getCurrentPosition(function(position) {
    loadWeather(position.coords.latitude+','+position.coords.longitude); //load weather using your lat/lng coordinates
  });
});

/* 
*Set to PVD by default
*/
$(document).ready(function() {
  loadWeather('Providence',''); //@params location, woeid
    setInterval(getWeather, 600000); //Update the weather every 10 minutes.
});

function loadWeather(location, woeid) {
  $.simpleWeather({
    location: location,
    woeid: woeid,
    unit: 'f',
    success: function(weather) {
	  
    html = '<h4><i class="icon-'+weather.code+'"></i> '+weather.temp+'&deg;'+weather.units.temp+'</h4>';
	  html += '<ul>'+weather.title+'</ul>';
    html += '<ul class="currently">Right now it is '+weather.currently+'</ul>'; 
	  html += '<ul>The high will be '+weather.high+' and the low will be '+weather.low+'</ul>';
	  html += '<ul>Tomorrow it will be '+weather.forecast[1].text+'</ul>';
      $("#weather").html(html);  
    },
    error: function(error) {
      $("#weather").html('<p>'+error+'</p>');
    }
  });
}
