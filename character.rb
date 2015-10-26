character = ARGV[0].split("n")
U = 100
Numeric.unit = U

custom(:block) do |**_|
  square(U)
end

custom(:topleft) do |**_|
  intersection do
    block
    circle(U)[U, U]
  end
end

custom(:topright) do |**_|
  topleft.rotate(90)[0, 0]
end

custom(:bottomright) do |**_|
  topright.rotate(90)[0, 0]
end

custom(:bottomleft) do |**_|
  bottomright.rotate(90)[0, 0]
end

union do
  character.each_with_index do |line, row|
    line.split("").each_with_index do |shape, col|
      case shape
      when "0"
        block[~col, ~row]
      when "1"
        topleft[~col, ~row]
      when "2"
        topright[~col, ~row]
      when "3"
        bottomright[~col, ~row]
      when "4"
        bottomleft[~col, ~row]
      end
    end
  end
end
