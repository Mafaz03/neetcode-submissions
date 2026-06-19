class Twitter:

    def __init__(self):
        self.dq = deque([])
        self.follow_hash = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        if userId not in self.follow_hash: 
            self.follow_hash[userId] = {userId}
        
        self.dq.append((tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = []
        
        for tweetId, authorId in reversed(self.dq):
            if authorId in self.follow_hash[userId]:
                posts.append(tweetId)
                
            if len(posts) == 10: break
        
        return posts

    def follow(self, followerId: int, followeeId: int) -> None:
        # self.follow(1, 2) user 1 follows user 2

        if followerId not in self.follow_hash:
            self.follow_hash[followerId] = {followerId, followeeId}

        if followeeId not in self.follow_hash[followerId]:
            self.follow_hash[followerId].add(followeeId)
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        # self.unfollow(1, 2) user 1 unfollows user 2

        if followerId in self.follow_hash:
            if followeeId in self.follow_hash[followerId] and followerId != followeeId:
                self.follow_hash[followerId].remove(followeeId)