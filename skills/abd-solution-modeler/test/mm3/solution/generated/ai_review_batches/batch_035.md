# Hypothesis concept review – batch 35

## Classification instructions

For each concept below, read its referenced chunks and classify:

| Classification | Meaning |
|----------------|---------|
| **real** | Genuine domain concept with clear identity |
| **amalgamation** | Two loosely related concepts merged; should be split |
| **instance** | Example of a concept (add type property or state) |
| **subtype** | Should be under a parent in concept_hierarchy |
| **false_positive** | Chunk doesn't support the concept; remove or fix chunk_ids |

Output format (one block per concept):
```
Concept: <name>
Classification: <real|amalgamation|instance|subtype|false_positive>
Parent (if subtype): <parent concept name or "">
Suggested change: <brief description>
```


---

## Concept: Rook

Chunk count: 2
Performs actions: ['act_0411']

### Chunk texts

**Chunk 1** (`b6064e74b184`):

```
CHAPTER 8: ACTION & ADVENTURE

241

The following is an example of the M&M rules in action during a conflict scene.

Three heroes: Princess, Rook, (see pages 50-53) and Ultramarine (a battlesuit wearer), tipped-off by one of Rook’s contacts
about smugglers unloading a shipment down at the docks late at night, have staked-out the vessel. Once they see the
smugglers moving the goods, Rook signals it is time to move in and take them down!

ROUND 1

Gamemaster (GM): Okay, everyone, make an initiative check.

The players of Princess, Rook, and Ultramarine each roll the die, adding their character’s initiative modifier and getting the fol-
lowing results: Ultramarine: 13, Rook: 11, Princess: 26!

The GM rolls one initiative check for the smugglers (with an initiative modifier of +0), getting a result of 11. Although Rook has
the same result, he has a higher initiative modifier (+5) and so will go before the smugglers. The GM also rolls a secret initiative
check result of 16 for something the players don’t know yet...

GM: Okay, you get the “go” signal from Rook and leap into action! (Looking at the initiative count) Princess, what do you
do?

Princess: I jump from the pier onto the deck of the ship as my move action, landing right in front of all the smugglers
and say, “You guys want to just give up now and save yourselves a beating? Please feel free to say no.” Then I give them a
big smile.

GM: You want to try and intimidate them? That’s a standard action. You want to make it a routine check?

Princess: No, I’ll roll for it. Princess’ player rolls an Intimidation check with her bonus of +6. I got a 16 anyway, same as my
routine check result!.

The GM compares Princess’ result to the smugglers’ Will defense, which is 12. Her check succeeded with one degree. The smug-
glers are impaired (–2 on their checks) until the end of Princess’ next turn.

GM: The smugglers look shocked at your sudden appearance and hesitate, clearly shaken. Ultramarine, it’s your turn.

Ultramarine: Like shooting fish in a barrel… I surge up out of the water on the other side of the ship and fly up to the
deck (move action) then level the arm with my netline primed at the smugglers, my voice amplified by the speakers in my
suit. “Or you can call it quits right now.”

GM: You going for the Intimidation check, too?

Ultramarine: No, I think I’d rather ready an attack with my netline, if any of the smugglers decide to get stupid, then wait
to see what happens. That’s a standard action, right

[... truncated ...]
```

**Chunk 2** (`eab98ce0e1fc`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Hero: ____________________________________     Player: ____________________________

The Rook

Jon

Gender: _____________     Age: ________    Height: ____________     Weight: _____________     Eyes: ___________________     Hair: _____________________

Male

31

6’0”

Identity: _______________________________________________  (cid:80)(cid:3)Secret (cid:80)(cid:3)Public
Jack Cooper      X
Blue

195 lbs

Brown

Group Affiliation: ________________________________     Base of Operations: ______________________________________     Power Level: ________

None

26  150
Power Point Totals: Abilities _________+ Powers _________+ Advantages _________+ Skills _________+ Defenses _________= ___________

68

8

Emerald City
19
29

Strength

Stamina

3
3

Agility

Dexterity

5
5

Fighting

Intellect

8
5

Awareness

Presence

2
3

Offense

Initiative

+5

Unarmed

+15  Close, Damage 3

Fighting Staff  +15  Close, Damage 5, Reach 1

Rook’s Talons  +15  Ranged, Damage 5

Defense

Dodge (agl)

Parry (FGT)

Fortitude (STA)

Toughness (STA)

Will (awe)

14
14
8
6
/
3*
8

*Without Defensive Roll.

Benefit 4 (Multi-
millionaire), Defensive Roll
3, Equipment 6, Inventor, Jack-of-all-
trades, Move-by Action, Power Attack,
Quick Draw, Well-informed

Advantages

Skills

Acrobatics 5 (+10), Athletics 5
(+8), Close Combat: Unarmed 7
(+15), Intimidation 6 (+9), Investigation 1
(+6), Perception 6 (+8), Ranged Combat:
Throwing 10 (+15), Sleight of Hand 3
(+8), Stealth 8 (+13), Technology 5
(+10), Treatment 1 (+6), Vehicles 1 (+6)

Fall), Removable (–2 points) • 6 points

