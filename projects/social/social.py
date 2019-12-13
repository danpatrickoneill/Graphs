import random
from util import names, Stack, Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            # return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            # return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            # return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        if avgFriendships >= numUsers:
            print("Error: number of users must be greater than average number of friendships.")
            return
        # Add users
        for i in range(numUsers):
            self.add_user(random.choice(names))

        # Create friendships
        total_friendships = (numUsers * avgFriendships) // 2
        # count = 0
        # while (count < total_friendships):
        #     friend_one = random.randint(1, numUsers - 1)
        #     # print(numUsers, friend_one)
        #     if self.add_friendship(friend_one, random.randint(friend_one + 1, numUsers)):
        #         count += 1
        potential_friendships = []
        for i in range(1, numUsers):
            for j in range(i+1, numUsers + 1):
                potential_friendships.append((i, j))
        print(potential_friendships)
        random.shuffle(potential_friendships)
        for pair in potential_friendships[:total_friendships]:
            self.add_friendship(pair[0], pair[1])


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set

        queue = Queue()
        queue.enqueue([user_id])
        while queue.size():
            path = queue.dequeue()
            user = path[-1]
            if user not in visited:
                visited[user] = path

                for friend in self.friendships[user]:
                    new_path = path.copy()
                    new_path.append(friend)
                    queue.enqueue(new_path)
        visited_names = {self.users[key].name: [self.users[num].name for num in visited[key]] for key in visited}
        print(visited_names)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
