#!/usr/bin/ruby
##
# Name: poster.rb
# Purpose: Manages blog posts for a tumblr blog
# Date: December 31, 2010
#
# Developer: Christopher Woodall <chris.j.woodall at gmail.com>
# Copyright: Apache License 2.0
##

# Gems
require 'rubygems'
require 'bundler/setup' # Bundler Support
require 'maruku' # For markdown parsing

# Standard Libraries
require 'date'
require 'ftools' 
require 'optparse'

# Poster Libraries
require 'poster_lib'

program_name = 'poster.rb'
date = DateTime.now

defaults = nil
# Config File
File.open( "#{ENV['HOME']}/.poster", "w+" ) do |conf_file|
	conf = read_file conf_file
	if conf == ''
		conf_file.puts "author: - blank"
		conf_file.puts "company: - blank"
		conf_file.puts "post_location: - #{ENV['HOME']}/posts"
		conf_file.rewind
		conf = read_file conf_file
	end
	defaults = {}
	YAML.load(conf).each {|key, item| defaults[key.to_sym] = item} 
	puts defaults[:post_location]
end

# Parse the arguments
options = {}
optparse = OptionParser.new do |opts|
	opts.banner = "Usage: #{program_name} [options]"
	
	options[:create] = false
	opts.on( '-c', '--create', 'Flag to create a markdown post' ) do
		options[:create] = true
	end
	
	options[:format] = false
	opts.on( '-f', '--format FORMAT_TYPE', 'Creates a formatted file (Options: html or latex)') do |format|
		options[:format] = format
	end
	
	options[:post] = false
	opts.on( '-p', '--post POST_NAME', 'Sets the post name') do |post|
		options[:post] = post
	end
	
	options[:author] = defaults[:author]
	opts.on( '-a', '--author AUTHOR_NAME', 'Sets the author name (Default: blank)') do |author_name|
		options[:author] = author_name
	end
	
	opts.on( '-h', '--help', 'Display this screen' ) do
		puts opts
		exit
	end
end
optparse.parse!


if options[:post]
	post_name = options[:post]
else
	puts 'Name of post? '
	post_name = gets.chomp
end

file_path = "#{defaults[:post_location]}/#{post_name}"
	
File.makedirs "#{defaults[:post_location]}"
if options[:create]
	# Make the directory and then make the file and fill it with starter information
	File.open("#{file_path}.md", 'w') do |file|
		file.puts "# #{post_name}"
		file.puts 
		file.puts "Author: #{options[:author]}"
		file.puts
		file.puts '(content goes here)'
		file.puts 
		file.puts "(c) Happy Robot Labs #{date.year.to_s}"
	end
elsif options[:format]
	File.open("#{file_path}.md", 'r') do |file|
		File.open(file_path + '.' + options[:format].downcase, 'w') do |wfile|
			# Read all of the blog post into md_string then close the blog post
			md_string = read_file file
			file.close

			# Format and write the blog post into HTML or a PDF
			case options[:format].downcase
			when 'html'
				wfile.puts Maruku.new(md_string).to_html
			when 'latex'
				wfile.puts Maruku.new(md_string).to_latex
			end
		end
	end
end