• Flash Bombs: Ranged Burst Area Affliction 3 (Resisted by Fortitude; Vision

Powers & Devices
____________________________________________________________________________________________________________________________________________
Cowl: Senses 3 (Extended Vision, Low-Light Vision, Radio), Removable (–1 point) • 2 points
____________________________________________________________________________________________________________________________________________
Wings of the Rook: Flight 5 (60 MPH), Subtle (sound baffling), Wings; Movement 1 (Safe
____________________________________________________________________________________________________________________________________________
Flashlight: Feature 1 (Illumination) • 1 point      Mini-Tracers: Feature 1 (Tracking) • 1 point
___________________________________________________________

[... truncated ...]
```

---

## Concept: Routine

Chunk count: 4
Performs actions: ['act_0018', 'act_0268', 'act_0433', 'act_0437']

### Chunk texts

**Chunk 1** (`086d54227650`):

```
CHAPTER 8: ACTION & ADVENTURE
CHAPTER 8: ACTION & ADVENTURE

CHAPTER 8: ACTION & ADVENTURE

Certain advantages and effects may enhance or work in
conjunction  with  certain  maneuvers.  See  their  descrip-
tions for details.

nuses  cannot  more  than  double. The  changes  to  attack
and  defense  bonus  last  until  the  start  of  your  next  turn.
This maneuver does not apply to effects requiring no at-
tack check or allowing no resistance check.

When you make an attack, you can take a penalty of up to
–2 on the effect modifier of the attack and add the same
number (up to +2) to your attack bonus. Your effect modi-
fier cannot be reduced below +0 and your attack bonus
cannot more than double in this way. The changes are de-
clared before you make the attack check and last until the
start of your next turn.

ATTACK

When  you  make  an  attack  you  can  take  a  penalty  of  up
to –2 on your active defenses (Dodge and Parry) and add
the  same  number  (up  to  +2)  to  your  attack  bonus. Your
defense bonuses cannot be reduced below +0 and your
attack  bonus  cannot  more  than  double. The  changes  to
attack and defense bonus are declared before you make
the attack check and last until the start of your next turn.

When you make an attack you can take a penalty of up to
–2 on your attack bonus and add the same number (up to
+2) to your active defenses (Dodge and Parry). Your attack
bonus cannot be reduced below +0 and your defense bo-

You can use Intimidation in combat as a standard action
to undermine an opponent’s confidence. Make an Intimi-
dation check as a standard action opposed by the better
of your target’s Insight or Will defense. If your Intimidation
check succeeds, your target is impaired (a –2 circumstance
penalty on checks) until the end of your next round. With
four or more degrees of success, the target is disabled (a
–5 penalty) until the end of your next round.

FEINT

You can use Deception as a standard action to mislead an
opponent in combat. Make a Deception check as a stan-
dard action opposed by the better of your target’s Decep-
tion or Insight. If your Deception check succeeds, the tar-
get is vulnerable against your next attack, until the end of
your next round (see Vulnerable in the Conditions sec-
tion of The Basics chapter).

When you attack a defenseless target at close range, you
can  choose  to  make  the  attack  as  a  routine  check  (see
Routine  Checks  in  The  Basics  chapter).  This  generally

```

**Chunk 2** (`179f10a90f72`):

```
CHAPTER 2: SECRET ORIGINS

23

nuses for your character, paying 1 power point per +1 de-
fense over the base rank provided by your hero’s abilities.
To improve your hero’s Toughness, see Advantages and
Powers, following. See the Abilities chapter for details.
5. SKILLS

Choose  the  skill  ranks  you  want  your  character  to  have
and pay 1 power point per 2 total skill ranks. See the Skills
chapter for details.

6. ADVANTAGES

Choose the advantages you want your character to have
and pay 1 power point per advantage or rank in a advan-
tage. See the Advantages chapter for details.

7. POWERS

Create  your  hero’s  powers  by  choosing  their  desired  ef-
fects  and  paying  the  effects’  base  cost,  adjusted  for  any
modifiers, and multiplied by the number of ranks. See the
Powers chapter for details.
8. COMPLICATIONS

Choose at least two complications for your hero. You can
have more, if you want, and the more complications your
hero  faces,  the  greater  your  chances  for  earning  hero

points during the game. See the Complications section
of this chapter for details.
9. DETAILS

Go  through  the  limits  listed  under  Power  Level  in  this
chapter and make sure your hero’s traits all fit within them.
If not, adjust the traits accordingly until they do.

Go back through and add up the costs of your hero’s abili-
ties, defenses, skills, advantages, and powers. You should
end  up  with  a  figure  equal  to  the  starting  power  points
shown on the Starting Power Points table. If not, double-
check your math and either remove or add traits to your
character to reach the starting power point total.

Figure out things like your hero’s name, appearance, origin,
background, and motivation. If you can, consider creating a
sketch or detailed description of your hero’s costume.

10. GAMEMASTER APPROVAL

Show your new hero to the Gamemaster for approval. The
GM should check again to make sure your power points
are  spent  and  added  up  correctly,  your  hero  follows  the
power  level  guidelines  and  any  other  guidelines  set  for
the  series,  and  that  the  character  is  generally  complete
and  suited  to  the  overall  game.  Once  your  GM  has  ap-
proved, your new hero is ready for play!

You design a MUTANTS & MASTERMINDS hero by spending pow-
er points on different traits. Each ability, skill, advantage,
power, and other trait has an associated power point cost.

The game’s power level provides a guideline for how many
power points you

[... truncated ...]
```

**Chunk 3** (`b054d3b34f13`):

```
CHAPTER 6: POWERS

173

Precise: If you can Nullify multiple effects, this modifier al-
lows you to choose which are nullified and which are not.
Flat +1 point.

Randomize: Rather than being countered, the effect(s) tar-
geted by your Nullify acquire the Uncontrolled flaw and go
out of control (as dictated by the GM). +0 cost per rank.

Selective: If you have an Area Nullify effect, this extra al-
lows you to choose who in the area is affected, nullifying
some targets and not others. +1 cost per rank.

Sustained:  If  this  modifier  is  applied  to  Concentration
Nullify, keeping the countered effect(s) suppressed is only
a free action for you each turn. +1 cost per rank.

FLAWS

Side Effect: If you fail to nullify an effect, you might suffer
some kind of “backlash” or similar side effect. –1 cost per
rank.

DEFENSE

Action: None • Range: Personal
Duration: Permanent • Cost: 1 point per rank

Protection shields you against damage, giving you +1 to
your Toughness  defense  per  rank.  So  Protection  4  gives
you +4 Toughness.

FLAWS

Sustained:  Your  Protection  is  a  sustained  effect,  rather
than permanent. The effect can be turned on and off and
can be improved using extra effort, including using it to
perform  stunts  (see  Extra  Effort).  Sustained  Protection
might be a power like a personal force field, or the ability
to consciously harden your skin and turn it into armor. +0
cost per rank.

QUICKNESS

GENERAL

Action: Free • Range: Personal
Duration: Sustained • Cost: 1 point per rank

You  can  perform  routine  tasks—anything  that  can  be
done as a routine check (see Routine Checks in The Ba-
sics  chapter)—fast,  perhaps  very  fast.  Subtract  your  ef-
fect rank from the normal time rank to perform a task to
determine how long it takes you. So, for example, if you
have Quickness 7, a routine task normally taking an hour
(time rank 9) takes you (9 – 7 = time rank 2) 30 seconds.
Non-routine checks are not affected by Quickness, nor is
movement speed.

If you can perform a task in less than a second (time rank
–2), the GM may choose to treat that task as a free action
for you (although the GM can still limit the number of free
actions you can accomplish in a turn as usual).

174

```

**Chunk 4** (`f47cb1a00aa5`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

One player—the Gamemaster or “GM”—takes responsibility for running a MUTANTS & MASTERMINDS game. The Game-
master  creates  the  adventure,  runs  the  players  through  it,  takes  on  the  roles  of  the  various  other  characters  the
heroes encounter, and handles any questions about the rules as they arise. The Gamemaster also adjudicates the
process of character creation, deciding what traits, modifiers, and so forth are appropriate for the particular game,
along with the best way to express certain concepts in game terms. While Gamemastering is a big responsibility, it’s
not as hard as it might seem, and providing a fun and entertaining game for your friends can be quite rewarding.

While the players are responsible for keeping track of their characters and deciding on their actions, the Gamemaster is
responsible for everything else that happens in the game. A good GM tries to make sure the game runs as smoothly as
possible and is enjoyable for all of the players. Many components go into creating a good MUTANTS & MASTERMINDS game.
The following sections give you the basics, but experience is the best tool to help you become a better Gamemaster.

can  be  broken  down  into  a  series
of tasks the heroes must perform, from piecing together
clues  about  a  villain’s  latest  scheme  to  blasting  said  vil-
lain through a wall and disarming his doomsday device in
the nick of time. It’s up to the Gamemaster to assign the
difficulty of these and numerous other tasks in the game
and to determine the outcome of the heroes’ efforts. This
section  offers  some  general  guidelines  on  assigning  the
difficulty of a task.

THE 55% RULE

tract 10 from the DC. So a DC 25 action (a formidable task)
requires a bonus of +15 in order to have a 55% chance of
success (on a roll of 10 or higher).

Keep in mind that this chance of success on a task allows
a character to automatically succeed at that task as a rou-
tine  check  (see  Routine  Checks,  following,  and  in  The
Basics chapter). This is intentional; the average character
only really fails at an average task when hurried or under
stress. A 55% chance also allows a player to spend a hero
point to automatically succeed, since a hero point ensures
a die roll of at least 11. (See Hero Points, page 20.)

A good guideline to keep in mind is the chance of an aver-
age character (with a modifier of 0) succeeding

[... truncated ...]
```

---

## Concept: Routine Checks

Chunk count: 8
Receives actions: ['act_0122', 'act_0132', 'act_0163', 'act_0170', 'act_0430']

### Chunk texts

**Chunk 1** (`179f10a90f72`):

```
CHAPTER 2: SECRET ORIGINS

23

nuses for your character, paying 1 power point per +1 de-
fense over the base rank provided by your hero’s abilities.
To improve your hero’s Toughness, see Advantages and
Powers, following. See the Abilities chapter for details.
5. SKILLS

Choose  the  skill  ranks  you  want  your  character  to  have
and pay 1 power point per 2 total skill ranks. See the Skills
chapter for details.

6. ADVANTAGES

Choose the advantages you want your character to have
and pay 1 power point per advantage or rank in a advan-
tage. See the Advantages chapter for details.

7. POWERS

Create  your  hero’s  powers  by  choosing  their  desired  ef-
fects  and  paying  the  effects’  base  cost,  adjusted  for  any
modifiers, and multiplied by the number of ranks. See the
Powers chapter for details.
8. COMPLICATIONS

Choose at least two complications for your hero. You can
have more, if you want, and the more complications your
hero  faces,  the  greater  your  chances  for  earning  hero

points during the game. See the Complications section
of this chapter for details.
9. DETAILS

Go  through  the  limits  listed  under  Power  Level  in  this
chapter and make sure your hero’s traits all fit within them.
If not, adjust the traits accordingly until they do.

Go back through and add up the costs of your hero’s abili-
ties, defenses, skills, advantages, and powers. You should
end  up  with  a  figure  equal  to  the  starting  power  points
shown on the Starting Power Points table. If not, double-
check your math and either remove or add traits to your
character to reach the starting power point total.

Figure out things like your hero’s name, appearance, origin,
background, and motivation. If you can, consider creating a
sketch or detailed description of your hero’s costume.

10. GAMEMASTER APPROVAL

Show your new hero to the Gamemaster for approval. The
GM should check again to make sure your power points
are  spent  and  added  up  correctly,  your  hero  follows  the
power  level  guidelines  and  any  other  guidelines  set  for
the  series,  and  that  the  character  is  generally  complete
and  suited  to  the  overall  game.  Once  your  GM  has  ap-
proved, your new hero is ready for play!

You design a MUTANTS & MASTERMINDS hero by spending pow-
er points on different traits. Each ability, skill, advantage,
power, and other trait has an associated power point cost.

The game’s power level provides a guideline for how many
power points you

[... truncated ...]
```

**Chunk 2** (`2f722833852f`):

```
CHAPTER 5: ADVANTAGES

139

initiative result, followed by all the other characters who
do not have this advantage.

SET-UP

COMBAT, RANKED

speed in the round, regardless of the number of attacks
you  make. You  stop  attacking  once  you  miss,  run  out  of
movement, or there are no more minions within range of
your attack.

You can transfer the benefits of a successful combat use of
an interaction skill to your teammate(s). For example, you
can feint and have your target vulnerable against one or
more allies next attack(s), rather than yours. Each rank in
the advantage lets you transfer the benefit to one ally. The
interaction skill check requires its normal action, and the
affected allies must be capable of interacting with you (or
at least seeing the set-up) to benefit from it.

TAUNT

SKILL

You  can  demoralize  an  opponent  with  Deception  rather
than  Intimidation  (see  Demoralize  under  the  Intimida-
tion skill description), disparaging and undermining con-
fidence  rather  than  threatening. Targets  resist  using  De-
ception, Insight, or Will defense.

SIDEKICK

GENERAL, RANKED

TEAMWORK

GENERAL

You  have  another  character  serving  as  your  partner  and
aide.  Create  your  sidekick  as  an  independent  character
with (advantage rank x 5) power points, and subject to the
series power level. A sidekick’s power point total must be
less than yours. Your sidekick is an NPC, but automatically
helpful  and  loyal  to  you.  Gamemasters  should  generally
allow you to control your sidekick, although sidekicks re-
main NPCs and the GM has final say in their actions.

Sidekicks  do  not  earn  power  points.  Instead,  you  must
spend earned power points to increase your rank in Side-
kick to improve the sidekick’s power point total and traits;
each  point  you  spend  to  increase  your  rank  in  Sidekick
grants  the  sidekick  5  additional  power  points.  Sidekicks
also do not have hero points, but you can spend your own
hero points on the sidekick’s behalf with the usual bene-
fits. Sidekicks are not minions, but full-fledged characters,
so they are not subject to the minion rules.

You’re  effective  at  helping  out  your  friends.  When  you
support a team check (see Team Checks in The Basics
chapter)  you  have  a  +5  circumstance  bonus  to  your
check.  This  bonus  also  applies  to  the  Aid  action  and
Team Attacks.

COMBAT, RANKED

You have a +1 damage bonus with thrown weapons per
rank in this advantage. You can also thr

[... truncated ...]
```

**Chunk 3** (`7db012c9a682`):

```
CHAPTER 4: SKILLS

113

You can get a general idea of just how good a particu-
lar character’s skill bonus is using the general difficulty
class  guidelines  given  in  The  Basics  along  with  the
rules  for  routine  checks  (see  Routine  Checks  in  that
chapter).

For  example,  a  +5  total  skill  modifier  means  the  char-
acter can routinely achieve a result of 15 (a tough task).
Safe to say the character is a pro, able to routinely han-
dle tasks that would prove too much for someone less
skilled.  A  character  with  a  +10  skill  modifier  achieve  a
DC 20 (challenging task) on a routine basis, a real level of
expertise, while a +15 modifier can routinely complete
DC  25  (formidable)  tasks.  At  the  high  end,  a  +30  skill
modifier  can  routinely  accomplishing  the  nigh  impos-
sible (DC 40 tasks)!

Certain skills, called interaction skills, are aimed at deal-
ing  with  others  through  social  interaction.  Interaction
skills allow you to influence the attitudes of others and get
them to cooperate with you in one way or another. Since
interaction skills are intended for dealing with others so-
cially, they have certain requirements.

First,  you  must  be  able  to  interact  with  the  subject(s)  of
the  skill. They  must  be  aware  of  you  and  able  to  under-
stand you. If they can’t hear or understand you for some
reason, you have a –5 circumstance penalty to your skill
check (see Circumstance Modifiers in The Basics).

Interaction  skills  work  best  on  intelligent  subjects,  ones
with  an  Intellect  rank  of  –4  or  better. You  can  use  them
on creatures with Int –5, but again with a –5 circumstance
penalty;  they’re  just  too  dumb  to  get  the  subtleties  of
your  point. You  can’t  use  interaction  skills  at  all  on  sub-
jects lacking one or more mental abilities. (Try convincing
a  rock  to  be  your  friend—or  afraid  of  you—sometime.)

If you don’t find a particular skill on the list, like climbing,
bluffing, or search, remember that each skill in MUTANTS &
covers a lot of ground. So, you’ll find climbing
isn’t its own skill, but is listed as part of Athletics, while
bluffing and search are under Deception and Investiga-
tion, respectively. When in doubt, read through the skill
you think is most similar to what you’re looking for.

The  Immunity  effect  (see  the  Powers  chapter)  can  also
render characters immune to interaction skills.

You  can  use  interaction  skills  on  groups  of  subjects

[... truncated ...]
```

**Chunk 4** (`903a8c445c1a`):

```
CHAPTER 1: THE BASICS

11

Time Rank = Distance Rank - Speed Rank

Reversing  the  previous  formula,  we  can  also  figure  out
how long it takes someone at a particular speed to cov-
er  a  given  distance,  by  subtracting  the  speed  rank  from
the distance rank to get a time rank. So a normal human
(speed  0)  walking  30  miles  (distance  13)  takes  about  16
hours. A hero with Speed 14 covers the same distance in
(13 – 14 = –1) just 3 seconds!

Throwing Distance Rank =
Strength Rank - Mass Rank

As  another  example,  the  distance  rank  a  hero  can  throw
something equals the hero’s Strength rank minus the mass
rank of the object. So a hero with Strength 10 (able to lift 25
tons), picks up a 10-ton truck (mass rank 9). Since 10-9=1,
the hero can then toss the truck rank 1 distance (60 feet)!

GAME PLAY

A session of the MUTANTS & MASTERMINDS game resembles an issue of a comic book or an episode of an animated series.
The Gamemaster and the players get together and tell a story through the process of playing the game. The length of
the game session can vary, from just a couple hours to several hours or more. Some adventures may be completed in a
single session while others may take multiple sessions, just as some comic book stories are told in one issue while others
span multiple issues, forming a story arc or mini-series. The episodic nature of the game allows you to choose when to
stop playing and allows you to start up again at any time you and your friends want.

Also like a comic book, a M&M game consists of a series of interrelated scenes. Some scenes are fairly straightforward,
with the heroes interacting with each other and the supporting cast. In these cases the GM generally just asks the play-
ers to describe what their heroes are doing and in turn describes how the other characters react and what they do. There
may be some improvisational acting as everyone plays out the roles of their characters. When the action starts hap-
pening, such as when the heroes are staving off a disaster or fighting villains, time becomes more crucial and is broken
down into action rounds, and the players generally have to make die rolls to see how their heroes do.

CHECKS

Your hero stands perched on the rooftop, looking down
through the skylight. In the abandoned warehouse below,
the  villain  throws  the  switch  that  begins  lowering  your
hero’s friends into the vat of boiling acid! You turn to the
Gamemaster and say:

“I leap down, smashing throug

[... truncated ...]
```

**Chunk 5** (`b054d3b34f13`):

```
CHAPTER 6: POWERS

173

Precise: If you can Nullify multiple effects, this modifier al-
lows you to choose which are nullified and which are not.
Flat +1 point.

Randomize: Rather than being countered, the effect(s) tar-
geted by your Nullify acquire the Uncontrolled flaw and go
out of control (as dictated by the GM). +0 cost per rank.

Selective: If you have an Area Nullify effect, this extra al-
lows you to choose who in the area is affected, nullifying
some targets and not others. +1 cost per rank.

Sustained:  If  this  modifier  is  applied  to  Concentration
Nullify, keeping the countered effect(s) suppressed is only
a free action for you each turn. +1 cost per rank.

FLAWS

Side Effect: If you fail to nullify an effect, you might suffer
some kind of “backlash” or similar side effect. –1 cost per
rank.

DEFENSE

Action: None • Range: Personal
Duration: Permanent • Cost: 1 point per rank

Protection shields you against damage, giving you +1 to
your Toughness  defense  per  rank.  So  Protection  4  gives
you +4 Toughness.

FLAWS

Sustained:  Your  Protection  is  a  sustained  effect,  rather
than permanent. The effect can be turned on and off and
can be improved using extra effort, including using it to
perform  stunts  (see  Extra  Effort).  Sustained  Protection
might be a power like a personal force field, or the ability
to consciously harden your skin and turn it into armor. +0
cost per rank.

QUICKNESS

GENERAL

Action: Free • Range: Personal
Duration: Sustained • Cost: 1 point per rank

You  can  perform  routine  tasks—anything  that  can  be
done as a routine check (see Routine Checks in The Ba-
sics  chapter)—fast,  perhaps  very  fast.  Subtract  your  ef-
fect rank from the normal time rank to perform a task to
determine how long it takes you. So, for example, if you
have Quickness 7, a routine task normally taking an hour
(time rank 9) takes you (9 – 7 = time rank 2) 30 seconds.
Non-routine checks are not affected by Quickness, nor is
movement speed.

If you can perform a task in less than a second (time rank
–2), the GM may choose to treat that task as a free action
for you (although the GM can still limit the number of free
actions you can accomplish in a turn as usual).

174

```

**Chunk 6** (`c84a4002269b`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

MOVEMENT

Movement effects allow characters to get around in vari-
ous  ways.  Some  provide  a  speed  rank  with  a  particular
form of movement—such as ground, air, or water—while
others offer different modes of movement, like walking on
walls or slithering along the ground like a snake.

Although  activating  a  movement  effect  is  typically  a  free
action, the character must still take a move action in order
to actually move using the effect. So, for example, the ac-
tion of the Flight effect is “free” and activating it grants the
character a Flight speed rank equal to the effect rank. Mov-
ing that speed rank still requires a move action, however.

SENSORY

Senses  in  MUTANTS  &  MASTERMINDS  are  grouped  into  sense
types, descriptors for how different sensory effects work. The
sense types, and some of the senses included in them, are:

•

•

•

•

•

Visual: normal sight, darkvision, infravision, low-light
vision, microscopic vision, ultravision, X-Ray vision

Auditory: normal hearing, sonar (accurate ultrason-
ic), ultrasonic hearing

Olfactory: normal smell and taste, scent

Tactile: normal touch, tremorsense

Radio: radio, radar (accurate radio)

•  Mental: mental awareness, Mind Reading, Precogni-

Sensory effects enhance or alter the senses. Some senso-
ry effects improve the user’s senses while others grant en-
tirely new senses or fool the senses in some way. Sensory
effects are typically a free action to activate and sustain, or
are permanent and always in effect.

•

tion, Postcognition

Special: This is the catchall for other sensory descrip-
tors  not  given  above,  including  unusual  senses  or
exotic descriptors like cosmic, gravitic, magical, and
so forth.

Using  powers  is  a  fairly  simple  matter.  Some  power  effects  work  automatically.  Others—particularly  those  affecting
other people—require some effort to use, like an attack check or a effect check. Powers affecting others allow resistance
checks against their effects.

In  some  cases,  you  may  be  required  to  make  an  effect
check  to  determine  how  well  an  effect  works.  A  power
check  is  just  like  any  other  check:  d20,  plus  the  power’s
rank,  plus  any  applicable  modifiers,  against  a  difficulty
class set by the Gamemaster. The results of various power
checks are described in this chapter.

Effect Check = d20 + rank +
modifiers vs. difficulty class

Many  power  effects  allow  for

[... truncated ...]
```

**Chunk 7** (`db54782984cc`):

```
CHAPTER 8: ACTION & ADVENTURE
CHAPTER 8: ACTION & ADVENTURE

CHAPTER 8: ACTION & ADVENTURE

NO COVER

COVER

Targets may also hide behind obstructions to gain cover
against your attacks. Obstructions that do not physically
block  attacks  but  simply  make  the  target  harder  to  per-
ceive—such as lighting, fog, or foliage—provide conceal-
ment rather than cover.

Partial Cover applies a –2 circumstance penalty to your
attack check. It generally means about half of the target
is behind cover, such as around a corner, behind a tree or
pillar, or a low wall.

Total  Cover  applies  a  –5  circumstance  penalty  to  your  at-
tack check, with three-quarters or more of the target behind
cover, like a narrow window, or crouched behind a wall.

Damage  resistance  check,  for  example,  is  incapaci-
tated, regardless of the degree of failure.

•

Certain  traits  (like  the  Takedown  advantage)  are
more effective against or specifically target minions.

DEFENSES

Your defenses determine how difficult it is to hit you with
various attacks. Most attacks target your active defenses,
Dodge and Parry: close attacks target Parry while ranged
attacks target Dodge.

You  add  your  defense  rank  to  a  base  value  of  10  (like  a
routine  check)  to  determine  your  defense  class  against
an attack, which is the DC of the attack check:

If a target is completely behind cover, then you cannot at-
tack that target (although you can attack the cover itself ).

Defense Class = defense + 10

Cover  also  grants  a  circumstance  bonus  to  Dodge  resis-
tance  checks  against  area  effects  equal  to  its  penalty  to
attack checks, so long as the target has cover with respect
to the origin point of the effect. So someone behind total
cover also gains a +5 to Dodge checks against area effects.

MINIONS

Minions  are  minor  characters  subject  to  special  rules  in
combat, and generally easier to defeat than normal char-
acters.  Villains  often  employ  hordes  of  minions  against
heroes. The following rules apply to minions:

•  Minions  cannot  score  critical  hits  against  non-min-

ions.

•

•

Non-minions  can  make  attack  checks  against  min-
ions as routine checks.

 If a minion fails a resistance check, the minion suffers
the worst degree of the effect. So a minion failing a

So a hero with Parry 11 has a defense class of 21 (11 + 10)
against close attacks. If the same hero has Dodge 9, that is
a defense class of 19 (9 + 10) against ranged attack

[... truncated ...]
```

**Chunk 8** (`f41e7b13c82a`):

```
CHAPTER 4: SKILLS
CHAPTER 4: SKILLS

CHAPTER 4: SKILLS

DISGUISE

You can use makeup, costumes, and other props to change
your appearance. Your Deception check result determines
the effectiveness of the disguise, opposed by others’ Per-
ception check results. The GM makes the Deception check
secretly so you are not sure exactly how well your disguise
holds up under scrutiny.

Disguise  is  heavily  dependent  on  circumstances:  favor-
able ones include appropriate costuming and a subject
resembling your normal appearance, while unfavorable
circumstances include disguising yourself as a member
of a different race or sex, or not having sufficient props
(which can be up to a –5 modifier). If you are imperson-
ating  a  particular  individual,  anyone  who  knows  that
individual gets a circumstance bonus to the Perception
check: regular associates get a +2, while friends get a +5
and intimate loved ones a +10.

Successfully  acting  like  who  you  appear  to  be  may  also
require a Deception check with a DC equal to the observ-
er’s Insight check, modified by familiarity if the observer
knows the subject well, as mentioned previously.

A disguise normally requires at least 10 minutes of prepa-
ration.  The  GM  makes  Perception  checks  for  those  who
encounter you immediately upon meeting you and each
hour or day thereafter, depending on circumstances.

FEINTING

You can use Deception as a standard action to mislead an
opponent in combat. Make a Deception check as a stan-
dard action opposed by the better of your target’s Decep-
tion or Insight. If your Deception check succeeds, the tar-
get is vulnerable against your next attack, until the end of
your next round (see Vulnerable in the Conditions sec-
tion of The Basics chapter).
INNUENDO

You  can  use  Deception  to  send  covert  messages  using
word-play and double-meanings while apparently talking
about other things. The DC for a basic message is 10. Com-
plex messages or messages trying to communicate new
information have DCs of 15 or 20, respectively. The recipi-
ent of the message must make a Insight check against the
same DC to understand it.

DC

10

15

20

TASK

Basic message

Complex message

Message containing new or detailed information

Anyone listening in on your innuendo can attempt a In-
sight  check  against  the  message  DC.  If  successful,  the
eavesdropper notices a message hidden in your conversa-

tion. If the eavesdropper gets at least two degrees of suc-
cess, he also unders

[... truncated ...]
```

---

## Concept: Safe Fall

Chunk count: 9

### Chunk texts

**Chunk 1** (`02269b6c9ef6`):

```
CHAPTER 2: SECRET ORIGINS

49

Power Point Totals:  Abilities 50 + Powers 10  + Advantages 17 + Skills  45 + Defenses 28  = 150

ROOK

Jon  wants  to  create  a  hero  who’s  a  vigilante  type,  someone  with  no  superpowers,  but
great training and skill, along with various crime-fighting gadgets. The hero is intended for

a power level 10 game, with 150 starting power points.

Jon starts out with abilities. He wants his hero to be capable both physically and men-
tally. So he assigns rank 5 to both Agility and Dexterity to make his hero quick, ag-
ile, and accurate, and a 5 to Intellect to make him equally quick on the uptake. He
puts 3 each into Strength and Stamina making his hero well above average in those
abilities, but not quite as much as the others. Similarly, he gives his hero Presence 3
and Awareness 2, both above average, but not his strongest suits. Lastly, since he sees
his hero as a real combat expert, Jon gives him Fighting 8. Each ability rank costs 2 power

points, so Jon has spent 68 of his 150 points, just over a third.

Next, he looks at skills. He wants his hero to be quite skilled and makes a wish list of the skills he
wants. He starts out assigning 8 ranks to each of those skills—knowing skills
cost 1 power point per 2 ranks—but that would use up more than his re-
maining points! So he shifts those ranks around, decreasing less important
skills—like Sleight of Hand and Treatment—and increasing Ranged Com-
bat to match the hero’s Close Combat bonus. When he’s done, Jon has as-
signed 58 ranks in skills, quite a respectable amount, and spent 29 points
(58 ranks, divided by 2). That leaves him with 53 power points remaining.

Fortunately, Jon has decided his hero doesn’t really have any powers, relying
on skills, advantages, and equipment. So he turns to his character’s defenses. He
buys up his Dodge from 5 (for his Agility) to 14 for 9 points and his Parry from 8 (for
his Fighting) to 14 for 6 points. He increases Will from 2 (for his Awareness) to 8 for
another 6 points and gives his hero Fortitude 8, adding 5 points to his basic Stamina 3.

Jon has spent a total of (9 + 6 + 6 + 5) or 26 points on defenses, about half of what he has left.

Now he looks at his hero’s Toughness. Jon can’t increase that directly by spending power points; Tough-
ness can only be improved using advantages and powers, and his hero doesn’t have any powers. His hero
has Toughness 3 from his Stamina and his Toughness defense can be up to 6, given his Dodge

[... truncated ...]
```

**Chunk 2** (`19a54c3b3576`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

6-9

Magic Sword: Strength-based Damage 3 (6 Damage
with Strength), Multiattack 6, Penetrating 6, Easily
Removable (-6 points) • 9 points

10-11

12-13

Modified Nunchaku: Strength-based Damage 2 (5
Damage with Strength), Multiattack 5, Improved
Grab, Improved Trip, Reach 3, Ricochet; Movement
1 (Swinging); Easily Removable (-6 points) • 9 points

Perfect Aim: Perception Range Damage 5, Easily
Removable (ranged or improvised weapon, -6
points) • 9 points

14-15

Rapid Shot: Ranged Multiattack Damage 5, Easily
Removable (ranged weapon, -6 points) • 9 points

16-20

Super-Shield: Array (13 points plus 2 points of

Alternate Effects), Easily Removable (-6 points)
• 9 points total

•  Blocking: Deflect 13 • 13 points

•  Shield Bash: Strength-based Damage 2 (5

Damage with Strength), Penetrating 5 • 1 point

•  Shield Throw: Strength-based Ranged Damage 2
(5 Damage with Strength), Multiattack 5 • 1 point

Roll 1d20 once and record the result.

1-2

3-6

7-10

11-12

Blindsight: Senses 6 (Accurate, Analytical and

Extended Hearing, Hearing Counters Illusion)
• 6 points

Catlike Balance: Enhanced Skills 2 (Acrobatics 4),
Leaping 2 (30 feet), Movement 1 (Safe Fall)
• 6 points

Healing Factor: Immunity 1 (Disease); Regeneration

5 • 6 points

Probing Sight: Mind Reading 4, Limited to Surface
Thoughts, Visually Sense-Dependent; Senses 4
(Vision Penetrates Concealment) • 6 points

13-14

Reinforced Body: Impervious Toughness 6 • 6 points

15-16

17-20

Resilient: Immunity 6 (Cold, Drowning, Heat, Need
for Sleep, Pressure, Starvation and Thirst) • 6 points

Super-Soldier: Enhanced Fortitude 2, Regeneration

2; Speed 2 (8 MPH) • 6 points

DEFENSE

DODGE
+7

PARRY
+6

FORTITUDE
+5

TOUGHNESS
+0

WILL
+8

ABILITIES

POWERS

56

15

13

SKILLS

DEFENSES

TOTAL

40

26

150

•  Motivation—Recognition:  The  Weapon  Master  is
driven by a need to be recognized as the best at what
he does.

•

•

•

Disability:  The  Weapon  Master  has  a  disability  of
some sort, such as blindness or only one arm, that he
overcomes through his skills or powers.

Honor:  The  Weapon  Master  abides  by  a  warrior’s
code of honor.

Rival: The Weapon Master has a foil—another Weap-
on Master who tries to outdo him at every turn.

Weather  Controllers  combine  control  over  the  elements
of air and water with cold and electrical energy. They gen-
erally command the more violent aspects of the weather,
such as 

[... truncated ...]
```

**Chunk 3** (`3739eabb7a65`):

```
CHAPTER 6: POWERS

171

Concentration:  Concentration  Move  Object  requires
more attention to maintain. You cannot concentrate to in-
crease your lifting capacity or to grab or move another ob-
ject while you are still “holding” your first. –1 cost per rank.

Limited Direction: You can only move objects in a par-
ticular direction or path, such as only up and down (to-
wards and away from the ground), only directly towards
or  away  from  you  (attraction  and  repulsion),  and  so
forth. This is useful for “gravitic” or “magnetic” versions of
the effect. –1 cost per rank.

Limited Material: You can only move a particular type of
object or material, such as only metals, plants, rock, water,
and so forth. –1 cost per rank (The GM may allow a –2 cost
per  rank  flaw  for  a  particularly  limited  type  of  material,
such as only precious metals, leaves, sand, or petroleum).

MOVEMENT

MOVEMENT

Action: Free • Range: Personal
Duration: Sustained • Cost: 2 points per rank

You have a special form of movement. For each rank in this
effect, choose one of the following options:

You  can  move  instantly  from  one  dimension  to  another
as a move action. For 1 rank, you can move between your
home dimension and one other. For 2 ranks you can move
between  any  of  a  related  group  of  dimensions  (mystical
dimensions,  alien  dimensions,  etc).  For  3  ranks  you  can
travel to any dimension. You can carry up to 50 lbs. (mass
rank 0) of additional material with you when you move. If
you apply the Increased Mass modifier, you can carry ad-
ditional mass up to your modifier rank.

You’re  adapted  to  a  particular  environment,  such  as  un-
derwater,  zero  gravity,  and  so  forth  (see  Environmental
Hazards,  pages  185-187,  for  details). You  suffer  none  of
the normal unfavorable circumstance or movement pen-
alties associated with that environment, moving and act-
ing normally. You are still affected by environmental haz-
ards like suffocation, exposure, and so forth. You need the
Immunity effect to ignore such things.

PERMEATE

You  can  pass  through  solid  objects  as  if  they  weren’t
there. For 1 rank, you can move at speed rank –2 through
any physical object. For 2 ranks, you can move at speed
rank –1 and for 3 ranks, you move at your normal speed
through  any  obstacles. You  cannot  breathe  while  com-
pletely  inside  a  solid  object,  so  you  either  need  Im-
munity to Suffocation or have to hold your breath. You
may also need Pe

[... truncated ...]
```

**Chunk 4** (`43d5c758bf78`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

WASP

Insect Senses: Senses 4 (Acute Smell, Darkvision,

Ranged Touch) • 4 points

16-20

Sting: Cumulative Affliction 8 (Resisted and Overcome
by Fortitude; Impaired, Disabled, Incapacitated),
Linked to Damage 8, Accurate 2 • 26 points

Roll 1d20 once and record the result.

CANINE

Bite: Strength-based Damage 3, Improved Critical,

Wings: Flight 6 (120 MPH), Wings • 6 points

Penetrating 3 • 7 points

Canine Senses: Senses 3 (Low-light Vision, Acute

and Tracking Olfactory) • 3 points

1-10

Canine Movement: Leaping 2 (30 feet); Speed 4 (30

Talons: Strength-based Damage 1, Accurate 2, Fast Grab

MPH) • 6 points

• 4 points

Roll 1d20 once and record the result.

FALCON

Flight: Flight 6 (120 MPH), Wings • 6 points

Keen Eyesight: Senses 3 (Extended 2 and Rapid

Vision) • 3 points

1-10

Sonic Scream: Cone Area Affliction 9 (Resisted

and Overcome by Fortitude; Dazed and Auditory
Impaired, Stunned and Auditory Disabled,
Incapacitated and Auditory Unaware), Extra
Condition, Quirk—Impaired, Disabled, Unaware
Limited to One Sense (-4 points) • 23 points

11-20

OWL

Nightvision: Senses 2 (Extended Vision, Low-light

Vision) • 2 points

11-20

Shriek: Cone Area Affliction 8 (Resisted and
Overcome by Will; Dazed and Vulnerable,
Stunned and Defenseless, Incapacitated)
• 24 points

Silent Flight: Flight 5 (60 MPH), Subtle, Wings • 6 points

Howl: Auditory Perception Area Affliction

10 (Resisted and Overcome by Will; Dazed
and Impaired, Disabled and Stunned), Extra
Condition, Limited Degree • 20 points

FELINE

Claws: Strength-based Damage 1, Accurate,

Improved Critical • 3 points

Feline Senses: Senses 3 (Low-light Vision, Acute and

Tracking Olfactory) • 3 points

Feline Movement: Leaping 3 (60 feet); Movement
3 (Safe Fall, Sure-footed, Trackless); Movement
1 (Water-walking), Limited to Solid Surfaces;
Movement 1 (Wall-crawling), Limited to One
Move Action; Speed 4 (30 MPH) • 15 points

Plus roll 1d20 once and record the result.

1-5

Black Cat: Reaction Visual Perception

Area Affliction 5 (Resisted by Dodge,
Overcome by Will; Vulnerable,
Defenseless, Incapacitated), Side-
effect (Always happens, chosen by
player) • 15 points

```

**Chunk 5** (`442f2e5a5a37`):

```
CHAPTER 2: SECRET ORIGINS

81

1-3

Burrowing: Burrowing 6 (4 MPH), Penetrating • 12

points

4-8

Flight: Flight 6 (120 MPH) • 12 points

9-14

Super-Leaping: Leaping 12 (4 miles) • 12 points

15-20

Super-Movement: Speed 5 (60 MPH); Leaping 7

(1,000 feet) • 12 points

Roll 1d20 once and record the result.

1-2

3-6

7-10

11-14

15-17

18-20

Enhanced Senses: Senses 5 (Extended Auditory 2,
Extended Vision 2, Low-light Vision) • 5 points

Fast Recovery: Regeneration 4, Enhanced

Advantage 1 (Diehard) • 5 points

Faster: Depending on the Movement Power you
rolled; Burrowing: add 1 rank of Penetrating
Burrowing and Senses 3 (Infravision, Direction
Sense, Distance Sense); Flight: add 2 ranks of
Flight and an Alternate Effect of Swimming 6;
Super-Leaping: add 5 ranks of Leaping; Super-
Movement: add 2 ranks of Speed and 3 ranks of
Leaping • 5 points

Immortal: Immortality 2, Enhanced Advantage 1

(Diehard) • 5 points

Like Hitting a Brick Wall: Reaction Damage 1,

Penetrating 1 • 5 points

Pliable Form: Elongation 1 (15 feet); Movement 2

(Permeate, Safe Fall) • 5 points

DEFENSE

DODGE
+5

PARRY
+0

FORTITUDE
+0

TOUGHNESS
+0

WILL
+5

ABILITIES

POWERS

36

88

3

SKILLS

DEFENSES

TOTAL

13

10

150

•

Identity:  Some  Powerhouses  keep  their  identity  a
secret  from  the  rest  of  the  world.  Especially  those
Powerhouses  that  can  change  into  and  out  of  their
super-powered identity.

•  Motivation—Acceptance:  Those  Powerhouses  with
the  Prejudice  complication  often  choose  this  mo-
tivation  and  become  a  hero  in  order  to  earn  a  place
in  “normal”  society.  An  alien  Powerhouse  may  also
choose this motivation even if he or she doesn’t look
unusual.

•  Motivation—Patriotism:  Many  Powerhouses  are
die-hard  patriots  and  fight  to  defend  or  represent
their country.

•  Motivation—Responsibility: Due to their incredible
powers, many Powerhouses become heroes because
they feel as if they have a responsibility to do so.

•

•

•

Power  Loss:  Some  Powerhouses  lose  their  powers
in the presence of a certain substance, while others
physically transform from a normal human form and
return to it often.

Prejudice: The Powerhouse often looks unusual and
struggles with feeling isolated or like an outsider, or
even being treated like a monster!

Relationship: The Powerhouse typically has a small
group of friends he or she relies on for human con-
tact and friendship. These relationships are very im-
portant to the Powerhous

[... truncated ...]
```

**Chunk 6** (`ab9b367b750f`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

STRENGTH
3
STAMINA
2

POWERS

AGILITY
5
DEXTERITY
5

FIGHTING
7
INTELLECT
0

AWARENESS
1
PRESENCE
2

Choose two of the following • 10 points

•  Blocking: Deflect 7, Easily Removable (weapon or shield, –2 points)

•  Crippling Strike: Affliction 7 (Resisted by Fortitude; Impaired, Hindered,

Incapacitated), Easily Removable (weapon, –2 points)

•  Fast: Quickness 3, Speed 2 (8 MPH)

•  Gadgets: Variable 1 (5 points), Easily Removable (–2 points)

•  Healing Factor: Regeneration 5

•

Improvised Weapons: Damage 2, Strength-based, Ranged 5, Easily
Removable (–2 points)

•  Super-Hearing: Senses 5 (Accurate Hearing, Danger Sense,

Extended Hearing, Ultra-Hearing)

•  Super-Vision: Senses 5 (Darkvision, Extended Vision, Microscopic

Vision 2)

•  Urban Acrobat: Leaping 1, Movement 2 (Safe Fall, Swinging)

EQUIPMENT

Weapon: Choose one of the following • 15 points.

Bow (or Crossbow): Ranged Damage 5 with: Multiattack or five

Alternate Effects (trick arrows).

Daggers (or Knives): Strength-based Damage 2, Ranged 5,

Multiattack 5, Improved Critical, Improved Defense, Improved
Disarm.

Gun (revolver or semi-automatic): Multiattack Ranged Damage 5.
Sword (including Katana): Strength-based Damage 2,

Multiattack 5, Penetrating 5, Improved Defense, Improved
Disarm, Improved Smash.

Whip: Damage 4, Multiattack, Improved Grab, Improved

Hold, Improved Trip, Reach 3
•  Movement 1 (Swinging).

Vehicle: Motorcycle • 10 points

Defensive Roll 4, Equipment 5, Evasion, Improved Critical (weapon)

Plus  choose  six  of  the  following:  Accurate  Attack,  Agile  Feint,
Assessment,  Connected,  Contacts,  Defensive  Attack,  Improved  Critical
(weapon),  Improved  Defense,  Improved  Disarm,  Improved  Initiative,
Improved Smash, Improved Trip, Power Attack, Precise Attack (choose
one), Takedown, Taunt, Uncanny Dodge.

SKILLS

Acrobatics  8  (+13),  Athletics  8  (+11),  Close  Combat:  Weapon  6  (+13),
Deception 8 (+10), Expertise: (Choose One) 6 (+6), Expertise: Weapons 8
(+8), Intimidation 6 (+8), Investigation 6 (+6), Perception 8 (+9), Ranged
Combat:  Weapon  8  (+13),  Sleight  of  Hand  6  (+11),  Stealth  8  (+13),
Vehicles 4 (+9)

OFFENSE

INITIATIVE +5*

Weapon +13

Weapon +13

Close, Damage 5, Crit. 19-20*

Ranged, Damage 5, Crit. 19-20

* Varies depending on Advantages and Weapon chosen.

PL10PL10

DEFENSE

DODGE

PARRY

WILL

12

14

9

FORTITUDE

TOUGHNESS

8

6/2*

*Without Defen

[... truncated ...]
```

**Chunk 7** (`cfadcb33d64b`):

```
CHAPTER 2: SECRET ORIGINS

85

POWERS

Roll 1d20 once and record the result.

1-3

Shapeshifter: Variable 9 (45 points, for assuming

different shapes), Move Action • 72 points

Size-Changer: Roll 1d20 once or choose Giant Size
or Shrinking. You may take the other power as an
Alternate Effect by reducing Giant Size’s Power-
lifting to only 1 rank and dropping the Impervious
extra from Shrinking’s Protection 1. Also, only take
the Flight Belt supplied by the Giant Size power.

11-20

Density Decrease: Insubstantial 4
(Incorporeal, affected by magic),
Reaction, Linked to Flight 1 (4 MPH),
Limited to air-walking, and Immunity
10 (Life Support), Quirk: immunity to
suffocation requires holding breath, and
Concealment 1 (Hearing), Continuous;
Disruption Attacks: Array (24 points),
Incorporeal Weapon (Affects Corporeal
Damage 12, Resisted by Fortitude,
Limited to the Toughness of object used
as weapon), AE: Disrupt Electronics
(Close Range Affects Corporeal Nullify 12
(electronics), Simultaneous), AE: Disrupt
Synapses (Affects Corporeal Affliction
12 (Resisted and Overcome by Fortitude;
Dazed, Stunned, Incapacitated); Innate
Understanding of Powers (Enhanced
Advantages 13 (Close Attack 6, Defensive
Roll 2, Hide in Plain Sight, Redirect, Set-up
2, Teamwork), Enhanced Skill -4 (Close
Combat: Unarmed -8) (Note: the Innate
Understanding of Powers abilities only
work when no powers are active or when
Density Decrease is active) • 72 points

14-16

17-20

Specific Shapeshifter: Variable 9 (45 points, for

assuming different shapes), Continuous, Limited
(Choose one type of entity you can turn into:
Animals, Machines, Humanoids, Aliens, etc.), Move
Action • 72 points

Stretcher: Strength-based Damage 6; Elongation 8
(1,800 feet); Enhanced Advantages 14 (Accurate
Attack, Chokehold, Close Attack 2, Evasion, Fast
Grab, Improved Grab, Improved Hold, Improved
Trip, Interpose, Power Attack, Precise Attack
(Close; Cover), Takedown 2); Enhanced Skill 4
(Close Combat: Grab +8); Impervious Toughness 8,
Limited—Physical Impact Damage; Insubstantial
1 (Liquid), Precise; Morph 2 (Humanoid Forms),
Distracting; Movement 6 (Environmental
Adaptation - Tight Spaces, Safe Fall, Slithering,
Sure-footed, Swinging, Wall-crawling); Protection 7;
Speed 3 (16 MPH) • 72 points

DEFENSE

DODGE
+6

PARRY
+6

FORTITUDE
+6

TOUGHNESS
+0

WILL
+6

ABILITIES

POWERS

32

72

6

SKILLS

DEFENSES

TOTAL

16

24

150

•

Fame:  Many  Shapeshifters  (especially  heroic  ones)
don’t worry about hiding their

[... truncated ...]
```

**Chunk 8** (`db8b2bdf371a`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Energy Blast: Ranged Damage 12

Take the Gimmick Blaster and Energy Blast
(above), plus roll 1d20 three times (re-roll if you
get the same result twice) and add them to the
Gimmick Blaster array as Alternate Effects. Name
each of these Alternate Effects as appropriate for
your character’s gimmick.

1-3

4-5

6-8

9-11

12-14

Create 7, Continuous, Innate

Move Object 12

Ranged Affliction 12 (Resisted and
Overcome by Fortitude; Dazed,
Stunned, Incapacitated)

Ranged Affliction 12 (Resisted by
Dodge, Overcome by Damage;
Vulnerable, Defenseless,
Incapacitated)

Ranged Cloud Area Affliction 8

(Resisted and Overcome by Fortitude;
Dazed and Visually Impaired,
Stunned and Visually Disabled) Extra
Condition, Limited Degree

15-17

Ranged Burst Area Damage 8

18-20

Close Cone Area Damage 8, Penetrating 8

Personal Combat Enhancers: Enhanced Advantage

11 (All-out Attack, Defensive Attack, Evasion,
Extraordinary Effort, Diehard, Fearless, Great
Endurance, Improved Critical (Unarmed),
Improved Initiative, Takedown 2); Enhanced
Strength 3; Enhanced Trait 5 (Close Attack 5);
Activation—Move Action (-1 point), Removable
(-4 points) • 17 points

8-12

13-14

15-16

Physical Boosters: Enhanced Strength 8; Leaping

2 (30 feet); Quickness 2; Speed 2 (8 MPH);
Activation—Move Action (-1 point), Removable
(-4 points) • 17 point

17-20

High-tech Arsenal: Ray Gun (Ranged Damage 12,
AE: Power Truncheon (Strength-based Damage
8), AE: Stunner (Ranged Affliction 12 (Resisted
and Overcome by Fortitude; Dazed, Stunned,
Incapacitated)), AE: Force Capsule Grenade
(Ranged Affliction 12 (Resisted by Dodge,
Overcome by Damage; Hindered and Vulnerable,
Defenseless and Immobile), Extra Condition,
Limited Degree); Easily Removable (-10 points)
• 17 points

Roll 1d20 once and record the result.

1-5

6-10

Combat Training and Armored Costume:
Enhanced Advantage 2 (Defensive Roll 2),
Enhanced Defenses (Dodge 4, Parry 4), Protection
4, Removable (-1 point) • 13 points

Displacer Field: Enhanced Defenses (Dodge 6, Parry
6) Linked to Protection 4, Sustained, Removable
(-3 points) • 13 points

11-15

Energy-Absorbing Body Suit: Protection 10,

Impervious 6, Removable (-3 points) • 13 points

16-20

Force Field: Immunity 6 (Critical Hits, Cold, Heat,

High Pressure, Radiation) Linked to Protection 10,
Sustained, Removable (-3 points) • 13 points

Roll 1d20 once and record the result.

1-4

5-8

9-16

17-20

Biologica

[... truncated ...]
```

**Chunk 9** (`e087f7a0b70b`):

```
CHAPTER 2: SECRET ORIGINS

57

Take  the  Weapon  Array  and  the  Plasma  Blast  (above),
plus roll 1d20 four times on the table below (re-roll if you
get the same result twice) and add them to the Weapon
Array as Alternate Effects.

1-2

•  Electrified Shell: Reaction Damage 6 • 1 point

3-4

5-7

8-9

10-12

13-15

16-18

19-20

•  Electro-Stunner: Ranged Affliction 10 (Resisted
by Dodge and Overcome by Fortitude; Dazed,
Stunned, Incapacitated), Accurate 4 • 1 point

•  Plasma Bolts: Ranged Multiattack Damage 6,

Accurate 6 • 1 point

•  Force Capsule: Ranged Affliction 10 (Resisted

by Dodge and Overcome by Damage; Hindered
and Vulnerable, Defenseless and Immobile), Extra
Condition, Limited Degree, Accurate 4 • 1 point

•  Micro Rockets: Ranged Burst Area Damage 8

• 1 point

•  Omni-Blaster: Cone Area Damage 10,

Penetrating 4 • 1 point

•  Strength and Accuracy Booster: Enhanced
Strength 8; Enhanced Trait 6 (Close Attack 6)
• 1 point

•  Tractor/Presser Beam: Move Object 10,

Accurate 4 • 1 point

Ability Amplifier: Enhanced Defenses 16 (Dodge 4,

Fortitude 4, Parry 4, Will 4), Removable (-3 points) • 13 points

Armored Shell: Impervious Protection 8, Removable (-3

points) • 13 points

Sealed Systems: Immunity 10 (Life Support), Removable (-2

points) • 8 points

Roll 1d20 once and record the result.

1-7

8-10

Gravity Drivers: Flight 7 (250 MPH), Removable

(-3 points) • 11 points

•  Space Flight: Movement 2 (Environment

Adaptation—Zero-G , Space Travel 1) • 1 point

Locomotion Systems: Speed 7 (250 MPH); Leaping
4 (120 feet); Movement 2 (Choose two: Safe Fall,
Swinging, Wall-crawling 1, a second rank of
Wall-crawling), Removable (-3 points) • 12 points

Rocket Turbines: Flight 7 (250 MPH), Removable

(-3 points) • 11 points

11-17

•  Aquatic Turbines: Swimming 8 (120 MPH);

Movement 1 (Environment Adaptation—Aquatic)
• 1 point

18-20

Teleport-Tech: Teleport 3 (250 feet), Easy, Extended
(8 miles), Change Direction, Change Velocity,
Turnabout, Removable (-3 points) • 12 points

Communication Systems: Radio Communication 2,

Removable (-2 points) • 6 points

Sensors: Senses 2 (Extended Vision, Infravision), Removable

(-0 points) • 2 points

DEFENSES

DODGE
+4

PARRY
+2

FORTITUDE
+2

TOUGHNESS
+0

WILL
+4

ABILITIES

POWERS

36

76

10

SKILLS

DEFENSES

TOTAL

16

12

150

•

Identity: The Battlesuit often has a secret identity he
or she tries to protect.

•  Motivation—Responsibility:  Whether  an  inventor
of  military  weapons,  a  trained 

[... truncated ...]
```

---

## Concept: Salinas

Chunk count: 0
Performs actions: ['act_0452', 'act_0455']

### Chunk texts

---

## Concept: Sanguine

Chunk count: 0
Receives actions: ['act_0488']

### Chunk texts

---

## Concept: Scene

Chunk count: 0
Receives actions: ['act_0502', 'act_0505']

### Chunk texts

---

## Concept: Scuba

Chunk count: 1
Receives actions: ['act_0362']

### Chunk texts

**Chunk 1** (`115dd3a349cb`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

EQUIPMENT

In addition to their amazing devices, characters often make use of various mundane equipment—ordinary things found
in the real world—ranging from a simple set of tools to cell phones, laptop computers, and even common appliances.
These items are known as equipment to differentiate them from devices.

EQUIPMENT

Equipment  is  acquired  with  points  from  the  Equipment
advantage. Each piece of equipment has a cost in points,
just  like  other  traits.  The  character  pays  the  item’s  cost
out of the points from the Equipment advantage and can
thereafter have and use that item.

An  item’s  cost  is  based  on  its  effects  and  features,  just
like a power (see the Powers chapter for more informa-
tion), so a ranged weapon has a cost based on its Ranged
Damage  rank.  Equipment  often  provides  the  Features
effect,  including  some  specific  equipment  Features  de-
scribed in this chapter. Indeed, some items of equipment
provide only Features.

Just as with power effects, there is a diminishing value in
having multiple items with a similar function, or a single
piece of equipment with multiple functions, usable only
one at a time. Equipment can have the Alternate Effect
modifier (see the Extras section of the Powers chapter),
such as a weapon capable of different modes of opera-
tion, or a reconfigurable tool.

Characters can also have Alternate Equipment, an array of
items usable only one at a time. This is typically a multi-
function  item,  or  a  kit  or  collection  of  various  smaller
items. The  classic  example  is  the  utility  belt  (see  its  de-
scription  later  in  this  chapter).  Alternate  Equipment  can
also  include  things  like  an  arsenal  of  weapons  the  char-
acter can swap out, providing different sets of weapons,
with only a limited number usable at once.

Characters may not necessarily carry all their equipment
with them at all times. The GM may allow players to spend
a hero point in order to have a particular item of equip-
ment “on-hand” at a particular time. This is essentially an
equipment  “power  stunt”—a  one-time  use  of  the  item
for  one  scene—and  the  Gamemaster  rules  whether  or
not having a particular item on-hand is even possible. For
example, a hero out for an evening in his secret identity
might have something like a concealed weapon or other
small item on-hand, but it’s unlikely the character is carry-
i

[... truncated ...]
```

---

## Concept: Second World War

Chunk count: 1

### Chunk texts

**Chunk 1** (`f877c8ee4307`):

```
CHAPTER 2: SECRET ORIGINS

31

Consider  the  effects  of  age  on  your  hero.  Someone  who
fought  in  the  Second World War  is  likely  to  have  a  differ-
ent worldview than a modern teenager who just acquired
super-powers, to say nothing of an immortal who has seen
civilizations rise and fall or a godlike being from the dawn of
time. A character’s age may influence the choice of certain
traits. Aged characters are likely to have lower physical abil-
ity ranks, for example, while younger ones may have fewer
skill ranks (having had less time to train in various skills).

What  does  your  hero  look  like?  Consider  things  like  the
character’s  race,  sex,  ethnicity,  and  other  factors  in  ap-
pearance.  Is  the  hero  even  human?  Superheroes  can  be
aliens,  robots,  androids,  spirits,  and  beings  of  pure  en-
ergy.  Is  the  character  short  or  tall? What  about  hair  and
eye color? Does the hero have any distinguishing marks
or unique features; is his appearance unusual in any way
(apart from running around in a costume, that is)? Does
the  hero  qualify  for  the  Attractive  advantage?  (See  the
Advantages  chapter  for  details.)  What  about  complica-
tions stemming from the hero’s looks?
COSTUME

A costume is a big part of a superhero’s appearance. Like
code  names,  most  heroes  have  a  distinctive  costume,
usually  something  skin-tight  and  colorful,  often  embla-
zoned  with  a  symbol  or  logo.  Other  heroes  wear  more
military-style outfits, fatigues or body armor with numer-
ous bandoliers and belts. A suit of armor may serve as the
hero’s costume: anything from ancient mail to a high-tech

battlesuit. A few heroes don’t wear a special costume, just
ordinary street clothes (which in itself can be pretty dis-
tinctive among a group of spandex-clad heroes).

In the comics, costumes are generally immune to the kind
of  routine  wear-and-tear  a  hero’s  powers  should  inflict
on them. For example, heroes who can burst into flames
don’t usually incinerate their clothing. The same is true for
heroes who change their size or shape. Although a hero’s
costume can be damaged or torn by attacks and other cir-
cumstances, it’s usually immune to the hero’s powers. This
doesn’t cost any points; it’s just the way costumes work.
For more on costumes as equipment, see the Gadgets &
Gear chapter.

Although heroes spend a lot of time fighting crime and us-
ing their powers to help others, most also try to find time
to have li

[... truncated ...]
```

---

## Concept: Secondary Effect

Chunk count: 4

### Chunk texts

**Chunk 1** (`0713e58acd4e`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

EXTRAS

NAME

COST

Accurate

1 flat per rank

+2 attack check bonus per rank

Affects Corporeal

1 flat per rank

Effect works on corporeal beings with rank equal to extra rank.

Affects Insubstantial

1-2 flat points

Effect works on insubstantial beings at half (1 rank) or full (2 ranks) effect.

Affects Objects

+0-1 per rank

Fortitude resisted effect works on objects.

Affects Others

+0-1 per rank

Personal effect works on others.

Alternate Effect

1-2 flat points

Substitute one effect for another in a power.

Alternate Resistance

+0-1 per rank

Effect uses a different resistance.

Area

Attack

Contagious

+1 per rank

+0 per rank

+1 per rank

Effect works on an area.

Personal effect works on others as an attack.

Effect works on anyone coming into contact with its target.

Dimensional

1-3 flat points

Effect works on targets in other dimensions.

Extended Range

1 flat per rank

Doubles ranged effect’s distances per rank.

Feature

Homing

1 flat per rank

1 flat per rank

Adds a minor capability or benefit to an effect.

Attack effect gains additional chances to hit.

Impervious

+1 per rank

Resistance ignores effects with difficulty modifier of half extra rank or less.

Increased Duration

+1 per rank

Improves effect’s duration.

Increased Mass

1 flat per rank

Effect can carry a greater amount of mass.

Increased Range

+1 per rank

Improves effect’s range.

Incurable

Indirect

Innate

Insidious

Linked

Multiattack

Penetrating

Precise

Reach

Reaction

Reversible

Ricochet

1 flat point

Effect cannot be countered or removed using Healing or Regeneration.

1 flat per rank

Effect can originate from a point other than the user.

1 flat point

1 flat point

0 flat points

+1 per rank

1 flat per rank

1 flat point

1 flat per rank

+1 or 3 per rank

1 flat point

1 flat per rank

Effect cannot be Nullified.

Result of the effect is more difficult to detect.

Two or more effects work together as one.

Effect can hit multiple targets or a single target multiple times.

Effect overcomes Impervious Resistance.

Effect can perform delicate and precise tasks.

Extend effect’s reach by 5 feet per rank.

Changes effect’s required action to reaction.

Effect can be removed at will as a free action.

Attacker can bounce effect to change direction.

Secondary Effect

+1 per rank

Instant effect works on the target twice.

Selective

Sleep

Split

Subtle

Sustained

Triggered

+1 per rank



[... truncated ...]
```

**Chunk 2** (`75f616f43b9d`):

```
CHAPTER 2: SECRET ORIGINS

97

6-10

11-15

Jinx: Selective Burst Area Luck Control
2 (negate hero or luck point, force
re-roll), Luck 5 • 15 points

Lucky Cat: Selective Burst Area Luck

Control 2 (grant re-roll, bestow luck
point), Luck 5 • 15 points

16-20

Nine Lives: Immortality 15, Limited:
only works eight times • 15 points

Thick Hide: Protection 4, Impervious 11 • 15 points

Roll 1d20 once and record the result.

ELEPHANT

Groundstrike (Alternate Effect of Strength Damage):

Burst Area Affliction 10 (Resisted by Dodge,
Overcome by Fortitude; Hindered and Vulnerable,
Stunned and Prone), Extra Condition, Limited to Two
Degrees, Limited to targets on the ground • 1 point

1-10

Immovable: Immunity 10 (being moved), Sustained

• 10 points

Power-Lifting: Enhanced Strength 4, Limited to

Lifting • 4 points

Trunk: Extra Limb 1, Elongation 1 • 2 points

Tusks: Strength-based Damage 2, Improved Critical 2

• 4 points

RHINO

Armored Plates: Immunity 4 (critical hits, self-

inflicted slam damage) • 4 points

11-20

Great Horn: Strength-based Damage 3, Improved

Critical 2 • 5 points

Unstoppable Charge: Penetrating 15 on Damage,

Limited to slam attacks; Speed 4 (30 MPH) • 12 points

Reptilian Movement: Movement 1 (Slithering) • 2 points

Heat Sensing Pits: Senses 1 (Infravision) • 1 points

Scaly Hide: Protection 2 • 2 points

Roll 1d20 once and record the result.

CROCODILE

Aquatic: Movement 1 (Environmental Adaptation—

Aquatic), Swimming 6 (30 MPH) • 8 points

1-6

Brute Strength: Enhanced Strength 2 • 4 points

Regrowth: Regeneration 2 • 2 points

Rending Bite: Strength-based Damage 2, Improved

Critical, Secondary Effect • 17 points

LIZARD

Paralyzing Spit: Affliction 10 (Resisted by Dodge,

Overcome by Fortitude; Dazed, Stunned,
Paralyzed), Accurate 2, Reach 3 • 15 points

Prehensile Tail: Elongation 1, Extra Limb 1 • 2 points

Regrowth: Regeneration 1, Persistent • 2 points

Speedy: Leaping 2 (30 feet); Movement 2 (Wall-

crawling 2); Speed 3 (16 MPH) • 9 points

Teeth and Claws: Strength-based Damage 2,

Accurate • 3 points

7-13

98

SNAKE

Tensile Strength: Elongation 4 (120 feet); Enhanced

14-20

Strength 4, Limited to Grabs • 8 points

Venomous Bite: Progressive Weaken Stamina 7
(Resisted by Fortitude), Accurate 2 • 23 points

DEFENSE

DODGE
+6

PARRY
+4

FORTITUDE
+4

TOUGHNESS
+0

WILL
+6

ABILITIES

POWERS

68

36

6

SKILLS

DEFENSES

TOTAL

20

20

150

•  Motivation—Acceptance: The Totem can be regard-
ed as a pariah or outcast in h

[... truncated ...]
```

**Chunk 3** (`bfdbb051d926`):

```
CHAPTER 6: POWERS

195

Example:  The  villain  Doctor  Shock  can  create  an
aura  of  electricity  around  his  body,  damaging  any-
one  or  anything  touching  him.  This  is  a  Reaction
Damage effect, causing Damage when Doctor Shock
is touched. Of course, Doctor Shock’s aura zaps any-
one  or  anything  touching  him,  including  his  allies!
The only way he can prevent this is to turn the aura
off  altogether.  If  Doctor  Shock  possessed  the  ability
to have his aura only damage people and things he
wants it to damage, he would need to have the Selec-
tive modifier applied to the effect as well.

The Reaction modifier applies +1 cost per rank to effects
with  a  default  action  of  free,  +3  cost  per  rank  to  effects
with a default standard action.

FLAT • 1 POINT

You can remove conditions caused by a Reversible effect at
will as a free action, so long as the subject is within the ef-
fect’s range. Examples include removing the damage condi-
tions caused by a Damage effect, repairing damage done by
Weaken Toughness, or removing an Affliction instantly. Nor-
mally, you have no control over the results of such effects.

RICOCHET

FLAT • 1 POINT PER RANK

You  can  ricochet  or  bounce  an  attack  effect  with  this
modifier off of a solid surface to change its direction. This
allows you to attack around corners, overcome cover and
possibly  make  a  surprise  attack  against  an  opponent.  It
does not allow you to affect multiple targets. The “bounce”
has no effect apart from changing the attack’s direction.
You  must  be  able  to  define  a  clear  path  for  your  attack,
which must follow a straight line between each ricochet.
Each  rank  in  Ricochet  allows  you  to  bounce  the  attack
once before it hits. Ricochet may grant a bonus to hit due
to surprise, at the GM’s discretion.

+1 COST PER RANK

An  instant  duration  effect  with  this  modifier  affects  the
target  once  immediately  (when  the  effect  is  used)  and
then  once  again  on  the  following  round,  at  the  end  of
the attacker’s turn. The target gets the normal resistance
check against the secondary effect.

Secondary Effects don’t stack, so if you attack a target with
your Secondary Effect on the round after a successful hit,
it doesn’t affect the target twice; it simply delays the sec-
ond  effect  for  another  round. You  can  attack  the  target
with a different effect, however. So, for example, if you hit
a target with a Secondary Damage Effect then, o

[... truncated ...]
```

**Chunk 4** (`d4cad3e10e05`):

```
CHAPTER 2:
ORIGINS .............. 23
HERO ARCHETYPES ......... 23
HERO DESIGN ................... 23
POINTS ................ 24
Starting Power Points .......... 24
Spending Power Points ...... 24
Power Level ............................. 24
Reallocating

Power Points ........................ 26
COMPLICATIONS .............. 27
Choosing Complications .... 27
Motivation ............................... 27
Other Complications ........... 28
BACKGROUND .................. 30
Name ......................................... 30
Origin ......................................... 30
Age ............................................. 31
Appearance ............................. 32
Personality ............................... 33
Goals .......................................... 33

IMPROVEMENT .............. 33
Increasing Power Level ....... 33
CHARACTER

ARCHETYPES .................. 34
Battlesuit .................................. 35
Construct ................................. 36
Crime Fighter .......................... 37
Energy Controller .................. 38
Gadgeteer ................................ 39
Martial Artist ........................... 40
Mimic ......................................... 41
Mystic ........................................ 42
Paragon .................................... 43
Powerhouse ............................ 44
Psychic ...................................... 45
Shapeshifter ............................ 46
Speedster ................................. 47
Warrior ...................................... 48
Weapon Master...................... 49
FIGHTER -

THE ROOK ....................... 50

POWERHOUSE -

PRINCESS ........................ 52

GENERATOR.................... 54

22

Quickness ...............................174
Regeneration ........................175
Remote Sensing ..................175
Senses .....................................176
Shrinking ................................180
Speed ......................................180
Summon .................................180
Swimming..............................183
Teleport ..................................183
Transform ...............................184
Variable ...................................184
Weaken ...................................186
MODIFIERS...................... 187
Applying Modifiers .............187
Extras .......................................188
Accurate ...............................188
Affects Corporeal ...............188
Affects Insubstantial .........188
Affects Obj

[... truncated ...]
```

---

## Concept: Secret Origins

Chunk count: 83

### Chunk texts

**Chunk 1** (`02269b6c9ef6`):

```
CHAPTER 2: SECRET ORIGINS

49

Power Point Totals:  Abilities 50 + Powers 10  + Advantages 17 + Skills  45 + Defenses 28  = 150

ROOK

Jon  wants  to  create  a  hero  who’s  a  vigilante  type,  someone  with  no  superpowers,  but
great training and skill, along with various crime-fighting gadgets. The hero is intended for

a power level 10 game, with 150 starting power points.

Jon starts out with abilities. He wants his hero to be capable both physically and men-
tally. So he assigns rank 5 to both Agility and Dexterity to make his hero quick, ag-
ile, and accurate, and a 5 to Intellect to make him equally quick on the uptake. He
puts 3 each into Strength and Stamina making his hero well above average in those
abilities, but not quite as much as the others. Similarly, he gives his hero Presence 3
and Awareness 2, both above average, but not his strongest suits. Lastly, since he sees
his hero as a real combat expert, Jon gives him Fighting 8. Each ability rank costs 2 power

points, so Jon has spent 68 of his 150 points, just over a third.

Next, he looks at skills. He wants his hero to be quite skilled and makes a wish list of the skills he
wants. He starts out assigning 8 ranks to each of those skills—knowing skills
cost 1 power point per 2 ranks—but that would use up more than his re-
maining points! So he shifts those ranks around, decreasing less important
skills—like Sleight of Hand and Treatment—and increasing Ranged Com-
bat to match the hero’s Close Combat bonus. When he’s done, Jon has as-
signed 58 ranks in skills, quite a respectable amount, and spent 29 points
(58 ranks, divided by 2). That leaves him with 53 power points remaining.

Fortunately, Jon has decided his hero doesn’t really have any powers, relying
on skills, advantages, and equipment. So he turns to his character’s defenses. He
buys up his Dodge from 5 (for his Agility) to 14 for 9 points and his Parry from 8 (for
his Fighting) to 14 for 6 points. He increases Will from 2 (for his Awareness) to 8 for
another 6 points and gives his hero Fortitude 8, adding 5 points to his basic Stamina 3.

Jon has spent a total of (9 + 6 + 6 + 5) or 26 points on defenses, about half of what he has left.

Now he looks at his hero’s Toughness. Jon can’t increase that directly by spending power points; Tough-
ness can only be improved using advantages and powers, and his hero doesn’t have any powers. His hero
has Toughness 3 from his Stamina and his Toughness defense can be up to 6, given his Dodge

[... truncated ...]
```

**Chunk 2** (`04f4880a6e63`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

HIGHTECH GEAR

Advantage: Equipment 10 (Equipment listed
immediately below)

Smartphone, Restraints, Flashlight, Multi-tool,
Rebreather • 6 points

Headquarters—Size: Huge, Toughness: 10;
Features: Communications, Computer, Concealed,
Garage, Gym, Laboratory, Living Space, Power
System, Security System, Workshop • 15 points

Motorcycle: Medium; Str 1; Speed 6; Defense 10;

Toughness 8 • 10 points

Swingline: Movement 1 (Swinging) • 2 points

Utility Belt • 17 points

11-20

•  Bolos: Ranged Cumulative Affliction 4 (Resisted
by Dodge, Overcome by Damage; Hindered and
Vulnerable, Defenseless and Immobilized), Extra
Condition, Limited Degree • 12 points

•  Boomerangs: Strength-based Ranged Damage 1,

Accurate 2 • 1 point

ure. This motivation is especially appropriate for the
Dark Avenger.

•  Motivation—Thrills: You don’t have any powers, per
se, but why should that stop you from having fun?

•

Enemy: The Crime Fighter usually has at least one vil-
lain central to his or her existence who plagues the
hero consistently.

ELEMENTAL

The Elemental is a being composed of a pure element, usu-
ally one of the classical four elements of earth, air, fire, or
water. They have powers reflecting their elemental compo-
sition, as well as control and mastery over that element.
ABILITIES

•  Explosives: Ranged Burst Area Damage 4 • 1 point

Roll 1d20 once and record the result.

•  Power-Knuckles: Strength-based Damage 3,

Improved Critical, Inaccurate • 1 point

•  Taser: Ranged Cumulative Affliction 4 (Resisted
and Overcome by Fortitude; Dazed, Stunned,
Incapacitated) • 1 point

•  Tear-Gas Pellets: Ranged Cloud Area Affliction 4
(Resisted and Overcome by Fortitude; Dazed and
Visually Impaired, Stunned and Visually Disabled),
Extra Condition, Limited Degree • 1 point

DEFENSES

DODGE
+7

PARRY
+5

FORTITUDE
+4

TOUGHNESS
+0

WILL
+8

ABILITIES

POWERS

68

7/0*

SKILLS

DEFENSES

28/35*

TOTAL

23

24

150

*If you rolled Gadgeteer on the Powers/Equipment table,
then  you  have  Powers  7  and  Advantages  28,  otherwise
you have Powers 0 and Advantages 35.

•  Motivation—Patriotism:  You  strongly  believe  in  the
ideals your country was founded on and fight to uphold
them... especially from those who would twist them to
their own purposes. Patriotic Crime Fighters often have
a military background, but they don’t have to.

•  Motivation—Doing Good: Crime Fighters with this
motivation ar

[... truncated ...]
```

**Chunk 3** (`079ee72c1633`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Comic books are full of storylines involving personal complications, and players are encouraged to come up with some
for their heroes. Complications have a specific use in the game as well: they give the Gamemaster a “handle” on your
hero, different challenges to introduce or include in adventures. When the GM does so, you earn hero points you can
use to enhance your character’s chances of success, amongst other things. (See Hero Points in The Basics and Action
& Adventure chapters for more information.)

Choose at least two complications for your hero: a Motiva-
tion and at least one other. You can take as many compli-
cations  as  you  wish,  although  the  GM  may  set  limits  for
the sake of being able to keep track of them all. Compli-
cations  are  also  self-limiting,  in  that  you  only  earn  hero
points  for  those  complications  that  actually  come  into
play.  So  even  if  you  have  more  than  a  dozen,  if  the  GM
can only include a couple in a game session, then those
are the ones that earn you hero points for that game. You
can—and generally should—look for opportunities to in-
clude your hero’s complications and offer suggestions to
the GM, who makes the final decision on which complica-
tions come into play at any given time.

The GM also decides what complications are appropriate
for  the  game  and  can  overrule  any  particular  complica-
tion,  based  on  the  style  and  needs  of  the  story  and  the
series.  Keep  in  mind  the  adventure  needs  to  have  room
for all of the heroes’ complications, so individual ones can
only come up so often.

Every  hero  has  something  that  drove  him  or  her  to  be-
come  a  hero  in  the  first  place—a  motivation  that  keeps
them going when things get tough. Sometimes motiva-
tion  is  the  only  difference  between  a  hero  and  a  villain.
What  made  your  hero  decide  to  fight  for  justice  rather
than turning toward more selfish goals? How does it affect
the  hero’s  methods  of  fighting  crime?  Is  there  anything
that might change or affect the hero’s motivation?

Motivation is a complication because it often determines
what a hero will do in a particular situation. The GM can
use your hero’s motivation to encourage certain actions,
and enemies may do the same. When you properly play
out your hero’s motivation, even if it isn’t necessarily the
“smartest” thing to do, the GM awards you a

[... truncated ...]
```

**Chunk 4** (`1081db3c43af`):

```
CHAPTER 2: SECRET ORIGINS

69

15-20

Scientist: At heart, you’re a scientist. You’re always
working on something in the lab, but you like to get
“out in the field” and test the practical applications
of your inventions. Plus, there are all sorts of unusual
things out in the world that you’d never get to
experience in the lab.

TINKERER

Accurate Attack, Luck, Power Attack

INVENTOR

Benefit 3 (Millionaire)

SKILLS

Close Combat: Unarmed or Gadgets 6, Expertise: Science 10,
Ranged Combat: Gadgets 6, Technology 10, Vehicles 4

Take the skills listed above, then roll 1d20 once and record
the result.

1-5

6-10

Businessman/woman: You know how to run a
business.

Explorer: You have the skills necessary to explore
new places.

11-15

Investigator: You’re a talented detective.

16-20

Infiltrator: You’re stealthy.

BUSINESSMAN/WOMAN

Expertise: Business 5, Insight 6, Persuasion 5

EXPLORER

Athletics 7, Perception 5, Stealth 4

INVESTIGATOR

Insight 4, Investigation 7, Perception 5

INFILTRATOR

Deception 6, Sleight of Hand 4, Stealth 6

POWERS

Roll 1d20 once and record the result.

ADVENTURER

STRENGTH
2
STAMINA
2
GIMMICK

AGILITY
2
DEXTERITY
2

STRENGTH
2
STAMINA
1

AGILITY
2
DEXTERITY
2
SCIENTIST

FIGHTING
4
INTELLECT
8

AWARENESS
3
PRESENCE
2

FIGHTING
4
INTELLECT
9

AWARENESS
4
PRESENCE
1

STRENGTH
1
STAMINA
2

AGILITY
2
DEXTERITY
2

FIGHTING
4
INTELLECT
10

AWARENESS
4
PRESENCE
0

Beginner’s Luck, Eidetic Memory, Equipment 3 (Headquarters),
Improvised Tools, Inventor, Skill Mastery (Technology)

Headquarters—Size:  Large,  Toughness:  10;  Features:
Communications, Computer, Fire Prevention System, Infirmary,
Laboratory,  Library,  Living  Space,  Personnel,  Power  System,
Security System, Workshop • 15 points

Take the advantages listed above, then roll 1d20 once and
record the result.

1-5

Athletic: You take care of yourself and are physically fit.

6-10

Natural Leader: You’re a natural leader.

11-15

Tinkerer: You’re constantly tinkering with your
inventions and are able to get the most out of them.

16-20

Well-to-do Inventor: You either inherited wealth or
have made money off some of your more mundane
inventions.

ATHLETIC

Evasion, Improved Initiative, Uncanny Dodge

LEADER

8-12

Inspire 2, Leadership

70

1-4

5-7

Energy Projector Device: Ranged Damage 8,
Accurate 2; AE: Ranged Affliction 8 (Resisted
and Overcome by Fortitude; Dazed Stunned,
Incapacitated), Accurate 2; AE: Ranged
Multiattack Damage 5, Accurate 3; AE: Close Cone
Area Dazzle 9

[... truncated ...]
```

**Chunk 5** (`13ce58f9b33f`):

```
CHAPTER 2: SECRET ORIGINS

67

SKILLS

Ranged Combat: Energy Control 5, Choose One: Deception 7
or Intimidation 7

Take the skills listed above, then roll 1d20 twice (re-roll if
you get the same result twice) and record the results.

1-4

Athlete: You have undergone intensive physical
training.

5-8

Cool: You’re young and trendy

9-10

Observant: You are alert and watchful.

11-14

Popular: You know how to deal with people.

15-18

Pilot/Driver: You are a skilled race car driver or
hotshot pilot.

19-20

Sly: You’re sneaky and low-key.

ATHLETE

Acrobatics 4, Athletics 4

COOL

Expertise: Popular Culture 4, Perception 4

As a descriptor, substitute any one energy type on the
list  below  (or  one  you  come  up  with)  in  place  of  the
word, “Energy,” or “Energy Control type,” above.

An  Energy  Controller’s  personality  often  reflect  the
energy type he or she controls, so the descriptions for
Abilities, Advantages, and Skills can help narrow down
which energy type fits your character if you prefer to as-
sign one to your hero.

Alternatively, you might decide to randomly determine
your  Energy  Controller’s  descriptor  by  rolling  on  the
table below.

Roll 1d20 once and record the result.

1-3

4-5

6-7

Cold: You emit cold or remove heat.

Cosmic: You wield the very versatile and
primal cosmic energy.

Darkness: You control darkness—be it
shadow, void, or some other-dimensional
force—or else subtract light.

8-9

Electrical: You generate electricity.

10-12

Fire: You produce flame and heat.

13

14

15-16

17-18

19

20

Hellfire: You control an extra-dimensional,
flame-like energy.

Light: You generate intense light and heat.

Magnetic: You generate magnetic fields and
manipulate ferrous metals.

Plasma: You project super-heated gas, or
plasma.

Sonic: You manipulate and generate sound.

Vibration: You produce and control vibration
and resonant frequencies.

OBSERVANT

Investigation 4, Perception 4

POPULAR

Insight 4, Persuasion 4

PILOT/DRIVER

Technology 4, Vehicles 4

SLY

Sleight of Hand 4, Stealth 4

POWERS

Roll 1d20 once and record the result.

Energy Control: Array (24 points, plus 3 points of

Alternate Effects)

•  Energy Blast: Ranged Damage 12 • 24 points

Quick Change: Feature 1 (transform into costume as

1-10

a free action) • 1 point

11-15

16-20

Take the Energy Control array and Energy Blast
(above), then roll 1d20 three times on the Alternate
Effects sidebar (re-roll if you get the same result
twice) and add them to the E

[... truncated ...]
```

**Chunk 6** (`14dd371ce972`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

DEFENSES

Once you have the first power in your Energy Control ar-
ray,  roll  1d20  three  times  on  the  Alternate  Effects  table
(re-roll if you get the same result twice) and add them to
the Energy Control array as Alternate Effects.

1-2

3-4

5-6

•  Dazzle: Cumulative Ranged Affliction 12 (Resisted

by Dodge, Overcome by Fortitude; Impaired,
Disabled, Unaware), Limited to One Sense (Choose
one sense: Vision or Auditory) • 1 point

•  Disintegrate: Ranged Affects Objects Weaken

Toughness 8 • 1 point

•  Energy Burst: Choose One: Burst Area Damage
10, Penetrating 4 • 1 point or Ranged Burst Area
Damage 8 • 1 point

DODGE
+4

PARRY
+1

FORTITUDE
+5

TOUGHNESS
+0

WILL
+6

ABILITIES

POWERS

34

82

4

SKILLS

DEFENSES

TOTAL

14

16

150

7-8

•  Energy Constructs: Create 12 • 1 point

9-10

•  Energy Manipulation: Deflect 12, Reflect,
Redirect, Limited to Energy attacks • 1 point

•  Motivation—Recognition: Energy Controllers, par-
ticularly those with a flashy energy type, often desire
fame and attention.

11-12

•  Energy Weapon: Penetrating Damage 12 • 1 point

13-14

15-16

17-18

•  Environmental Control: Environment 12 (8 miles;
Choose two: Cold, Heat, Impede Movement, Light,
Visibility) • 1 point

•  Obscure: Ranged Visual Concealment 4 Attack,

Choose One Extra: Burst Area or Cloud Area • 1 point

•  Snare: Cumulative Ranged Affliction 8 (Resisted
by Dodge, Overcome by Damage; Hindered and
Vulnerable, Defenseless and Immobile), Extra
Condition, Limited to Two Degrees • 1 point

19-20

•  Telekinesis: Move Object 12 • 1 point

Energy Immunity: Immunity 5 (Energy Control type damage)

• 5 points

Roll 1d20 once and record the result.

1-5

6-10

11-20

Energy Absorption: Enhanced Strength 10, Fades;

Enhanced Stamina 10, Fades • 20 points

Energy Shield: Enhanced Defenses 10 (Dodge 5, Parry
5); Impervious Protection 5, Sustained • 20 points

Force Field: Impervious Protection 10, Sustained

• 20 points

Energy Sense: Senses 1 (Energy type Awareness) • 1 point

Roll  1d20  twice  (re-roll  if  you  get  the  same  result  twice)
and record the results.

1-4

5-8

Energy Aura: Reaction Damage 4, Activation

(Standard Action, -2 points) • 14 points

Energy Form: Insubstantial 3 (Energy Control type),

Activation (Move Action, -1 point) • 14 points

9-16

Flight: Flight 7 (250 MPH) • 14 points

17-18

Scry: Visual Remote Sensing 14 (60 miles), Medium
(presence or cond

[... truncated ...]
```

**Chunk 7** (`1631a649fb6e`):

```
CHAPTER 2: SECRET ORIGINS

79

•

Identity:  The  Paragon  often  hides  his  or  her  true
identity  from  the  rest  of  the  world.  Often  the  Para-
gon feels that this “normal” identity keeps him or her
grounded and in touch with the rest of humanity.

•  Motivation—Doing Good: The Paragon is motivat-
ed to be a hero because it’s the right thing to do.

•  Motivation—Patriotism:  The  Paragon  is  a  patriot
and fights to uphold the ideals of his or her country.

•  Motivation—Responsibility:  The  Paragon  is  often
motivated  by  the  belief  that  with  power  comes  re-
sponsibility.

•

•

•

Power  Loss:  Usually  caused  by  transforming  back
to a normal human form, some Paragons lack access
to  their  powers  all  the  time.  If  you  choose  this  op-
tion, create a non-powered version of your character
that doesn’t have any of its Powers, has human-level
Abilities, and may even have lower ranks of Skills and
completely different Advantages.

Prejudice:  Some  Paragons  are  appear  inhuman  in
some way and are treated with distrust or fear by the
public.

Relationship:  Paragons  often  have  a  large  number
of  friends,  family,  or  fans  that  get  into  trouble  with
alarming frequency.

•  Weakness: Because the Paragon is so powerful in so
many ways, he or she often suffers from a crippling
weakness to a particular type of attack.

The Powerhouse is the strongest one there is! Where other
archetypes spread their points out amongst a number of
different  powers  and  abilities,  the  Powerhouse  concen-
trates  on  two  things:  strength  and  protection.  In  fights,
the Powerhouse is always on the front line, tearing it up
and,  even  so,  is  usually  the  last  one  standing. The  Pow-
erhouse  is  often  inhuman-looking,  either  because  he  or
she’s been turned into a hulking brute, or is from an alien
world, or is capable of transforming into living stone, steel,
or something equally resistant to damage.
ABILITIES

Roll 1d20 once and record the result.

1-6

7-14

Alternate Form: You are made of a highly resistant
material like metal or stone.

Innate Power: You’re an alien or are from some
hidden offshoot of humanity with incredible powers.

15-20 Mutate/Mutant: You were either born with mutant

powers or were mutated in a one-in-a-million
accident or experiment.

FORM

STRENGTH
4
STAMINA
4

AGILITY
1
DEXTERITY
0

FIGHTING
6
INTELLECT
0

AWARENESS
1
PRESENCE
2

POWER

STRENGTH
4
STAMINA
4

AGILITY
1
DEXTERITY
0

FIGHTING
6
IN

[... truncated ...]
```

**Chunk 8** (`17270869c240`):

```
CHAPTER 2: SECRET ORIGINS

87

Roll 1d20 once and record the result.

1-5

Fighter: You were trained in combat.

6-10

Nimble: You are quick-footed.

11-15

Prodigy: You have learned a little bit of everything.

16-20

Team-Player: You have experience working as part
of a super-team.

FIGHTER

Close Attack 2, Equipment (Sword or other melee weapon)

NIMBLE

Evasion, Instant Up, Move-by Action

PRODIGY

Beginner’s Luck, Eidetic Memory, Well-informed

TEAM-PLAYER

Interpose, Set-up, Teamwork

SKILLS

Roll 1d20 twice (do not re-roll if you get the same result
twice) and record the results.

1-4

5-8

Athlete: You are a trained athlete.

Charmer: People like you.

9-12

Police: You work in law enforcement.

13-16

Scientist: You are an expert in a field of science.

17-20

Thief: You’ve operated outside the law.

16-20

ATHLETE

Acrobatics 4, Athletics 8, Perception 4

CHARMER

Deception 6, Insight 4, Persuasion 6

POLICE

Insight 4, Investigation 6, Perception 6

SCIENTIST

Expertise: (Choose One) 6, Technology 6, Vehicles 4

THIEF

Deception 4, Stealth 6, Technology 6

POWERS

Roll 1d20 once and record the result.

Running: Roll 1d20 once:

1-10

Gravity-Defying Runner: Movement
3 (Wall-crawling 2, Water Walking),
Limited to While Moving; Quickness 10;
Speed 15 (64,000 MPH) • 28 points

1-10

11-15

16-20

Rapid Metabolism: Immunity 1 (Poison);
Quickness 11; Regeneration 5; Speed
11 (4,000 MPH) • 28 points

Time-Traveler: Movement 3 (Time

Travel—any time); Quickness 10; Senses
4 (Precognition), Check Required
(Intellect or Expertise: History); Speed
10 (2,000 MPH) • 28 points

11-15

Flying: Roll 1d20 once:

Cosmic Speedster: Flight 9 (1,000 MPH);

Immunity 6 (cold, heat, radiation,
suffocation, vacuum); Movement 2
(Environmental Adaptation—Zero-G;
Space Travel 1) • 28 points

Hypersonic: Flight 14 (32,000 MPH) • 28

points

Hyper-Speed: Flight 10 (2,000 MPH);

Quickness 8 • 28 points

1-5

6-15

16-20

Teleporting: Roll 1d20 once:

1-5

6-10

Dimensional Walker: Movement 3

(Dimension Travel—any dimension);
Teleport 11 (8 miles) • 28 points

Proximal: Teleport 9 (2 miles), Accurate,

Turnabout • 28 points

Transmit: Teleport 9 (2 miles), Easy,

11-15

Extended (500 miles), Medium (Choose
One), Turnabout • 28 points

16-20

World-Walker: Teleport 9 (2 miles),
Extended (500 miles), Turnabout
• 28 points

Speedster Stunts: Array (20 points plus 1 point of Al-
ternate Effect)

Roll 1d20 once and record the result as the first power in
the  Speedster  Stunts  a

[... truncated ...]
```

**Chunk 9** (`179f10a90f72`):

```
CHAPTER 2: SECRET ORIGINS

23

nuses for your character, paying 1 power point per +1 de-
fense over the base rank provided by your hero’s abilities.
To improve your hero’s Toughness, see Advantages and
Powers, following. See the Abilities chapter for details.
5. SKILLS

Choose  the  skill  ranks  you  want  your  character  to  have
and pay 1 power point per 2 total skill ranks. See the Skills
chapter for details.

6. ADVANTAGES

Choose the advantages you want your character to have
and pay 1 power point per advantage or rank in a advan-
tage. See the Advantages chapter for details.

7. POWERS

Create  your  hero’s  powers  by  choosing  their  desired  ef-
fects  and  paying  the  effects’  base  cost,  adjusted  for  any
modifiers, and multiplied by the number of ranks. See the
Powers chapter for details.
8. COMPLICATIONS

Choose at least two complications for your hero. You can
have more, if you want, and the more complications your
hero  faces,  the  greater  your  chances  for  earning  hero

points during the game. See the Complications section
of this chapter for details.
9. DETAILS

Go  through  the  limits  listed  under  Power  Level  in  this
chapter and make sure your hero’s traits all fit within them.
If not, adjust the traits accordingly until they do.

Go back through and add up the costs of your hero’s abili-
ties, defenses, skills, advantages, and powers. You should
end  up  with  a  figure  equal  to  the  starting  power  points
shown on the Starting Power Points table. If not, double-
check your math and either remove or add traits to your
character to reach the starting power point total.

Figure out things like your hero’s name, appearance, origin,
background, and motivation. If you can, consider creating a
sketch or detailed description of your hero’s costume.

10. GAMEMASTER APPROVAL

Show your new hero to the Gamemaster for approval. The
GM should check again to make sure your power points
are  spent  and  added  up  correctly,  your  hero  follows  the
power  level  guidelines  and  any  other  guidelines  set  for
the  series,  and  that  the  character  is  generally  complete
and  suited  to  the  overall  game.  Once  your  GM  has  ap-
proved, your new hero is ready for play!

You design a MUTANTS & MASTERMINDS hero by spending pow-
er points on different traits. Each ability, skill, advantage,
power, and other trait has an associated power point cost.

The game’s power level provides a guideline for how many
power points you

[... truncated ...]
```

**Chunk 10** (`19a54c3b3576`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

6-9

Magic Sword: Strength-based Damage 3 (6 Damage
with Strength), Multiattack 6, Penetrating 6, Easily
Removable (-6 points) • 9 points

10-11

12-13

Modified Nunchaku: Strength-based Damage 2 (5
Damage with Strength), Multiattack 5, Improved
Grab, Improved Trip, Reach 3, Ricochet; Movement
1 (Swinging); Easily Removable (-6 points) • 9 points

Perfect Aim: Perception Range Damage 5, Easily
Removable (ranged or improvised weapon, -6
points) • 9 points

14-15

Rapid Shot: Ranged Multiattack Damage 5, Easily
Removable (ranged weapon, -6 points) • 9 points

16-20

Super-Shield: Array (13 points plus 2 points of

Alternate Effects), Easily Removable (-6 points)
• 9 points total

•  Blocking: Deflect 13 • 13 points

•  Shield Bash: Strength-based Damage 2 (5

Damage with Strength), Penetrating 5 • 1 point

•  Shield Throw: Strength-based Ranged Damage 2
(5 Damage with Strength), Multiattack 5 • 1 point

Roll 1d20 once and record the result.

1-2

3-6

7-10

11-12

Blindsight: Senses 6 (Accurate, Analytical and

Extended Hearing, Hearing Counters Illusion)
• 6 points

Catlike Balance: Enhanced Skills 2 (Acrobatics 4),
Leaping 2 (30 feet), Movement 1 (Safe Fall)
• 6 points

Healing Factor: Immunity 1 (Disease); Regeneration

5 • 6 points

Probing Sight: Mind Reading 4, Limited to Surface
Thoughts, Visually Sense-Dependent; Senses 4
(Vision Penetrates Concealment) • 6 points

13-14

Reinforced Body: Impervious Toughness 6 • 6 points

15-16

17-20

Resilient: Immunity 6 (Cold, Drowning, Heat, Need
for Sleep, Pressure, Starvation and Thirst) • 6 points

Super-Soldier: Enhanced Fortitude 2, Regeneration

2; Speed 2 (8 MPH) • 6 points

DEFENSE

DODGE
+7

PARRY
+6

FORTITUDE
+5

TOUGHNESS
+0

WILL
+8

ABILITIES

POWERS

56

15

13

SKILLS

DEFENSES

TOTAL

40

26

150

•  Motivation—Recognition:  The  Weapon  Master  is
driven by a need to be recognized as the best at what
he does.

•

•

•

Disability:  The  Weapon  Master  has  a  disability  of
some sort, such as blindness or only one arm, that he
overcomes through his skills or powers.

Honor:  The  Weapon  Master  abides  by  a  warrior’s
code of honor.

Rival: The Weapon Master has a foil—another Weap-
on Master who tries to outdo him at every turn.

Weather  Controllers  combine  control  over  the  elements
of air and water with cold and electrical energy. They gen-
erally command the more violent aspects of the weather,
such as 

[... truncated ...]
```

**Chunk 11** (`1af862ab5396`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Battlesuits  typically  fall  into  one  of  three  categories:
they’re either ranged combatants, melee powerhouses, or
a mix of the two. No matter what role the Battlesuit fills,
the  person  inside  the  armor  tends  to  be  a  fairly  normal
person, possibly highly trained or highly intelligent, who
relies on the armor to provide his or her powers.
ABILITIES

Roll 1d20 once and record the result.

13-16

17-20

Scientist: You work as a scientist and/or have
natural talent in that area.

Wealthy: Whether you inherited or earned it, you’re
a part of the upper-crust of society.

COMBATANT

Accurate Attack, All-out Attack, Improved Initiative, Interpose,
Move-by Action

INVENTOR

Eidetic Memory, Improvised Tools, Inventor, Ultimate Effort
(Technology), Well-informed

1-12

Genius: You’re incredibly intelligent and likely had a
hand in creating your battlesuit.

LUCKY

13-18

19-20

Military: You were trained by the military as a
soldier or scientist and may have received or stolen
your battlesuit from them.

Accidental: You chanced upon your armor
somehow, either the armor’s creation was a one-
time fluke, it was found by you, or it was given to
you by an organization or aliens.

GENIUS

STRENGTH
0
STAMINA
1

AGILITY
1
DEXTERITY
2

FIGHTING
2
INTELLECT
8

AWARENESS
2
PRESENCE
2

MILITARY

STRENGTH
3
STAMINA
3

AGILITY
1
DEXTERITY
2
ACCIDENTAL

FIGHTING
3
INTELLECT
2

AWARENESS
2
PRESENCE
2

STRENGTH
2
STAMINA
1

AGILITY
3
DEXTERITY
2

FIGHTING
2
INTELLECT
3

AWARENESS
3
PRESENCE
2

Roll  1d20  twice  (re-roll  if  you  get  the  same  result  twice)
and record the results.

1-4

5-8

Combatant: You have natural talent or you’ve been
trained in combat, both in armor and out.

Inventor: You know your way around technology, have
a headquarters, and can build gadgets given time.

9-12

Lucky: Things are easy for you.

Beginner’s Luck, Luck 2, Redirect, Teamwork

SCIENTIST

Equipment 3 (Headquarters), Skill Mastery (Expertise:
Science), Skill Mastery (Technology)

Headquarters—Size: Large, Toughness: 10; Features:
Communications, Computer, Fire Prevention System, Hangar,
Infirmary, Laboratory, Library, Living Space, Power System,
Security System, Workshop • 15 points)

WEALTHY

Attractive, Benefit 4 (Multi-millionaire)
SKILLS

Roll 1d20 twice (do not re-roll if you get the same result
twice) and record the results.

1-4

People Person: You’re good with people and in
business.

5-16


[... truncated ...]
```

**Chunk 12** (`1b8011530852`):

```
CHAPTER 2: SECRET ORIGINS

101

11-15

16-20

Vigilante: You use your weapons to fight crime and
injustice.

Weaponsmith: You craft your own weapons and
even augment them with the latest technology.

SOLDIER

Expertise: Military 6, Vehicles 6

TIME-DISPLACED

PERSONALITY

Deception 8, Intimidation 8, Persuasion 8

TALKER

Deception 10, Insight 4, Persuasion 10

POWERS

Expertise: History 6, Choose One: Expertise: Magic 6 or
Technology 6

VIGILANTE

Roll 1d20 once and record the result.

Expertise: Streetwise 6, Investigation 6

WEAPONSMITH

Expertise: Weapons 6, Technology 6

Roll 1d20 once and record the result.

1-6

Flamboyant: You fight with great flair.

7-14

Instinctive: You let your well-honed reflexes take over.

15-20

Sneaky: You prefer to avoid a direct confrontation.

FLAMBOYANT

Acrobatics 8, Athletics 4, Sleight of Hand 4

INSTINCTIVE

Acrobatics 6, Athletics 6, Stealth 4

SNEAKY

Acrobatics 6, Athletics 4, Stealth 6

Roll 1d20 once and record the result.

1-4

5-8

Assertive: You know how and when to take charge.

Cunning: You are good at manipulating others.

9-12

Empathic: You seem to understand others.

13-16

Forceful Personality: Others seem to instinctively
respect you.

17-20

Smooth Talker: You know how to get your way.

ASSERTIVE

Insight 8, Intimidation 8, Persuasion 8

CUNNING

Deception 10, Insight 8, Perception 6

EMPATHIC

Insight 10, Perception 6, Persuasion 8

Bow and Trick Arrows: Array (10 points plus five

Alternate Effects), Easily Removable (-6 points) • 9
points total

Standard Arrow: Ranged Damage 5 • 10 points

Roll 1d20 five times (re-roll if you get the same result
twice) and add them to the Bow and Trick Arrows
array as Alternate Effects.

1-2

3-4

5-6

7-8

1-5

9-10

11-12

13-14

15-16

17-18

19-20

•  Boomerang Arrow: Ranged Damage

4, Homing, Subtle • 1 point

•  Boxing Glove Arrow: Ranged
Affliction 5 (Resisted by Dodge,
Overcome by Fortitude; Dazed,
Stunned, Incapacitated) • 1 point

•  Cable Arrow: Movement 1

(Swinging) • 1 point (if you get this
result twice, place the Cable Arrow
outside the array instead for 2
points): Cable Arrow: Movement 1
(Swinging) • 2 points

•  Explosive Arrow: Burst Area Ranged
Damage 5, Unreliable (five uses)
• 1 point

•  Flare Arrow: Ranged Cumulative

Affliction 5 (Resisted and Overcome
by Fortitude; Visually Impaired,
Visually Disabled, Visually Unaware),
Limited to One Sense • 1 point

•  Knockout Gas Arrow: Burst Area
Ranged Affliction 5 (Resisted and
Overcome by Fort

[... truncated ...]
```

**Chunk 13** (`267bbd73af09`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

INNOCENT

Animal Empathy, Luck

INCISIVE

Daze (Deception), Taunt

SPONTANEOUS

Improved Initiative, Uncanny Dodge

SUBTLE

Evasion, Hide in Plain Sight

SKILLS

Roll 1d20 twice (do not re-roll if you get the same result
twice) and record the results.

1-3

Dynamic: You are a good all-around athlete.

4-7

Empathic: You understand what makes other
people tick.

8-10

Furtive: You don’t like to stand out.

11-14

Inscrutable: Your emotions are difficult to read.

15-18 Observant: Little escapes your notice.

19-20

Sponge: You possess an open and receptive mind.

DYNAMIC

Acrobatics 6, Athletics 6

EMPATHIC

Insight 8, Persuasion 4

FURTIVE

Deception 6, Stealth 6

INSCRUTABLE

Deception 8, Perception 4

OBSERVANT

Insight 6, Perception 6

SPONGE

Expertise: Current Events 4, Expertise: Popular Culture 4,
Investigation 4

POWERS

Roll 1d20 once and record the result.

1-2

Animal Mimicry: Variable 10 (50 points, to mimic
Traits of one animal at a time), Continuous
• 80 points

Mental Duplication: Mind Reading 10, Limited
to Duplicated mind; Variable 10 (50 points, for
duplicating a subject’s mental traits), Continuous,
Resistible by Will • 80 points

Nemesis: Variable 8 (40 points, for traits suitable for
confronting a particular opponent), Continuous,
Free Action • 80 points

Object Mimicry: Variable 8 (40 points, for traits of

object touched), Reaction • 80 points

3-4

5-6

7-9

10-13

Power Duplication: Variable 10 (50 points, for

duplicating one target’s powers), Continuous
• 80 points

14-15

Power Theft: Cumulative Affliction 12 (Resisted

and Overcome by Will; Powers Impaired, Powers
Disabled, Transformed—Powerless) Linked to
Variable 8 (40 points, for duplicating one target’s
powers), Move Action, Limited to Afflicted
subjects • 80 points

16-17

Reflex Memory: Variable 8 (40 points, for observed
Skills and Advantages), Continuous, Free Action
• 80 points

18-20

Android Body: Immunity 30 (Fortitude Effects),
Reduced Traits (Stamina —, Fortitude —);
Protection 5 • 16 points

Power Duplication: Variable 8 (40 points, for

duplicating a target’s powers), Continuous • 64 points

DEFENSES

DODGE
+5

PARRY
+5

FORTITUDE
+5

TOUGHNESS
+0

WILL
+5

ABILITIES

POWERS

32

80

6

SKILLS

DEFENSES

TOTAL

12

20

150

•  Motivation—Acceptance: Due to the nature of their
powers, many Mimics feel as if they lack an identity of
their own. They may seek acceptance as unique indi-
v

[... truncated ...]
```

**Chunk 14** (`301534069c2d`):

```
CHAPTER 2: SECRET ORIGINS

99

5-8

Cybernetic Implants: Enhanced Awareness

2; Enhanced Advantages 2 (Eidetic Memory,
Improved Initiative); Enhanced Defenses 4 (Parry
2, Dodge 2); Senses 6 (Accurate and Extended
Hearing, Analytical and Extended Vision,
Infravision) • 16 points

9-15

Healing Factor: Enhanced Stamina 2; Immunity 2
(disease, poison); Regeneration 10 • 16 points

16-20

Tactical Mastermind: Enhanced Intellect 2,

Enhanced Awareness 2; Enhanced Advantages
3 (Defensive Roll 2, Uncanny Dodge); Senses
5 (Danger Sense, Detect Weakness—Acute,
Analytical, Ranged) • 16 points

OTHERWORLDLY

Roll 1d20 once and record the result.

1-4

5-6

7-11

12-17

18-20

Alien: Enhanced Stamina 2; Immunity 7 (Cold, Heat,
Pressure, Radiation, Suffocation, Vacuum); Mental
Communication 1; Senses 1 (Mental Awareness)
• 16 points

Aquatic: Enhanced Stamina 2; Immunity 3 (Cold,

Drowning, Pressure); Movement 1 (Environmental
Adaptation—Aquatic); Senses 1 (Low-light Vision);
Swimming 6 (30 MPH) • 16 points

Exemplar: Enhanced Stamina 1, Enhanced

Awareness 1, Enhanced Defenses 2 (Dodge 1,
Parry 1); Immunity 2 (Aging, Disease); Quickness 4;
Speed 4 (30 MPH) • 16 points

Immortal: Enhanced Awareness 2; Immortality
5, Limited (choose effect); Immunity 3 (Aging,
Disease, Poison); Protection 2; Regeneration 2
• 16 points

Winged: Enhanced Awareness 2, Enhanced

Defenses 4 (Dodge 2, Parry 2); Flight 6 (120 MPH),
Wings; Immunity 1 (Cold); Senses 1 (Extended
Vision) • 16 points

HUMAN

Roll 1d20 once and record the result.

11-20

Unique Weapon: Strength-based Damage 3,

Accurate, Penetrating 10 plus roll 1d20 once:

1-5

6-10

Atom Slicer: Weaken Toughness 10,

Penetrating 2, Linked to Damage, Easily
Removable (-10 points) • 16 points

Boom Staff: Movement 3 (Space Travel

3), Portal; Easily Removable (-10
points) • 16  points

11-15

Dimension Cutter: Movement 3

(Dimension Travel 3), Portal; Easily
Removable (-10 points) • 16 points

16-20

Thundering Mallet: Cumulative
Affliction 10 (Resisted and
Overcome by Fortitude; Vulnerable,
Defenseless), Limited Degree, Linked
to Damage, Penetrating 2; Easily
Removable (-10 points) • 16 points

DEFENSE

DODGE
+4

PARRY
+2

ABILITIES

POWERS

FORTITUDE
+2

TOUGHNESS
+0

WILL
+6

78

32

9

SKILLS

DEFENSES

TOTAL

17

14

150

•  Motivation—Patriotism:  Duty  to  country  may  have
motivated the warrior to have undergone experiments
that transformed him or to visit the world outside his
home.

•  Motivation—Responsibility:  The  war

[... truncated ...]
```

**Chunk 15** (`301ee8a15809`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Heroes in MUTANTS & MASTERMINDS cover a diverse range of power levels, from the first costumed adventurers of the Golden
Age, who relied solely on their skills and a few gimmicks (and modern vigilantes of the mean streets, who do much the
same), to the greatest protectors of the world, who take on cosmic threats on a regular basis. The following are some com-
mon power levels and starting power point values suitable for different M&M games:

LEVEL 8 - MASKED ADVENTURERS

This power level fits the “Mystery Men” era of the Golden Age of comic books, as well as for teams of mostly non-powered
adventurers: heroes who rely more on their skills and wits (and maybe a few gadgets) rather than amazing powers. The sug-
gested starting value of 120 power points creates well-rounded heroes at this level, particularly if the emphasis is on skills
and advantages—and maybe a power or two—rather than a lot of powers. Think Dr. Tomorrow and Foreshadow rather than
Captain Thunder and Daedalus. A higher starting power point total allows for more diverse capabilities within the same limits.

Heroes at this level often focus more on skill than sheer damage output, often having fighting skills in the 10–12 range,
but commensurately lower damage and effect ranks (using just their fists or small arms).

LEVEL 10 - SUPER HEROES

The suggested starting power level for MUTANTS & MASTERMINDS suits mature and experienced “adventurers” of the previous
level along with a wide range of younger or focused superhumans. This is the power level of the Sentinels, characters like
Bowman and Seven, and a great many of other heroes. It’s also good for powerful, but relatively inexperienced heroes like
Megastar when he first joined the Next-Gen.

Power level 10 heroes may have a balance of attack and effect, defense and resistance, or may go for being stronger on
one side than the other, having great combat skill, but comparatively limited damage, for example, or great Toughness,
but lowered defenses.

LEVEL 12 - BIG LEAGUES

Power level 12 is where you find many of the members of the current Freedom League: Daedalus, Lady Liberty, and the
Raven, to name a few. They are “senior” heroes, usually with considerable capabilities (and, often, experience). Those lacking
superhuman powers (such as the Raven) have amazing levels of skill and resources to draw upon while the superhuman
types are often among the most capable in

[... truncated ...]
```

**Chunk 16** (`3c75d5b04a0e`):

```
CHAPTER 2: SECRET ORIGINS

41

Power Point Totals:  Abilities 32 + Powers 84  + Advantages 1 + Skills  12 + Defenses 21  = 150

PL10PL10

MYSTIC
MYSTIC

STRENGTH
0
STAMINA
0

POWERS

AGILITY
1
DEXTERITY
3

FIGHTING
4
INTELLECT
3

AWARENESS
6
PRESENCE
4

Astral Projection: Remote Sensing 10 (visual,

auditory, mental), physical body is defenseless,
Subtle 2 • 32 points.

•  Levitation: Flight 4 (30 MPH) and

Mystic Shield: Protection 12, Impervious,
Sustained • 1 point.

Mystic Senses: Senses 2 (Magical
Awareness, Radius) • 2 points.

Spellcasting: Ranged Damage 12

(mystic blast) • 24 points.

•  Choose five Alternate Effects • 5 points.

Fearless, Ranged Attack 5, Ritualist, Trance

SKILLS

Expertise: Magic 10 (+13), Insight 6 (+12),
Intimidation 4 (+8), Perception 4 (+10), Sleight of Hand 4 (+7)

OFFENSE

INITIATIVE +1

Spellcasting +8

Ranged, Damage 12 plus others

Unarmed +4

Close, Damage 0

DEFENSE

DODGE

PARRY

WILL

FORTITUDE

TOUGHNESS

6

12

8

6

13

Power Point Totals:  Abilities 42 + Powers 64  + Advantages 8 + Skills  14 + Defenses 22  = 150

42

```

**Chunk 17** (`3e277f7add29`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

11-15

Powerful Connection: You have a strong
connection or mastery over the magic at your
command.

16-20

Student of the Arts: You study and research
constantly in order to keep informed.

CENTERED

Fearless, Ultimate Effort (Will checks)

ENCHANTER

Artificer, Skill Mastery (Expertise: Magic)

3-4

5-6

7-8

9-10

11-12

13-14

CONNECTION

15-16

Accurate Attack, Power Attack

ARTS

Ritualist, Well-informed

SKILLS

17-18

19-20

•  Dispel Magic: Nullify 8, Broad (Magic),

Simultaneous • 1 point

•  Enervation: Ranged Weaken 8, Broad (Physical

Abilities (one at a time)) • 1 point

•  Enhanced Strength: Enhanced Strength 9;
Enhanced Trait 6 (Close Attack 6) • 1 point

•  Ghost Hands: Perception Move Object 7, Precise,

Subtle 2 • 1 point

•  Healing Hand: Healing 5, Energizing, Persistent,

Restorative, Stabilize • 1 point

•  Maddening Blast: Ranged Damage 8, Resisted by

Will • 1 point

•  Mystic Bindings: Ranged Affliction 12 (Resisted
and Overcome by Will; Hindered and Vulnerable,
Defenseless and Immobile), Extra Condition,
Limited Degree • 1 point

•  Mystic Constructs: Create 7, Continuous, Innate,

Precise, Subtle • 1 point

•  Phantasms: Illusion 4 vs. All Senses, Area (30

cubic feet), Resistible by Will, Selective • 1 point

Expertise: Magic 10, Insight 6, Perception 4

Take the skills listed above, then roll 1d20 once and record
the result.

Astral Projection (Remote Sensing 8 (Visual, Auditory,

Mental), Limited—Physical body is defenseless, Subtle
2), AE: Levitation and Mystic Shield (Flight 4 (30 MPH);
Sustained Protection 12, Impervious 6) • 27 points

1-8

Affecting Presence: You have the skills necessary to
explore new places.

9-14

Occult Investigator: You make it a point to
investigate unusual crimes. You may even consult for
the police.

15-20

Prestidigitator: You’ve studied the art of deception.

PRESENCE

Intimidation 4, Persuasion 4

INVESTIGATOR

Investigation 4, Sleight of Hand 4

PRESTIDIGITATOR

Deception 4, Sleight of Hand 4

POWERS

Magic Spells: Array (24 points, plus 5 points of Alternate

Effects)

•  Magical Blast: Ranged Damage 12 • 24 points

Take the Magic Spells and Magical Blast (above), plus roll
1d20 five times (re-roll if you get the same result twice) and
add them to the Magic Spells array as Alternate Effects.

1-2

•  Billowing Darkness: Ranged Burst Area
Concealment 4 Attack (All Visual) • 1 point

Roll 1d20 once and record the 

[... truncated ...]
```

**Chunk 18** (`43d5c758bf78`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

WASP

Insect Senses: Senses 4 (Acute Smell, Darkvision,

Ranged Touch) • 4 points

16-20

Sting: Cumulative Affliction 8 (Resisted and Overcome
by Fortitude; Impaired, Disabled, Incapacitated),
Linked to Damage 8, Accurate 2 • 26 points

Roll 1d20 once and record the result.

CANINE

Bite: Strength-based Damage 3, Improved Critical,

Wings: Flight 6 (120 MPH), Wings • 6 points

Penetrating 3 • 7 points

Canine Senses: Senses 3 (Low-light Vision, Acute

and Tracking Olfactory) • 3 points

1-10

Canine Movement: Leaping 2 (30 feet); Speed 4 (30

Talons: Strength-based Damage 1, Accurate 2, Fast Grab

MPH) • 6 points

• 4 points

Roll 1d20 once and record the result.

FALCON

Flight: Flight 6 (120 MPH), Wings • 6 points

Keen Eyesight: Senses 3 (Extended 2 and Rapid

Vision) • 3 points

1-10

Sonic Scream: Cone Area Affliction 9 (Resisted

and Overcome by Fortitude; Dazed and Auditory
Impaired, Stunned and Auditory Disabled,
Incapacitated and Auditory Unaware), Extra
Condition, Quirk—Impaired, Disabled, Unaware
Limited to One Sense (-4 points) • 23 points

11-20

OWL

Nightvision: Senses 2 (Extended Vision, Low-light

Vision) • 2 points

11-20

Shriek: Cone Area Affliction 8 (Resisted and
Overcome by Will; Dazed and Vulnerable,
Stunned and Defenseless, Incapacitated)
• 24 points

Silent Flight: Flight 5 (60 MPH), Subtle, Wings • 6 points

Howl: Auditory Perception Area Affliction

10 (Resisted and Overcome by Will; Dazed
and Impaired, Disabled and Stunned), Extra
Condition, Limited Degree • 20 points

FELINE

Claws: Strength-based Damage 1, Accurate,

Improved Critical • 3 points

Feline Senses: Senses 3 (Low-light Vision, Acute and

Tracking Olfactory) • 3 points

Feline Movement: Leaping 3 (60 feet); Movement
3 (Safe Fall, Sure-footed, Trackless); Movement
1 (Water-walking), Limited to Solid Surfaces;
Movement 1 (Wall-crawling), Limited to One
Move Action; Speed 4 (30 MPH) • 15 points

Plus roll 1d20 once and record the result.

1-5

Black Cat: Reaction Visual Perception

Area Affliction 5 (Resisted by Dodge,
Overcome by Will; Vulnerable,
Defenseless, Incapacitated), Side-
effect (Always happens, chosen by
player) • 15 points

```

**Chunk 19** (`442f2e5a5a37`):

```
CHAPTER 2: SECRET ORIGINS

81

1-3

Burrowing: Burrowing 6 (4 MPH), Penetrating • 12

points

4-8

Flight: Flight 6 (120 MPH) • 12 points

9-14

Super-Leaping: Leaping 12 (4 miles) • 12 points

15-20

Super-Movement: Speed 5 (60 MPH); Leaping 7

(1,000 feet) • 12 points

Roll 1d20 once and record the result.

1-2

3-6

7-10

11-14

15-17

18-20

Enhanced Senses: Senses 5 (Extended Auditory 2,
Extended Vision 2, Low-light Vision) • 5 points

Fast Recovery: Regeneration 4, Enhanced

Advantage 1 (Diehard) • 5 points

Faster: Depending on the Movement Power you
rolled; Burrowing: add 1 rank of Penetrating
Burrowing and Senses 3 (Infravision, Direction
Sense, Distance Sense); Flight: add 2 ranks of
Flight and an Alternate Effect of Swimming 6;
Super-Leaping: add 5 ranks of Leaping; Super-
Movement: add 2 ranks of Speed and 3 ranks of
Leaping • 5 points

Immortal: Immortality 2, Enhanced Advantage 1

(Diehard) • 5 points

Like Hitting a Brick Wall: Reaction Damage 1,

Penetrating 1 • 5 points

Pliable Form: Elongation 1 (15 feet); Movement 2

(Permeate, Safe Fall) • 5 points

DEFENSE

DODGE
+5

PARRY
+0

FORTITUDE
+0

TOUGHNESS
+0

WILL
+5

ABILITIES

POWERS

36

88

3

SKILLS

DEFENSES

TOTAL

13

10

150

•

Identity:  Some  Powerhouses  keep  their  identity  a
secret  from  the  rest  of  the  world.  Especially  those
Powerhouses  that  can  change  into  and  out  of  their
super-powered identity.

•  Motivation—Acceptance:  Those  Powerhouses  with
the  Prejudice  complication  often  choose  this  mo-
tivation  and  become  a  hero  in  order  to  earn  a  place
in  “normal”  society.  An  alien  Powerhouse  may  also
choose this motivation even if he or she doesn’t look
unusual.

•  Motivation—Patriotism:  Many  Powerhouses  are
die-hard  patriots  and  fight  to  defend  or  represent
their country.

•  Motivation—Responsibility: Due to their incredible
powers, many Powerhouses become heroes because
they feel as if they have a responsibility to do so.

•

•

•

Power  Loss:  Some  Powerhouses  lose  their  powers
in the presence of a certain substance, while others
physically transform from a normal human form and
return to it often.

Prejudice: The Powerhouse often looks unusual and
struggles with feeling isolated or like an outsider, or
even being treated like a monster!

Relationship: The Powerhouse typically has a small
group of friends he or she relies on for human con-
tact and friendship. These relationships are very im-
portant to the Powerhous

[... truncated ...]
```

**Chunk 20** (`457931504c50`):

```
CHAPTER 2: SECRET ORIGINS

27

larly, you may suffer a circumstance penalty to interaction
when dealing with characters of a strongly differing mo-
tivation.

At the GM’s option motivation can function as a descriptor
for powers (see Descriptors, page 204), allowing character
to  have  a  power  affecting  only  subjects  with  a  particular
motivation,  for  example,  or  the  ability  to  detect  charac-
ters  with  a  particular  motivation  (see  Detect,  page  177).
Gamemasters should be very careful when applying power
modifiers based on subjective qualities like motivation. An
attack  power  affecting  only “evil”  targets,  for  example,  is
useless against inanimate objects, constructs, and animals
(which cannot have such a quality) as well as “good” targets.
It  might  also  not  affect  characters  without  a  specific  evil
motivation (such as selfish mercenaries, violent vigilantes,
or despots devoted solely to order, but not “evil” per se).

Some characters may derive their powers from their mo-
tivation in some way, such as heroes who draw strength
from  their  convictions,  faith,  or  morality. This  provides  a
descriptor for those powers, but the hero may also suffer
Power  Loss  (see  page  28)  from  a  change  or  wavering  in
motivation.

A character with different motivations may find them in
conflict from time to time. Such conflicts provide roleplay-
ing opportunities and complications for players and story
hooks for the Gamemaster. For example, a hero motivated
by Patriotism may discover a secret government agency
acting against the interests of justice in the world. What
is stronger, the hero’s patriotism or the desire to see the
truth known and justice done? Some conflicts may even
result  in  heroes  changing  motivations.  See  Changing
Complications, in the following section, for more on this.

Other  possible  complications,  and  their  uses  in  adven-
tures, include:

•

•

Accident: You cause or suffer some sort of accident.
Perhaps a stray blast damages a building or hurts an
innocent bystander, your fire powers set off sprinkler
systems, or you cause volatile chemicals to explode.
A  hero  with  this  as  a  regular  complication  may  be
especially  accident-prone,  inexperienced  with  their
powers, or even jinxed! The GM decides the effects of
an  accident,  but  they  should  be  troublesome.  Acci-
dents can lead to further complications; perhaps the
hero develops a guilt-complex, obsession, or phobia
involving t

[... truncated ...]
```

**Chunk 21** (`5610c4e8f961`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

ENHANCED

STRENGTH
3
STAMINA
4
NATURAL

AGILITY
6
DEXTERITY
6

STRENGTH
3
STAMINA
3

AGILITY
7
DEXTERITY
7
SELF-MADE

FIGHTING
7
INTELLECT
1

AWARENESS
1
PRESENCE
0

FIGHTING
8
INTELLECT
0

AWARENESS
0
PRESENCE
0

STRENGTH
3
STAMINA
3

AGILITY
6
DEXTERITY
6

FIGHTING
7
INTELLECT
0

AWARENESS
2
PRESENCE
1

Defensive Roll 3 and choose two: Accurate Attack, All-out
Attack, Defensive Attack, Power Attack

Take the advantages listed above, then roll 1d20 twice (re-
roll if you get the same result twice) on the Advantages I
table and record the results. Then roll on the Advantages
II table as directed.

TACTICIAN

Assessment, Skill Mastery (Insight), Teamwork

CONDITIONING

Diehard, Great Endurance, Skill Mastery (Athletics)

FIGHTER

Benefit (Ambidexterity), Precise Attack (Choose One: Close or
Ranged; Cover), Quick Draw

Roll 1d20 once and record the result.

1-5

Fast: You often hit your opponent before he has a
chance to react.

6-10

Imposing: Opponents find you unsettling.

11-15 Quick: You are shifty and hard to hit.

16-20

Tricky: Your antics distract your opponents.

FAST

Improved Initiative, Takedown

IMPOSING

Daze (Intimidation), Startle

QUICK

Agile Feint, Evasion

TRICKY

Daze (Deception), Taunt

SKILLS

1-4

5-8

Alert: You are ready to fight at any moment.

Dead Eye: Your aim is impeccable.

9-11

Field Commander: You have led others into battle.

12-14

Master Tactician: You can spot and take advantage
of an enemy’s weakness.

15-17

Peak Conditioning: You are incredibly fit.

18-20

Reactive Fighter: You are a fast, adaptive
combatant, capable of fighting blind or adjusting for
difficult shots.

Acrobatics 4, Athletics 4, Expertise: (Choose One) 6

Take the skills listed above, then choose between Set I or
Set II below (you may wait to make this choice until after
you  know  what  weapon  your  character  uses),  then  roll
on the Background, Mental, and Physical Skills tables
as directed.

Set I: Close Combat: Weapon 6, Close Combat: Unarmed 4,

Ranged Combat: (Choose One) 4

ALERT

Evasion, Precise Attack (Choose One: Close or Ranged;
Concealment), Uncanny Dodge

EYE

Set II: Close Combat: (Choose One) 6, Ranged Combat:

Weapon 8

Improved Aim, Improved Critical (weapon), Ultimate Effort (Aim)

Roll 1d20 once and record the result.

COMMANDER

Inspire, Leadership, Skill Mastery (Persuasion)

1-5

Soldier: You trained in the military.

6-10

Time-Displaced: You 

[... truncated ...]
```

**Chunk 22** (`5e2f6b7f48fe`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

•  Motivation—Doing Good: Some Shapeshifters are

heroes because it’s the right thing to do.

•  Motivation—Recognition: Shapeshifters sometimes
become heroes in order to receive praise or fame.

•  Motivation—Thrills: Many Shapeshifters become he-
roes because they enjoy the action and adventure... and
their powers often keep them from any lasting injury.

•

Relationships:  Shapeshifters  often  have  close
friends and family around them.

SPEEDSTER

Speedsters can move great distances in little or no time.
They  do  this  either  by  running  or  flying  at  superhuman
speeds, or by instantly transporting themselves from one
place to another. Because of their great speed, Speedsters
seldom need ranged powers. Speedsters are also able to
use their movement mode to break the laws of physics in
ways even other fast superheroes are incapable of doing.

ABILITIES

Roll 1d20 once and record the result.

1-10

11-15

16-20

Veteran: You’re an experienced hero who has
come into his own.

Youth: You’re still just an impulsive kid, new to the
scene and experimenting with your powers.

Old-Timer: You’ve seen a lot more than most heroes,
but you’re not quite ready to hang up your cleats.

VETERAN

STRENGTH
2
STAMINA
2
YOUTH

AGILITY
4
DEXTERITY
3

STRENGTH
1
STAMINA
1

AGILITY
5
DEXTERITY
5
OLD-TIMER

FIGHTING
4
INTELLECT
1

AWARENESS
2
PRESENCE
2

FIGHTING
4
INTELLECT
0

AWARENESS
2
PRESENCE
2

STRENGTH
1
STAMINA
1

AGILITY
3
DEXTERITY
2

FIGHTING
5
INTELLECT
2

AWARENESS
3
PRESENCE
3

```

**Chunk 23** (`634190f2dd84`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PL10PL10

PSYCHIC
PSYCHIC

STRENGTH
0
STAMINA
0

POWERS

AGILITY
1
DEXTERITY
2

FIGHTING
2
INTELLECT
2

AWARENESS
6
PRESENCE
3

Mental Awareness: Senses 2 (Mental Sense,

Radius) • 2 points.

Telekinesis: Move Object 8, Accurate 4 • 20 points.

Telekinetic Field: Protection 12, Impervious,

Sustained • 24 points.

Telekinetic Levitation: Flight 5 (60 MPH) • 10 points.

Telepathy: Mind Reading 5 Linked to Area
Mental Communication 2 • 20 points.

•  Telepathic Illusion: Illusion 4 (all senses),

Resisted by Will, Selective • 1 point.

•  Mental Blast: Perception Range Damage 5,

Resisted by Will • 1 point.

OPTIONS

To customize, you may choose the following option
with no change in point total:

•  Mind Control: Replace the Telepathic Illusion Alternate

Effect with Affliction 5 (Resisted by Will; Dazed, Compelled,
Controlled), Cumulative, Perception Range.

Ultimate Effort (Will defense)

SKILLS

Expertise: (Choose One) 6 (+8), Insight 6 (+12),
Perception 4 (+10), Persuasion 8 (+11)

OFFENSE

Mental Blast —

Telekinesis +10

Unarmed +2

DEFENSE

DODGE

PARRY

WILL

INITIATIVE +1

Perception Range, Damage 5,
Resisted by Will (DC 20)

Ranged, Str 8 Grab

Close, Damage 0

FORTITUDE

TOUGHNESS

6

12

8

8

14

```

**Chunk 24** (`6717e2899e27`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

METAL

Beginner’s Luck, Eidetic Memory, Luck, Taunt

WATER

Assessment, Evasion, Trance, Uncanny Dodge

WOOD

Favored Environment (Choose One), Hide in Plain Sight, Precise
Attack (Close, Concealment), Teamwork

Roll 1d20 once and record the result.

1-4

Crane: You avoid direct confrontation, countering
and pinpointing weaknesses.

5-8

Dragon: Your style emphasizes versatility and balance.

9-12

13-16

Monastic: You learned your martial arts from a
temple or mystical city.

Ninja: You are skilled in the arts of stealth and
assassination.

17-20

Soldier: You were trained by the military.

AGENT

Acrobatics 4, Athletics 4, Close Combat: Unarmed 2, Insight 4,
Investigation 4, Perception 4, Stealth 6, Technology 4

MERCENARY

Acrobatics 4, Athletics 6, Close Combat: Unarmed 2, Expertise:
Streetwise 6, Insight 4, Intimidation 6, Perception 4

MONASTIC

Acrobatics 4, Athletics 4, Close Combat: Unarmed 2, Expertise:
Philosophy 6, Insight 6, Perception 6, Treatment  4

9-12

Leopard: You rely on sheer speed and eschew defense.

NINJA

13-16

Snake: You fight from unusual stances and positions
to catch your opponent off-guard.

17-20

Tiger: You strike with great strength and ferocity.

CRANE

Defensive Attack, Evasion, Grabbing Finesse, Improved
Defense, Improved Disarm, Instant Up, Move-by Action,
Redirect, Set-up

DRAGON

Accurate Attack, All-out Attack, Defensive Attack, Evasion,
Fast Grab, Grabbing Finesse, Improved Disarm, Improved Trip,
Move-by Action

LEOPARD

All-out Attack, Improved Critical (Unarmed), Improved
Initiative, Improved Trip, Move-by Action, Seize Initiative, Skill
Mastery (Acrobatics), Startle, Takedown

SNAKE

Chokehold, Defensive Attack, Fast Grab, Grabbing Finesse,
Improved Disarm, Improved Grab, Improved Hold, Prone
Fighting, Weapon Bind

TIGER

1-12

All-out Attack, Defensive Attack, Improved Critical (Unarmed),
Improved Smash, Move-by Action, Skill Mastery (Athletics),
Startle, Takedown, Weapon Break

SKILLS

If you rolled Mystic Endowment for Abilities, roll 1d20 once
and record the result. Otherwise, roll 1d20 twice (do not re-
roll if you get the same result twice) and record the results.

1-4

Agent: You work with a government or private spy
agency.

5-8

Mercenary: You contract out your fighting skills.

Acrobatics 6, Athletics 4, Close Combat: Unarmed 2,
Deception 4, Perception 4, Sleight of Hand 6, Stealth 6

SOLDIER

Acrobatics 4, Athletics 6, Cl

[... truncated ...]
```

**Chunk 25** (`685941d4ae65`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

The Elementals described here generally have traits such as Insubstantial default to Permanent. However, some elemen-
tals may be able to transform between their elemental and a flesh and blood form. Such elementals may have Sustained
powers and possibly the Activation Flaw if the transformation takes time or effort. In this case, the Activation Flaw can free
up a point that the player can spend on an additional Alternate Effect or Advantage.

Alternately, the elementals who are considered Embodiments (as rolled on the Abilities) may have Innate forms that can-
not be turned off even by nullification effects. Players may wish to take a point from another trait (such as an Alternate
Effect or Advantage) to buy the Innate Extra.

•  Earth Blast: Ranged Damage 10 • 1 point

5-10

•  Earthen Snare: Cumulative Affliction 10 (Resisted
by Dodge, Overcome by Damage; Hindered and
Vulnerable, Immobile and Defenseless), Extra
Condition, Limited to Two Degrees • 1 point

11-14

Particulate Form: Elongation 7; Insubstantial 2;

Movement 2 (Slithering, Sure-Footed); Speed 2;
Visual Concealment 4, Partial • 23 points

Sandstorm: Environment 5 (Visibility -5; 500 feet

radius) • 10 points

Plant Form: Visual Concealment 4, Limited: in

vegetation; Immunity 2 (Plant Powers); Teleport 7,
Medium (Plants) • 13 points

Plant Control: Array (20 points + four Alternate Effects)

•  Plant Toxin: Cumulative Affliction 10 (Resisted
and Overcome by Fortitude; Dazed, Stunned,
Incapacitated) 20 points

Take the Plant Control array and Plant Toxin (above)
and roll 1d20 four times (re-roll if you get the same
result) and add them to the array as Alternate Effects.

1-4

5-8

9-12

13-16

17-20

•  Animate Tree: Summon 10,

Controlled, Limited to Size and
Availability of tree • 1 point

•  Entanglement: Burst Area

Cumulative Affliction 10 (Resisted
by Dodge, Overcome by Damge;
Hindered and Vulnerable, Defenseless
and Immobile), Extra Condition,
Limited to Two Degrees, Limited:
Requires Ambient Plant-life • 1 point

•  Plant Perception: Remote Sensing 5
(All Senses), Medium (Plants) • 1 point

•  Wood Objects: Create 7, Innate,

Movable • 1 point

•  Transmit: Teleport 10, Extended,

Medium (Plants) • 1 point

Rock Form: Reaction Damage 7 (to being hit),

Limited to effect rank or Damage rank, whichever
is less; Enhanced Strength 2; Immunity 1 (Own
Powers); Impervious Protection 4 • 34 points

Plus add the fo

[... truncated ...]
```

**Chunk 26** (`6890e166bca9`):

```
CHAPTER 2: SECRET ORIGINS

29

A lot of background details go into making your hero more than just a collection of numbers. Take a moment (if you
haven’t already) to consider some of the following things about your character:

NAME

What is your character’s name? That is to say, what is the
name  the  hero  uses  in  public,  that  appears  in  one-inch
type  in  the  newspaper  headlines?  Most  heroes  adopt
unique  and  distinctive “code  names,”  so  consider  a  suit-
able name for yours. Code names are often based on pow-
ers, theme, or style. Here are some options to consider:
ORIGIN

A name may be based on the hero’s origin, power source,
nation (or even world) of birth, and such.
POWERS

Choose a name based on the hero’s powers: Firestarter or
Blaze for a flame-controlling character, Thunder or Spark
for an electrical character, and so forth.

THEME

Maybe  the  character  has  a  theme  or  style  suggesting  a
name: Paladin might be a medieval knight displaced into
the present day, with a magical sword and armor. Madame
Macabre may be all about magic and the occult.

TITLES

Names  may  include  various  titles  like  Mister,  Miss,  Ms.,
Doctor,  Sir,  Lord,  Lady,  and  Madam  or  even  royal  titles
like  King,  Queen,  Prince,  Princess,  Duke,  Baron,  Emperor
and so forth. Military ranks are also popular parts of hero
names, especially General, Major, and Captain.
GENDER

Names often include gender designations like Man/Wom-
an, Boy/Girl, Lad/Lass, and so forth.
SOUND

Some  code-names  don’t  really  have  anything  to  do  with  a
character’s powers or background—they just sound cool: Kis-
met, Scion, Animus, Damask, and so forth. They may hint at
the hero’s powers or origin, or have nothing to do with them.

REAL NAME

Some heroes go by their given name, not using a code-
name at all. Oftentimes these names still sound like code-

names,  however.  They  may  also  be  nicknames,  such  as
“Dash” for someone with the name Dashell, or “Buzz” for
someone  with  the  name  Buzcinski,  or  whatever  other
nickname a character may have, such as “Stretch” or “Tiny”.

ORIGIN

What’s  the  origin  of  your  hero’s  powers?  It  can  be  any-
thing from a character born with the potential for powers
to someone granted them by an accident—exposure to a
strange meteor, radiation, genetic engineering, or any of
countless similar encounters. Here are some of the more
common superhero origins:
ACCIDENT

Perhaps  the  most  common  origin. The  hero  

[... truncated ...]
```

**Chunk 27** (`6c8715df5e97`):

```
CHAPTER 2: SECRET ORIGINS

35

Power Point Totals:  Abilities 30 + Powers 84  + Advantages 8 + Skills  12 + Defenses 16  = 150

PL10PL10

CONSTRUCT
CONSTRUCT

STRENGTH
11
STAMINA
-

POWERS

AGILITY
3
DEXTERITY
3

FIGHTING
9
INTELLECT
5

AWARENESS
1
PRESENCE
0

Armored: Protection 11, Impervious 6 • 17 points.

Unliving: Immunity to Fortitude Effects • 30 points.

OPTIONS

Choose one of the following • 20 points.

Elemental: Ranged Damage 10 (See Elemental Control in the

Powers chapter.)

Soldier: Ranged Damage 10 (built-in weapon)

Undead Revenant: Immortality 5, Regeneration 10

Wraith: Insubstantial 4

Eidetic Memory, Ranged Attack 5

SKILLS

Investigation 2 (+7), Perception 5 (+6), Persuasion 4 (+4), Technology
5 (+10), Vehicles 2 (+5)

OFFENSE

INITIATIVE +3

Ranged +8

Unarmed +9

Ranged, Damage *

Close, Damage 11

* Damage bonus depends on the option chosen under Powers.

DEFENSE

DODGE

PARRY

WILL

9

9

9

FORTITUDE

Immune

TOUGHNESS

11

Power Point Totals:  Abilities 54 + Powers 67  + Advantages 6 + Skills  9 + Defenses 14  = 150

36

```

**Chunk 28** (`6d18f5cb0ab3`):

```
CHAPTER 2: SECRET ORIGINS

25

Archetypes), a hero with more sheer power than skill (like
the Powerhouse), or a hero who is a roughly equal mix of
both (like the Warrior) who are all within the series limit,
PL10. The same is true of the various other traits, such as
placing a greater reliance of Dodge and Parry over Tough-
ness, or vice versa.

The  GM  may  want  to  keep  an  eye  on  combinations  that
swing wildly towards one side or another: the hero with no
Dodge/Parrry bonus to speak of but a massive Toughness
bonus,  or  the  one  with  no  real  attack  bonus  but  capable
of  dishing  out  a  tremendous  amount  of  damage.  For  the
most part, these designs are self-limiting, but they can pose
problems in comparison to better-balanced heroes. A dis-
parity of more than 50% between a pair of power level lim-
ited traits is something to look at closely before approving.

CHARACTERS

While the GM should keep the power level guidelines and
suggested  starting  power  points  of  the  series  in  mind
while  creating  villains  and  members  of  the  supporting
cast, non-player characters are not restricted by the series
power level and are built on as many power points as the
GM wants to give them. In other words, there is no need
to add up the “cost” of a non-player character. Just assign
the appropriate traits at the desired ranks.

Determine  an  NPC’s  effective  power  level  based  on  the
character’s  highest  appropriate  offensive  and  defensive

trait(s).  This  power  level  is  simply  an  approximation  to
show what level of challenge that NPC offers, and is not
necessarily related to the NPC’s power point total, which
may be greater than or less than the recommended start-
ing power points for that power level.

Example: The Gamemaster is creating a villain for
a power level 10 series. The bad guy has a +8 total
attack bonus with a primary attack doing 16 dam-
age. Adding these together and dividing by 2 gives
the GM a power level of 12 [(16 + 8)/2]. So long as
none of the villain’s other traits exceed this, the GM
notes the villain’s power level as 12, a reasonable
challenge for a group of PL10 heroes.

Normally a hero’s traits are fixed. Once power points are
spent  on  them,  they  remain  there.  In  some  cases,  how-
ever,  the  Gamemaster  may  allow  players  to  re-allocate
their  characters’  points,  changing  their  traits  within  the
limits of the series power level, perhaps even losing some
traits and gaining entirely 

[... truncated ...]
```

**Chunk 29** (`6e090a5bf703`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

HOTHEADED

STRENGTH
1
STAMINA
2

AGILITY
4
DEXTERITY
3

FIGHTING
3
INTELLECT
0

AWARENESS
2
PRESENCE
2

RESERVED

STRENGTH
0
STAMINA
2

AGILITY
4
DEXTERITY
3

FIGHTING
3
INTELLECT
2

AWARENESS
3
PRESENCE
0

Roll  1d20  twice  (re-roll  if  you  get  the  same  result  twice)
and record the results.

1-4

Aggressive: You like to take the offensive.

5-7

8-11

12-13

14-16

17-20

Disciplined: You were trained to fight smartly and
as part of a team.

Intimidating: You use your powers in a loud and
impressive fashion.

Hidden Reserves: When you need to, you can push
yourself and your powers to amazing levels.

Precise: You are careful and exact in using your
powers.

Wisecracker: Your powers give you great
confidence, and you let everyone know it.

AGGRESSIVE

All-out Attack, Power Attack

DISCIPLINED

Assessment, Teamwork

INTIMIDATING

Daze (Intimidation), Startle

RESERVES

Extraordinary Effort, Great Endurance

PRECISE

Accurate Attack, Precise Attack (Ranged, Cover)

WISECRACKER

Fearless, Taunt

```

**Chunk 30** (`73f84062d601`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Some heroes gain powers from a deliberate effort, such as
a scientific or mystical technique for transforming someone
into  a  super-being.  Like  accidents,  experiments  are  often
impossible to duplicate. The hero may be a willing volun-
teer or a victim chosen to test out the technique. Some he-
roes create their own powers, either developing the power-
granting procedure or building their own devices.
MUTANT

A  hero  may  simply  be  born “different,”  with  the  genetic
potential for super-powers. These latent powers typically
emerge in a time of stress, especially the changes brought
on by puberty, although they might also appear as a re-
sult of an accident (combining the accident and mutant
origins).
TRAINING

Finally,  some  heroes  acquire  powers  through  hard  work
and training, whether physical discipline, studying esoter-
ic  martial  arts  techniques,  meditation  and  introspection
to unlock hidden mental powers, or mastering the arts of
magic.  Such  training  is  typically  arduous  and  not  every-
one has what it takes to accomplish it. Heroes who gained
their powers through training may have rivals or foes who
trained with them (see the Enemy and Rivalry complica-
tions later in this chapter).

Origins  can  serve  as  descriptors  for  a  character’s  powers
(see  Descriptors  in  the  Powers  chapter).  For  example,  a
super-powered mutant has the “mutant” descriptor, mean-
ing  the  character  may  be  detected  by  mutant-detection
powers, affected by mutant-specific devices, and so forth.
The same is true for a mystic, an alien, or any other origin.

Your  GM  may  decide  to  limit  the  origins  for  the  series
you’re  playing  for  story  reasons.  The  Gamemaster  may
set  specific  guidelines,  ranging  from  restricting  certain
types of origins (no aliens or no mystics, for example) to
requiring all heroes share a common type of origin, such
as everyone is a mutant or the result of a unique accident.
Consult with your GM before you choose a particular ori-
gin for your hero.

AGE

How  old  is  the  character?  Superheroes  tend  to  hover  in
that  indeterminate  age  between  20  and  40,  but  some
heroes are younger, often teenagers, and some are older,
possibly much older, depending on a hero’s background.
For example, the hero might have fought in World War II
but ended up in the present day due to time travel or sus-
pended animation

[... truncated ...]
```

**Chunk 31** (`75c6a0d7757a`):

```
CHAPTER 2: SECRET ORIGINS

75

MYSTIC

The  Mystic  commands  vast  magical  powers  and  uses
them  to  defend  the  Earth  from  otherworldly  threats  as
well  as  to  combat  the  evils  found  just  down  the  street.
The  Mystic  typically  has  extensive  knowledge  of  magic
and other realms, but few real-world skills to speak of. The
magical powers the Mystic commands are nearly limitless,
allowing  the  Mystic  to  fire  blasts  of  magical  energy,  fly,
create  illusions,  heal  others,  travel  to  other  dimensions,
and reproduce virtually any other power imaginable.
ABILITIES

Roll 1d20 once and record the result.

1-6

Host: You’re the host of a mystical being which gives
you access to supernatural powers.

7-13

Magical Heritage: Your family has a long history of
being blessed with magical powers... or perhaps it’s
cursed.

14-20

Mystic Master: You’ve trained long and hard to
master the mystic arts.

HOST

STRENGTH
1
STAMINA
0

AGILITY
1
DEXTERITY
3

FIGHTING
4
INTELLECT
2

AWARENESS
5
PRESENCE
5

HERITAGE

STRENGTH
0
STAMINA
0

AGILITY
1
DEXTERITY
3

FIGHTING
4
INTELLECT
2

AWARENESS
7
PRESENCE
4

MASTER

AGILITY
1
DEXTERITY
3

STRENGTH
0
STAMINA
0

FIGHTING
4
INTELLECT
3

AWARENESS
6
PRESENCE
4

Equipment 3 (Headquarters), Ranged Attack 5, Trance

Headquarters—Size: Medium, Toughness: 10; Features:
Concealed, Dual-size (Huge), Laboratory, Library, Living Space,
Personnel, Sealed, Security System, Self-repairing, Workshop
• 15 points

Take the advantages listed above, then roll 1d20 once and
record the result.

1-5

Centered: You’ve trained yourself to remain calm
and centered, no matter what.

6-10

Enchanter: You can create magical artifacts.

76

```

**Chunk 32** (`75f616f43b9d`):

```
CHAPTER 2: SECRET ORIGINS

97

6-10

11-15

Jinx: Selective Burst Area Luck Control
2 (negate hero or luck point, force
re-roll), Luck 5 • 15 points

Lucky Cat: Selective Burst Area Luck

Control 2 (grant re-roll, bestow luck
point), Luck 5 • 15 points

16-20

Nine Lives: Immortality 15, Limited:
only works eight times • 15 points

Thick Hide: Protection 4, Impervious 11 • 15 points

Roll 1d20 once and record the result.

ELEPHANT

Groundstrike (Alternate Effect of Strength Damage):

Burst Area Affliction 10 (Resisted by Dodge,
Overcome by Fortitude; Hindered and Vulnerable,
Stunned and Prone), Extra Condition, Limited to Two
Degrees, Limited to targets on the ground • 1 point

1-10

Immovable: Immunity 10 (being moved), Sustained

• 10 points

Power-Lifting: Enhanced Strength 4, Limited to

Lifting • 4 points

Trunk: Extra Limb 1, Elongation 1 • 2 points

Tusks: Strength-based Damage 2, Improved Critical 2

• 4 points

RHINO

Armored Plates: Immunity 4 (critical hits, self-

inflicted slam damage) • 4 points

11-20

Great Horn: Strength-based Damage 3, Improved

Critical 2 • 5 points

Unstoppable Charge: Penetrating 15 on Damage,

Limited to slam attacks; Speed 4 (30 MPH) • 12 points

Reptilian Movement: Movement 1 (Slithering) • 2 points

Heat Sensing Pits: Senses 1 (Infravision) • 1 points

Scaly Hide: Protection 2 • 2 points

Roll 1d20 once and record the result.

CROCODILE

Aquatic: Movement 1 (Environmental Adaptation—

Aquatic), Swimming 6 (30 MPH) • 8 points

1-6

Brute Strength: Enhanced Strength 2 • 4 points

Regrowth: Regeneration 2 • 2 points

Rending Bite: Strength-based Damage 2, Improved

Critical, Secondary Effect • 17 points

LIZARD

Paralyzing Spit: Affliction 10 (Resisted by Dodge,

Overcome by Fortitude; Dazed, Stunned,
Paralyzed), Accurate 2, Reach 3 • 15 points

Prehensile Tail: Elongation 1, Extra Limb 1 • 2 points

Regrowth: Regeneration 1, Persistent • 2 points

Speedy: Leaping 2 (30 feet); Movement 2 (Wall-

crawling 2); Speed 3 (16 MPH) • 9 points

Teeth and Claws: Strength-based Damage 2,

Accurate • 3 points

7-13

98

SNAKE

Tensile Strength: Elongation 4 (120 feet); Enhanced

14-20

Strength 4, Limited to Grabs • 8 points

Venomous Bite: Progressive Weaken Stamina 7
(Resisted by Fortitude), Accurate 2 • 23 points

DEFENSE

DODGE
+6

PARRY
+4

FORTITUDE
+4

TOUGHNESS
+0

WILL
+6

ABILITIES

POWERS

68

36

6

SKILLS

DEFENSES

TOTAL

20

20

150

•  Motivation—Acceptance: The Totem can be regard-
ed as a pariah or outcast in h

[... truncated ...]
```

**Chunk 33** (`7f0cf6f57819`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

GOALS

How would you describe your hero’s personality? While
heroes  tend  to  share  a  desire  to  use  their  powers  for
good and uphold the law, they also show a diverse range
of attitudes. One hero may be dedicated to the ideals of
truth,  justice,  and  equality  while  another  is  a  vigilante
willing to break the law in order to ensure justice is done.
Some heroes are forthright and cheerful while others are
grim and unrelenting. Consider your hero’s attitudes and
personality traits. Don’t overlook the effect of Motivation
on  your  hero’s  personality  and  vice  versa  (see  Motiva-
tion, previously).

Finally, what are your hero’s goals? All heroes want things
like peace and justice to one degree or another, but what
other  things  does  your  hero  want?  One  hero  may  want
to  find  his  long-lost  family  while  another  may  want  to
avenge a terrible wrong done to her in the past. A mon-
strous or alien hero may seek acceptance and a new home
on Earth, while a teen hero may want to live up to the leg-
acy of a mentor or predecessor. Giving your hero a goal
beyond simply “doing good” can help give the character
more  depth  and  provide  opportunities  for  roleplaying
and complications during the game. Don’t overlook it.

The Gamemaster awards heroes power points at the end of each MUTANTS & MASTERMINDS story. This represents the experi-
ence and confidence the heroes have gained, along with other factors contributing to an improvement in their abilities,
skills, and powers.

Generally, heroes each receive 1 power point for a successfully completed adventure that lasts for one game session.
If the heroes overcame especially powerful foes or difficult challenges, the GM can increase the power point award to
2 points. For adventures lasting more than one game session, the heroes should get 1 power point per session, plus a
possible power point at the end if they did particularly well.

Gamemasters may vary the rate of advancement by awarding more power points per adventure, allowing heroes to
increase in power faster, which may suit certain styles of play. The Gamemaster also may choose not to award a power
point for an adventure in which the heroes did especially poorly, such as failing to defeat a villain’s major scheme or al-
lowing many innocent people to suffer harm they could have prevented.

Players can spend their heroes’ awarded power points in-betwee

[... truncated ...]
```

**Chunk 34** (`803cb2a8c272`):

```
CHAPTER 2: SECRET ORIGINS

37

Power Point Totals:  Abilities 84 + Powers 0  + Advantages 12 + Skills  39 + Defenses 15  = 150

PL10PL10

STRENGTH
1
STAMINA
2

POWERS

AGILITY
4
DEXTERITY
3

FIGHTING
4
INTELLECT
0

AWARENESS
2
PRESENCE
2

Energy Aura: Damage 3, Reaction • 12 points.

Energy Control: Ranged Damage 12 • 24 points.

•  Choose three Alternate Effects • 3 points.

Energy Immunity: Immunity 5 (Energy Control type) • 5 points.

Flight: Flight 7 (250 MPH) • 14 points.

Force Field: Protection 10, Impervious, Sustained • 20 points.

Quick Change: Feature 1 (transform into costume as a free action)

• 1 point.

OPTIONS

The main option for an Energy Controller is the type of energy the
hero wields. See Energy Control in the Powers chapter for
some examples.

Accurate Attack, All-out Attack, Power Attack, Precise
Attack (Ranged; Cover), Taunt

SKILLS

Acrobatics 6 (+10), Deception 7 (+9), Insight 4 (+6),
Perception 4 (+6), Persuasion 4 (+6), Ranged Combat:
Energy Control 5 (+8)

OFFENSE

INITIATIVE +4

Energy Control +8

Ranged, Damage 12 plus others

Unarmed +4

Close, Damage 1

DEFENSE

DODGE

PARRY

WILL

FORTITUDE

TOUGHNESS

7

12

8

4

8

Power Point Totals:  Abilities 36 + Powers 79  + Advantages 5 + Skills  15 + Defenses 15  = 150

38

```

**Chunk 35** (`818544ba2429`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

do in the hope of gaining acceptance for him- or her-
self as well as other psychics.

•  Motivation—Responsibility:  Some  Psychics  use
their powers for good, because they feel they must
have been given their powers to help others.

•

•

Power  Loss:  Because  mental  powers  often  require
some  amount  of  focus;  drugs,  disorientation  of  any
kind, or noisy settings may prevent a Psychic from us-
ing his or her powers.

Quirk—Impressionable:  Psychic’s  with  telepathy
may  pick  up  personality  traits  and  attitudes  from
people they’ve interacted with using their powers.

Shapeshifters include characters who actually change their
shape to become animals, machines, mythic creatures, or hu-
manoid monsters, as well as characters who can change their
density, grow, shrink (or both!), or stretch to fantastic lengths.

ABILITIES

Roll 1d20 once and record the result.

1-10

Everyman: You’re an ordinary, everyday Joe. Or
you’re an alien being or construct made to look and
behave just like you’re an ordinary, everyday Joe.

11-20 Whiz: You’re an inventor, scientist, or incredibly smart.
EVERYMAN

STRENGTH
2
STAMINA
2

AGILITY
2
DEXTERITY
2

FIGHTING
2
INTELLECT
2

AWARENESS
2
PRESENCE
2

WHIZ

STRENGTH
2
STAMINA
2

AGILITY
2
DEXTERITY
0

FIGHTING
2
INTELLECT
7

AWARENESS
1
PRESENCE
0

Defensive Roll 3, Move-by Action

9-12

13-16

Smart Alec: You never stop talking. Sometimes
people want to hit you.

Spontaneous: You have poor impulse control,
which is actually a blessing in combat.

17-20 Wealthy: You inherited or have money of your own

somehow.

SPEED

Evasion, Improved Initiative

INVENTOR

Inventor, Skill Mastery (Choose One)

ALEC

Daze (Deception), Taunt

SPONTANEOUS

Improved Initiative, Uncanny Dodge

WEALTHY

Benefit 2 (Independently Wealthy)

SKILLS

Close Combat: Unarmed 8

Take the skill listed above, then roll 1d20 twice and record
the result (do not re-roll if you get the same result).

1-4

5-8

Adventurer: You like action and adventure and you
have the skills to keep you alive while pursuing them.

Explorer: You’re well traveled and know how to
blaze your own trails.

9-12

Infiltrator: You’re a trained deceiver and infiltrator.

13-16

Investigator: You’re a talented detective.

17-20

Researcher: You’ve been educated in technology
and a field of interest.

ADVENTURER

Athletics 4, Expertise: (Choose One) 4, Perception 4

EXPLORER

Athletics 4, Perception

[... truncated ...]
```

**Chunk 36** (`8558df91a0a1`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PL10PL10

GADGETEER
GADGETEER

STRENGTH
0
STAMINA
0

POWERS

AGILITY
2
DEXTERITY
3

FIGHTING
4
INTELLECT
10

AWARENESS
5
PRESENCE
0

Blaster: 24-point Array, Easily Removable (-10 points).

•  Ranged Damage 12 • 24 points

•  Dazzle 12 • 1 point.

Force Shield Belt: Protection 10,
Impervious, Sustained, Precise,
Removable (-4 points)
• 21 points.

Jetpack: Flight 5 (60 MPH),
Removable (-2 points)
 • 10 points.

Quick-Thinking: Quickness 4,

Limited to Mental Tasks • 2 points.

Beginner’s Luck, Defensive Roll 2, Eidetic Memory, Improved
Initiative, Improvised Tools, Inspire 2, Inventor, Luck, Ranged Attack
5, Skill Mastery (Technology)

SKILLS

Expertise: Engineering 5 (+15), Expertise: Science 10 (+20), Insight
5  (+10),  Investigation  4  (+14),  Perception  5  (+10),  Technology  10
(+20), Vehicles 5 (+8)

OFFENSE

INITIATIVE +6

Blaster +8

Unarmed +4

Ranged, Damage 12 or Dazzle 12

Close, Damage 0

DEFENSE

DODGE

PARRY

WILL

8

8

10

FORTITUDE

7

TOUGHNESS

12/10*

*Without Defensive Roll

```

**Chunk 37** (`85cc7f979174`):

```
CHAPTER 2: SECRET ORIGINS

65

Water Control: Array (20 points + four Alternate

Effects)

•  Water Blast: Ranged Damage 10 • 20 points

Take the Water Control array and Water Blast
(above) and roll 1d20 four times (re-roll if you get the
same result) and add them to the array as Alternate
Effects.

1-4

•  Dehydrate: Cumulative Affliction
10 (Resisted by and Overcome by
Fortitude; Fatigued, Exhausted,
Incapacitated) • 1 point

1-10

5-8

9-12

13-16

17-20

•  Drown: Progressive Affliction
6 (Resisted and Overcome by
Fortitude; Dazed, Stunned,
Incapacitated) • 1 point

•  Hard Water Objects: Create 10

• 1 point

•  Move Water: Perception Ranged
Move Object 10, Limited to Water
• 1 point

•  Watery Snare: Ranged Affliction 10
(Resisted by Dodge, Overcome by
Strength; Hindered and Vulnerable,
Immobile and Defenseless), Extra
Condition, Limited to Two Degrees
• 1 point

11-15

Ice Form: Enhanced Strength 8; Immunity 7 (cold
damage, ice effects); Impervious Protection 8;
Senses 2 (Tracking, Infravision) • 45 points

Ice Slide: Flight 5 (60 MPH), Platform • 5 points

Ice Control: Array (20 points + four Alternate Effects)

•  Ice Blast: Ranged Damage 10 • 20 points

Take the Ice Control array and Ice Blast (above) and
roll 1d20 four times (re-roll if you get the same result)
and add them to the array as Alternate Effects.

1-4

5-8

9-12

13-16

•  Cold Blast: Ranged Affliction 10
(Resisted by and Overcome by
Fortitude; Fatigued, Exhausted,
Incapacitated) • 1 point

•  Cold Field: Environment 10 (Extreme

Cold) • 1 point

•  Ice Shapes: Create 6, Continuous,

Innate • 1 point

•  Icy Snare: Cumulative Affliction 10
(Resisted by Dodge, Overcome by
Damage; Hindered and Vulnerable,
Immobile and Defenseless), Extra
Condition, Limited to Two Degrees
• 1 point

17-20

•  Icy Surfaces: Environment 10
(Impede Movement) • 1 point

ABILITIES

POWERS

28

86

3

SKILLS

DEFENSES

TOTAL

14

19

150

•  Motivation—Acceptance: A transformed elemental
may lament his lost humanity and be isolated as a re-
sult of his new, inhuman form.

•

•

Accident:  Many  Elementals  have  difficulty  interact-
ing with others due to their nature. Fire Elementals, in
particular, are apt to inadvertently cause destruction
in their wake, but even Water Elementals may cause
property damage by just their presence.

Enemy: Elementals may have a rivalry or feel enmity
towards their diametric opposite (fire to water, earth
to air) and towards beings associated with their op-
posing element.

•

[... truncated ...]
```

**Chunk 38** (`872471930ea9`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

HUMAN

STRENGTH
5
STAMINA
6

AGILITY
6
DEXTERITY
6

FIGHTING
10
INTELLECT
1

AWARENESS
4
PRESENCE
1

OTHERWORLDLY

STRENGTH
7
STAMINA
8

AGILITY
6
DEXTERITY
4

FIGHTING
8
INTELLECT
1

AWARENESS
2
PRESENCE
3

Agile Feint, Power Attack, Takedown

Take the advantages listed above, then roll 1d20 once on
both  the  Background  Advantages  table  and  the  Com-
bat Advantages table and record the results.

1-5

Field General: You know how to lead in battle.

6-10

Hunter: You honed your talents hunting the most
dangerous game or bounties.

11-15

Mysterious Past: Your memories are lost or
implanted but you demonstrate competence in
unexpected areas.

16-20

Survivor: You are always the last one standing.

ADVANTAGES—FIELD GENERAL

Inspire, Leadership, Teamwork

ADVANTAGES—HUNTER

Skill Mastery (Perception), Tracking, and Choose One: Favored
Environment or Favored Foe

ADVANTAGES—AGILE

Evasion, Grabbing Finesse, Improved Defense

ADVANTAGES—DARING

All-out Attack, Fearless, Improved Critical (Choose One Attack)

ADVANTAGES—GRAPPLER

Chokehold, Improved Grab, Improved Hold

ADVANTAGES—SKILLFUL

Accurate Attack, Defensive Attack, Precise Attack (Close;
Concealment)

SKILLS

Acrobatics 6, Athletics 6, Insight 4, Perception 6

Take the skills listed above, then roll 1d20 once and record
the result.

1-4

Advanced: You come from a society more highly
developed than our own.

5-8

Charismatic: You have a way with people.

9-12

Cultured: You are well learned and articulate.

13-16 Military: You are experienced in the ways of war.

17-20 Mystical: You are familiar with myth and magic.

ADVANCED

Technology 6, Vehicles 6

CHARISMATIC

Insight 6, Persuasion 6

CULTURED

Expertise: History 6, Persuasion 6

MILITARY

Expertise: Tactics 6, Intimidation 6

ADVANTAGES—MYSTERIOUS PAST

MYSTICAL

Beginner’s Luck, Benefit (Cipher), Language (Choose One)

Expertise: (Choose One: Magic or Mythology) 6, Insight 6

SURVIVOR

POWERS

Diehard, Great Endurance, Ultimate Effort (Toughness checks)

HUMAN

Roll 1d20 once and record the result.

1-5

Agile: You seldom suffer a solid hit.

6-10

Daring: You fight with a devil-may-care attitude.

11-15

Grappler: You like to keep your opponents right in
front of you.

16-20

Skillful: You fight with flair and precision.

1-4

Animalistic: Comprehend Animals 2; Enhanced

Stamina 2; Enhanced Skill 2 (Perception 4); Senses
6 (Acute and Tracking Smell, Danger Sense,

[... truncated ...]
```

**Chunk 39** (`8757660124bd`):

```
CHAPTER 2: SECRET ORIGINS

83

4-5

6-12

13-14

15-16

17-19

11-15

Induce Blindness: Perception Range

Cumulative Affliction 8 (Resisted and
Overcome by Will; Visually Impaired,
Visually Disabled, Visually Unaware),
Limited to one sense • 24 points

Mental Blast: Perception Range Damage

1-5

6, Resisted by Will • 24 points

Mental Illusions: Illusion 6 (All Senses),
Feedback, Resistible by Will, Selective
• 24 points

Mental Paralysis: Perception Range

Cumulative Affliction 6 (Resisted and
Overcome by Will; Dazed, Stunned,
Paralyzed) • 24 points

Mind Control: Perception Range

Cumulative Affliction 6 (Resisted and
Overcome by Will; Dazed, Compelled,
Controlled) • 24 points

20

Weaken Resolve: Perception Range

Weaken Will 8 • 24 points

Telekinetic: Take Telekinesis, listed immediately

below, then roll on the Telekinetic Table.

Telekinesis: Move Object 10, Accurate 4 • 24 points

Telekinetic Table: Roll 1d20 once and record the result
as the first power in an array, then roll 1d20 three times
and add each result as a 1-point Alternate Effect (re-roll
if you get the same result as your first roll).

1-3

4-7

8-12

Telekinetic Column: Line Area 2 (60

feet) Damage 8 • 24 points

Telekinetic Constructs: Create 8,

Movable • 24 points

Telekinetic Bolt: Ranged Damage 10,

Accurate 4 • 24 points

16-20

13-14

Telekinetic Grab: Ranged Concentration

Affliction 10 (Resisted by Dodge,
Overcome by Damage; Hindered and
Vulnerable, Defenseless and Immobile),
Accurate 4, Extra Condition, Instant
Recovery, Limited Degree • 24 points

Roll 1d20 once and record the result.

Armored Costume and Combat Training: Protection 4,
Subtle, Removable (-1 point); Enhanced Advantages 8
(Defensive Attack, Defensive Roll 2, Evasion, Improved
Defense, Improved Initiative, Instant Up, Takedown);
Enhanced Defenses 8 (Dodge 4, Parry 4) • 20 points

Precognitive Reactions: Enhanced Advantages 8
(Defensive Roll 4, Evasion 2, Improved Defense,
Improved Initiative); Enhanced Defenses 12 (Dodge
6, Parry 6) • 20 points

Psychokinetic Shield: Protection 10, Impervious 5,

Sustained, Linked to Immunity 10 (Mental effects),
Limited to Half Effect • 20 points

Telekinetic Shield: Impervious Protection 10,

Sustained • 20 points

6-10

11-15

16-20

Roll 1d20 once and record the result.

1-2

Levitation: Flight 2 (8 MPH), Subtle • 5 points

3-6

7-8

Mental Awareness: Senses (Mental Awareness,

Acute, Detect, Radius, Range) • 5 points

Telekinetic Flight: Flight 5 (60 MPH), Distracting •

[... truncated ...]
```

**Chunk 40** (`8ad0833a1563`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

WEREWOLF

STRENGTH
7
STAMINA
6

AGILITY
4
DEXTERITY
1

FIGHTING
9
INTELLECT
0

AWARENESS
3
PRESENCE
1

Roll 1d20 once and record the result.

REFINED

Expertise (Choose One) 4, Insight 4, Perception 6, Persuasion 10

TEEN

Deception 8, Expertise: Popular Culture 4, Expertise:
Streetwise 4, Perception 4, Technology 4

TEMPTER

Deception 12, Insight 6, Perception 6

POWERS

Aristocrat: You used your powers to gain wealth
and social status.

1-5

6-10

Heartthrob: People are attracted to your dark and
handsome looks.

11-15

Savage: You delight in your strength and power.

16-20

Wilder: You are comfortable in the wild and possibly
more bestial or feral than others of your kind.

ARISTOCRAT

Benefit 2 (Wealthy), Equipment 2 (Lair Headquarters)

Lair Headquarters—Size: Large, Toughness: 10; Features:
Concealed or Secret, Defense Systems or Deathtraps, Laboratory
or Workshop, Library, Living Space, Security System • 10 points

HEARTTHROB

Attractive, Daze (Deception), Fascinate (Choose One:
Deception or Persuasion), Inspire

SAVAGE

Agile Feint, Evasion, Great Endurance, Power Attack

WILDER

Animal Empathy, Great Endurance, Favored Environment
(Choose One), Track

SKILLS

Roll 1d20 once and record the result.

1-4

5-8

9-12

Bestial: You are feral and powerful.

Mysterious: You are enigmatic and secretive.

Refined: You are experienced with the finer things
in… life.

13-16

Teen: You are young and exploring your newfound
powers.

17-20

Tempter: You are cunning and deceitful.

BESTIAL

Athletics 6, Intimidation 12, Perception 6

MYSTERIOUS

Deception 8, Perception 8, Stealth 8

Roll 1d20 once and record the result, then roll on the De-
mon, Vampire, or Werewolf table below depending on
which set of Abilities you rolled.

1-6

Brutish Strength: Enhanced Strength 4 • 8 points

7-12

13-20

Devilish Speed: Enhanced Advantages 6 (Close
Attack 4, Improved Initiative 2); Quickness 2
• 8 points

Supernatural Might: Enhanced Strength 2; Power-
lifting 2; Enhanced Advantages 2 (Close Attack 2)
• 8 points

DEMON

Demonic Physiology: Protection 3 • 3 points

Hellfire Control: Array (20 points plus 1 Alternate Effect) • 21

points total

Roll 1d20 once and record the result as the first power in
the Hellfire Control array, then roll again (re-roll if you get
the same result on the second roll) and add the result to
the Hellfire Control array as a 1-point Alternate Effect.

1-3

4-6

7-11

12

[... truncated ...]
```

**Chunk 41** (`8d5f5f31a27f`):

```
CHAPTER 2: SECRET ORIGINS

45

Power Point Totals:  Abilities 32 + Powers 78  + Advantages 1 + Skills  12 + Defenses 26  = 150

PL10PL10

STRENGTH
1
STAMINA
2

POWERS

AGILITY
2
DEXTERITY
2

FIGHTING
6
INTELLECT
1

AWARENESS
2
PRESENCE
3

Shapeshift:  Variable  9  (45  points)  for  assuming  different  shapes,
Move Action • 72 points

Defensive Roll 3, Move-by Action, Taunt

SKILLS

Close  Combat:  Unarmed  4  (+10),  Deception  6  (+9),  Expertise:
Zoology 4 (+5), Perception 6 (+8), Stealth 6 (+8)

OFFENSE

1 Varies based on shape.

INITIATIVE +21

Unarmed +101

Close, Damage 11

DEFENSE

DODGE

PARRY

WILL

FORTITUDE

TOUGHNESS

81

81

101

81

5/2*1

*Without Defensive Roll

Power Point Totals:  Abilities 38 + Powers 72  + Advantages 5 + Skills  13 + Defenses 22  = 150

46

```

**Chunk 42** (`919d7063d0ae`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Hero: ____________________________________     Player: ____________________________

Princess

Julia

Identity: _______________________________________________  (cid:80)(cid:3)Secret (cid:80)(cid:3)Public

Jessica Prentiss     X
135 lbs  Green

Female  19

Gender: _____________     Age: ________    Height: ____________     Weight: _____________     Eyes: ___________________     Hair: _____________________
10
Group Affiliation: ________________________________     Base of Operations: ______________________________________     Power Level: ________
150
Power Point Totals: Abilities _________+ Powers _________+ Advantages _________+ Skills _________+ Defenses _________= ___________

Emerald City
13
11

Blonde

None

5’6”

27

88

11

Strength

Stamina

12
12

Agility

Dexterity

5
3

Fighting

Intellect

6
2

Awareness

Presence

2
2

Offense

Unarmed

+8  Close, Damage 12

Thrown Object  +6  Ranged, Damage 12

Initiative

+9

Defense

Dodge (agl)

Parry (FGT)

Fortitude (STA)

Toughness (STA)

Will (awe)

8
8
12
12
8

Advantages

All-out Attack,
Attractive, Diehard,
Extraordinary Effort, Improved
Initiative, Inspire 2, Interpose, Power
Attack, Ultimate Effort (Toughness
checks), Well-informed

Acrobatics 4 (+9), Athletics
4 (+16), Close Combat:
Unarmed 2 (+8), Intimidation 4 (+6),
Perception 6 (+8), Ranged Combat:
Throwing 3 (+6), Stealth 3 (+8)

Skills

Toughness 8; Regeneration 2 • 15 points

Powers & Devices
____________________________________________________________________________________________________________________________________________
Fast: Speed 4 (30 MPH) • 4 points
____________________________________________________________________________________________________________________________________________
Leaping: Leaping 7 • 7 points
____________________________________________________________________________________________________________________________________________
Resilient: Immunity 5 (Cold, Disease, Heat, Pressure, Radiation); Impervious
____________________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________________
Unrecognizable: Feature 1 (No one can tell Jessica and Princess are the same
________________________________________________________________

[... truncated ...]
```

**Chunk 43** (`93337a63364b`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

HOOD: COMPLICATIONS AND UP-FRONT REWARDS

Some roleplaying game systems include complications, disadvantages, or similar problematic character traits which offer
“bonus points” for creating the character; essentially, you get more points for your character’s good traits when you take
on some bad ones.

The problem with such “up-front” rewards for giving a character flaws is that the player gets all of the reward (the bo-
nus design points) immediately, but the disadvantage only occasionally limits or affects the character, sometimes even
randomly. Since there is only so much “screen time” in a game session, there is virtually no way for the GM to spotlight
every one of every character’s disadvantages, so some end up being worth “more” in the sense of reward in exchange for
drawbacks. Plus, after they have “paid out” their initial benefit, front-loaded negative traits are nothing but a burden to the
character from that point forward, leading players to try and avoid or mitigate them as much as possible.

Complications address this issue by having a “pay-as-you-go” approach: if the GM uses a complication in the game, and
the player responds by going along with it, the player gets a reward in the form of a hero point. This means that although
the hero has to deal with some “bad stuff” from time to time, there is an upside, and a reason for players to want their
characters’ complications to come into play! Why do powerful heroes lead such complicated lived? They need the points!

•

•

•

•

•

•

•

When  this  happens,  and  poses  a  challenge  for  you,
your complication comes into play.

Prejudice: You are part of a minority group subject
to  the  prejudices  of  others,  which  create  problems.
Similarly, characters with unusual origins or appear-
ance might face prejudice, such as a demonic-look-
ing hero who is considered suspect. Some Gamemas-
ters and gaming groups may prefer not to deal with
issues of prejudice in their games, in which case the
GM is free to ban this complication.

Quirk:  Complications  can  often  come  from  various
personality  quirks:  likes,  dislikes,  hobbies,  neuroses,
and  so  forth.  For  example,  a  hero  might  have  the
quirk of always leaving some sort of “calling card” for
the authorities along with a captured criminal. That
could become a complication if somebody else starts
imitating it, or uses it to cause trouble for the hero.

Rel

[... truncated ...]
```

**Chunk 44** (`9575430bef02`):

```
CHAPTER 2: SECRET ORIGINS

43

Power Point Totals:  Abilities 36 + Powers 84  + Advantages 1 + Skills  17 + Defenses 12  = 150

PL10PL10

STRENGTH
12
STAMINA
14

POWERS

AGILITY
1
DEXTERITY
1

FIGHTING
6
INTELLECT
0

AWARENESS
1
PRESENCE
1

Shockwave: Burst Area Damage 10, Limited: Both the

Powerhouse and its targets must be in contact with the ground
• 10 points

•  Groundstrike: Burst Area Affliction 10 (Resisted by Fortitude;
Vulnerable, Defenseless), Instant Recovery, Limited Degree,
Limited: Both the Powerhouse and its targets must be in
contact with the ground • 1 point

Leaping: Leaping 10 • 10 points

Super-Stamina: Enhanced Stamina 10, Immunity 12

(Cold and Heat Damage, Fatigue, Pressure), Impervious
Toughness 12 • 44 points

Super-Strength: Enhanced
Strength 8, plus Enhanced
Strength 4, Limited to
Lifting (Lifting Str16;
1,600 tons) • 20 points

All-out Attack, Power Attack,
 Ultimate Effort (Toughness
checks)

SKILLS

Close  Combat:  Unarmed  2  (+8),  Expertise:  Choose  One  6  (+6),
Insight  5  (+6),  Intimidation  7  (+8),  Perception  5  (+6),  Ranged
Combat: Throwing 7 (+8)

OFFENSE

INITIATIVE +1

Throw +8

Unarmed +8

Ranged, Damage 12

Close, Damage 12

DEFENSE

DODGE

PARRY

WILL

FORTITUDE

TOUGHNESS

14

14

6

6

6

Power Point Totals:  Abilities 36 + Powers 85  + Advantages 3 + Skills  16 + Defenses 10  = 150

44

```

**Chunk 45** (`997bf2eca013`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PLAYER

Interpose

TOUGH

Ultimate Effort (Toughness checks)

QUICK

Improved Initiative

SKILLS

Close Combat: Unarmed 2

Take  the  skill  listed  above,  then  roll  1d20  twice  (re-roll  if
you get the same result twice) and record the results.

1-4

5-8

Athlete: You’re a trained athlete.

Ex-Military: You used to be in the armed forces.

9-12

Charmer: You have a way with people.

13-16

Rough Upbringing: You were raised on the streets
or have had a hard life.

17-20

Sharp Mind: You’re difficult to fool.

ATHLETE

Athletics 4, Perception 4, Ranged Combat: Throwing 4

Roll  1d20  once  and  record  the  result  as  the  first  power
in  an  array,  then  roll  1d20  once  and  add  the  result  as  a
1-point Alternate Effect (re-roll if you get the same result
as your first roll).

1-3

4-6

7-9

Energy Blast: Ranged Damage 10, Accurate 5,

Distracting, Tiring • 10 points

Foot Stomp: Line Area Damage 10, Powerhouse and
target must be in contact with the same surface
• 10 points

Groundstrike: Burst Area Affliction 10 (Resisted

and Overcome by Fortitude; Dazed and Hindered,
Stunned and Prone, Incapacitated), Extra
Condition, Instant Recovery, Powerhouse and
target must be in contact with the same surface
• 10 points

10-12

13-14

Shockwave: Burst Area Damage 10, Powerhouse
and targets must be in contact with the same
surface • 10 points

Super-Breath: Close Range Cone Area Move Object
5, Limited to moving toward and away, Linked
to Cone Area Damage 5, Unreliable (only the
Damage is Unreliable) • 10 points

15-17

Cut Loose!: Penetrating 10 on Strength • 10 points

18-20

Thunderclap: Cone Area Affliction 10 (Resisted and
Overcome by Fortitude; Dazed, Stunned), Limited
Degree • 10 points

EX-MILITARY

Expertise: Military 4, Perception 4, Ranged Combat: Throwing 4

CHARMER

Deception 4, Insight 4, Persuasion 4

UPBRINGING

Only if you rolled Solid Form or Super-Strength on the
Offensive  Powers  table,  take  Super-Stamina,  directly
below, then roll on the table below, as directed. Do not
take Super-Stamina if you rolled Density or Growth on
the  Offensive  Powers  table,  instead,  roll  on  the  table
below.

Expertise: Streetwise 4, Intimidation 6, Perception 2

Super-Stamina: Enhanced Stamina 10 • 20 points

MIND

Expertise: (Choose One) 4, Insight 4, Perception 4

POWERS

Roll 1d20 once and record the result.

Roll  1d20  four  times  (re-roll  if  you  get  the  s

[... truncated ...]
```

**Chunk 46** (`9b4ab26032fa`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PL10PL10

SPEEDSTER
SPEEDSTER

STRENGTH
2
STAMINA
2

POWERS

AGILITY
4
DEXTERITY
3

FIGHTING
4
INTELLECT
0

AWARENESS
1
PRESENCE
2

Fast Attack: Damage 3, Strength-based, Multiattack and

Selective on 5 Damage • 13 points

•  Damage 3, Strength-based, Burst Area and Selective on 5 Damage

• 1 point

Fast Defense: Enhanced Dodge 11, Enhanced Parry 11

• 22 points

Super-Speed: Enhanced Initiative 3, Quickness 10, Speed 15

(64,000 MPH)• 28 points

Run On Water: Movement 1 (Water Walking), Limited to While

Moving • 1 point

Run Up Walls: Movement 2 (Wall-crawling 2), Limited to While

Moving • 2 points

Defensive Roll 3, Improved Initiative 3, Instant Up, Move-by Action

SKILLS

Acrobatics 4 (+8), Athletics 8 (+10), Close Combat: Unarmed 6 (+10),
Deception 6 (+8), Expertise: (Choose One) 6 (+6), Perception 8 (+9),
Ranged Combat: Thrown 6 (+9), Technology 6 (+6)

OFFENSE

INITIATIVE +16

Throw +9

Ranged, Damage 2

Fast Attack +10

Close, Damage 5, Multiattack 5, Selective 5

DEFENSE

DODGE

PARRY

WILL

15

15

10

FORTITUDE

TOUGHNESS

10

5/2*

*Without Defensive Roll

```

**Chunk 47** (`9b8b75c1b5e7`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PL10PL10

STRENGTH
12
STAMINA
1

POWERS

AGILITY
1
DEXTERITY
2

FIGHTING
8
INTELLECT
5

AWARENESS
2
PRESENCE
0

Battlesuit: Removable (–21 points)

Armor: Protection 11, Impervious

 • 22 points.

Boot Jets: Flight 8 (500 MPH) • 16 points.

Comm System: Radio Communication 2

 • 8 points.

Life Support System: Immunity 10 • 10 points.

Sensors: Senses 12 (Accurate Radio Extended 3 [radar], Darkvision,
Direction Sense, Distance Sense, Infravision, Time Sense, Ultra-
Hearing) • 12 points.

Servo Motors: Enhanced Strength 12 • 24 points.

•  Force Beams: Ranged Damage 12 • 1 point.

Tactical Computer: Enhanced Dodge 2, Enhanced Fighting 4,

Enhanced Ranged Attack 2 • 12 points.

Accurate Attack, Improvised Tools, Inventor, Ranged Attack 2, Ranged
Attack 4, Second Chance (Technology checks)

SKILLS

Expertise: (Choose one of Business, Engineering, or Science) 5 (+10),
Insight  4  (+6),  Perception  3  (+5),  Persuasion  4  (+4), Technology  8
(+13)

OFFENSE

INITIATIVE +1

Force Beam +8

Unarmed +8

Ranged, Damage 12

Close, Damage 12

DEFENSE

DODGE

PARRY

WILL

8

8

8

FORTITUDE

TOUGHNESS

6

12

```

**Chunk 48** (`a25964ce768c`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

The MUTANTS & MASTERMINDS Roleplaying Game allows you to create any sort of hero you want by choosing your character’s
abilities, skills, powers, and other traits. You have a “budget” of power points with which to build your hero. There are
also certain limits and guidelines imposed by the game’s power level, chosen by the Gamemaster, but within those
limits you can build a wide range of characters.

The quickest and easiest way to create your own MUTANTS & MASTERMINDS hero is to look through the various hero arche-
types on pages 35-49, choose one that fits the type of hero you want to play, and customize it to match your ideas. With
just a few quick choices, you have a new hero, complete and ready for the game!

Each archetype offers a complete, ready-to-play power level 10 hero, the recommended starting power level for MUTANTS
& MASTERMINDS. Some archetypes offer a few simple choices in terms of skills, advantages, or sets of powers to fit different
themes. For example, many archetypes offer a choice of an Expertise skill to round out the character’s background and
interests outside of superheroism.

Some archetypes also offer an Options section, where you can change some of the pre-existing trait choices to create a
different kind of hero. For example, the Crime Fighter archetype has options for a hero with less equipment, but super-
human senses, or a special vehicle of some type. Other archetypes offer similar options.

Even if the archetype does not have an Options section that does not mean you cannot customize the archetype to suit
the type of hero you want to play! The archetypes are just starting points: if you are more familiar with character design
in MUTANTS & MASTERMINDS, feel free to change any or all of your chosen archetype’s traits. So long as you stay within the
bounds of available power points, series power level, and your Gamemaster’s approval, you’re fine.

Please note, the characters on pages 35-49 include some Advantages in italicized print. Those advantages are from an
Enhanced Advantage effect listed in their powers.

Designing a hero from scratch in MUTANTS & MASTERMINDS follows a series of simple steps, using the information presented
in the other chapters of this book. You’ll need a copy of the character sheet found in the back of the book (and also avail-
able online) and some scratch paper to design your character. If you’re pressed for time, looking for some inspiration,


[... truncated ...]
```

**Chunk 49** (`a37758230a66`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

DETECTIVE

STRENGTH
3
STAMINA
4

AGILITY
4
DEXTERITY
4

FIGHTING
8
INTELLECT
5

AWARENESS
4
PRESENCE
2

INVENTOR

STRENGTH
3
STAMINA
3

AGILITY
5
DEXTERITY
5

FIGHTING
8
INTELLECT
7

AWARENESS
2
PRESENCE
1

1-8

9-15

16-20

Incredible Presence: You are physically impressive
or otherwise intimidating. You also a natural leader.

Wealthy Socialite: You are wealthy and know a lot
of people.

World Traveler: You have traveled the world, met
people everywhere, and learned a number of
languages.

PRESENCE

Daze (Intimidation), Skill Mastery (Intimidation), Startle,
Leadership

SOCIALITE

Benefit 3 (Millionaire), Connected

TRAVELER

Languages 3 (choose four), Contacts

Close Attack 2, Defensive Roll 2, Improved Initiative, Jack-of-
all-trades, Power Attack, Ranged Attack 7, Well-informed.

Take the advantages listed above, then roll on the Back-
ground Advantages, Mental Advantages, and Physical
Advantages tables below.

Roll 1d20 once and record the result. If you rolled the Dark
Avenger for your Abilities, take Incredible Presence in-
stead of rolling on this table.

Roll 1d20 twice (re-roll if you get the same result twice) and
record the results. If you rolled the Detective for your Abili-
ties, take Sleuth and only roll once, re-roll if you get Sleuth
again. If you rolled Inventor for your Abilities, take Scien-
tist and only roll once, re-roll if you get Scientist again.

1-10

11-15

Criminologist: You study your enemies and know
how they think and behave.

Scientist: You are a trained scientist and capable of
inventing gadgets of your own.

16-20

Sleuth: You’re a student of observation.

```

**Chunk 50** (`a67593d532fb`):

```
CHAPTER 2: SECRET ORIGINS

59

UNDEAD

Roll 1d20 once and record the result.

1-7

8-14

15-20

Bestial: Enhanced Traits 16 (Close Attack 8, Diehard,
Evasion, Improved Critical (Unarmed), Improved
Initiative 2, Takedown, Uncanny Dodge); Leaping
2 (30 feet); Movement 1 (Wall-crawling); Senses 2
(Darkvision) • 22 points

Unholy Strength and Vitality: Enhanced Strength
3; Enhanced Trait 5 (Close Attack 5); Leaping 3 (60
feet); Regeneration 5; Speed 3 (16 MPH) • 22 points

Wraith: Flight 1 (4 MPH); Insubstantial 4,

Concentration, Distracting; Strength-based
Damage 2; Enhanced Advantages 6 (Close
Attack 6) • 22 points

Damage Resistance: Impervious Protection 8 • 16 points

Unliving: Immunity 38 (Aging, Critical Hits, Fortitude effects,

Sensory Affliction effects) • 38 points

Roll 1d20 once and record the result.

1-6

7-13

14-20

Fast and Tough: Enhanced Defenses 12 (Dodge 8,

Parry 4); Impervious Protection 2 • 16 points

Unnatural Speed: Enhanced Defenses 16 (Dodge

10, Parry 6) • 16 points

Unnatural Toughness: Enhanced Defenses 8
(Dodge 6, Parry 2); Impervious Protection 4
• 16 points

Roll 1d20 once and record the result.

1-12

13-20

Inhuman Brain: Immunity 10 (Mental effects)

• 10 points

Almost Human: Enhanced Defenses 5 (Will 5);

Immunity 5 (Emotion effects) • 10 points

DEFENSES

DODGE
+0

PARRY
+0

FORTITUDE
+0

TOUGHNESS
+0

WILL
+0

ABILITIES

POWERS

34

102

2

SKILLS

DEFENSES

TOTAL

12

0

150

•  Motivation—Acceptance: The Construct often feels
like  an  outsider,  either  because  it’s  not  human  and
wants to be, or used to be human and wants to be
again. Regardless, the Construct is a hero because it
wants to be accepted by the rest of humanity.

•  Motivation—Doing Good: An artificial intelligence or
magically created Construct may have been created to
“do good” and pursues that goal to the best of its ability.

•  Motivation—Justice:  A  revenant  or  ghost-pos-
sessed Construct may recall enough of its former life
to  be  on  the  prowl  for  revenge  against  the  specific
people that killed it, or against all members of groups
with similar motivations.

•  Motivation—Responsibility: The Construct may feel
that its powers and abilities were given to it for a rea-
son, so it has a responsibility to help however it can.

•

•

Enemy:  The  Construct  could  be  a  rogue  android,
golem,  or  summoned  elemental  hunted  by  its
creator(s)  or  another  person  or  group  who  believes
the Construct is evil for some reason.

Prej

[... truncated ...]
```

**Chunk 51** (`a8c6225b93ed`):

```
CHAPTER 2: SECRET ORIGINS

77

DEFENSE

DODGE
+7

PARRY
+4

FORTITUDE
+6

TOUGHNESS
+0

WILL
+7

ABILITIES

POWERS

42

59

11

SKILLS

DEFENSES

TOTAL

14

24

150

•

•

•

Accident:  The  Mystic  commands  incredible  super-
natural powers, but sometimes those powers get out
of control, or awaken sleeping horrors, or cause other
unintended consequences that have to be dealt with.

Enemy: Some Mystics are plagued by enemies who
want to displace them or steal their power.

Honor:  It’s  not  uncommon  for  a  Mystic  to  follow  a
code of conduct that keeps them on the straight and
narrow,  perhaps  because  it’s  the  right  thing  to  do,
perhaps because they need to in order to keep their
powers in check.

•  Motivation—Acceptance:  Mystics  are  often  either
not from Earth or were trained in the mystic arts on
another  world. When  they  come  to  this  plane  they
use their talents to help others and hopefully earn a
place for themselves on their adopted world.

•  Motivation—Responsibility: The Mystic was given
his  or  her  power  for  a  reason—to  defend  Earth,  to
hunt down otherworldly creatures, or any number of
other options. Or perhaps the Mystic recognizes that
his or her power comes with a price.

•

•

Power  Loss:  Mystics  often  have  the  Complication
that  prevents  them  from  using  their  powers  when
they can’t move and/or speak to cast their spells.

Prejudice: Some Mystics are surrounded by an aura
of “otherness”  that  sets  them  apart  from  the  rest  of
humanity and makes it difficult for them to interact
with others. Or, maybe people just fear witches.

PARAGON

Paragons are what people first think of when they think
of superheroes. A Paragon is nearly perfect in every way:
fast, strong, tough, often has the ability to fly, and repre-
sents everything good about humanity. Paragons are of-
ten talented in a wide range of areas and easily take on
leadership roles.
ABILITIES

Roll 1d20 once and record the result.

1-6

7-14

15-20

Man of Action: You’re the height of human
perfection, whether through a lifetime of
experimental training or due to influence from some
outside source.

Superhuman: You’re a powerful mutant, alien, or
human who’s gained incredible abilities.

Vessel: You are the vessel for the power of a god or
some other supernatural force.

ACTION

STRENGTH
6
STAMINA
6

AGILITY
6
DEXTERITY
4

FIGHTING
6
INTELLECT
3

AWARENESS
4
PRESENCE
2

SUPERHUMAN

STRENGTH
8
STAMINA
8
VESSEL

AGILITY
4
DEXTERITY
4

FIGHTIN

[... truncated ...]
```

**Chunk 52** (`aa943c38ef67`):

```
CHAPTER 2: SECRET ORIGINS

89

d20 once on that table to determine if your base form and
duplicates are Energy Controllers, Martial Artists, or Pow-
erhouses. Your base form has the same abilities, powers,
advantages, skills, defenses, and totals as the summoned
characters, but with the addition of the Summon Twin or
Summon Triplets power.

Summon Twin: Summon 8 (One PL8, 120 point
duplicate), Heroic, Mental Link • 33 points

PL 8

STR
STA

1  AGL
2  DEX

2
4

FGT
INT

1  AWE
PRE
0

2
2

Powers: Energy Control (Array (16 points),
Energy Blast (Ranged Damage 8), AE: Energy
Explosion (Ranged Burst Area Damage
5), AE: Energy Bolts (Ranged Multiattack
Damage 5), AE: Dazzle (Cumulative Ranged
Affliction 8 (Resisted by Dodge and Overcome
by Fortitude; Impaired, Disabled, Unaware),
Limited to Vision); Energy Field (Sustained
Protection 6 Linked to Reaction Damage 2,
Precise); Energy Flight (Flight 6 (120 MPH));
Energy Immunity (Immunity 1 (Immune
to own powers)); Transform (Quick Change
(Feature 1, change into costume as a free
action))

Advantages: Accurate Attack, Power Attack,
Set-up, Teamwork

Skills: Acrobatics 4 (+8), Athletics 4 (+5),
Expertise (Choose One) 4 (+4), Perception 4
(+6), Ranged Combat: Energy Control 4 (+8)

Offense: Init +4, Energy Blast +8 (Ranged,
Damage 8 or other effects), Unarmed +1
(Close, Damage 1)

Defense: Dodge 8, Parry 8, Fort 8, Tou 8,
Will 8

1-6

1-10

Totals: Abilities 32 + Powers 50 + Advantages 2
+ Skills 10 + Defenses 23 = 117

1-6

Note: Roll on the Energy Controller
archetype’s Energy Descriptors table to
determine the type of energy you control.

PL 8

11-20

7-13

STR
STA

1  AGL
4  DEX

5
5

FGT
INT

10  AWE
PRE

1

2
0

Equipment: Smartphone, Flashlight,
Motorcycle, Restraints, Swingline (Movement
1 (Swinging)), Tonfa (Strength-based Damage
2, Reach 1), AE: Throwing Disks (Ranged,
Strength-based Damage 1)

Advantages: Chokehold, Daze (Deception),
Defensive Roll 2, Equipment 4, Evasion,
Improved Initiative, Instant Up, Power Attack,
Quick Draw, Set-up, Teamwork

Skills: Acrobatics 7 (+12), Athletics 6 (+10),
Deception 8 (+8), Expertise (Choose One)
7 (+8), Perception 6 (+8), Ranged Combat
(Throwing Disks) 5 (+10), Stealth 7 (+12),
Vehicles 4 (+9)

Offense: Init +9, Throwing Disks +10 (Ranged,
Damage 5), Tonfa +10 (Close, Damage 6),
Unarmed +10 (Close, Damage 4)

Defense: Dodge 10, Parry 10, Fort 8, Tou 6/4,
Will 8

Totals: Abilities 62 + Powers 0 + Advantages 15
+ Skills 25 + Defenses 15 = 117

14-20

PL 8

STR
STA

9  

[... truncated ...]
```

**Chunk 53** (`ab9b367b750f`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

STRENGTH
3
STAMINA
2

POWERS

AGILITY
5
DEXTERITY
5

FIGHTING
7
INTELLECT
0

AWARENESS
1
PRESENCE
2

Choose two of the following • 10 points

•  Blocking: Deflect 7, Easily Removable (weapon or shield, –2 points)

•  Crippling Strike: Affliction 7 (Resisted by Fortitude; Impaired, Hindered,

Incapacitated), Easily Removable (weapon, –2 points)

•  Fast: Quickness 3, Speed 2 (8 MPH)

•  Gadgets: Variable 1 (5 points), Easily Removable (–2 points)

•  Healing Factor: Regeneration 5

•

Improvised Weapons: Damage 2, Strength-based, Ranged 5, Easily
Removable (–2 points)

•  Super-Hearing: Senses 5 (Accurate Hearing, Danger Sense,

Extended Hearing, Ultra-Hearing)

•  Super-Vision: Senses 5 (Darkvision, Extended Vision, Microscopic

Vision 2)

•  Urban Acrobat: Leaping 1, Movement 2 (Safe Fall, Swinging)

EQUIPMENT

Weapon: Choose one of the following • 15 points.

Bow (or Crossbow): Ranged Damage 5 with: Multiattack or five

Alternate Effects (trick arrows).

Daggers (or Knives): Strength-based Damage 2, Ranged 5,

Multiattack 5, Improved Critical, Improved Defense, Improved
Disarm.

Gun (revolver or semi-automatic): Multiattack Ranged Damage 5.
Sword (including Katana): Strength-based Damage 2,

Multiattack 5, Penetrating 5, Improved Defense, Improved
Disarm, Improved Smash.

Whip: Damage 4, Multiattack, Improved Grab, Improved

Hold, Improved Trip, Reach 3
•  Movement 1 (Swinging).

Vehicle: Motorcycle • 10 points

Defensive Roll 4, Equipment 5, Evasion, Improved Critical (weapon)

Plus  choose  six  of  the  following:  Accurate  Attack,  Agile  Feint,
Assessment,  Connected,  Contacts,  Defensive  Attack,  Improved  Critical
(weapon),  Improved  Defense,  Improved  Disarm,  Improved  Initiative,
Improved Smash, Improved Trip, Power Attack, Precise Attack (choose
one), Takedown, Taunt, Uncanny Dodge.

SKILLS

Acrobatics  8  (+13),  Athletics  8  (+11),  Close  Combat:  Weapon  6  (+13),
Deception 8 (+10), Expertise: (Choose One) 6 (+6), Expertise: Weapons 8
(+8), Intimidation 6 (+8), Investigation 6 (+6), Perception 8 (+9), Ranged
Combat:  Weapon  8  (+13),  Sleight  of  Hand  6  (+11),  Stealth  8  (+13),
Vehicles 4 (+9)

OFFENSE

INITIATIVE +5*

Weapon +13

Weapon +13

Close, Damage 5, Crit. 19-20*

Ranged, Damage 5, Crit. 19-20

* Varies depending on Advantages and Weapon chosen.

PL10PL10

DEFENSE

DODGE

PARRY

WILL

12

14

9

FORTITUDE

TOUGHNESS

8

6/2*

*Without Defen

[... truncated ...]
```

**Chunk 54** (`ac75d3f2b9e6`):

```
CHAPTER 2: SECRET ORIGINS

95

MYSTIC

MUTATION

Assessment, Ritualist, Trance

Expertise: (Choose one) 8, Investigation 6, Technology 6

PLAYFUL

Daze (Deception), Redirect, Taunt

SNEAKY

Evasion, Hide in Plain Sight, Improved Initiative

Roll 1d20 once and record the result.

1-5

Dominating: You are afforded respect by other
creatures.

6-10

Predator: You are on the top of the food chain.

11-15

Trickster: You are a cunning prankster.

16-20 Wise: You are astute and perceptive.

DOMINATING

1-5

Altruistic: You value the group over the individual.

Athletics 4, Intimidation 12, Perception 4

6-10

11-15

16-20

Cooperative: You are accustomed to a codependent
community.

Egoistic: You look out for yourself and your own
survival.

Vengeful: You go out of your way to spite others,
even at cost to yourself.

ALTRUISTIC

Inspire, Interpose, Leadership

COOPERATIVE

Animal Empathy, Set-up, Teamwork

EGOISTIC

Favored Environment (Choose One), Great Endurance,
Uncanny Dodge

VENGEFUL

Daze (Intimidation), Favored Foe (Choose One), Startle

SKILLS

Roll on the Origin Skills table and Disposition Skills tables.

Roll 1d20 once and record the result.

1-6

7-12

13-20

Awakened: You are an unusual member of your
species with a human intellect and perhaps even a
human form.

Invocation: You were granted your powers by
calling upon the animal spirits.

Mutation: You came upon your powers through a
freak accident.

AWAKENED

Athletics 6, Perception 6, Stealth 8

INVOCATION

Insight 8, Perception 6, Treatment 6

96

PREDATOR

Acrobatics 4, Athletics 4, Perception 6, Stealth 6

TRICKSTER

Acrobatics 6, Deception 6, Sleight of Hand 4, Stealth 4

WISE

Insight 8, Perception 8, Treatment 4

POWERS

Find the entry below for the type of Totem that matches
what you rolled for your Abilities.

Roll 1d20 once and record the result.

SCORPION

1-5

Climbing: Movement 2 (Wall-crawling 2) • 4 points

Sting: Progressive Weaken Stamina 10, Accurate 2

• 32 points

SPIDER

Spider-Movement: Leaping 2 (30 feet); Movement

3 (Swinging, Wall-crawling 2) • 8 points

Spider Senses: Senses 4 (Danger Sense, Darkvision,

Ranged Touch) • 4 points

6-10

Web Snare: Ranged Cumulative Affliction 6

(Resisted by Dodge, Overcome by Damage;
Hindered and Vulnerable, Defenseless and
Immobilized), Accurate 5, Extra Condition,
Limited to Two Degrees • 23 points

•  Web Tether: Move Object 7, Accurate 5 • 1 point

SWARM

Blinding Barrage: Burst Area Visual (All)

Concealment Attack 4 • 12 points

1

[... truncated ...]
```

**Chunk 55** (`b511fe78f53a`):

```
CHAPTER 2: SECRET ORIGINS

63

OVERSEER

Contacts, Leadership

UNOBTRUSIVE

Favored Environment (Choose One), Choose One: Evasion or
Improved Initiative

SKILLS

Ranged Combat: (Element) Control 6

Choose One: Acrobatics 4, or Athletics 4, or Close Combat:
Unarmed 4

Choose One: Deception 6 or Intimidation 6

Roll 1d20 once and record the result.

1-5

6-20

Android Host: Enhanced Strength 6, Reduced

Stamina 7 (Stamina —); Enhanced Defenses 8
(Dodge 4, Parry 4); Immunity 20 (upgrades Life
Support to all Fortitude effects); Protection 8
• 34 points

Gaseous Form: Visual Concealment 4, Partial;
Enhanced Advantages 2 (Defensive Roll 2);
Enhanced Defenses 18 (Dodge 9, Parry 9);
Insubstantial 2, Permanent • 34 points

Take the skills listed above, then roll 1d20 once and record
the result. If you rolled Embodiment for Abilities, take Na-
tive instead of rolling on this table.

Flight: Flight 7 (250 MPH) • 14 points

1-5

6-10

Native: You are well versed in or have researched
the properties of your element.

Pilot/Driver: You are proficient in the care and use
of planes or cars.

11-15

Scientist: You are knowledgeable in the sciences.

16-20

Soldier: You are a former military man.

Air Control: Array (24 points plus 2 Alternate Effects)

•  Air Blast: Ranged Damage 12 • 24 points

Take the Air Control Array and Air Blast (above) and roll
1d20  twice  (re-roll  if  you  get  the  same  result  twice)  and
add them to the Air Control array as Alternate Effects.

NATIVE

Expertise: Elements 8, Perception 4

PILOT/DRIVER

Expertise: Repair 4, Vehicles 8

SCIENTIST

Expertise: Science 8, Technology 4

SOLDIER

Athletics 4, Expertise: Military 8

POWERS

1-3

4-6

•  Fog: Environment 12 (Visibility -5; 8 mile radius)

• 1 point

•  Suffocation: Progressive Ranged Affliction 6
(Resisted and Overcome by Fortitude; Dazed,
Stunned, Incapacitated) • 1 point

7-10

•  Tornado: Cylinder Area Move Object 8,

Concentration Duration, Damaging • 1 point

11-13

•  Wind Binding: Ranged Affliction 12 (Resisted

by Dodge, Overcome by Strength; Hindered and
Vulnerable, Immobile and Defenseless), Extra
Condition, Limited Degree • 1 point

14-17

•  Wind Control: Move Object 12 • 1 point

18-20

•  Wind Screen: Deflect 12, Cylinder Area (×2),
Limited to Attacks Targeting Dodge • 1 point

Elemental Constitution: Immunity 12 (Critical Hits, Life

Support) • 12 points

Earthen Body: Enhanced Strength 8; Impervious Protection

8 • 32 points

Reconstitution: Regeneration 10, Source (El

[... truncated ...]
```

**Chunk 56** (`b95c26d52ee0`):

```
CHAPTER 2: SECRET ORIGINS

47

Power Point Totals:  Abilities 36 + Powers 67  + Advantages 5 + Skills  25 + Defenses 17  = 150

PL10PL10

OFFENSE

INITIATIVE +6

Ranged +8

Ranged, Damage depends on
weapon

Unarmed +10

Close, Damage 10

DEFENSE

DODGE

PARRY

WILL

10

10

10

FORTITUDE

10

TOUGHNESS

10/8*

*Without Defensive Roll

WARRIOR
WARRIOR

STRENGTH
10
STAMINA
8

POWERS

AGILITY
6
DEXTERITY
4

FIGHTING
10
INTELLECT
1

AWARENESS
4
PRESENCE
4

Super-Strength: Enhanced Strength 2,

Limited to Lifting (Lifting Str12;
100 tons) • 2 points.

Plus choose one of the following • 10 points.

•  Aquatic: Immunity 1 (Drowning), Swimming 6,
 Movement 1 (Environmental Adaptation,
Aquatic), Senses 1 (Low-light Vision).

•  Fast: Quickness 5, Speed 5

•  Leaping: Leaping 10

•  Super-Senses: Senses 10 (Accurate and

Analytical Hearing, Danger Sense, Extended
Hearing and Vision, Hearing Counters Illusion,
Tracking Vision, Ultra-Hearing) or 10 ranks of
other Senses.

•  Wind-Riding: Flight 5

OPTIONS

To customize, choose one of the following options
with no change in point total:

•  Strong Warrior: +2 Strength, –2 Fighting (including

–2 Parry).

•  Weapon Warrior: -3 Strength, Unique Weapon

(Strength-based Damage 3, Penetrating 5,
Easily Removable), also choose two additional
Advantages from the list given in the Advantages section

Agile Feint, Defensive Roll 2, Move-by Action, Power
Attack, Ranged Attack 4, Takedown

Plus choose four of the following: Accurate Attack,
All-out Attack, Animal Empathy, Benefit, Defensive
Attack, Favored Environment (choose one),
Favored Foe, Fearless, Improved Critical,
Improved Disarm, Languages (choose one),
Leadership, Precise Attack (choose one),
Skill Mastery, Tracking

SKILLS

Acrobatics 6 (+12), Athletics 5 (+15),
Expertise: (Choose one of History,
Mythology, or Tactics) 4 (+5),
Insight 6 (+10), Intimidation 5
(+9), Perception 6 (+10),
Stealth 4 (+10)

Power Point Totals:  Abilities 94 + Powers 12  + Advantages 14 + Skills  18 + Defenses 12y  = 150

48

```

**Chunk 57** (`bc6e8d2fe577`):

```
CHAPTER 2: SECRET ORIGINS

93

Supernatural Resistance: Roll 1d20 three times
(re-roll if you get the same result twice) and record
the results.

1-3

4-6

Immunity 5 (Cold, Heat, Pressure,
Radiation, Vacuum) • 5 points

Immunity 5 (Disease, Poison, Starvation

and Thirst, Suffocation) • 5 points

11-20

7-8

Immunity 5 (Alteration effects) • 5 points

9-10

Immunity 5 (Cold damage) • 5 points

11-12

Immunity 5 (Electricity damage) • 5 points

13-14

Immunity 5 (Emotion effects) • 5 points

15-17

Immunity 5 (Fire damage) • 5 points

18-20

Immunity 5 (Magic damage) • 5 points

Roll 1d20 once and record the result.

1-7

Eyes of Darkness: Senses 2 (Darkvision) • 2 points

8-14

15-20

Spider-Climb: Movement 1 (Wall-crawling)

• 2 points

Vampire Bite: Weaken Stamina 4, Grab-based

• 2 points

WEREWOLF

Thick Skin: Protection 3; Impervious Toughness 9, Lim-
ited—Not versus magical or silver weapons • 9 points

Roll 1d20 once and record the result.

Brother to Wolves: Summon 2 (Wolves and

1-10

Dogs), Horde, Mental Link, Multiple Minions 3 (8
minions), Sacrifice • 20 points

Deathly Howl: Auditory Perception Area Affliction
10 (Resisted and Overcome by Will; Dazed and
Impaired, Disabled and Stunned), Extra Condition,
Limited Degree • 20 points

1-4

5-10

Demonic Cape: Flight 6 (120 MPH), Gliding,

11-20

Removable (-1 point) • 5 points

Demonic Movement: Leaping 2 (30 feet); Speed 3

(16 MPH) • 5 points

11-16 Giant Bat Wings: Flight 5 (60 MPH), Wings • 5 points

17-20

Hellrider: Movement 2 (Wall-crawling, Water

Walking), Limited to While Moving; Speed 6 (120
MPH), Activation (standard action, -2 points),
Removable (-1 point) • 5 points

VAMPIRE

Blood Drain: Regeneration 10, Source (Blood) • 5 points

Roll 1d20 once and record the result.

1-5

6-20

Living Vampire: Enhanced Stamina 13; Immunity

4 (aging, disease, need for sleep, poison);
Impervious Toughness 8 • 38 points

Undead Invulnerability: Immunity 30 (Fortitude
effects); Impervious Protection 8, Limited—Not
against blessed or magical weapons • 38 points

Roll 1d20 once and record the result.

1-6

7-12

13-20

Children of the Night: Summon 2 (Bats, Rats, and

Wolves), Horde, Mental Link, Multiple Minions 3 (8
minions), Sacrifice • 20 points

Dominate: Perception Ranged Affliction 10 (Resisted

and Overcome by Will; Entranced, Compelled,
Controlled), Visually Sense-Dependent • 20 points

Mist Form: Insubstantial 2, Linked to Flight 5 (60

MPH) • 20 points

Roll 1d20 once and record the result.

[... truncated ...]
```

**Chunk 58** (`c0c1858f03fe`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PL10PL10

SKILLS

Acrobatics 6 (+12), Athletics 6 (+9), Close Combat: Unarmed 2 (+14),
Deception 6 (+10), Expertise: (Choose One) 4 (+8), Insight 6 (+10),
Intimidation  8  (+12),  Investigation  8  (+12),  Perception  6  (+10),
Ranged Combat: Thrown 8 (+14), Sleight of Hand 4 (+10), Stealth 8
(+14), Technology 2 (+6), Vehicles 4 (+10)

OFFENSE

INITIATIVE +6

Boomerang +14

Unarmed +14

Ranged, Damage 4

Close, Damage 3

DEFENSE

DODGE

PARRY

WILL

12

12

10

FORTITUDE

TOUGHNESS

6

8/5*

*Without Defensive Roll

STRENGTH
3
STAMINA
3

AGILITY
6
DEXTERITY
6

FIGHTING
12
INTELLECT
4

AWARENESS
4
PRESENCE
4

EQUIPMENT

Commlink • 1 point.

Costume: Protection 2 • 2 points.

Grapple Gun: Movement 1 (Swinging) • 2 points.

Utility Belt: Array (12 points)

•  Flash-Bangs: Burst Area Dazzle 3 (Visual and Auditory) • 12 points.

•  Smoke Pellets: Cloud Area Concealment Attack 4 (visual) • 1

point.

•  Sleep Gas Pellets: Ranged Cloud Area Affliction 4 (Resisted by

Fortitude; Daze, Stun, Asleep) • 1 point.

•  Boomerangs: Strength-based Damage 1, Ranged 4 • 1 point.

OPTIONS

To customize, choose one of the following options with
no change in point total:

•  Gimmick: Replace Equipment advantage and optional
advantages with a 10-point Removable power device.

•  Sentinel: Drop Commlink and Utility Belt from

equipment, add a tonfa or similar weapon (Damage 1).
Change  Equipment to 1 rank and add 3 points
worth of Senses. Remove optional advantages to
add more Senses, if desired.

•  Vehicle: Replace optional advantages with a
vehicle worth up to 20 equipment points
(an additional 4 ranks of Equipment).

Defensive Roll 3, Equipment 4, Uncanny Dodge
Plus choose four of the following: Agile
Feint, Assessment, Benefit, Contacts,
Defensive Attack, Daze (Intimidation),
Hide in Plain Sight, Jack-of-all-trades,
Power Attack, Precise Attack (Close;
Concealment), Skill Mastery
(Stealth), Startle, Takedown, Throwing
Mastery, Ultimate Effort (Investigation)

```

**Chunk 59** (`c1c422470246`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

TALENT

STRENGTH
1
STAMINA
1

AGILITY
2
DEXTERITY
2

FIGHTING
1
INTELLECT
3

AWARENESS
6
PRESENCE
2

Roll 1d20 once and record the result.

DABBLER

Expertise: (Choose One) 4, Insight 4, Perception 4

NINJA

Acrobatics 4, Perception 4, Stealth 4

SNEAK

Deception 4, Perception 4, Stealth 4

STUDENT

Expertise: (Choose One) 6, Insight 2, Perception 4

1-4

5-8

9-12

13-16

Charmed Life: You live a charmed life; maybe
you’re just lucky, but maybe it’s low-level psionic
influence... who can say?

POWERS

Contemplative: You are always calm and
controlled.

Perfect Mind: You use a greater percentage of
your mind.

Thought Leader: You use your abilities to help
others reach greater heights.

Roll  1d20  once  to  determine  if  you  should  roll  on  the
Psionic,  Mentalist,  or  Telekinetic  table,  then  roll  1d20
again on that table and record the result.

17-20

Trained Fighter: You know how to fight.

LIFE

Attractive, Fascinate (Persuasion), Luck

CONTEMPLATIVE

Fearless, Trance, Ultimate Effort (Will checks)

MIND

Eidetic Memory, Jack-of-all-trades, Ultimate Effort (Will checks),

LEADER

Choose either: Inspire, Leadership, and Teamwork, or Inspire 2
and Leadership or Teamwork

FIGHTER

Improved Initiative, Power Attack, Uncanny Dodge

SKILLS

Roll 1d20 twice (do not re-roll if you get the same result
twice) and record the results.

1-4

5-8

Charmer: You’re good with people.

Dabbler: You dabble in whatever interests you.

9-12

Ninja: You have been trained in the way of the ninja.

13-16

17-20

Sneak: You’re sneaky and underhanded when you
need to be.

11-15

Student: You’re a high-school, college, or post-
graduate student.

CHARMER

Deception 4, Insight 4, Persuasion 4

Psionic: Take Telepathy, listed immediately below,

then roll on the Psionic Table.

Telepathy: Mind Reading 5 Linked to Area Mental

Communication 3 • 25 points

Psionic Table: Roll 1d20 once and record the result
as the first power of an array, then roll 1d20 twice
and add each result as a 1-point Alternate Effect (re-
roll if you get the same result as your first roll).

1-3

4-7

ESP: Remote Sensing 6 (Normal Visual,
Normal Auditory, Mental) • 24 points

Mental Blast: Perception Range Damage

6, Resisted by Will • 24 points

1-10

8-11

Psi-Knife: Damage 8, Penetrating 4,

Accurate 4, Resisted by Will • 24 points

12-14

15-17

Psionic Invisibility: Concealment 10,

Affects Others, Limited—Concealme

[... truncated ...]
```

**Chunk 60** (`c53b199f9ade`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PL10PL10

OFFENSE

INITIATIVE +11

Mimic +11

Unarmed +81

Ranged, Mimic1

Close, Damage 11

DEFENSE

DODGE

PARRY

WILL

FORTITUDE

TOUGHNESS

81

11

81

81

81

STRENGTH
1
STAMINA
1

POWERS

AGILITY
1
DEXTERITY
1

FIGHTING
8
INTELLECT
1

AWARENESS
1
PRESENCE
2

Mimic: Variable 12 (60 points) for duplicating a subject’s traits,
Continuous, Move Action, Limited to One Subject, Resistible
(Dodge, DC 22) • 84 points.

Assessment

SKILLS

Deception 6 (+8), Expertise: (Choose One)
 4 (+5), Insight 8 (+9), Perception 6 (+7)

1 These bonuses will vary based
on the traits mimicked

```

**Chunk 61** (`c8f2e2af058e`):

```
CHAPTER 2: SECRET ORIGINS

71

mankind, he or she may also become a hero for the
same reason.

•  Motivation—Recognition:  Some  Gadgeteers  want
their genius recognized not just by other  scientists,
but by millions of adoring fans.

•  Motivation—Responsibility:  The  Gadgeteer  often
feels it’s only right to use his or her incredible intel-
ligence to help others.

•  Motivation—Thrills:  Gadgeteers  love  to  push  the
limit and live on the edge of scientific research, so it
only makes sense that they might like dressing up in
tights and taking on the role of a hero.

•

•

Quirk—Psychological Problems: Perhaps the Gad-
geteer’s  devices  have  slowly  been  poisoning  his
or  her  mind,  or  biofeedback  caused  by  improperly
functioning cybernetics or other mechanical systems
have  caused  the  Gadgeteer  to  exhibit  some  sort  of
mental problem.

Relationship:  Gadgeteers  often  have  a  number  of
important  people  in  their  life,  either  family,  loved
ones, other researchers, or employees who like to get
into trouble.

The Martial Artist has honed his skills in unarmed combat
to  bridge  the  physical  gap  between  him  and  his  super-
powered  associates.  In  fact,  some  Martial  Artists  display
feats  that  seem  impossible  by  normal  standards—and
may have a mystical origin.
ABILITIES

Roll 1d20 once and record the result.

1-6

7-14

Finesse and Control: Your speed and reflexes
almost too fast to be human.

Mystic Endowment: You have unlocked your
body’s potential by cultivating your inner energy.

15-20

Strength and Power: You have trained your body
close to human perfection.

CONTROL

STRENGTH
3
STAMINA
3

AGILITY
7
DEXTERITY
5

FIGHTING
13
INTELLECT
0

AWARENESS
5
PRESENCE
0

ENDOWMENT

STRENGTH
3

AGILITY
5

FIGHTING
12

AWARENESS
6

STAMINA
3

DEXTERITY
5

INTELLECT
1

PRESENCE
1

POWER

AGILITY
6
DEXTERITY
4

STRENGTH
4
STAMINA
4

FIGHTING
12
INTELLECT
1

AWARENESS
4
PRESENCE
1

Agile Feint, Defensive Roll 4, Improved Initiative, Power Attack,
Takedown

Take the advantages listed above, then roll 1d20 once and
record the result.

1-6

Armed Fighter: You are an expert with exotic
weapons.

7-13 Wealthy: You are well connected and rich.

14-20

Well Traveled: You have walked the world righting
wrongs and challenging senseis.

FIGHTER

Equipment 2 (select one weapon), Improvised Weapon, Quick
Draw

WEALTHY

Benefit 3 (Millionaire), Connected

TRAVELED

Contacts, Languages 1 (Choose One), Tracking, Well-informed

If you rolle

[... truncated ...]
```

**Chunk 62** (`c8f8dadd6203`):

```
CHAPTER 2: SECRET ORIGINS

91

SHADOWS

PL 6

4  AGL

STR
STA  —  DEX

0  FGT
INT

0

6  AWE
0  PRE

0
0

Powers: Claws (Strength-based Damage 2,
Affects Corporeal), Float (Flight 1 (4 MPH),
Shadow Form (Immunity 30 (Fortitude
Effects), Insubstantial 4 (Incorporeal;
Innate; Permanent), Protection 4, Strength
Affects Corporeal)

Skills: Perception 4 (+4), Stealth 12 (+12)

Offense: Init +0, Claws +6 (Close, Damage 6)

Defense: Dodge 6, Parry 6, Fort Immune,
Tou 4, Will 5

Totals: Abilities 10 + Powers 61 +
Advantages 0 + Skills 8 + Defenses 11 = 90

15-20

15-20

SUMMONER

Defensive Roll 4 and Choose One: Artificer, Ritualist, or Inventor

SKILLS

SUMMONER

Perception 4, Stealth 4, and Choose One Expertise: Magic 6 or
Technology 6

DEFENSE

SUMMONER

DODGE
+10

PARRY
+8

FORTITUDE
+4

TOUGHNESS
+0

WILL
+7

POINTS*

ABILITIES

POWERS

48

61

5

SKILLS

DEFENSES

TOTAL

7

29

150

*These numbers are for the Summoner only; for the Du-
plicator,  use  the  totals  listed  for  the  appropriate Twin  or
Triplets, then add the points for the Summon power.

•  Motivation—Acceptance:  The  Summoner  has  un-
usual abilities that make him or her an outsider. He or
she uses those powers to gain acceptance.

•  Motivation—Doing  Good:  Some  Summoners  are
heroes because they believe it’s the right thing to do.

•  Motivation—Responsibility:  With

the  powers
they’ve  been  given,  some  Summoners  believe  it’s
their responsibility to help others.

•  Motivation—Thrills:  Outside  of  their  Summon
ability, many Summoners don’t have a lot of powers.
Some may find the constant threat of danger to be a
bit much, but not this Summoner! The more danger,
the better!

•

•

•

Power Loss: Summoners may need to speak or move
their  hands  in  order  to  summon  their  minion(s).
When these Summoners are bound and/or gagged,
they lose their powers.

Relationship: A Summoner may have friends or fam-
ily to whom he’s responsible—but it may be that the
Summoner needs to keep his summoned creature(s)
happy as well. The Summoner may have Controlled
minions,  but  that  doesn’t  mean  he  can  be  mean  to
them and still expect them to show up!

Secret: The Summoner’s minions and abilities come
from  somewhere;  what  if  their  origin  is  particularly
dark or dangerous? The Summoner would certainly
want to keep that secret private as long as possible.

Supernatural Creatures are fantastical beings out of folk-
tales and scary stories. They’re generally regarded as ur-
ban  l

[... truncated ...]
```

**Chunk 63** (`cb4093e23f62`):

```
CHAPTER 2: SECRET ORIGINS

55

VS. RANDOM

The MUTANTS & MASTERMINDS Quickstart Character Generator is random, but it’s not 100% random. It was built to create a
character that fits within the concept of one of 20 different super-heroic archetypes—and it does that really well!—but, it
doesn’t give you a completely random character that combines a bunch of disparate powers at wildly differing ranks that
you then have to make work as a character.

The goal for this character generator is to get new players playing a hero of their very own as quickly as possible—and not
just playing, but playing a hero who is effective in a game with which they may be completely unfamiliar. Plus, by using
Archetypes often seen in comics as the starting point, all the heroes should be easily identifiable to anyone with even a
passing knowledge of comic characters.

If creating a character with the Quickstart Character Generator gets you interested in writing up a completely new char-
acter from scratch, a good place to go for inspiration on how to create powers is the Power Profiles. Each entry covers
a type of power, like Fire, Gravity, Darkness, Armor, or Mental powers. The profiles include information on common
descriptors for the power you’re interested in as well as new features, example powers, and typical complications for
someone possessing such powers.

Players taking their first stab at creating a new character will likely find the Powers section most useful because it provides
examples of offensive, defensive, movement, and utility powers. There’s a brief explanation of each sample power along
with its M&M write-up using the game’s effects. The write-ups even include its power point cost per rank, so you don’t
have to figure it out.

You can get individual Power Profile PDFs, or the collected book at http://www.greenronin.com/store/category/power-
profiles.html

Once  you’re  playing  the  game,  have  a  little  experience
using  Hero  Points,  and  even  accumulated  a  few  Power
Points to spend to improve your hero, the character gen-
erator  is  an  excellent  place  to  look  for  inspiration  when
it’s  time  to  come  up  with  just  the  right  Alternate  Effect.
Whether  you  need  an  Alternate  Effect  when  you’re  in  a
pinch  during  a  game  (by  spending  those  Hero  Points!)
or  between  sessions  when  it’s  time  to  make  permanent
changes and additions to your hero (by spending Power
Points),  this  booklet  is  filled  with  hundreds  of  sam

[... truncated ...]
```

**Chunk 64** (`cefb93c1d699`):

```
CHAPTER 2: SECRET ORIGINS

73

If  you  rolled  Mystic  Endowment  for  Abilities,  then  roll
1d20 once on the table below and record the result. Oth-
erwise, do not roll for Utility Powers.

1-4

5-8

9-12

17-20

Chi Sense: Senses 5 (Danger Sense; Detect Life—

Acute, Radius, Ranged) • 5 points

Meditation: Immunity 5 (choose five: aging, cold,
disease, heat, need for sleep, poison, starvation
and thirst, suffocation (suffocation counts as two
choices)), Sustained • 5 points

Perfect Serenity: Immunity 5 (interaction effects)

• 5 points

Weightless Step: Leaping 3 (60 ft.); Movement 1

(Trackless) • 5 points

DEFENSE

DODGE
+6

PARRY
+0

FORTITUDE
+6

TOUGHNESS
+0

WILL
+5

ABILITIES

POWERS

72

SKILLS

32/16*

0/20*

DEFENSES

17

150

29/25*

TOTAL

*If you rolled Mystic Endowment for Abilities.

•  Motivation—Recognition: The title of “best fighter

alive” is one that drives many Martial Artists.

•  Motivation—Thrills: The Martial Artist became a su-

perhero in order to seek excitement.

•

•

Honor: Some Martial Artists live by a warrior’s code
of honor or a life of ascetic discipline.

Rivalry: Martial Artists often have a nemesis or fated
rival against whom they measure themselves.

MIMIC

The Mimic copies the traits of others to use as his own. This
affords  him  immense  versatility,  limited  primarily  by  the
type and availability of his subjects. At the same time, the
Mimic usually has few other abilities upon which to rely.
ABILITIES

Roll 1d20 once and record the result.

1-8

9-12

Blank Slate: You are equally capable of pursuing
any path.

Metamind: Your great mental capacity allows you
to master anything.

13-20

Perfect Weapon: You are a weapon created
specifically to use your opponent’s powers against
them.

SLATE

STRENGTH
2
STAMINA
2

AGILITY
2
DEXTERITY
2

FIGHTING
2
INTELLECT
2

AWARENESS
2
PRESENCE
2

METAMIND

STRENGTH
1
STAMINA
1

AGILITY
1
DEXTERITY
1

FIGHTING
2
INTELLECT
8

AWARENESS
1
PRESENCE
1

WEAPON

STRENGTH
1
STAMINA
1

AGILITY
1
DEXTERITY
1

FIGHTING
8
INTELLECT
1

AWARENESS
2
PRESENCE
1

Roll  1d20  three  times  (re-roll  if  you  get  the  same  result
twice) and record the results.

1-4

Complementary: You are good at fitting in where
needed.

5-8

Discerning: You are good at sizing up people.

9-11

Engramatic: You’ve retained a little fragment of
everyone you’ve mimicked.

12-13

Innocent: You are naïve and pure.

14-16

Incisive: You know exactly which buttons to push.

17-18

Spontaneous: You don’t let yo

[... truncated ...]
```

**Chunk 65** (`cfadcb33d64b`):

```
CHAPTER 2: SECRET ORIGINS

85

POWERS

Roll 1d20 once and record the result.

1-3

Shapeshifter: Variable 9 (45 points, for assuming

different shapes), Move Action • 72 points

Size-Changer: Roll 1d20 once or choose Giant Size
or Shrinking. You may take the other power as an
Alternate Effect by reducing Giant Size’s Power-
lifting to only 1 rank and dropping the Impervious
extra from Shrinking’s Protection 1. Also, only take
the Flight Belt supplied by the Giant Size power.

11-20

Density Decrease: Insubstantial 4
(Incorporeal, affected by magic),
Reaction, Linked to Flight 1 (4 MPH),
Limited to air-walking, and Immunity
10 (Life Support), Quirk: immunity to
suffocation requires holding breath, and
Concealment 1 (Hearing), Continuous;
Disruption Attacks: Array (24 points),
Incorporeal Weapon (Affects Corporeal
Damage 12, Resisted by Fortitude,
Limited to the Toughness of object used
as weapon), AE: Disrupt Electronics
(Close Range Affects Corporeal Nullify 12
(electronics), Simultaneous), AE: Disrupt
Synapses (Affects Corporeal Affliction
12 (Resisted and Overcome by Fortitude;
Dazed, Stunned, Incapacitated); Innate
Understanding of Powers (Enhanced
Advantages 13 (Close Attack 6, Defensive
Roll 2, Hide in Plain Sight, Redirect, Set-up
2, Teamwork), Enhanced Skill -4 (Close
Combat: Unarmed -8) (Note: the Innate
Understanding of Powers abilities only
work when no powers are active or when
Density Decrease is active) • 72 points

14-16

17-20

Specific Shapeshifter: Variable 9 (45 points, for

assuming different shapes), Continuous, Limited
(Choose one type of entity you can turn into:
Animals, Machines, Humanoids, Aliens, etc.), Move
Action • 72 points

Stretcher: Strength-based Damage 6; Elongation 8
(1,800 feet); Enhanced Advantages 14 (Accurate
Attack, Chokehold, Close Attack 2, Evasion, Fast
Grab, Improved Grab, Improved Hold, Improved
Trip, Interpose, Power Attack, Precise Attack
(Close; Cover), Takedown 2); Enhanced Skill 4
(Close Combat: Grab +8); Impervious Toughness 8,
Limited—Physical Impact Damage; Insubstantial
1 (Liquid), Precise; Morph 2 (Humanoid Forms),
Distracting; Movement 6 (Environmental
Adaptation - Tight Spaces, Safe Fall, Slithering,
Sure-footed, Swinging, Wall-crawling); Protection 7;
Speed 3 (16 MPH) • 72 points

DEFENSE

DODGE
+6

PARRY
+6

FORTITUDE
+6

TOUGHNESS
+0

WILL
+6

ABILITIES

POWERS

32

72

6

SKILLS

DEFENSES

TOTAL

16

24

150

•

Fame:  Many  Shapeshifters  (especially  heroic  ones)
don’t worry about hiding their

[... truncated ...]
```

**Chunk 66** (`d329357e5091`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

GOLEM

STRENGTH
8
STAMINA
-

AGILITY
0
DEXTERITY
0

FIGHTING
6
INTELLECT
0

AWARENESS
4
PRESENCE
4

TECHNOLOGICAL

STRENGTH
8
STAMINA
-
UNDEAD

AGILITY
0
DEXTERITY
2

FIGHTING
6
INTELLECT
4

AWARENESS
1
PRESENCE
1

STRENGTH
6
STAMINA
-

AGILITY
2
DEXTERITY
3

FIGHTING
6
INTELLECT
1

AWARENESS
2
PRESENCE
2

Roll 1d20 once and record the result.

6-10

1-10

11-15

Brawler: You know how to use your strength to your
advantage.

Dabbler: You have some magical or technological
knowledge and can create useful devices or artifacts.

16-20

Perfect Recall: You have an uncanny memory.

BRUTE

Athletics 6, Intimidation 6

EXPERT

Perception 4, Choose One: Expertise: Magic 8 or Technology 8

SEEKER

Investigation 5, Perception 3, Persuasion 4

SNEAK

Deception 6, Stealth 6

POWERS

Find  the  entry  below  for  the  type  of  Construct  that
matches what you rolled for your Abilities.

GOLEM

Roll 1d20 once and record the result.

1-5

Blast: Ranged Damage 8, Accurate 6 • 22 points

Elemental Body: Enhanced Advantages 6 (Close

Attack 6); plus roll 1d20 once:

1-5

6-10

11-15

16-20

Damaging Aura: Reaction Damage 6

• 22 points

Gaseous Form: Flight 3 (16 MPH);

Insubstantial 2 (Gaseous) • 22 points

Liquid Form: Concealment 10 (All

Senses; Limited—In Liquid, Passive);
Insubstantial 1 (Liquid); Swimming 6
(30 MPH) • 22 points

Particulate Form: Elongation 2 (30
feet); Insubstantial 2 (Particulate);
Movement 2 (Permeate 2) • 22 points

BRAWLER

Improved Grab, Choose One: Power Attack or Accurate Attack

11-20

Unstoppable: Enhanced Strength 4; Enhanced Trait
2 (Close Attack 2); Immortality 5; Regeneration 2
• 22 points

DABBLER

Choose one set: Artificer, Skill Mastery (Expertise: Magic); or,
Inventor, Skill Mastery (Technology)

TECHNOLOGICAL

Roll 1d20 once and record the result.

RECALL

Eidetic Memory, Well-informed

SKILLS

Roll 1d20 twice (do not re-roll if you get the same result
twice) and record the results.

1-5

Brute: You’re big and intimidating.

6-10

Expert: You know a lot about magic or technology.

11-15

Seeker: You’re looking for clues to your origin or past.

16-20

Sneak: You’re stealthy.

1-4

Blast: Ranged Damage 9, Accurate 4 • 22 points

5-8

Retractable Claws and Combat Computer: Strength-
based Damage 2, Penetrating 6; Enhanced Traits
14 (All-out Attack, Close Attack 4, Diehard, Evasion,
Fast Grab, Improved Critical (Claws), Improved
Initiative 2, Precise Atta

[... truncated ...]
```

**Chunk 67** (`d5fc086574e9`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

LUCKY

Beginner’s Luck, Luck 2, Redirect

RESOURCES

Equipment 4 (Headquarters)

8-14

Super-strength: Enhanced Strength 4 • 8 points

15-20

Soldier: Enhanced Trait 4 (Close Attack 4); Power-

lifting 4 • 8 points

Headquarters—Size: Gargantuan, Toughness: 12; Features:
Communications, Computer, Gym, Infirmary, Isolated,
Laboratory, Library, Living Space, Personnel, Power System,
Security System, Teleport (Affects Others), Workshop • 20 points

WARRIOR

All-out Attack, Improved Initiative, Interpose, Move-by Action

Immunities: Immunity 10 (Life Support) • 10 points

Invulnerability: Protection 4 • 4 points

Roll 1d20 once and record the result.

WEALTHY

Benefit 4 (Multi-millionaire)

SKILLS

1-15

Flight: Flight 8 (500 MPH) • 16 points

16-20

Super Movement: Speed 3 (16 MPH); Leaping 7

(900 feet); Movement 3 (Swinging, Wall-crawling
2) • 16 points

Roll  1d20  twice  (re-roll  if  you  get  the  same  result  twice)
and record the results.

If you have the Superhuman or Vessel set of abilities, role
once on this table. Do not roll on this table otherwise.

1-5

Athlete: You’re a trained athlete.

6-10

Broad Training: You have a broad set of skills from
your education or experiences.

11-15

Charismatic: You’re good with people.

16-20

Learned: You’re well educated, with some
technological training.

ATHLETE

Acrobatics 6, Athletics 6, Perception 4

TRAINING

1-4

5-7

8-11

Improved Invulnerability: Impervious Toughness 6

• 6 points

Inhuman Physiology: Enhanced Advantage 1

(Diehard); Immunity 2 (Critical Hits); Regeneration 3
• 6 points

Enhanced Senses: Senses 6 (Extended Auditory
2, Extended Vision 2, Microscopic Vision, Ultra-
Hearing) • 6 points

12-15 Quickness: Quickness 6 • 6 points

16-18

Telepathy: Mental Communication 1, Subtle 2

• 6 points

19-20

Traveler: Movement 3 (Dimension Travel 3) • 6 points

Expertise: (Choose One) 4, Insight 2, Perception 2, Persuasion
4, Ranged Combat: Throwing 4

CHARISMATIC

Expertise: (Choose One) 4, Insight 4, Perception 4, Persuasion 4

DEFENSE

LEARNED

Expertise: (Choose One) 6, Perception 4, Technology 6

POWERS

DODGE
+4

PARRY
+4

FORTITUDE
+4

TOUGHNESS
+0

SUPERHUMAN/VESSEL

DODGE
+4

PARRY
+0

FORTITUDE
+2

TOUGHNESS
+0

WILL
+6

WILL
+6

If you have the Man of Action Abilities, don’t roll for your
Offensive Power, instead, take Find Weakness:

Find Weakness: Strength-based Damage 4; Enhanced

Advantage 4 (Close At

[... truncated ...]
```

**Chunk 68** (`da1c0758b454`):

```
CHAPTER 2: SECRET ORIGINS

51

NotesPowerpointsHeropointsGear & EquipmentMUTANTS & MASTERMINDS

PRINCESS

Julia wants to play a fairly straightforward hero: super-strong and tough, but also a beautiful
young woman with an eye for fashion! She draws a sketch of a smiling, slender woman in a

pink T-shirt that says “Princess” on it in silver sequins, holding a car over her head!

Right off, Julia knows Princess is strong, really strong. So she assigns her Strength 12;
higher than PL10, but still not so high that she can’t also have a reasonable close
combat bonus. That Strength is enough for Princess to lift a hundred tons! She

can heft that car with ease! Julia gives her Stamina 12 to match.

Since she sees Princess as graceful, like a gymnast, Julia gives her Agility
5, but she goes with Dexterity 3, since her character isn’t as coordinated
(although she’s still above average). Likewise, Julia assigns Princess 2 ranks
each  in  Intellect,  Awareness,  and  Presence;  she’s  smart,  sassy,  and  deter-
mined, but not amazingly so. Julia wants Princess to be a capable close-up
fighter, so she gives her Fighting 6. That’s a total of 44 ranks in abilities for 88

power points, leaving 62 remaining.

Next up: powers. Julia wants Princess to be fast and tough. She gives her 4 ranks of
Speed, allowing her to keep up with a slow-moving car, and assigns her 5 ranks in Im-
munity (allowing her to ignore cold, disease, heat, pressure, and radiation) along with some
Impervious Toughness (8 ranks) and Regeneration (2 ranks). That’s 19 points in powers,

43 remaining.

Given her great Strength and Agility, Julia also sees Princess as being able to jump re-
ally far, so she gives her 7 ranks in Leaping as well. That’s another 7 points, leaving 36.

Julia looks over the advantage list, taking notes as she goes. She likes the idea of
Princess being a real toughy: having things like Diehard and Ultimate Tough-
ness,  along  with  Interpose  (allowing  her  to  take  the  hit  for  a  teammate).
But she also wants her to be quick and inspirational. She likes Attractive,
Extraordinary  Effort,  Inspire,  and  Well-informed.  That’s  seven  advan-
tages thus far. She rounds out the list with some combat maneuvers
like All-out Attack and Power Attack (since Princess can cut loose if
she needs to), Improved Initiative (she’s quick) and another rank
of Inspire. That’s another four advantages, for a total of 11 points.

Julia  asks  the  Gamemaster  about  one  more  advantage: 

[... truncated ...]
```

**Chunk 69** (`db8b2bdf371a`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Energy Blast: Ranged Damage 12

Take the Gimmick Blaster and Energy Blast
(above), plus roll 1d20 three times (re-roll if you
get the same result twice) and add them to the
Gimmick Blaster array as Alternate Effects. Name
each of these Alternate Effects as appropriate for
your character’s gimmick.

1-3

4-5

6-8

9-11

12-14

Create 7, Continuous, Innate

Move Object 12

Ranged Affliction 12 (Resisted and
Overcome by Fortitude; Dazed,
Stunned, Incapacitated)

Ranged Affliction 12 (Resisted by
Dodge, Overcome by Damage;
Vulnerable, Defenseless,
Incapacitated)

Ranged Cloud Area Affliction 8

(Resisted and Overcome by Fortitude;
Dazed and Visually Impaired,
Stunned and Visually Disabled) Extra
Condition, Limited Degree

15-17

Ranged Burst Area Damage 8

18-20

Close Cone Area Damage 8, Penetrating 8

Personal Combat Enhancers: Enhanced Advantage

11 (All-out Attack, Defensive Attack, Evasion,
Extraordinary Effort, Diehard, Fearless, Great
Endurance, Improved Critical (Unarmed),
Improved Initiative, Takedown 2); Enhanced
Strength 3; Enhanced Trait 5 (Close Attack 5);
Activation—Move Action (-1 point), Removable
(-4 points) • 17 points

8-12

13-14

15-16

Physical Boosters: Enhanced Strength 8; Leaping

2 (30 feet); Quickness 2; Speed 2 (8 MPH);
Activation—Move Action (-1 point), Removable
(-4 points) • 17 point

17-20

High-tech Arsenal: Ray Gun (Ranged Damage 12,
AE: Power Truncheon (Strength-based Damage
8), AE: Stunner (Ranged Affliction 12 (Resisted
and Overcome by Fortitude; Dazed, Stunned,
Incapacitated)), AE: Force Capsule Grenade
(Ranged Affliction 12 (Resisted by Dodge,
Overcome by Damage; Hindered and Vulnerable,
Defenseless and Immobile), Extra Condition,
Limited Degree); Easily Removable (-10 points)
• 17 points

Roll 1d20 once and record the result.

1-5

6-10

Combat Training and Armored Costume:
Enhanced Advantage 2 (Defensive Roll 2),
Enhanced Defenses (Dodge 4, Parry 4), Protection
4, Removable (-1 point) • 13 points

Displacer Field: Enhanced Defenses (Dodge 6, Parry
6) Linked to Protection 4, Sustained, Removable
(-3 points) • 13 points

11-15

Energy-Absorbing Body Suit: Protection 10,

Impervious 6, Removable (-3 points) • 13 points

16-20

Force Field: Immunity 6 (Critical Hits, Cold, Heat,

High Pressure, Radiation) Linked to Protection 10,
Sustained, Removable (-3 points) • 13 points

Roll 1d20 once and record the result.

1-4

5-8

9-16

17-20

Biologica

[... truncated ...]
```

**Chunk 70** (`dcdc4c459ab6`):

```
CHAPTER 2: SECRET ORIGINS

61

CRIMINOLOGIST

EXPERT

Assessment, Skill Mastery (Expertise: Streetwise)

Perception 6, Technology 8, Treatment 6

SCIENTIST

INVESTIGATOR

Inventor, Skill Mastery (Technology)

Expertise: Streetwise 4, Insight 5, Investigation 6, Perception 5

SLEUTH

SNEAK

Skill Mastery (Investigation), Tracking

Deception 6, Sleight of Hand 6, Stealth 8

POWERS/EQUIPMENT

Roll 1d20 once and record the result. If you rolled the In-
ventor set of Abilities, take Gadgets instead of rolling.

Roll 1d20 once and record the result.

1-10

Acrobat: You’re a trained acrobat, capable of
incredible feats of agility.

11-15 Martial Artist: You’re a trained fighter.

16-20

Thief: You’re a trained thief, able to disappear with a
moment’s notice.

ACROBAT

Evasion, Instant Up

1-4

ARTIST

Defensive Attack, Uncanny Dodge

THIEF

Hide in Plain Sight, Skill Mastery (Stealth)

SKILLS

Close Combat: Unarmed 6

Take the skill listed above, then if you rolled Dark Aveng-
er  for  your  Abilities,  take  Avenger  and  roll  once,  re-roll
if  you  get  Avenger  again.  If  you  rolled  the  Detective
for  your  Abilities,  take  Investigator  and  roll  once,  re-roll
if  you  get  Investigator  again.  If  you  rolled  Inventor  for
your Abilities, take Expert and roll once, re-roll if you get
Expert again.

1-4

Athlete: You’re physically capable and impressive.

5-8

Avenger: You’ve trained yourself in a number of
useful skills.

5-10

6-10

9-12

Expert: You know a lot about some subjects.

13-16

Investigator: You’ve studied investigation and other
forms of observation.

17-20

Sneak: You’re stealthy.

ATHLETE

Acrobatics 6, Athletics 8, Intimidation 6

AVENGER

Expertise: Streetwise 6, Intimidation 8, Vehicles 6

11-15

16-20

Advantage: Equipment 10 (Equipment listed
immediately below)
Smartphone • 2 points
Headquarters—Size: Medium, Toughness: 8;
Features: Communications, Computer, Concealed,
Garage, Gym, Living Space, Power System, Security
System • 10 points

Motorcycle: Medium; Str 1; Speed 6; Defense 10;

Toughness 8 • 10 points

Knife: Strength-based Damage 1, Improved Critical

• 2 points

Customized Heavy Pistol with Laser Sight:
Ranged Damage 4, Accurate 2 • 10 points

Customized Assault Rifle: Ranged Multiattack

Damage 5, Accurate • 16 points

GADGETS

Advantage: Equipment 3 (Headquarters)
Headquarters—Size: Large, Toughness: 10;
Features: Communications, Computer, Concealed,
Fire Prevention System, Gym, Infirmary, Laboratory,
Living Space,

[... truncated ...]
```

**Chunk 71** (`dd5713402cfd`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PL 7

STR
STA

8  AGL
8  DEX

0
0

FGT
INT

6  AWE
PRE
0

0
2

Powers: Foot Stomp (Line Area Damage 7,
Limited—Must be on same surface as target);
Super-Movement (Leaping 6 (500 feet));
Super-Tough (Immunity 10 (Life Support),
Impervious Toughness 4)

14-20

Advantages: Accurate Attack, All-out Attack,
Diehard, Fast Grab, Set-up 2, Takedown,
Teamwork

Skills: Athletics 3 (+11), Intimidation 4 (+6),
Perception 5 (+5)

Offense: Init +0, Unarmed +6 (Close, Damage 8)

Defense: Dodge 6, Parry 6, Fort 8, Tou 8, Will 6

Totals: Abilities 48 + Powers 26 + Advantages 8
+ Skills 6 + Defenses 12 = 100

SUMMONER

Roll 1d20 once on this table if you have the Summoner set
of Abilities and record the result.

15-20

Equipment: Bow (Ranged Damage 3),
Club (Strength-based Damage 2), Knife
(Strength-based Damage 1, Improved
Critical), Nunchaku (Strength-based
Damage 2, Improved Critical), Shuriken
(Ranged Multiattack Damage 1), Sword
(Strength-based Damage 3, Improved
Critical)

Advantages: Equipment 4, Evasion, Hide
in Plain Sight, Quick Draw

Skills: Acrobatics 6 (+10), Athletics 6 (+8),
Perception 3 (+5), Ranged Combat (Ninja
Weapons) 3 (+7), Sleight of Hand 4 (+8),
Stealth 10 (+14)

Offense: Init +4, Bow +7 (Ranged, Damage
3), Sword +7 (Close, Damage 5, Crit. 19-20),
Unarmed +7 (Close, Damage 2)

Defense: Dodge 10, Parry 10, Fort 6, Tou
2, Will 6

Totals: Abilities 42 + Powers 8 + Advantages
7 + Skills 16 + Defenses 17 = 90

ROBOTS

PL 6

8  AGL

STR
STA  —  DEX  0

2  FGT

2  AWE

0
INT  —  PRE  —

Imaginary Friend: Summon 10 (One PL10,

150-point character; Choose or roll up another
character using the tables in this book and use
that as your summoned creature. Note: the
summoned creature may not have minions, a
headquarters, or any other traits the GM decides
are outside the scope of the Summon power),
Controlled, Heroic, Mental Link • 51 points

Roll 1d20 once and record the result. (Only roll on
this table if you Summon the Imaginary Friend.)

1-4

5-8

Invisibility: Concealment 10 (All
senses), Blending • 10 points

Lucky: Luck Control 2 (Force a re-roll,
Negate luck), Luck 4 • 10 points

9-12

Mimic: Variable 2 (10 points),

Limited—Can only mimic a trait of
Imaginary Friend, Increased Action
(Standard), Tiring • 10 points

13-16

Shapechange: Morph 2 (Humanoids)

• 10 points

17-20

Projections: Create 5 • 10 points

Summon Animals: Summon 4 (Sixteen PL4,

60-point minions; You can s

[... truncated ...]
```

**Chunk 72** (`e05fc680a484`):

```
CHAPTER 2: SECRET ORIGINS

33

The following archetypes are ready to play for a power level 10 series. Some require a few simple choices or offer options
for customization. Gamemasters can also use these archetypes as ready-made villains, if desired.

The Gadgeteer and Martial Artist rely a great deal on their
advantages (as do other archetypes like the Crime Fighter
and Weapon Master). You’ll want to read the descriptions
of all of the character’s advantages from the Advantages
chapter so you know the benefits they provide. Remem-
ber to make use of them during play to give your charac-
ter every appropriate, well, advantage.

In particular, note how some advantages and even pow-
ers work together. The Gadgeteer can use Quick-Thinking
to speed up the process of inventing (see Inventing, page
211) and Skill Mastery (Technology) to make some invent-
ing  checks  as  routine.  Similarly,  note  the  Martial  Artist’s
Power Attack advantage, good for doing extra damage to
slow, tough, opponents, and the Skill Mastery (Acrobatics)
advantage  for  pulling  off  formidable  (DC  25)  Acrobatics
checks as routine!

The  Mimic  and  Mystic  archetypes  are  both  very  flexible,
although in different ways, and it pays to know what your
character is capable of doing before you are immersed in
the midst of a game.

In the case of the Mimic, the GM may wish to put together
note cards or some other quick reference to the powers of
other characters whom the Mimic might wish to duplicate.
That way, you can see at a glance what traits the character
can copy, and simply hand the card to the player for refer-
ence.  Experienced  Mimics  may  even  build  up  a “hand”  of
such cards they reference often.

For  the  Mystic,  in  addition  to  choosing  your  charac-
ter’s  five  set  Alternate  Effects  (see  Alternate  Effect  on
page  188),  read  the  Magic  sample  power  on  page  168
of the Powers chapter and give some thought to power
stunts your character can do; spur of the moment spells
whipped up to fit a particular need. Mytics are very effec-
tive at power stunts and you might want to reserve a hero
point (or two) for that purpose.

The  Paragon  and  Powerhouse  are  among  the  strongest
archetypes,  able  to  lift  and  carry  a  lot  of  weight.  Just  to
give you an idea, the Paragon can lift a loaded 747 aircraft,
whereas the Powerhouse can lift four times that amount.
Both can easily smash through stone or bend steel.

Both archetypes are pretty tough, to

[... truncated ...]
```

**Chunk 73** (`e087f7a0b70b`):

```
CHAPTER 2: SECRET ORIGINS

57

Take  the  Weapon  Array  and  the  Plasma  Blast  (above),
plus roll 1d20 four times on the table below (re-roll if you
get the same result twice) and add them to the Weapon
Array as Alternate Effects.

1-2

•  Electrified Shell: Reaction Damage 6 • 1 point

3-4

5-7

8-9

10-12

13-15

16-18

19-20

•  Electro-Stunner: Ranged Affliction 10 (Resisted
by Dodge and Overcome by Fortitude; Dazed,
Stunned, Incapacitated), Accurate 4 • 1 point

•  Plasma Bolts: Ranged Multiattack Damage 6,

Accurate 6 • 1 point

•  Force Capsule: Ranged Affliction 10 (Resisted

by Dodge and Overcome by Damage; Hindered
and Vulnerable, Defenseless and Immobile), Extra
Condition, Limited Degree, Accurate 4 • 1 point

•  Micro Rockets: Ranged Burst Area Damage 8

• 1 point

•  Omni-Blaster: Cone Area Damage 10,

Penetrating 4 • 1 point

•  Strength and Accuracy Booster: Enhanced
Strength 8; Enhanced Trait 6 (Close Attack 6)
• 1 point

•  Tractor/Presser Beam: Move Object 10,

Accurate 4 • 1 point

Ability Amplifier: Enhanced Defenses 16 (Dodge 4,

Fortitude 4, Parry 4, Will 4), Removable (-3 points) • 13 points

Armored Shell: Impervious Protection 8, Removable (-3

points) • 13 points

Sealed Systems: Immunity 10 (Life Support), Removable (-2

points) • 8 points

Roll 1d20 once and record the result.

1-7

8-10

Gravity Drivers: Flight 7 (250 MPH), Removable

(-3 points) • 11 points

•  Space Flight: Movement 2 (Environment

Adaptation—Zero-G , Space Travel 1) • 1 point

Locomotion Systems: Speed 7 (250 MPH); Leaping
4 (120 feet); Movement 2 (Choose two: Safe Fall,
Swinging, Wall-crawling 1, a second rank of
Wall-crawling), Removable (-3 points) • 12 points

Rocket Turbines: Flight 7 (250 MPH), Removable

(-3 points) • 11 points

11-17

•  Aquatic Turbines: Swimming 8 (120 MPH);

Movement 1 (Environment Adaptation—Aquatic)
• 1 point

18-20

Teleport-Tech: Teleport 3 (250 feet), Easy, Extended
(8 miles), Change Direction, Change Velocity,
Turnabout, Removable (-3 points) • 12 points

Communication Systems: Radio Communication 2,

Removable (-2 points) • 6 points

Sensors: Senses 2 (Extended Vision, Infravision), Removable

(-0 points) • 2 points

DEFENSES

DODGE
+4

PARRY
+2

FORTITUDE
+2

TOUGHNESS
+0

WILL
+4

ABILITIES

POWERS

36

76

10

SKILLS

DEFENSES

TOTAL

16

12

150

•

Identity: The Battlesuit often has a secret identity he
or she tries to protect.

•  Motivation—Responsibility:  Whether  an  inventor
of  military  weapons,  a  trained 

[... truncated ...]
```

**Chunk 74** (`e17d1554782d`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Dense Fog: Visual (All) Concealment 4 Attack, Burst

1-8

Arc Riding: Leaping 10 • 10 points

Weather Control array as Dynamic Alternate Effects (re-
roll if you get the same result twice).

Arctic Freeze: Ranged Cumulative Affliction 10
(Resisted by Dodge, Overcome by Damage;
Hindered and Vulnerable, Defenseless and
Immobile), Extra Condition, Limited Degree
• 30 points

Dazzling Strike: Ranged Cumulative Affliction 10

(Resisted and Overcome by Fortitude; Vision and
Auditory Impaired, Vision and Auditory Disabled,
Vision and Auditory Unaware) • 30 points

Area (×3), Selective • 28 points

Downdraft: Ranged Affliction 10 (Resisted and

Overcome by Strength; Hindered and Impaired,
Stunned and Prone, Incapacitated), Alternate
Resistance (Strength), Concentration Duration,
Extra Condition, Instant Recovery • 30 points

Glacier: Create 9, Continuous, Innate, Linked to
Environment 2 (Cold, Impede Movement 1)
• 30 points

Hailstorm: Ranged Cloud Area Damage 9, Indirect 2

(falling from above) • 30 points

Lightning Bolt: Ranged Damage 12, Accurate 3,
Indirect 3 (any point downwards) • 30 points

Stormy Weather: Environment 10 (2 miles; Cold,

Impede Movement, Visibility) • 30 points

Tornado: Cylinder Area Move Object 10,

Concentration Duration, Damaging • 30 points

Wind Screen: Deflect 10, Cylinder Area (×3), Limited

to Attacks Targeting Dodge • 30 points

1-2

3-4

5-6

7-8

9-10

11-12

13-14

15-16

17-18

19-20

Roll 1d20 once and record the result.

1-5

Aquatic: Immunity 3 (Cold, Drowning, Pressure),
Senses 5 (Darkvision, Accurate and Extended
Hearing); Swimming 2 (2 MPH), Stacks with other
Swimming • 10 points

6-10

Cold Immunity: Immunity 10 (Cold effects) • 10 points

11-20

Weather-Proof: Immunity 10 (Weather effects)

• 10 points

Roll 1d20 once and record the result.

1-7

8-14

15-20

Force Field: Impervious Protection 8, Sustained

• 16 points

Vigorous: Enhanced Stamina 3; Enhanced Defenses

10 (Dodge 5, Parry 5), Sustained • 16 points

Wind Shield: Enhanced Defenses 16 (Dodge 8, Parry

8), Sustained • 16 points

Roll 1d20 once and record the result.

Swimming: Movement 1 (Environmental

9-12

Adaptation—Aquatic); Swimming 8 (120 MPH),
Stacks with other Swimming • 10 points

13-20 Wind Riding: Flight 5 (60 MPH) • 10 points

DEFENSE

DODGE
+2

PARRY
+0

FORTITUDE
+4

TOUGHNESS
+0

WILL
+6

ABILITIES

POWERS

40

75

7

SKILLS

DEFENSES

TOTAL

16

12

150

•  Moti

[... truncated ...]
```

**Chunk 75** (`e53b2f1b3ca2`):

```
CHAPTER 2: SECRET ORIGINS

39

Power Point Totals:  Abilities 48 + Powers 42  + Advantages 16 + Skills  22 + Defenses 22  = 150

PL10PL10

STRENGTH
4
STAMINA
3

AGILITY
6
DEXTERITY
4

FIGHTING
13
INTELLECT
0

AWARENESS
5
PRESENCE
0

Accurate Attack, Agile Feint, All-out Attack, Assessment, Chokehold,
Daze (Intimidation), Defensive Attack, Defensive Roll 4, Evasion,
Improved Critical (Unarmed), Improved Defense, Improved
Disarm, Improved Grab, Improved Initiative, Improved Smash,
Improved Trip, Instant Up, Move-by Action, Power Attack, Precise
Attack (Close, Concealment), Prone Fighting, Redirect, Seize
Initiative, Skill Mastery (Acrobatics), Takedown, Trance, Uncanny
Dodge, Weapon Break

SKILLS

Acrobatics 10 (+16), Athletics 10 (+14), Close Combat:
Unarmed 3 (+16), Expertise: Philosophy 5 (+5), Insight 8 (+13),
Intimidation 8 (+8), Perception 8 (+13), Stealth 8 (+14)

OFFENSE

INITIATIVE +10

Unarmed +16

Close, Damage 4, Crit. 19-20

DEFENSE

DODGE

PARRY

WILL

13

13

9

FORTITUDE

TOUGHNESS

11

7/3*

*Without Defensive Roll

Power Point Totals:  Abilities 70 + Powers 0  + Advantages 31 + Skills  30 + Defenses 19  = 150

40

```

**Chunk 76** (`e5eb32b8480c`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

something else that looks more interesting). This method
combines  the  best  of  the  two  options  above  because  it
limits your choices, but also allows you to control, to some
extent, what you get.

Important note: No matter which option you use when
creating  a  character,  feel  free  to  alter  the  results  of  your
rolls to make sure you get a character you find interesting.
This is not cheating! Simply because these tables are in this
book doesn’t make them “rules” that you have to “follow.”
Instead, consider them play aids with guidelines to make
it easier to create your character…because that’s exactly
what they are.

Every superhero has challenges that make his or her life
more…interesting. Just like the characters in the comics,
your  hero  needs  at least  two  Complications;  one  should
be  a  Motivation  and  the  other  (or  others)  is  up  to  you.
Each Archetype lists a number of suggestions appropriate
for that Archetype. This is your hero, so take the Compli-
cations  that  make  the  most  sense  to  you.  If  none  of  the
suggestions work for you, there are more Complications
to choose from in Chapter 2.

Once you have your character’s various traits and Compli-
cations determined and on paper, you’re ready to play! Your
character should be appropriate for a Power Level 10 (PL10)
game, so you can start playing right away without changes.

It’s  possible,  however,  that  you  have  an  advantage  that
doesn’t mesh correctly with your skills. For example, you
might get the Daze (Intimidation), Skill Mastery (Technol-
ogy),  or  Assessment  advantages,  each  of  which  requires
a  specific  skill  to  work  correctly:  Intimidation,  Technol-
ogy, and Insight, respectively. If that’s the case, feel free to
choose a different advantage, or if you like the effect the
advantage gives you, swap one of your skills for the one
you need. Instances in which this is a problem should be
rare, but they can happen.

Another aspect of “pulling it all together” is making sure
the character is interesting to you. Do this by customizing
your character a bit, if necessary. This is your hero, after all!
Gamemaster, you should work with your players to swap
around a few points’ worth of Abilities, Advantages, Skills,
and/or  Powers  so  they  end  up  with  a  character  more  to
their liking. Usually, this process is as simple as replacing
ranks  of  one  effect  for  

[... truncated ...]
```

**Chunk 77** (`eab98ce0e1fc`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Hero: ____________________________________     Player: ____________________________

The Rook

Jon

Gender: _____________     Age: ________    Height: ____________     Weight: _____________     Eyes: ___________________     Hair: _____________________

Male

31

6’0”

Identity: _______________________________________________  (cid:80)(cid:3)Secret (cid:80)(cid:3)Public
Jack Cooper      X
Blue

195 lbs

Brown

Group Affiliation: ________________________________     Base of Operations: ______________________________________     Power Level: ________

None

26  150
Power Point Totals: Abilities _________+ Powers _________+ Advantages _________+ Skills _________+ Defenses _________= ___________

68

8

Emerald City
19
29

Strength

Stamina

3
3

Agility

Dexterity

5
5

Fighting

Intellect

8
5

Awareness

Presence

2
3

Offense

Initiative

+5

Unarmed

+15  Close, Damage 3

Fighting Staff  +15  Close, Damage 5, Reach 1

Rook’s Talons  +15  Ranged, Damage 5

Defense

Dodge (agl)

Parry (FGT)

Fortitude (STA)

Toughness (STA)

Will (awe)

14
14
8
6
/
3*
8

*Without Defensive Roll.

Benefit 4 (Multi-
millionaire), Defensive Roll
3, Equipment 6, Inventor, Jack-of-all-
trades, Move-by Action, Power Attack,
Quick Draw, Well-informed

Advantages

Skills

Acrobatics 5 (+10), Athletics 5
(+8), Close Combat: Unarmed 7
(+15), Intimidation 6 (+9), Investigation 1
(+6), Perception 6 (+8), Ranged Combat:
Throwing 10 (+15), Sleight of Hand 3
(+8), Stealth 8 (+13), Technology 5
(+10), Treatment 1 (+6), Vehicles 1 (+6)

Fall), Removable (–2 points) • 6 points

• Flash Bombs: Ranged Burst Area Affliction 3 (Resisted by Fortitude; Vision

Powers & Devices
____________________________________________________________________________________________________________________________________________
Cowl: Senses 3 (Extended Vision, Low-Light Vision, Radio), Removable (–1 point) • 2 points
____________________________________________________________________________________________________________________________________________
Wings of the Rook: Flight 5 (60 MPH), Subtle (sound baffling), Wings; Movement 1 (Safe
____________________________________________________________________________________________________________________________________________
Flashlight: Feature 1 (Illumination) • 1 point      Mini-Tracers: Feature 1 (Tracking) • 1 point
___________________________________________________________

[... truncated ...]
```

**Chunk 78** (`ebf52e380812`):

```
CHAPTER 2: SECRET ORIGINS

0
1

53

NotesPowerpointsHeropointsGear & EquipmentMUTANTS & MASTERMINDS

The  MUTANTS  &  MASTERMINDS  Quickstart  Character  Gen-
erator found on the following pages first appeared as a
booklet  included  with  the  M&M  Gamemaster’s  Kit.  Our
goal in creating it was to make it easier for new players
and  Gamemasters  to  create  characters.  It  proved  very
popular and when we had the chance, we offered up the
idea  of  including  an  updated  version  of  it  in  the  Hero’s
Handbook to the fans and their response was a resound-
ing, “Yes!”

This updated version of the Quickstart Character Genera-
tor includes clearer instructions, some new powers and
options for some of the archetypes, and fixes to a couple
of the archetypes to make sure they didn’t break any of
the rules.

HEROES

The  character  generator  allows  players  to  quickly  create
power level 10 starting characters. Using these tables, new
players can start playing their new hero in mere minutes.
All they need to do is roll a d20 to find out what Archetype
they  get,  then  roll  on  the  tables  for  that  Archetype  and
write  everything  down  on  a  character  sheet  or  piece  of
paper and they’re set!

Sure, this method removes a lot of choice from the pro-
cess,  but  that  speeds  up  character  creation,  since  the
player doesn’t have to make every single decision along
the way (or even know the rules!). It can also provide some
much-needed inspiration to a player who doesn’t have a
strong idea for a new hero. Experienced players may not
need to randomly generate characters, but they may still
want to. The results from the random tables can be inter-
esting in ways a carefully conceived and planned charac-
ter is not.

Finally,  the  Gamemaster  can  use  these  tables  to  quickly
come up with a villain or NPC hero. Randomly roll a char-
acter or pick the Archetype and powers that best fit the
needs  of  the  story  and  within  moments  the  character  is
ready to go!

No  matter  how  Gamemasters  and  players  end  up  using
the Quickstart Character Generator, it should make starting
a game easier, faster, and more fun.

There are a few different ways to use the character gen-
erator.  Gamemasters  and  players  should  agree  on  the
method  they’re  using  before  beginning,  and  work  with
each  other  during  the  process  to  make  sure  the  end  re-
sult is agreeable. After all, you’re here to have fun, so your
main goal should be to ma

[... truncated ...]
```

**Chunk 79** (`f877c8ee4307`):

```
CHAPTER 2: SECRET ORIGINS

31

Consider  the  effects  of  age  on  your  hero.  Someone  who
fought  in  the  Second World War  is  likely  to  have  a  differ-
ent worldview than a modern teenager who just acquired
super-powers, to say nothing of an immortal who has seen
civilizations rise and fall or a godlike being from the dawn of
time. A character’s age may influence the choice of certain
traits. Aged characters are likely to have lower physical abil-
ity ranks, for example, while younger ones may have fewer
skill ranks (having had less time to train in various skills).

What  does  your  hero  look  like?  Consider  things  like  the
character’s  race,  sex,  ethnicity,  and  other  factors  in  ap-
pearance.  Is  the  hero  even  human?  Superheroes  can  be
aliens,  robots,  androids,  spirits,  and  beings  of  pure  en-
ergy.  Is  the  character  short  or  tall? What  about  hair  and
eye color? Does the hero have any distinguishing marks
or unique features; is his appearance unusual in any way
(apart from running around in a costume, that is)? Does
the  hero  qualify  for  the  Attractive  advantage?  (See  the
Advantages  chapter  for  details.)  What  about  complica-
tions stemming from the hero’s looks?
COSTUME

A costume is a big part of a superhero’s appearance. Like
code  names,  most  heroes  have  a  distinctive  costume,
usually  something  skin-tight  and  colorful,  often  embla-
zoned  with  a  symbol  or  logo.  Other  heroes  wear  more
military-style outfits, fatigues or body armor with numer-
ous bandoliers and belts. A suit of armor may serve as the
hero’s costume: anything from ancient mail to a high-tech

battlesuit. A few heroes don’t wear a special costume, just
ordinary street clothes (which in itself can be pretty dis-
tinctive among a group of spandex-clad heroes).

In the comics, costumes are generally immune to the kind
of  routine  wear-and-tear  a  hero’s  powers  should  inflict
on them. For example, heroes who can burst into flames
don’t usually incinerate their clothing. The same is true for
heroes who change their size or shape. Although a hero’s
costume can be damaged or torn by attacks and other cir-
cumstances, it’s usually immune to the hero’s powers. This
doesn’t cost any points; it’s just the way costumes work.
For more on costumes as equipment, see the Gadgets &
Gear chapter.

Although heroes spend a lot of time fighting crime and us-
ing their powers to help others, most also try to find time
to have li

[... truncated ...]
```

**Chunk 80** (`f8e903dbf3d7`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

*If you rolled Vampire for Abilities, then you have Abilities
44, Powers 73, and Defenses 17; otherwise, you have Abili-
ties 62, Powers 52, and Defenses 20.

•  Motivation—Acceptance:  The  Supernatural  Crea-

ture is usually an outcast.

•  Motivation—Doing  Good:  Some  Supernatural
Creatures  attempt  to  go  against  the  grain  and  use
their powers for good.

•

•

•

Power Loss: Some Supernatural Creatures only have
their powers at night, or lose their powers when on
holy  ground  or  when  they  assume  human  form...  if
they have one.

Quirk—Angst:  The  Supernatural  Creature  often
feels great anguish over its lost humanity.

Reputation:  Most  humans  regard  Supernatural
Creatures with fear and hatred as a result of folklore
and myth.

•  Weakness:  Supernatural  Creatures  may  be  vulner-
able to holy weapons. Others may be unable to func-
tion in sunlight.

TOTEM

AVIAN

STRENGTH
4
STAMINA
6

AGILITY
8
DEXTERITY
4
CARNIVORAN

STRENGTH
7
STAMINA
6

AGILITY
5
DEXTERITY
2
PACHYDERM

STRENGTH
12
STAMINA
7
REPTILE

AGILITY
2
DEXTERITY
2

FIGHTING
8
INTELLECT
0

AWARENESS
4
PRESENCE
0

FIGHTING
10
INTELLECT
0

AWARENESS
3
PRESENCE
1

FIGHTING
5
INTELLECT
0

AWARENESS
3
PRESENCE
3

The Totem is a superhero whose powers are closely tied to
a particular animal. The Totem may have acquired its pow-
ers  through  an  accident  of  science,  an  invocation  of  the
animal spirits, or may even be an exceptional, self-aware
animal. Totem heroes tend to be as varied as the animals
they represent, and they can resemble other archetypes
such as the Martial Artist, Warrior, and Powerhouse.
ABILITIES

STRENGTH
10
STAMINA
8

AGILITY
4
DEXTERITY
3

FIGHTING
6
INTELLECT
1

AWARENESS
2
PRESENCE
0

Roll 1d20 once and record the result

Roll  on  both  the  Behavioral  Advantages  table  and  the
Social Advantages table.

1-4

Arthropod: Your totem is a spider, scorpion, wasp,
or even an insect swarm.

5-8

Avian: Your totem is a bird like a falcon or owl.

9-14

15-17

18-20

Carnivoran: Your totem is a carnivore from the
canine, lupine, or feline family.

Pachyderm: Your totem is a massive, thick-hided
mammal, such as an elephant or rhinoceros.

Reptile: Your totem is a reptile, such as a crocodile,
lizard, or snake.

ARTHROPOD

Roll 1d20 once and record the result.

1-4

5-8

9-12

Active: You are in constant motion.

Catch and Hold: You like to grab hold of your prey.

Mystic: Yo

[... truncated ...]
```

**Chunk 81** (`f97fb5b16662`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PL10PL10

PARAGON
PARAGON

STRENGTH
12
STAMINA
12

POWERS

AGILITY
3
DEXTERITY
1

FIGHTING
8
INTELLECT
0

AWARENESS
1
PRESENCE
1

Flight: Flight 9 (1,000 MPH)• 18 points.

Invulnerability: Enhanced Stamina 10,

Immunity 10 (Life Support), Impervious
Toughness 12 • 42 points.

Super-Speed: Quickness 2 • 2 points.

Super-Strength: Enhanced Strength 10, plus
Enhanced Strength 2, Limited to Lifting
(Lifting Str 14; 400 tons)
• 22 points.

Power Attack

SKILLS

Expertise: (Choose One) 7 (+7), Insight 6 (+7),
Perception 8 (+9), Persuasion 6 (+7), Ranged
Combat: Throwing 7 (+8)

OFFENSE

INITIATIVE +3

Throw +8

Ranged, Damage 12

Unarmed +8

Close, Damage 12

DEFENSE

DODGE

PARRY

WILL

FORTITUDE

TOUGHNESS

12

12

8

8

8

```

**Chunk 82** (`fd5ed2485118`):

```
CHAPTER 2: SECRET ORIGINS

103

1-4

Adapted: You learned to brave the elements.

5-8

9-12

Divine: Your powers reflect those of an ancient
storm god.

Facilitator: You are good at using your power to
help out others.

13-16

Raging: You are as tempestuous as the storms you
control.

17-20

Sovereign: You are regarded as royalty by your people.

Take the skill listed above, then roll 1d20 once and record
the result.

1-5

Attuned: You’re sensitive to your surroundings.

6-10

Organic: You understand how nature works.

11-15

Sneak: You have a shady past.

16-20

Spirited: You are full of energy.

ATTUNED

ADAPTED

Expertise: (Choose One) 8, Insight 8, Perception 8

Favored Environment (Choose One), Great Endurance

ORGANIC

DIVINE

Extraordinary Effort, Ritualist

Expertise: Biology 8, Perception 4, Persuasion 8, Treatment 4

SNEAK

FACILITATOR

Deception 4, Expertise: Streetwise 4, Sleight of Hand 8, Stealth 8

Set-up, Teamwork

RAGING

Daze (Intimidation), Power Attack

SOVEREIGN

Benefit (Status), Connected

SKILLS

Expertise: (Choose One) 8

SPIRITED

Acrobatics 8, Athletics 8, Intimidation 8

POWERS

Weather Control: Array (30 points, Dynamic plus 4 Dynamic

Alternate Effects) • 39 points

Roll 1d20 five times and record the first result as the first
(Dynamic)  power  in  the  array  and  add  the  rest  to  the

104

```

**Chunk 83** (`ffc525f7d497`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

11-14

Rapid Fire: Selective Ranged Multiattack Damage 4,

Accurate 4 • 20 points

15-18

Sonic Boom: Burst Area Damage 10 • 20 points

19-20

Vertigo Attack: Cumulative Affliction 9 (Resisted
and Overcome by Fortitude; Dazed, Stunned,
Incapacitated), Accurate 2 • 20 points

Roll  1d20  once  and  add  the  power  to  the  Speedster
Stunts array as an Alternate Effect

1-4

5-6

Air Control: Cone Area Move Object 10, Close

Range • 1 point

Anchor: Simultaneous Nullify Movement Effects 10

• 1 point

7-8

Phase Shift: Insubstantial 4 • 1 point

9-10

11-20

Temporal/Dimensional Duplicate: Summon
Duplicate 10, Active, Feedback • 1 point

Roll on the table above instead (re-roll if you get

the same result as earlier) • 1 point

Roll 1d20 once and record the result.

Bullet: Enhanced Defenses 12 (Dodge 6, Parry 6);

Protection 8, Impervious • 28 points

Hard Target: Enhanced Advantages 6 (Defensive

Roll 3, Improved Initiative 3), Enhanced Defenses
22 (Dodge 11, Parry 11) • 28 points

Natural Selection: Enhanced Agility 2, Enhanced
Stamina 2, Enhanced Defenses 20 (Dodge 10,
Parry 10) • 28 points

1-4

5-12

13-16

17-20

SUMMONER

The Summoner is an archetype that covers a lot of ground,
from heroes who create duplicates of themselves to those
who animate images, summon otherworldly creatures, or
create minions out of thin air. In order to make the Sum-
moner fit into this book, these tables produce a duplicator
(who  summons  duplicates  of  him-  or  herself )  or  a  sum-
moner whose summoned creatures are minions with de-
cent combat abilities.

There are a few options for the duplicator: a Martial Artist,
and Energy Controller, and a Powerhouse. These are only
examples of the sorts of duplicators you can use and you
are free to swap points around to change your duplicating
Martial Artist into a duplicating Battlesuit, Crime Fighter,
Weapon Master or any other archetype, just be sure the
duplicates  remain  within  their  power  level  limits  (117
points and PL8 for Twin or 100 points and PL7 for Triplets,
plus the cost of the Summon power).

Note  that  on  the  tables  below,  things  are  a  bit  different
than for the other archetypes in this book. Follow the in-
structions and it should be clear. The change is necessary
because  the  Summon  power  your  character  has  influ-
ences the number of points available to spend on other
sections of the character.
ABILITIES

R

[... truncated ...]
```

---

## Concept: Secret Origins Chapter

Chunk count: 2

### Chunk texts

**Chunk 1** (`919d7063d0ae`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Hero: ____________________________________     Player: ____________________________

Princess

Julia

Identity: _______________________________________________  (cid:80)(cid:3)Secret (cid:80)(cid:3)Public

Jessica Prentiss     X
135 lbs  Green

Female  19

Gender: _____________     Age: ________    Height: ____________     Weight: _____________     Eyes: ___________________     Hair: _____________________
10
Group Affiliation: ________________________________     Base of Operations: ______________________________________     Power Level: ________
150
Power Point Totals: Abilities _________+ Powers _________+ Advantages _________+ Skills _________+ Defenses _________= ___________

Emerald City
13
11

Blonde

None

5’6”

27

88

11

Strength

Stamina

12
12

Agility

Dexterity

5
3

Fighting

Intellect

6
2

Awareness

Presence

2
2

Offense

Unarmed

+8  Close, Damage 12

Thrown Object  +6  Ranged, Damage 12

Initiative

+9

Defense

Dodge (agl)

Parry (FGT)

Fortitude (STA)

Toughness (STA)

Will (awe)

8
8
12
12
8

Advantages

All-out Attack,
Attractive, Diehard,
Extraordinary Effort, Improved
Initiative, Inspire 2, Interpose, Power
Attack, Ultimate Effort (Toughness
checks), Well-informed

Acrobatics 4 (+9), Athletics
4 (+16), Close Combat:
Unarmed 2 (+8), Intimidation 4 (+6),
Perception 6 (+8), Ranged Combat:
Throwing 3 (+6), Stealth 3 (+8)

Skills

Toughness 8; Regeneration 2 • 15 points

Powers & Devices
____________________________________________________________________________________________________________________________________________
Fast: Speed 4 (30 MPH) • 4 points
____________________________________________________________________________________________________________________________________________
Leaping: Leaping 7 • 7 points
____________________________________________________________________________________________________________________________________________
Resilient: Immunity 5 (Cold, Disease, Heat, Pressure, Radiation); Impervious
____________________________________________________________________________________________________________________________________________
____________________________________________________________________________________________________________________________________________
Unrecognizable: Feature 1 (No one can tell Jessica and Princess are the same
________________________________________________________________

[... truncated ...]
```

**Chunk 2** (`997bf2eca013`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PLAYER

Interpose

TOUGH

Ultimate Effort (Toughness checks)

QUICK

Improved Initiative

SKILLS

Close Combat: Unarmed 2

Take  the  skill  listed  above,  then  roll  1d20  twice  (re-roll  if
you get the same result twice) and record the results.

1-4

5-8

Athlete: You’re a trained athlete.

Ex-Military: You used to be in the armed forces.

9-12

Charmer: You have a way with people.

13-16

Rough Upbringing: You were raised on the streets
or have had a hard life.

17-20

Sharp Mind: You’re difficult to fool.

ATHLETE

Athletics 4, Perception 4, Ranged Combat: Throwing 4

Roll  1d20  once  and  record  the  result  as  the  first  power
in  an  array,  then  roll  1d20  once  and  add  the  result  as  a
1-point Alternate Effect (re-roll if you get the same result
as your first roll).

1-3

4-6

7-9

Energy Blast: Ranged Damage 10, Accurate 5,

Distracting, Tiring • 10 points

Foot Stomp: Line Area Damage 10, Powerhouse and
target must be in contact with the same surface
• 10 points

Groundstrike: Burst Area Affliction 10 (Resisted

and Overcome by Fortitude; Dazed and Hindered,
Stunned and Prone, Incapacitated), Extra
Condition, Instant Recovery, Powerhouse and
target must be in contact with the same surface
• 10 points

10-12

13-14

Shockwave: Burst Area Damage 10, Powerhouse
and targets must be in contact with the same
surface • 10 points

Super-Breath: Close Range Cone Area Move Object
5, Limited to moving toward and away, Linked
to Cone Area Damage 5, Unreliable (only the
Damage is Unreliable) • 10 points

15-17

Cut Loose!: Penetrating 10 on Strength • 10 points

18-20

Thunderclap: Cone Area Affliction 10 (Resisted and
Overcome by Fortitude; Dazed, Stunned), Limited
Degree • 10 points

EX-MILITARY

Expertise: Military 4, Perception 4, Ranged Combat: Throwing 4

CHARMER

Deception 4, Insight 4, Persuasion 4

UPBRINGING

Only if you rolled Solid Form or Super-Strength on the
Offensive  Powers  table,  take  Super-Stamina,  directly
below, then roll on the table below, as directed. Do not
take Super-Stamina if you rolled Density or Growth on
the  Offensive  Powers  table,  instead,  roll  on  the  table
below.

Expertise: Streetwise 4, Intimidation 6, Perception 2

Super-Stamina: Enhanced Stamina 10 • 20 points

MIND

Expertise: (Choose One) 4, Insight 4, Perception 4

POWERS

Roll 1d20 once and record the result.

Roll  1d20  four  times  (re-roll  if  you  get  the  s

[... truncated ...]
```

---
