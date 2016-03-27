json.array!(@users) do |user|
  json.extract! user, :id, :username, :email, :expect_date
  json.url user_url(user, format: :json)
end
