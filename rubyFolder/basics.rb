counter = 1

puts "Using loop: util"
until counter > 10
  puts counter
  counter += 1
end

puts "using loop: for"
for num in 1..10
  puts num
end 

puts "using loop: loop do -> break"
i = 20
loop do
  i -= 1
print  "#{i}"+ " "
  break if i <= 0
end

