require 'rubygems'
require 'twitter'
require 'json'
require 'oauth'

Twitter.configure do |config|
  config.consumer_key = 'Lmu8u069qHXTAhufn2Q'
  config.consumer_secret = 'vuniu1cchXCVyY0SIO6jhTlsM0gEodHx83r5un1t4'
  config.oauth_token = '223154110-QXVs8CYsMxSJZDtPq30JMqPDnmsEokQtBohu7upD'
  config.oauth_token_secret = 'lxKOqBczLPXmwp3Y6mKpsl05N5JWwiRDWqvyv6nCASc'
end

puts Twitter.friends.users.sort{|a, b| a.followers_count <=> b.followers_count}.reverse.first.name
