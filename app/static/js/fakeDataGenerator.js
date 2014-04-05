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
        this.start = withDefault(start,0)
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
            zip:84062,
            street:add.street, 
            id:add.id,
            lat:add.lat,
            long:add.long 
        }
    }
    
    Generator.prototype.randomImage = function genRandomImage(text){
        if (text) text+="/"
        return "http://lorempixel.com/600/600/sports/"+text
    }

    Generator.prototype.next = function genSeq(approved, open){
        var dates = this.dates();
        var addr = this.randAddr();
        var id = this.end++;
        var open = open || Math.random() > 0.5;
        var approved = approved || open || Math.random() > 0.5;
        return {
            "id":id,
            "owner":Math.floor(Math.random() *10),
            "title":"Title of issue:" + id,
            "description":"description of issue #" + id,
            "location":{
                "lat": addr.lat,
                "long": addr.long,
                "address": addr.street
            },
            "open":open,
            "approved":approved,
            "priority":"medium",
            "image_url":this.randomImage("test"),
            "created_at":dates[0],
            "updated_at":dates[1],
        }
    }
    
    return Generator;
}())


var Users = (function UserGenerator(){
    function getRand(list){
        return list[Math.floor(Math.random() * list.length)]
    }
    function Users(){
        this.start = 0;
    }
    Users.prototype.names = ["Gretchen","Hillary","Philbert","Whinney","Philemon","Georgetta","April",
                              "Bertha","Sam","Steve","Alex", "Derek", "Xander", "Reynold", "Thelonious", "Spartacus"]
    Users.prototype.next = function nextUser(isAdmin, name){
        if (isAdmin == undefined)
            isAdmin = Math.random() > 0.1;
        if (name == undefined)
            name = getRand(this.names);
        return {
            id:this.start++,
            name:name,
            admin:isAdmin,
            email:name+"@haha.jk",
            password:name.toLowerCase()
        }
    }
    return Users;
}())

