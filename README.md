# Robots_VS_Dinosaurs

Welcome to Robots vs Dinosaurs.  This is where you'll pick one or the other and try to bash them!  Let's be honest, the dinosaurs should win every time.  


***
 
 A note:
    I severely struggled after a certain point here.  I was going good, writing things out but I was working backwards (from my smaller classes up to my larger ones.)  In putting it all together up and up, I kept getting lost in the .notation and what was where and I really started struggling.  I would fix one thing just to find that it messed up another.  Unfortunately, I started struggling when I should have been in the home stretch.  So I scrapped it all.  Started from scratch, went slow, and just got something that worked that was "technically" correct.  BUT that was not up to my standards.  So to redo I go.  2.0 notes below.

***

# Robots vs Dinosaurs 2.0

***

- My plan in reworking is to start small.  Add small changes that I think I can easily handle without ENTIRELY breaking what I have.  My first step will be to add defense and energy because that seems like simple calculating and variables.  
      - added stamina and a defense stat for each creature.  Defense is working, stamina is being calulated correctly but not currently being utilized.

- I want to add other weapons for the robots.  Not as a choice yet, but give them each different ones.   
   - robots are now assigned random weapons before the battle.  I've learned that even concatenating in Python is different!  

- Since I did different weapons for the robots, next will be different attacks for the dinos to make the battle more random.  For now, it will stay running its course on its own, but slowly it will change.  
   - I did the dinos a bit differently.  Their attacks are random each turn.  I added a shield to the robots and adjusted their numbers so victory is less certain for either side and moreso a result of "the card they're dealt".  I know a lot of these things are not even remotely in the user stories, but they're helping me to learn.

- Next I want to add different types of list for the player to pick from of robots and dinosaurs
   - Added multiple fleet/herd choices to pick from.  