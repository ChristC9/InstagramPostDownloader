from instaloader.instaloader import Instaloader
from instaloader.structures import Post
import os 
from dotenv import load_dotenv

# This is using the environment variables to login to the instagram account.
load_dotenv()
ig=Instaloader()

# This is using the environment variables to login to the instagram account.
ig.login(user=os.environ.get('IG_USER_NAME'),passwd=os.environ.get('IG_PW'))

# This is splitting the url that you have entered and storing the values in the list.
url_list=[]
url=input('Enter Url That You Want To Download For Post : ')
url_list=url.split('/')

# print(url_list)
# This is fetching the account name and shortcode from the url that you have entered.
account_name=url_list[3]
shortcode=url_list[5]


# This is fetching the post data from the instagram server.
post_data=Post.from_shortcode(ig.context,shortcode)

# This is downloading the post and saving it in the folder that you have specified.
ig.download_post(post=post_data,target=account_name)