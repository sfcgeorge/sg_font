# Just run `ruby generator.rb`

upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
chars = %w(period comma apostrophe quote semicolon colon question exclamation interrobang hyphen underscore forwardslash backslash pipe lbracket rbracket lsquare rsquare lbrace rbrace at hash pound dollar percent hat ampersand star plus equals tilde tick less more)

def generate(kind, mapping)
  characters = []
  File.open("#{kind}.txt") do |file|
    file.each do |line|
      characters << [] && next if line == "\n"
      characters.last << line
    end
  end

  characters.each_with_index do |char, i|
    charstr = char.join("").gsub("\n", "n")
    cmd = "vector_salad -f character.rb \"#{charstr}\" > characters/#{kind}_#{mapping[i]}.svg"
    puts cmd
    `#{cmd}`
  end
end

generate("upper", upper)
generate("lowerbig", lower)
generate("numbers", numbers)
generate("chars", chars)
