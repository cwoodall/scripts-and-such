#!/usr/bin/ruby
##
# Name: poster_lib.rb
# Purpose: Libary for poster.rb
# Date: December 31, 2010
#
# Developer: Christopher Woodall <chris.j.woodall at gmail.com>
# Copyright: Apache License 2.0
##

def read_file( file )
	begin
		md_string = ''
		while (line = file.gets) do
			md_string += line
		end
	rescue => err
		puts "Exception: #{err}"
		err
	end
	return md_string
end
