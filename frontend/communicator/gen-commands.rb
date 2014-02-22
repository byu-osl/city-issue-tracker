require 'json'
require 'hashie'

class JsMethod
  def initialize(method_hash)
    @hash = Hashie::Mash.new(method_hash)
    @hash.args.unshift("callback")
  end

  def encode_uri arg
    "#{arg}=\"+encodeURIComponent(#{arg})"
  end

  def url_string
    base_url = "\"#{@hash.path}\"".gsub(/:([a-z]+)"/, '"+\1')
    if @hash.request == "GET"
      @hash.args.delete "callback"
      @hash.args.delete "id"
      if @hash.args.size > 0
        base_url = base_url[0..-2]+"?"+@hash.args.map{|a| encode_uri(a)}.join("+\"&")
      end
    end
    base_url
  end

  def form_data
    if @hash.args.include? "form"
      return "form.serialize()"
    end
    return "{}"
  end

  def call_string
    rep = <<-call_s

    call_s
    rep.gsub(/\n/, "\n  ") 
  end

  def to_js
    rep = <<-jsRep

      //#{@hash.description}
      Communicator.prototype.#{@hash.name} = function(#{@hash.args.join(", ")}) {
        $.ajax({
          url: #{url_string},
          type: "#{@hash.request}",
          #{"data: #{form_data}," if @hash.request == "POST"}
          success: callback
        });
      };
    jsRep
    rep.gsub(/\n    /, "\n")   
  end
end

commands = JSON.parse(File.new("commands.json").read)
js_commands = commands.map{|c| JsMethod.new c}

out = File.new("communicator.js", "w")
scaffold = File.new("scaffold.js")

scaffold.each_line do |line|
  if line == "  // FUNCTIONS\n"
    js_commands.each do |c|
      out.write "  "+c.to_js
    end
  else
    out.write line
  end
end