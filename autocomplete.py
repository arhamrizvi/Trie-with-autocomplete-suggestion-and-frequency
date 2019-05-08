class Node:
    def __init__(self):
        self.child = 27 * [None] #each node is basically an array of size 27
        self.end = False #marks the end of a word
        self.count = 0 #to keep track of the count


class Trie:
    def __init__(self):
        self.root = Node() #root node

    # function for count
    def count(self, prefix):
        node = self.root

        for c in prefix:
            # convert
            char = ord(c) - ord('a')
            #print(char)
            # if character is present
            if node.child[char]:
                # move
                node = node.child[char]
            else:
                # create
                node.child[char] = Node()
                # move on
                node = node.child[char]
        return node.count

    #insert a word(key) into the trie
    def insert(self, key):
        node = self.root

        for c in key[0]:
            # convert
            char = ord(c) - ord('a')

            # word = key[0]
            # frequency = key[1]
            # definition = key[2]

            # last position has nothing
            if node.child[26] is None:
                node.child[26] = (key[1], char) #add the frequency and the link
            else:
                #last position has something, compare the frequency
                if key[1] == node.child[26][0]: #if frequency the same
                    if type(node.child[26][1]) == int: #if same type, meaning its just int and not the definition
                        if char < node.child[26][1]: #if char(link) is lower than the one stored already
                            node.child[26] = (key[1], char) #add freq and the link

                if key[1] > node.child[26][0]: #if frequency is greater than the one stored
                    node.child[26] = (key[1], char) #store the frequency and the link

            # if character is present
            if node.child[char]:
                # move or go to that char
                node = node.child[char]
            else:
                # create
                node.child[char] = Node()
                # move on
                node = node.child[char]
            #increment the count
            node.count += 1
        # mark it as end
        node.end = True
        # contains the freq and definition
        node.child[26] = (key[1], key[2])
        # increment the overall count
        self.root.count += 1


    # for retrieval of the word
    def auto(self, prefix):

        # start of root
        node = self.root

        # if string entered isnt empty
        if prefix != "":
            for i in prefix:
                # convert
                char = ord(i) - ord('a')
                # if character isnt present
                if not node.child[char]:
                    return ""
                # move on
                node = node.child[char]


        # if the types are not the same as in, you havent reached the definition
        while type(node.child[26][1])!=str:
            char = node.child[26][1]  # look at the 2nd value of the tuple
            a = char + ord('a')  # convert to ascii value
            a = chr(a)  # convert the ascii code to character
            prefix += a # add the letter to the prefix entered
            node = node.child[char] # move
        # return the prefix with the definition
        return (prefix,str(node.child[26][1]))




if __name__ == '__main__':

    #name = 'Dictionary.txt'
    name = 'bigger_dictionary.txt'
    t = Trie()

    file = open(name, 'r') #read the file in
    while True:
        word = file.readline().strip('\n')
        if word == "": #when theres no word
            break
        freq = file.readline().strip('\n')
        define = file.readline().strip('\n')
        file.readline()
        word = word.split(": ",1)
        freq = freq.split(": ",1)
        define = define.split(": ",1)
        t.insert([str(word[1]),int(freq[1]),str(define[1])])



    # ask user to enter a prefix
    prefix = input("Enter a prefix: ")

    while prefix!="***":
        try:
            # get the suggested word
            print("Auto-complete suggestion: "+t.auto(prefix)[0])
            # get the definition
            print("Definition: "+t.auto(prefix)[1])
            # get the count
            print("There are " + str(t.count(prefix)) + " words in the dictionary that have " + prefix + " as a prefix")
        except:
            # The word isnt there
            print("\nThere is no word in the dictionary that has " + prefix + " as a prefix")

        # ask user to enter a prefix
        prefix = input("\nEnter a prefix: ")

    print("Bye Alice!")