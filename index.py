import facebook

token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'


# Postare pe pagina in numele paginii
#fb.put_object(parent_object='me', connection_name='feed', message='hello')
#fb.put_photo(image=open('postare.jpg', 'rb'), message='photo!')

# class FacebookUser():

   def post_on_facebook(self, token):
      fb = facebook.GraphAPI(access_token=token)
# post object
#      fb.put_object(parent_object='me', connection_name='feed', message='hello')
# post photo
#      fb.put_photo(image=open('postare.jpg', 'rb'), message='photo!')


text_file = open("tokens.txt", "r")
lines = text_file.read().split()
print(lines)
print(len(lines))
text_file.close()

#user = FacebookUser()
i = 0
while i < len(lines):
  print(lines[i])
  i = + 1
  user.post_on_facebook(lines[i])
   
