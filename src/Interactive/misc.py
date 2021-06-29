import random

class Templates():
    
    @staticmethod
    def get_random_new_group_member_welcome_message(type='text'):

        if type == 'text':
            welcome_new_user = ["[username] just joined the group - glhf!",
                            "[username] just joined. Everyone, look busy!",
                            "[username] just joined. Can I get a heal?",
                            "[username] joined your party.",
                            "[username] joined. You must construct additional pylons.",
                            "Ermagherd. [username] is here.",
                            "Welcome, [username]. Stay awhile and listen.",
                            "Welcome, [username]. We were expecting you ( ͡° ͜ʖ ͡°)",
                            "Welcome, [username]. We hope you brought pizza.",
                            "Welcome [username]. Leave your weapons by the door.",
                            "A wild [username] appeared.",
                            "Swoooosh. [username] just landed.",
                            "Brace yourselves. [username] just joined the group.",
                            "[username] just joined. Hide your bananas.",
                            "[username] just arrived. Seems OP - please nerf.",
                            "[username] just slid into the group.",
                            "A [username] has spawned in the group.",
                            "Big [username] showed up!",
                            "Where’s [username]? In the group!",
                            "[username] hopped into the group. Kangaroo!!",
                            "[username] just showed up. Hold my beer.",
                            "Challenger approaching - [username] has appeared!",
                            "It's a bird! It's a plane! Nevermind, it's just [username].",
                            "It's [username]! Praise the sun! \\\\[T]/",
                            "Never gonna give [username] up. Never gonna let [username] down.",
                            "Ha! [username] has joined! You activated my trap card!",
                            "Cheers, love! [username]'s here!",
                            "Hey! Listen! [username] has joined!",
                            "We've been expecting you [username]",
                            "It's dangerous to go alone, take [username]!",
                            "[username] has joined the group! It's super effective!",
                            "Cheers, love! [username] is here!",
                            "[username] is here, as the prophecy foretold.",
                            "[username] has arrived. Party's over.",
                            "Ready player [username]",
                            "[username] is here to kick butt and chew bubblegum. And [username] is all out of gum.",
                            "Hello. Is it [username] you're looking for?",
                            "[username] has joined. Stay a while and listen!",
                            "Roses are red, violets are blue, [username] joined this group with you",
                            "Hi [username]! Welcome to our community❤️"]

            return welcome_new_user[random.randint(0, len(welcome_new_user)-1)]