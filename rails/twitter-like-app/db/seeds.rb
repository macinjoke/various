# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ name: 'Chicago' }, { name: 'Copenhagen' }])
#   Mayor.create(name: 'Emanuel', city: cities.first)

@user = User.new
@user.name = 'Tonkatu Tarou'
@user.username = 'tonkatu05'
@user.location = 'Hokkaido, Japan'
@user.about = 'Hello! Nice to meet you.'
@user.save

@user = User.new
@user.name = 'Alice Assange'
@user.username = 'alice'
@user.location = 'Tottori, Japan'
@user.about = 'I\'m free'
@user.save

