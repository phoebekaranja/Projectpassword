class User:
    """
    Class that generates new instances of users
    """
    users_list = [] # Empty users list

    def __init__(self,first_name,last_name,password):
        '''
        defining structure of the user object
        '''
      # docstring removed for simplicity
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
