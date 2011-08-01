# This program makes people happy 
#
# Author:: Christopher Woodall <chris.j.woodall at gmail.com>
# Copyright:: Copyright (c) July 2011 Christopher Woodall
# License:: MIT License

# A human being
class Person
  attr_reader :name, :status, :description

  def initialize(name, status, description)
    @name = name
    @status = status
    @description = description
  end

  def to_s
    "#{@name} is #{@status.to_s}"
  end

  def describe
    "#{@name} [#{@status.to_s}]: #{@description}"
  end
  # receives a message an optionally a person
  # if you are receiving a hug the persons status
  # will be changed to happy
  def hug(message, recipient=nil)
    if message == :receive
      @status = :happy
    elsif message == :give
      raise "ERROR: no recipient" if recipient == nil
      raise "ERROR: Recipient is an ALIEN... May be dangerous to hug" unless recipient.kind_of? Person
      recipient.hug :receive
    else
      raise "ERROR: Person @{@name} received an unrecognized message #{message}"
    end
  end
end

# Just a message for giving hugs easier, even if these hugs are from
# an unknown person
def give_hug_to (person)
  raise "ERROR: person must be a Person object" unless person.kind_of? Person
  
  person.hug :receive
end

# Lets define some people. If you were left out I am sorry
people = [ Person.new("Christopher Woodall", :neutral, "A pretty cool cat"),
           Person.new("Simon Mandic", :chilling, "Also pretty awesome"),
           Person.new("Kaity Reilly", :awesome, "<-- The status says it all"),
           Person.new("Gabriel Begun", :chilling, "Innovative? Probably. Living? To the fullest"),
           Person.new("Evan Kaloudis", :busy, "Too busy, editing, music, reviews"),
           Person.new("Everyone Else", :sad, "Everyone in the world")]

# Perform the hugging from the anonymous ruby gods
people.each do |person|
  puts
  puts person.describe
  puts "#{person.name} receiving hug"
  give_hug_to person
  puts person
  puts
end

## Output:
# Christopher Woodall [neutral]: A pretty cool cat
# Christopher Woodall receiving hug
# Christopher Woodall is happy
#
#
# Simon Mandic [chilling]: Also pretty awesome
# Simon Mandic receiving hug
# Simon Mandic is happy
#
#
# Kaity Reilly [awesome]: <-- The status says it all
# Kaity Reilly receiving hug
# Kaity Reilly is happy
#
#
# Gabriel Begun [chilling]: Innovative? Probably. Living? To the fullest
# Gabriel Begun receiving hug
# Gabriel Begun is happy
#
#
# Evan Kaloudis [busy]: Too busy, editing, music, reviews
# Evan Kaloudis receiving hug
# Evan Kaloudis is happy
#
#
# Everyone Else [sad]: Everyone in the world
# Everyone Else receiving hug
# Everyone Else is happy
