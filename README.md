# pyjsonp

Usage in JavaScript:

    var url = "http://iszz.azo.hr/iskzl/rs/podatak/export/json?postaja=156&polutant=5&tipPodatka=0&vrijemeOd=15.05.2015&vrijemeDo=18.05.2015";
    var encodedURI = encodeURIComponent(url);
    $.getJSON( "/dyn/?url="+ encodedURI, function( data ) {
      console.log(data);
    });
