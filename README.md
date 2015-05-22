# pyjsonp

Configure nginx/wsgi:
https://www.digitalocean.com/community/tutorials/how-to-deploy-python-wsgi-applications-using-uwsgi-web-server-with-nginx

Run :
    uwsgi --socket 127.0.0.1:8080 --protocol=http -w wsgiuwsgi --socket 127.0.0.1:8080 --protocol=uwsgi -w wsgi

Usage in JavaScript:

    var url = "http://iszz.azo.hr/iskzl/rs/podatak/export/json?postaja=156&polutant=5&tipPodatka=0&vrijemeOd=15.05.2015&vrijemeDo=18.05.2015";
    var encodedURI = encodeURIComponent(url);
    $.getJSON( "/dyn/?url="+ encodedURI, function( data ) {
      console.log(data);
    });
