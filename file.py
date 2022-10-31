import tweepy

#Keys
APIKey = "j8juQnDMcjJam6O7htT6AGkd1"
APISecret = "40HkmNCihW9VtIUhfr3kM2XBpUMzUklMdaRXzD6vkl5p25p5Br"

ClientKey = "1507575497789779971-9nSmm9ZV0MMKdzVhAtRyM8nyrxXvlC"
ClientSecret = "T4kY1YgMnOHmFpjFJZPPrrOBYNLXJL6Xxoe13sqPlGvLc"

#Conectando o sistema ao Twitter
auth = tweepy.OAuthHandler(APIKey, APISecret)
auth.set_access_token(ClientKey, ClientSecret)

