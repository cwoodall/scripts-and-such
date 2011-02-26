# Poster

Open-Source Blog Post manager written in Ruby

**THIS IS PRE-ALPHA SOFTWARE AND SHOULD BE TREATED ACCORDINGLY.**

## Installation & Setup

The dependencies for this script are:

- [Maruku](http://maruku.rubyforge.org/)

To install these dependencies you can use [bundler](http://www.gembundler.com) by 
changing to the appropriate directory in the appropriate directory and executing 
this code:

> $ gem install bundle # Unnecessary if bundler gem is already installed
> $ bundle install

Currently its just a script so you can run it like this:

> $ chmod +x poster.rb  
> $ ./poster.rb -p "Post Name" -c

or like this, if you don't want to change permissions:

> $ ruby poster.rb -p "Post Name" -c

You can now install poster using rake (will install to /usr/local/bin). 

** WARNING: Rakefile is not complete or well formed. Use at your own risk. Do not 
use on Windows **

> $ rake  
> $ rake install  

Now you can run the program as

> $ poster [options]

## Contributing to Poster

Feel free to contribute, please get in contact with me if you do want to contribute

## Resources

Libraries:

- [Maruku](http://maruku.rubyforge.org/)

My info:

- [Blog](http://www.happyrobotlabs.com)

- [Twitter](http://www.twitter.com/#!/cjwoodall92)