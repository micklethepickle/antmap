

function makeGeocodeRequest(query){

return 'https://maps.googleapis.com/maps/api/geocode/json?address=' + query.replace(" ", "+") + '&key=AIzaSyBxcLsh5UEYOPRUW_q3uCwLhcVTcYiXfaY'
}




function httpGet(URL){

var xmlHttp = null;
xmlHttp = XMLHttpRequest();
xmlHttp.open("GET", URL , false);
xmlHttp.send(null);

return JSON.parse(xmlHttp.response);

}


function geocode(address, latorLong){

var jsonResponse = httpGET(makeGeocodeRequest(address));

if (latOrLong == "lat".toLowerCase()){

return parseFloat(jsonResponse.results[0].geometry.location.lat);
}
else if (latOrLong == "long".toLowerCase()){
return parseFloat(jsonResponse.results[0].geometry.location.lat);
}

}
