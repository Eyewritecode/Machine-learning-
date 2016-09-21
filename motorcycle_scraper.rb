require 'Nokogiri'
require 'HTTParty'
require 'pry'
require 'json'
require 'csv'

motorcycles_listing = HTTParty.get("https://osaka.craigslist.jp/search/mca?lang=en&cc=us&query=motorcycles")

nokoObj = Nokogiri::HTML(motorcycles_listing)

motorcycle_name = []
motorcycle_price=[]
posted_on = []
nokoObj.css(".rows").css(".row").css(".hdrlnk").map do |tags|
	brand = tags.text
	motorcycle_name.push(brand)
end

nokoObj.css(".rows").css(".row").css(".l2").css(".price").map do |price|
	if price
		buy_at = price.text
	else
		buy_at = "N/A"
	end
	motorcycle_price.push(buy_at)
end
nokoObj.css(".rows").css(".row").css("time").map do |date|
	if date
		listing_date = date.text
	else
		listing_date = "N/A"
	end
	posted_on.push(listing_date)
end

motorcycles = Hash[motorcycle_name.zip posted_on]

#Pry.start(binding)
CSV.open("motorcycles.csv", 'w', write_headers: :true, headers: ["Brand Name", "Posted on", "Price"]) do |write|
	motorcycles.each do |vroum|
		write << vroum
	end
end
CSV.open("price.csv", 'w',write_headers: :true, headers: ["Price"]) do |price|
	motorcycle_price.each do |tst|
		if !tst.valid_encoding?
			tst = tst.encode("ISO-8859-1", invalid: :replace, replace: "?").encode('UTF-8')
		end
		price << [tst]
	end
end