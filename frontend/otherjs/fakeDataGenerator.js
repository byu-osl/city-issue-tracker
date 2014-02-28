Generator = (function Generator_Namespace(){
    
    function withDefault(val, def){
        if (val != undefined && val != null) return val
        else return def
    }
    
    function AddressStub(street, lat, long){
        this.street = street
        this.lat = lat
        this.long = long
    }
    
    function getRand(list){
        return list[Math.floor(Math.random() * list.length)]
    }
    
    function Generator(start){
        this.start = withDefault(start, Math.random()
        this.end = this.start;
    }

    Generator.prototype.dates = function dates(){
        return [Date.now(), Date.now(), Date.now()]
    }

    Generator.prototype.addresses = [
        new AddressStub("4087 West Juniper Road", 40.415350, -111.756257),
        new AddressStub("4148 W Sandalwood D", 40.417809, -111.757872),
        new AddressStub("4561 W Carriage Ln", 40.417646, -111.768086),
        new AddressStub("9737 Chesterfield Dr", 40.408872, -111.766353),
        new AddressStub("1041 W 9600 N", 40.405261, -111.756021),
        new AddressStub("3706 W Boxelder Dr", 40.407761, -111.746955),
        new AddressStub("4078 Honeylocust Ln", 40.420194, -111.755581)
    ]
    
    Generator.prototype.addresses.forEach(function(add,i){
        add.id = i
    })
    
    Generator.prototype.randAddr = function genAddr(){
        add = getRand(this.addresses)
        return {
            zip = 84062,
            street = add.street, 
            id = add.id,
            lat = add.lat,
            long = add.long 
        }
    }
    
    Generator.prototype.randomImage = function genRandomImage(text){
        if (text) text+="/"
        return "http://lorempixel.com/600/600/sports/"+text
    }

    Generator.prototype.next = function genSeq(){
        dates = this.dates();
        addr = this.randAddr();
        service_name = "Sidewalk and Curb Issues";
        return {
            "service_request_id":this.end++,
            "status":Math.random() > 0.5 ? "open" : "close",
            "status_notes":null,
            "service_name":service_name,
            "service_code":006,
            "description":null,
            "agency_responsible":null,
            "service_notice":null,
            "requested_datetime":dates[0],
            "updated_datetime":dates[1],
            "expected_datetime":dates[2],
            "address":addr.street,
            "address_id":addr.id,
            "zipcode":addr.zip,
            "lat":addr.lat,
            "long":addr.long,
            "media_url":this.randomImage(service_name.replace(/ /g, "-"))
        }
    ]
    
    return Generator;
}())
