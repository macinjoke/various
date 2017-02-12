class Project < ActiveRecord::Base
  has_many :tasks
  validates :title,
  presence: { message: "titleは必須です"},
  length: { minimum: 3, message: "3文字以上にしてください" }
end
