require 'Nokogiri'
require 'HTTParty'
require 'pry'
require 'json'
require 'csv'

motorcycles_listing = HTTParty.get("https://osaka.craigslist.jp/search/mca?lang=en&cc=us&query=motorcycles")

nokoObj = Nokogiri::HTML(motorcycles_listing)

motorcycle_name = []
motorcycle_price=[]
nokoObj.css(".rows").css(".row").css(".hdrlnk").map do |tags|
	brand = tags.text
	motorcycle_name.push(brand)
end

nokoObj.css(".rows").css(".row").css("time").map do |prix|
	price = prix.text
	motorcycle_price.push(price)
end

motorcycles = Hash[motorcycle_name.zip motorcycle_price]
puts motorcycles["Suzuki Sky wave scootor"]
#Pry.start(binding)
CSV.open("motorcycles.csv", 'w', write_headers: :true, headers: ["Brand Name", "Price"]) do |write|
	motorcycle_name.each do |vroum|
		write << [vroum]
	end
end
CSV.open("price.csv", 'w', write_headers: :true, headers: "Time") do |add|
	motorcycle_price.each do |price|
		add << [price]
	end
end