class StringManipulation:

    
    # Create Class Constructor
    def __init__(self,wlist):
        # Assign input list data to object variable
        self.wlist=wlist[:]


    # Create class method words_of_length
    def words_of_length(self,length):
        # initialize empty list
        res = []
        # read all word from list
        for i in self.wlist:
            # Check length of each word is equal to 'length' value
            if len(i)==length:
                # Append word in res list
                res.append(i)
        return res


    # Creare class method words_starts_with
    def words_starts_with(self,char):
        # initialize empty list
        res = []
        # read all word from list
        for i in self.wlist:
            # Check first character of each word is equal to 'char' value
            if i[0]==char:
                # Append word is res list
                res.append(i)
        return res

    # Create class method words_ends_with
    def words_ends_with(self,char):
        # initialize empty list
        res = []
        # read all word from list
        for i in self.wlsit:
            # Check last character of each words is equal to 'char' value
            if i[-1]==char:
                # Append word is res list
                res.append(i)
        return res

    # Create class method Pallindromes
    def Pallindromes(self):
        # initialize empty list
        res = []
        # read all word from list
        for i in self.wlist:
            # Check each word is equal to reverse of theat word
            if i==i[::-1]:
                # Append word in res list
                res.append(i)
        return res

    # Create class method Total_words
    def Total_words(self):
        # return length of list
        return len(self.wlist)

    # Create class method Longedt_word
    def Longest_word(self):
        # Assume first word is maximum length word
        maxword = self.wlist[0]
        # Read all word from list one by one
        for i in self.wlist:
            # Check each word length is greater that the length of maxword
            if len(i)>len(maxword):
                # If yes then assign maxword to a new word
                maxword=i
        return maxword

    # Create class method Longedt_word
    def Smallest_word(self):
        # Assume first word is minimum length word
        minword = self.wlist[0]
        # Read all word from list one by one
        for i in self.wlist:
            # Check each word length is smaller that the length of maxword
            if len(i)<len(minword):
                # If yes then assign minword to a new word
                minword=i
        return minword

    # Create class method Count
    def Count(self,word):
        # Return count value of 'word' in list
        return self.wlist.count(word)