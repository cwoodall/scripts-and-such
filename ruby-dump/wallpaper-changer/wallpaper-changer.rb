# Wallpaper Changer
# Christopher J. Woodall
require 'rubygems'
require 'appscript'
include Appscript
include MacTypes

base_dir = "/Users/cwoodall/Pictures/Wallpaper/"
backgrounds = Dir.glob("#{base_dir}/*.jpg")
# while 1
#   time = Time.now
#   puts time.hour
#   if time.hour > 12
#     app('Finder').desktop_picture.set(MacTypes::FileURL.path(backgrounds[1]))
#   end
#   sleep(10)
# end

while 1
  backgrounds.each do |background|
    # Set desktop background to whatever is in path
    app('Finder').desktop_picture.set(MacTypes::FileURL.path(background))
    sleep(10)
  end
end
