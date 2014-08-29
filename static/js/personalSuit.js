
function makeGeocodeRequest(query){

	var one = 1;
	var request = "https://maps.googleapis.com/maps/api/geocode/json?address=" + query.replace(/ /g, "+") + "&key=AIzaSyBxcLsh5UEYOPRUW_q3uCwLhcVTcYiXfaY";
	console.log(request);
	return request;
}




function httpGet(URL){

	var xmlHttp = null;
	xmlHttp = new XMLHttpRequest();
	xmlHttp.open("GET", URL , false);
	xmlHttp.send(null);

	return JSON.parse(xmlHttp.response);

}


function geocode(address, latOrLong){

	var jsonResponse = httpGet(makeGeocodeRequest(address));

	if (latOrLong.toLowerCase() == "lat"){
		console.log (jsonResponse.results[0].geometry.location.lat);
		return parseFloat(jsonResponse.results[0].geometry.location.lat);
	}
	else if (latOrLong.toLowerCase() == "long"){
		console.log(parseFloat(jsonResponse.results[0].geometry.location.lng))
		return parseFloat(jsonResponse.results[0].geometry.location.lng);
	}

}



/Some jquery/

		$(document).ready(function(){
			$("button").click(function(){
				$("#map-canvas").toggle("fast");
			}, function(){$(".span5").toggle("fast");
			});
		});



