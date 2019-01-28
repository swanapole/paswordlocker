class User:
    """
    Class that generates new instances of users
    """
    user_list=[]

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def save_user(self):
        """
        save_user method saves user objects into the user_list
        """
        User.user_list.append(self)

    @classmethod
    def user_exists(cls,characters):
        """
        user_exists method that checks is a user exists from the user list
        args:
            characters:password to search if the user exists
        returns:
            boolean:true or false depending on the condition
        """
        for user in cls.user_list:
            if user.password == characters:
                return True

        return False
