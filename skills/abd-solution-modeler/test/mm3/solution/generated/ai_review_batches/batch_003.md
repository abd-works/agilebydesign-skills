# Hypothesis concept review – batch 3

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

## Concept: Animal Empathy

Chunk count: 5

### Chunk texts

**Chunk 1** (`267bbd73af09`):

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

**Chunk 2** (`2b979f00a098`):

```
CHAPTER 5: ADVANTAGES .... 131
ACQUIRING

ADVANTAGES ............... 131

ADVANTAGE

DESCRIPTIONS ............. 131
Types of Advantages .........131
Accurate Attack ...................131
Agile Feint ..............................131
All-out Attack .......................131
Animal Empathy ..................131
Artificer ...................................131
Assessment ...........................132
Attractive................................132
Beginner’s Luck ....................134
Benefit, Ranked ....................134
Chokehold .............................134
Close Attack, Ranked .........134
Connected .............................134
Contacts .................................134
Daze .........................................134
Defensive Attack .................134
Defensive Roll .......................135
Diehard ...................................135
Eidetic Memory ...................135
Equipment,  ...........................135
Evasion ....................................135
Extraordinary Effort ............135
Fascinate ................................136
Fast Grab ................................136
Favored Environment ........136
Favored Foe ...........................136
Fearless ...................................136
Grabbing Finesse ................136
Great Endurance .................136
Hide in Plain Sight ..............136
Improved Aim ......................136
Improved Critical .................136
Improved Defense ..............136
Improved Disarm ................136
Improved Grab .....................137
Improved Hold .....................137
Improved Initiative .............137
Improved Smash .................137
Improved Trip .......................137
Improvised Tools .................137
Improvised Weapon ...........137
Inspire......................................137
Instant Up ..............................138
Interpose ................................138
Inventor ..................................138
Jack-of-All-Trades ................138
Languages, Ranked ............138
Leadership .............................138
Luck ..........................................139
Minion .....................................139
Move-by Action ...................139
Power Attack .........................139
Precise Attack .......................139
Prone Fighting .....................139

Quick Draw ............................139
Ranged Attack ......................139
Redirect ..................................139
Ritualist ................

[... truncated ...]
```

**Chunk 3** (`8ad0833a1563`):

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

**Chunk 4** (`ac75d3f2b9e6`):

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

**Chunk 5** (`b95c26d52ee0`):

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

---

## Concept: Animals

Chunk count: 1

### Chunk texts

**Chunk 1** (`b2722c49426d`):

```
CHAPTER 5: ADVANTAGES

135

FASCINATE

SKILL, RANKED

COMBAT

One of your interaction skills is so effective you can cap-
ture  and  hold  other’s  attention  with  it.  Choose  Decep-
tion,  Intimidation,  or  Persuasion  when  you  acquire  this
advantage. You can also use Fascinate with an appropri-
ate  Expertise  skill,  like  musician  or  singer,  at  the  GM’s
discretion.

You  are  subject  to  the  normal  guidelines  for  interaction
skills, and combat or other immediate danger makes this
advantage  ineffective. Take  a  standard  action  and  make
an  interaction  skill  check  against  your  target’s  opposing
check (Insight or Will defense). If you succeed, the target is
entranced. You can maintain the effect with a standard ac-
tion each round, giving the target a new resistance check.
The effect ends when you stop performing, the target suc-
cessfully resists, or any immediate danger presents itself.
Like all interaction skills, you can use Fascinate on a group,
but  you  must  affect  everyone  in  the  group  in  the  same
way.

You may take this advantage more than once. Each time, it
applies to a different skill.

FAST GRAB

COMBAT

When  you  hit  with  an  unarmed  attack  you  can  immedi-
ately make a grab check against that opponent as a free
action (see Grab, page 248). Your unarmed attack inflicts
its normal damage and counts as the initial attack check
required to grab your opponent.

COMBAT

You  have  an  environment  you’re  especially  suited  for
fighting  in.  Examples  include  in  the  air,  underwater,  in
space, in extreme heat or cold, in jungles or woodlands,
and so forth. While you are in your favored environment,
you gain a +2 circumstance bonus to attack checks or your
active defenses. Choose at the start of the round whether
the bonus applies to attack or defense. The choice remains
until the start of your next round. This circumstance bonus
is not affected by power level.

SKILL

You have a particular type of opponent you’ve studied or
are especially effective against. It may be a type of creature
(aliens, animals, constructs, mutants, undead, etc.), a pro-
fession (soldiers, police officers, Yakuza, etc.) or any other
category  the  GM  approves.  Especially  broad  categories
like “humans” or “villains” are not permitted. You gain a +2
circumstance  bonus  on  Deception,  Intimidation,  Insight,
and Perception checks dealing with your Favored Foe. This
circumstance bonus is not limited by power level.

FEARLES

[... truncated ...]
```

---

## Concept: Animate

Chunk count: 1
Performs actions: ['act_0117']

### Chunk texts

**Chunk 1** (`d1e949b40c7a`):

```
CHAPTER 3: ABILITIES

109

effect). They are immune to fatigued and exhausted
conditions,  but  cannot  exert  extra  effort.  Creatures
with no Stamina are often—but not necessarily—im-
mune to many of the other things affecting living be-
ings as well (see the Immunity effect in the Powers
chapter). They have no Fortitude defense.

Dexterity: A creature with no Dexterity cannot manip-
ulate objects and hence cannot make physical attacks.

Agility: A creature with no Agility is unable to move
its body under its own power and has no Dodge de-
fense.

defenses  apart  from  Toughness  (and  Fortitude,  if
they are alive).

•

Presence: Creatures without Presence are unable to
interact and immune to interaction skills. They have
no Will defense.

Lacking an ability is –10 power points; that is, it gives the
character  an  additional  10  power  points  to  spend  else-
where,  similar  to  having  a  –5  rank  in  an  ability,  but  with
different  effects.  MUTANTS  &  MASTERMINDS  heroes  cannot  be
absent an ability without Gamemaster permission, as it can
have significant effects on the character and the game.

Fighting: A creature with no Fighting is incapable of
making any sort of close attack (but may still be able
to launch ranged attacks, if it has Dexterity).

Absent abilities cannot be weakened (see the Weaken ef-
fect in the Powers chapter) or debilitated, since they are
not present at all in the first place!

Intellect: A creature with no Intellect is an automa-
ton, lacking free will and operating entirely on simple
instinct  or  pre-programmed  instructions.  Anything
with no Intellect is immune to mental effects and in-
teraction skills and has no Will defense.

Awareness:  Anything  with  no  Awareness  is  com-
pletely unaware and also has no Presence. It is an in-
animate object, not a creature. Objects are immune
to mental effects and interaction skills, and have no

Inanimate  objects  have  no  abilities  other  than  their
Toughness. Animate, but nonliving, constructs such as ro-
bots or zombies have Strength, Agility, and Dexterity, and
may  have  ranks  of  Awareness  and  Presence  (if  aware  of
their environment or capable of interaction), and Fighting
(if able to make close attacks). They may have Intellect (if
capable  of  independent  thought),  but  have  no  Stamina
(since  they  are  not  living  things).  See  Constructs  in  the
Gadgets & Gear chapter for more information.

•

•

•

•

•

Heroes face many hazards in their 

[... truncated ...]
```

---

## Concept: Apes

Chunk count: 0

### Chunk texts

---

## Concept: Applying Modifiers

Chunk count: 1

### Chunk texts

**Chunk 1** (`d4cad3e10e05`):

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

## Concept: Archetype

Chunk count: 1
Receives actions: ['act_0040']

### Chunk texts

**Chunk 1** (`ebf52e380812`):

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

---

## Concept: Area

Chunk count: 24
Performs actions: ['act_0281', 'act_0426']
Receives actions: ['act_0182', 'act_0426']

### Chunk texts

**Chunk 1** (`03f345278ec9`):

```
CHAPTER 8: ACTION & ADVENTURE

243

Objects  (targets  lacking  a  Stamina  rank)  take  damage
similar to other targets. Dazed and staggered results have
no real effect on inanimate targets, since they do not take
actions. Constructs, capable of action, are dazed and stag-
gered  normally  (see  Constructs  in  the  Gadgets  &  Gear
chapter).

Inanimate objects are defenseless by definition and there-
fore subject to finishing attacks (see the Finishing Attack
maneuver): essentially, you can choose between making
your attack on the object as a routine check or, if you make
the  attack  check  normally,  gaining  an  automatic  critical
hit if your attack hits, for a +5 bonus to effect.

Attacking an object held or worn by another character is a
smash action (see the Smash maneuver).

If an attacker’s intention is to bend, break or destroy an ob-
ject, then two degrees of failure on the Toughness check
results  in  a  break  (such  as  a  hole  punched  through  the
object) while three or more degrees of failure means the
object is destroyed (shattered, smashed to pieces, etc.).

The  Toughness  ranks  of  some  common  materials  are
shown on the Material Toughness table. The listed ranks
are for about an inch (distance rank –7) thickness of the
material: apply a +1 per doubling of thickness or a –1 per
halving of it. So a foot of stone is Toughness 8. Equipment
has Toughness based on its material. Devices have a base
Toughness equal to the total points in the device divided
by 5 (rounded down, minimum of 1).

The Healing and Regeneration effects can speed this pro-
cess. Lasting or more serious injuries are handled as com-
plications (see Lasting Injuries).

Objects, having no Stamina, do not recover from damage
unless they have an effect like Regeneration. Instead, they
must be repaired. See the guidelines under the Technol-
ogy skill when repairing damaged objects.

RANGE

An attack has one of three ranges: close, ranged, and per-
ception.  A  close  attack  can  only  affect  a  target  you  can
physically  reach,  by  touch  or  wielding  a  melee  weapon,
for example. A ranged attack can affect a target at a dis-
tance, while a perception attack can hit a target you are
able  to  accurately  perceive  automatically  without  need
for an attack check.

A ranged attack has a short range up to its rank x 25 feet,
at which it has no penalties. At medium range (up to rank
x 50 feet), the attack check has a –2 circumstance modi-
fier. At long range (up to

[... truncated ...]
```

**Chunk 2** (`0713e58acd4e`):

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

**Chunk 3** (`0f75307c0dea`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

tion effect). This is the base sense of the radio sense type.
It’s ranged, radius, and acute by default.

RADIUS

1-2 RANKS

You can make Perception checks with a radius sense for
any  point  around  you.  Subjects  behind  you  cannot  use
Stealth  to  hide  from  you  without  some  other  conceal-
ment. Auditory, olfactory, and tactile senses are normally
radius for humans. Cost is 1 rank for use with one sense, 2
ranks for one sense type.
RANGED

1 RANK

You can use a sense that normally has no range (taste or
touch  in  humans)  to  make  Perception  checks  at  range,
with the normal –1 per 10 feet modifier. This can be en-
hanced with the Extended Sense effect.

RAPID

1 RANK

You can read or take in information from a sense faster than
normal:  each  rank  increases  your  perception  speed  by  a
factor of 10 (x10, x100, etc.) with a single sense, double cost
for an entire sense type. You can use rapid vision to speed-
read, pick up on rapid flickering between frames of a film,
watch video replays in fast-forward speeds, and such, rapid
hearing to listen to time-compressed audio “blips,” and so
forth.

1 RANK

Precognition  and  Postcognition  can  be  problematic
abilities,  since  they  provide  players  with  considerable
information. Keep in mind precognitive and postcogni-
tive information is often cryptic or unclear, and changes
in circumstances may lead to changes in visions of the
future. If players use either too often, feel free to have
their visions become less and less clear as the timelines
become tangled by so much constant surveillance and
intervention.

Generally, Precognition is best treated as a plot device
for the GM to provide information to the player as suits
the  adventure,  similar  to  a  free  use  of  the  inspiration
ability of hero points. In fact, GMs looking to limit Pre-
cognition and Postcognition may wish to require extra
effort or hero points to use them, or require the Uncon-
trolled modifier.

one in an area. Apply the Selective modifier for the abil-
ity to choose who in the area does and does not benefit
from the Senses. To affect the area of a sense itself, use
the Extended and Radius  traits of the Senses  effect. +1
cost per rank.

Dimensional:  This  modifier  allows  you  to  extend  your
senses  into  other  dimensions.  It’s  assumed  to  apply  to
all your senses, allowing you to sense your proximate lo-
cation  in  the  other  dimension(s).  For

[... truncated ...]
```

**Chunk 4** (`150cf8210923`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

when you time-travel. If you apply the Increased Mass modi-
fier, you can carry additional mass up to your modifier rank.

HOOD: TIME, SPACE, AND DIMENSION TRAVEL

TRACKLESS

You leave no trail and cannot be tracked using visual sens-
es  (although  you  can  still  be  tracked  using  scent  or  other
means). You can walk across the surface of soft sand or snow
without leaving tracks and you have total concealment from
tremorsense (see Concealment, page 244). Each additional
rank renders you trackless to another sense type.
WALL-CRAWLING

You can climb walls and ceilings at your ground speed rank
–1 with no chance of falling and no need for an Athletics
check. You are still vulnerable while climbing, however. An
additional rank of this effect means you climb at your full
speed rank and are not vulnerable while climbing.
WATER-WALKING

You can stand or move at your normal ground speed on
the surface of water, quicksand, and other liquids without
sinking. If you fall prone for any reason, you sink into the
liquid normally. With 2 ranks of this effect, you can also lie
prone on a liquid surface without sinking; you only sink if
you choose to.

NULLIFY

ATTACK

Action: Standard • Range: Ranged
Duration: Instant • Cost: 1 point per rank

Nullify  can  counter  particular  effects  of  a  particular  de-
scriptor,  such  as  fire  effects,  magical  effects,  mental  ef-
fects, and so forth (see Countering Effects, at the start of
this chapter). You can counter one effect of your chosen
descriptor per use of Nullify. You can’t nullify innate effects
(see the Innate modifier description).

Make a ranged attack check to hit the target. Then make
an  opposed  check  of  your  Nullify  rank  and  the  targeted
effect’s  rank  or  the  target’s  Will  defense,  whichever  is
higher. If you are targeting the subject of an effect rather
than the effect’s user, make an opposed check of Nullify
rank vs. effect rank. If you win, the targeted effect turns off,
although the user can re-activate it normally. If you lose
the opposed check, you do not Nullify the effect. With two
or more degrees of failure, trying again against the same
subject in the same scene requires extra effort.
EXTRAS

Affects Insubstantial: Nullify does not require this modi-
fier to affect insubstantial targets, or the Insubstantial ef-
fect itself. You can attempt to nullify the effects of insub-
stantial targets normally.

Alternate Resistance

[... truncated ...]
```

**Chunk 5** (`2ec68f50f56a`):

```
CHAPTER 6: POWERS

151

Others with an acute sense able to detect your Commu-
nication  medium  can “tap  into”  your  transmissions  with
a Perception check (DC 10 + your Communication rank).
The eavesdropper must be within normal sensory range
of you or the receiver. With two degrees of success on the
check, the eavesdropped can also understand your trans-
missions. Effects like Concealment and Dazzle that target
your  Communication  medium  can  “jam”  or  block  your
transmissions.
EXTRAS

Area: You  can  broadcast  omni-directionally  to  every  re-
ceiver  within  your  maximum  Communication  range  at
once. Note this extra is only strictly necessary to commu-
nicate  with  everyone  over  a  wide  area  all  at  once;  since
using  and  maintaining  Communication  are  free  actions,
the GM may allow a communicator to establish and main-
tain contact with multiple discrete receivers—such as the
members  of  the  same  team—all  in  the  same  round.  +1
cost per rank.

Dimensional:  Communication  with  this  modifier  can
bridge  dimensional  barriers,  reaching  into  other  dimen-
sions and planes of existence. The Communication effect
still has its proximate range, and the GM may rule certain
subjects “out of range” of the effect, depending on their
relative positions in the other dimension. Flat +1 point.

Rapid: Your  communication  occurs  10  times  faster  than
normal speech. Each additional rank increases communi-
cation speed by a factor of 10. This is useful for high-speed
computer  links, “deep  sharing”  psychic  rapports,  and  so
forth. Flat +1 point.

Selective:  If  you  have  the  Area  extra,  you  can  choose
which receiver(s) within range get your Communication,
excluding  everyone  else.  This  allows  you  to  go  from  a
single receiver (point-to-point) to all potential receivers in
range (omni-directional) or anywhere in between. +1 cost
per rank.

Subtle:  Your  Communication  cannot  be  “overheard”  (it
is encrypted, scrambled, or otherwise protected). With 2
ranks, your Communication cannot even be detected (that
is,  no  one  can  even  tell  you  are  transmitting,  much  less
what you’re saying). Flat +1 or 2 points.

FLAWS

Limited:  Communication  may  be  limited  to  only  mem-
bers of a particular group, such as a species, family, mem-
bers  of  an  organization,  and  so  forth. This  is  in  addition
to limitations imposed by medium (that is, requiring sub-
jects to have a means of picking up on the Communica

[... truncated ...]
```

**Chunk 6** (`3e277f7add29`):

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

**Chunk 7** (`437f5039e60f`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

Perception range effects must accurately perceive a target in order to affect it. This generally means you cannot target
subjects with total concealment from your accurate senses with perception range effects. Thus, foes with Visual Conceal-
ment (the most common accurate sense) can be quite effective against characters relying on perception range attacks,
unless the attacker has an unusual accurate sense to circumvent the Concealment. This is one reason Visual Concealment
costs extra.

At the Gamemaster’s discretion, a successful Perception check to accurately locate a target with an acute sense may al-
low you to use perception range effects on that target; however, the target still benefits from concealment, granting a +5
circumstance bonus to resistance against the effect.

ranks. A plant’s sense of its surroundings is limited, so it
won’t be able to give (or recognize) detailed descriptions
or answer questions about events outside its immediate
vicinity.

SPIRITS

You can communicate with incorporeal and normally in-
visible and inaudible spirit beings, such as ghosts or cer-
tain extradimensional entities, depending on the context
of the setting. Rank 1 essentially allows you to function as
a “medium” of sorts, able to perceive spirits and relay what
you see and hear. Rank 2 allows you to be clearly under-
stood by denizens of the spirit world, as well. At the GM’s
discretion,  this  effect  may  extend  to  undead  creatures,
demons, or other supernatural entities, depending on the
setting.

FLAWS

Type: You can only comprehend a broad type of subject
(only elves, canines, avians, or sea creatures, for example).
For an additional flaw, you can only comprehend a narrow
type of subject (dogs, falcons, or dolphins, for example).
Broad –1 cost per rank. Narrow –2 cost per rank.

SENSORY

Action: Free • Range: Personal
Duration: Sustained • Cost: 2 points per rank

You gain total concealment from a particular sense while
this  effect  is  active,  although  you  are  still  detectable  to
other senses (even other senses of the same sense type;
so you could have full concealment against normal sight,
but not infravision or any other sense in the sight sense
type).  Each  additional  rank  gives  you  concealment  from
another sense; two ranks give you concealment for an en-
tire sense type. See Concealment on page 244 for the full
effects.

Concealment from visual senses costs double (2 ranks for
one

[... truncated ...]
```

**Chunk 8** (`481ffcf3c778`):

```
CHAPTER 5: ADVANTAGES
CHAPTER 5: ADVANTAGES

CHAPTER 5: ADVANTAGES

You can use combinations of advantages—particularly combat advantages—to create different “fighting styles” rang-
ing from martial arts to superhero combat techniques. For example, a “soft” fighting style focusing primarily on defense
might include the advantages Defensive Attack, Improved Defense, Improved Trip, and Instant Up. A “hard” fighting style
focused on offense might include All-out Attack, Improved Critical, Improved Smash, Power Attack, and Startle for a fierce
kiai shout! You can combine various advantages to create specific styles or allow players to mix-and-match to design their
own unique styles.

Use the following advantage combos as examples of how to create different fighting styles. Students who have not yet
mastered a style may have only some of a style’s associated advantages rather than all of them.

Any of these fighting styles might include ranks of the Close Attack advantage. Other fighting style advantages might
include:

•

•

•

•

Boxing: All-out Attack, Defensive Attack, Improved Critical (Unarmed), Power Attack, Takedown.

Judo: Accurate Attack, Defensive Attack, Improved Disarm, Improved Grab, Improved Hold, Improved Trip.

Kung Fu: Defensive Attack, Improved Critical (Unarmed), Improved Smash, Improved Trip, Instant Up, Power Attack,
Startle.

Sword-fighting: Accurate Attack, Defensive Attack, Improved Disarm, Improved Initiative, Power Attack, Taunt.

•  Wrestling: Chokehold, Fast Grab, Improved Grab, Improved Hold, Power Attack.

Comic book martial artists often have abilities far beyond the scope of the advantages and fighting styles given in this
chapter. Such superhuman martial arts abilities as leaping vast distances, punching through solid stone, shrugging off
damage, and killing with a mere touch are powers. See the Powers chapter for details.

bonus and add the same number (up to +5) to both your
active defenses (Dodge and Parry).

COMBAT, RANKED

You can avoid damage through agility and “rolling” with
an  attack. You  receive  a  bonus  to  your Toughness  equal
to your advantage rank, but it is considered an active de-
fense similar to Dodge and Parry (see Active Defenses in
the  Abilities  chapter),  so  you  lose  this  bonus  whenever
you  are  vulnerable  or  defenseless. Your  total Toughness,
including this advantage, is still limited by power level.

This advantage is common for heroes who lack either su-
perhuman speed or toughness, rely

[... truncated ...]
```

**Chunk 9** (`5ec359de437f`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

out of the way, and so forth). A successful resistance check
reduces the Area effect to half its normal rank against that
target (round down, minimum of 1 rank).

•

SHAPE

Choose one of the following options:

•

•

•

•

•

Burst: The effect fills a sphere with a 30-foot radius
(distance  rank  0).  Bursts  on  level  surfaces  (like  the
ground)  create  hemispheres  30  feet  in  radius  and
height.

Cloud: The effect fills a sphere with a 15-foot radius
(distance  rank  –1)  that  lingers  in  that  area  for  one
round after its duration expires (affecting any targets
in  the  area  normally  during  the  additional  round).
Clouds  on  level  surfaces  (like  the  ground)  create
hemispheres 15 feet in radius and height.

Cone:  The  effect  fills  a  cone  with  a  length,  width,
and height of 60 feet (distance rank 1), spreading out
from the effect’s starting point. Cones on a level sur-
face halve their final height.

Cylinder: The effect fills a cylinder 30 feet in radius
and height (distance rank 0).

Line:  The  effect  fills  a  path  6  feet  wide  and  30  feet
long  (distance  ranks  -2  and  0,  respectively)  in  a
straight  line.  Additional  ranks  of  area  increases  the
length.  To  increase  the  width,  purchase  additional
ranks for that.

Perception: The effect works on anyone able to per-
ceive the target point with a particular sense, chosen
when you apply this extra, like a Sense-Dependent ef-
fect (see the Sense-Dependent modifier). Targets get
a Dodge resistance check, as usual, but if the check is
successful suffer no effect (rather than half). Conceal-
ment that prevents a target from perceiving the effect
also blocks it. This modifier includes the Sense-Depen-
dent flaw (see Flaws) so it cannot be applied again. If
it is applied to an already Sense-Dependent effect, it
costs 2 points per rank rather than 1.

•

Shapeable: The effect fills a volume of 30 cubic feet
(volume rank 5), and you may shape the volume as
you wish, so long as it all remains contiguous. Affect-
ing  an  average-sized  human  requires  4  cubic  feet
(volume rank 2).

Each +1 point increase in cost per rank moves the area’s
distance  rank  up  by  1.  So  a  Burst  Area  with  +2  cost  per
rank has a 60-foot radius (distance rank 1), a 120-foot ra-
dius at +3 cost per rank (distance rank 2), and so forth.
RANGE

The Area modifier interacts with different ranges as follows:

•

Close: An effec

[... truncated ...]
```

**Chunk 10** (`634190f2dd84`):

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

**Chunk 11** (`6802eda7b562`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

•

•

•

•

Armor: Armor provides Protection for a vehicle in addi-
tion to its normal Toughness, possibly including Imper-
vious  Protection.  Some  vehicles  may  have  Sustained
Protection (such as force screens) instead of, or in addi-
tion to, Permanent Protection. 1 point per +1 Toughness.

Cloaking Device: A vehicle may have a “cloaking de-
vice” granting Concealment from visual senses. Some
vehicles  may  also  have  Concealment  from  auditory
senses or things such as radar, giving them a “stealth
mode.” 4 points (normal vision or all of another sense
type) or 8 points (all visual senses).

Immunity:  Vehicles  normally  provide
immunity
to  the  normal  hazards  of  environments  they  travel
through—such  as  underwater  or  in  space—at  no
additional  cost.  Additional  Immunity  effects  are  for
unusual hazards or circumstances, such as a car that
provides  a  sealed  air  system,  granting  immunity  to
suffocation and other atmospheric hazards.

Smokescreen:  The  vehicle  can  release  a  cloud  of
thick smoke or mist that provides an Area visual Con-
cealment Attack to hide the vehicle or confuse pur-
suers. 12 points.

•  Weapons:  Vehicle  weapons  are  based  on  various
attack  effects,  particularly  Damage  with  various
modifiers. Vehicles, especially military vehicles, may
mount versions of some of the weapons listed else-
where in this chapter.

A team of heroes may share a vehicle used by the whole
team, particularly useful for shuttling around team mem-

bers  who  cannot  fly  or  move  at  super-speed. The  mem-
bers of the team divide the equipment point cost of the
vehicle among them as they see fit, devoting the neces-
sary  ranks  of  the  Equipment  advantage  to  covering  the
vehicle’s cost.

Just like Alternate Equipment, characters may have mul-
tiple  vehicles. These  are  generally  Alternate  Equipment
by  definition,  since  it’s  difficult  to  drive  or  pilot  more
than one vehicle at a time! So the character pays the full
cost  for  the  most  expensive  vehicle,  and  then  1  equip-
ment point for each additional vehicle with the same or
lesser cost.

So a hero with an array of vehicles, such as a plane, boat,
and  car  pays  full  equipment  point  cost  for  the  most  ex-
pensive  of  the  vehicles  and  just  1  equipment  point  for
each  of  the  others.  The  hero’s  player  can  even  spend  a
hero point to pull out a m

[... truncated ...]
```

**Chunk 12** (`6e58428e1e90`):

```
CHAPTER 6: POWERS

167

EXTRAS

Area: Your Luck Control effect works equally on all targets
in the affected area. You spend only one hero point, but
the subjects are each affected individually. You must ap-
ply the same effect to all subjects at once. +1 cost per rank.

Luck: Each rank in this extra gives you the benefit of a rank
in the Luck advantage (see Luck in the Advantages chap-
ter). It is subject to the same limits as the Luck advantage
set by the GM. Flat +1 point per rank of Luck.

Selective: This extra, applied to Area Luck Control, allows
you to choose who in the area is or is not affected by it. +1
cost per rank.

FLAWS

Action: If the action required for Luck Control is increased
beyond a reaction, it is only usable during your turn each

Effect:  Perception  Ranged  Damage,  Resisted  by  Will  •
4 points per rank

You can strike targets’ minds with “mental force,” inflict-
ing  Damage  resisted  by  the  target’s  Will  rather  than
Toughness, but having no effect on targets immune to
effects resisted by Will, such as inanimate objects. Men-
tal Blasts are often, but not always, Subtle as well, which
costs a flat 1 point.

MAGIC

Effect: Ranged Damage • 2 points per rank

You are a sorcerer, witch, or wizard, able to cast a variety
of magical spells. Your basic default effect is a Blast of
eldritch  force,  able  to  inflict  Ranged  Damage  (see  the
Blast power, previously).

However,  like  the  Energy  Control  power,  Magic  can
have a wide range of Alternate Effects, each a separate
spell you have mastered. The possibilities are virtually
limitless, within the bounds of your hero’s descriptors
and  the  Gamemaster’s  approval.  Examples  include
mystic  bindings  (Affliction,  see  the  Snare  version),
dispelling  magical  effects  (Nullify  Magic),  conjuring
clouds of mist or fog (an Area Visual Concealment At-
tack), scrying distant places (Remote Sensing), or slip-
ping  between  the  dimensions  to  appear  elsewhere
(Teleport), to name just a few.

All Magic effects have the “magic” descriptor regardless
of their other descriptors, so a Blast of flames conjured
with magic has both the “magic” and “fire” descriptors,
for example.

Magicians  often  have  a  Power  Loss  complication  (see
Complications  in  The  Basics  chapter):  if  they  are  un-
able to freely speak and gesture to cast their spells, they
cannot  use  Magic  (or  any  related  magical  powers  reli-
ant on spellcasting). Certain styles of Magic may impose
ot

[... truncated ...]
```

**Chunk 13** (`72dc60c2e6cf`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

EXTRAS

Affects Objects: Weaken with this modifier works on inani-
mate objects, although the effect can still only affect traits
the objects possess. This is most often applied to Weaken
Toughness  for  an  effect  that  can  weaken  both  creatures
and objects. +1 cost per rank, +0 for Affects Only Objects.

Broad: You can Weaken any of a broad set of traits, one at
a time suited to your effects descriptors. So you might be
able to Weaken Abilities, for example, or Weaken Mental
Effects. You choose which trait from the set is weakened
when you use the effect. +1 cost per rank.

Concentration: Once you have hit with a Concentration
Weaken, so long as you continue to take a standard action
each turn to maintain the effect, the target must make a
new resistance check against it, with no attack check re-
quired. +1 cost per rank.

Incurable: Weaken with this modifier cannot have its ef-
fects  countered  by  another  power  (such  as  Restorative
Healing) without the Persistent modifier; the target must
recover from the Weaken normally. Flat +1 point.

MODIFIERS

Precise: A Weaken effect capable of reducing more than one
trait at once can have this modifier, allowing you to choose
which traits are affected, while not affecting others. Note this
differs from the Selective extra (following). Flat +1 point.

Progressive:  A  Progressive  Weaken  effect  reduces  the
affected  traits  each  round  until  the  target  successfully
resists. Make a new resistance check for the target at the
end of each turn; failure weakens the affected trait(s) fur-
ther, while success stops the Progressive Weaken, but the
target must still recover ranks already lost (at the rate of 1
point per turn). +2 cost per rank.

Selective: This extra is applied to an Area Weaken so it only
affects some targets and not others. Combined with Precise
(previously), you can use an Area Weaken to selectively af-
fect only certain traits of certain targets. +1 cost per rank.

Simultaneous: If applied to a Broad Weaken, this extra al-
lows it to affect all of the traits in its set at the same time.
Each trait loses the difference between the resistance check
result and the DC in power points on a failed check. So a
Simultaneous Weaken Fire Effects subtracts points from ev-
ery fire effect the target possesses with a single attack. The
effect must be Broad to apply this modifier. +1 cost per rank.

Modifiers  enhance  or  limit  effects  in  v

[... truncated ...]
```

**Chunk 14** (`7ed36e3d5075`):

```
CHAPTER 8: ACTION & ADVENTURE
CHAPTER 8: ACTION & ADVENTURE

CHAPTER 8: ACTION & ADVENTURE

DAMAGE

A successful attack with a Damage effect requires the tar-
get to make a Toughness resistance check.

Toughness vs. [Damage rank + 15]

Success : The damage has no effect.

Failure (one degree): The target has a –1 circumstance
penalty to further resistance checks against damage.

Failure (two degrees): The target is dazed until the end
of their next turn and has a –1 circumstance penalty to
further checks against damage.

Failure  (three  degrees):  The  target  is  staggered
and  has  a  -1  circumstance  penalty  to  further  checks
against damage. If the target is staggered again (three
degrees of failure on a Damage resistance check), ap-
ply  the  fourth  degree  of  effect. The  staggered  condi-
tion  remains  until  the  target  recovers  (see  Recovery,
following).

Failure (four degrees): The target is incapacitated .

The  circumstance  penalties  to Toughness  checks  are  cu-
mulative,  so  a  target  who  fails  three  resistance  checks
against  Damage,  each  with  one  degree  of  failure,  has  a
total –3 penalty.

If an incapacitated target fails a resistance check against
Damage,  the  target’s  condition  shifts  to  dying.  A  dying
target  who  fails  a  resistance  check  against  Damage  is
dead.

Strength provides a “built-in” Damage effect: the ability
to hit things! You can apply effect modifiers to the Dam-
age your Strength inflicts, making it Penetrating or even
an  Area  effect!  You  can  also  have  Alternate  Effects  for
your Strength Damage; see the Alternate Effect modi-
fier  for  details.  Like  other  Damage  effects,  a  character’s
Strength Damage is close range and instant duration by
default.

If you choose, a Damage effect can be Strength-based—
something like a melee weapon—allowing your Strength
Damage to add to it. You add your Strength and Damage
ranks together when determining the rank of the attack.
Any modifiers applied to your Damage must also apply to
your Strength rank if its bonus damage is to benefit from
them.  However,  any  decrease  in  your  Strength  reduces
the amount you can add to your Damage, and negative
Strength  subtracts  from  your  Damage!  Likewise,  any-
thing that prevents you from exerting your Strength also
stops you from using a Strength-based Damage effect. If
you can’t swing your fist, you can’t swing a sword, either.
On the other hand, a laser blade does the same damage
wheth

[... truncated ...]
```

**Chunk 15** (`7f148070d8bb`):

```
CHAPTER 6: POWERS

155

DAMAGE

ATTACK

Action: Standard • Range: Close
Duration: Instant • Cost: 1 point per rank

You can inflict damage on a target by making a close at-
tack. The exact nature of your Damage is up to you, with
the GM’s approval; it can be anything from a powerful im-
pact to razor claws, energy fields, or some other damaging
medium. The target resists with Toughness:

Toughness vs. [Damage rank + 15]

Success : The damage has no effect.

Failure (one degree): The target has a –1 circumstance
penalty to further resistance checks against damage.

Failure (two degrees): The target is dazed until the end
of their next turn and has a –1 circumstance penalty to
further checks against damage.

Failure  (three  degrees):  The  target  is  staggered
and  has  a  -1  circumstance  penalty  to  further  checks
against damage. If the target is staggered again (three
degrees of failure on a Damage resistance check), ap-
ply  the  fourth  degree  of  effect. The  staggered  condi-
tion  remains  until  the  target  recovers  (see  Recovery,
following).

Failure (four degrees): The target is incapacitated .

The  circumstance  penalties  to Toughness  checks  are  cu-
mulative,  so  a  target  who  fails  three  resistance  checks
against  Damage,  each  with  one  degree  of  failure,  has  a
total –3 penalty.

If an incapacitated target fails a resistance check against
Damage, the target’s condition shifts to dying. A dying tar-
get who fails a resistance check against Damage is dead.

Strength provides a “built-in” Damage effect: the ability
to hit things! You can apply effect modifiers to the Dam-
age your Strength inflicts, making it Penetrating or even
an  Area  effect!  You  can  also  have  Alternate  Effects  for
your Strength Damage; see the Alternate Effect modi-
fier  for  details.  Like  other  Damage  effects,  a  character’s
Strength Damage is close range and instant duration by
default.

If  you  choose,  a  Damage  effect  can  be  Strength-
based—something like a melee weapon—allowing your
Strength Damage to add to it. You add your Strength and
Damage  ranks  together  when  determining  the  rank  of
the attack. Any modifiers applied to your Damage must
also apply to your Strength rank if its bonus damage is
to  benefit  from  them.  However,  any  decrease  in  your
Strength reduces the amount you can add to your Dam-
age, and negative Strength subtracts from your Damage!
Likewise, anything that prevents you from exerting your
Stre

[... truncated ...]
```

**Chunk 16** (`87f598748db8`):

```
CHAPTER 6: POWERS

201

Items provided by the Equipment advantage (see the Advantages chapter) are essentially effects and other traits with Easily
Removable, along with the various other limitations outlined in the Gadgets & Gear chapter, amounting to a reduction of
–4 points per 5 power points of final cost. Thus the Equipment advantage provides 5 points worth of equipment per rank
(or 1 power point).

ture  to  find  certain  rare  parts,  specialized  help,  or  other
components.

SENSE-DEPENDENT

-1 COST PER RANK

For a flat 1-point reduction in the value of the Removable
flaw, you can define a device as Indestructible. It can still
be taken away, but cannot be damaged or destroyed, ex-
cept as a GM-imposed complication (earning the player a
hero point as usual). This reduction can lower the value of
the flaw to 0, in which case the character gets no power
point discount for the device.

The temporary loss of a removable power does not con-
stitute  a  complication,  any  more  than  the  result  of  any
other  flaw. You  can  have  a  device  or  power-object  as  a
descriptor without this flaw, if you wish, in which case the
power cannot be removed or taken away from you with-
out a complication applied by the GM (earning you a hero
point) or the use of an effect like Nullify, which has pre-
defined conditions for recovery.

-1 COST PER RANK

When applied to an effect that doesn’t normally allow a
resistance  check,  this  flaw  gives  it  one.  Choose  the  de-
fense when the flaw is applied. Since effects that work on
others  allow  a  resistance  check  by  definition,  this  nearly
always applies to personal effects that allow someone in-
teracting with them to circumvent the effect with a suc-
cessful check.

For  example,  an  Enhanced  Parry  defense  effect  might  re-
flect a low-level reading of a target’s mind to anticipate and
avoid attacks. It allows a Will resistance check to overcome
the effect, denying you the defense bonus against that op-
ponent (and applying this flaw to the effect). Likewise, your
Concealment  effect  might  be  illusory  rather  than  a  true
physical transformation, permitting a Will resistance check
for someone to overcome it. A sustained Protection effect
might be some sort of “kinetic field” that permits an attack-
er a Fortitude resistance check to overcome it.

When applied to an effect that does normally allow a re-
sistance check, this flaw gives it an additional one, which
may be the same as its normal 

[... truncated ...]
```

**Chunk 17** (`afba8b4a5938`):

```
CHAPTER 6: POWERS

159

LIGHT

You  can  raise  the  light  level  in  the  area,  countering  the
concealment of darkness, but not other forms of conceal-
ment. For 1 point per rank, you can create enough light to
reduce  total  concealment  to  partial  and  partial  conceal-
ment  to  none.  For  2  points  per  rank,  you  can  shed  light
as bright as a sunlit day, eliminating all concealment pro-
vided  by  natural  darkness.  Power  effects  with  the  dark-
ness descriptor may be countered with a successful power
check (see Countering Effects, page 148).

You impose a -2 modifier to Perception checks for 1 point
per rank, and a -5 for 2 points per rank. For more signifi-
cant  obscuring  of  senses  (via  darkness,  fog,  etc.)  use  an
Area Concealment Attack effect (see Concealment in this
chapter).
EXTRAS

Selective: With this extra you can vary the environment
within your affected area, affecting some while not affect-
ing  others,  or  even  mixing  and  matching  different  envi-
ronments (making part of the area cold and another hot,
for example). +1 cost per rank.

GENERAL

Action: None • Range: Personal
Duration: Permanent • Cost: 1 point per rank

You  have  extra  manipulative  limbs,  such  as  arms,  tenta-
cles, or even prehensile hair or a tail. Each rank in this ef-
fect grants you an extra limb.

Extra  Limbs  do  not  allow  you  to  take  additional  actions
in a round, although they do provide the benefits of the
Improved Grab advantage—grabbing with some of your
limbs and leaving others free. All additional limbs except
your dominant limb are considered your “off-hand.” If you
have the Benefit (Ambidexterity) advantage, you have no
off-hand penalties with any of your limbs.

If you apply all of your limbs to a grab attempt (rather than
taking the option to leave some of them free), you gain a

HOOD: EXTRA LIMBS, NOT EXTRA ACTIONS

As a default, Extra Limbs do not grant characters the abil-
ity to take extra actions in a round, simply because multi-
ple actions—especially extra standard actions usable for
attacks—tend to slow down and unbalance play.

As  an  option  for  including  some  combat  benefits  with
Extra  Limbs,  consider  allowing  the  application  of  the
Multiattack extra to the Strength of a character with Extra
Limbs, reflecting the ability to launch a flurry of attacks
at a single opponent, or to “spread” those attacks among
a number of nearby opponents. See the Multiattack de-
scription under Extras in this 

[... truncated ...]
```

**Chunk 18** (`bfdbb051d926`):

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

**Chunk 19** (`d4cad3e10e05`):

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

**Chunk 20** (`e17d1554782d`):

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

**Chunk 21** (`f1bc1ad153ee`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

Example:  Lady  Liberty,  rescuing  people  from  a
tenement  fire,  is  hemmed-in  by  collapsed  debris.
Her player decides to simply punch a path through.
Since  she’s  going  for  maximum  damage,  she  de-
cides  to  make  the  attack  check  normally  (rather
than a routine check). Given her attack bonus, she’ll
only miss on a natural 1 anyway. She succeeds and
does her Strength in Damage, +5 for the automatic
critical. The GM decides the brick, mortar, and heavy
beams have a toughness of 9 and makes a Tough-
ness  check,  rolling  a  5,  against  a  DC  30  (Lady  Lib-
erty’s Damage +15). A 14 result is three degrees of
failure, so she easily smashes through the debris and
clears the building, carrying people to safety!

The  Toughness  ranks  of  some  common  materials  are
shown on the Material Toughness table. The listed ranks
are for about an inch (distance rank –7) thickness of the
material: apply a +1 per doubling of thickness or a –1 per
halving of it. So a foot of stone is Toughness 8. Equipment
has Toughness based on its material. Devices have a base
Toughness equal to the total points in the device divided
by 5 (rounded down, minimum of 1).

MATERIAL

TOUGHNESS

Paper

Soil

Glass

Ice

Rope

Wood

Stone

Iron

Reinforced Concrete

Steel

Titanium

Super-alloys

RECOVERY

0

0

1

1

1

3

5

7

8

9

15

20+

Living targets remove one damage condition per minute
of  rest,  starting  from  their  worst  condition  and  working
back. So a damaged character recovers from being inca-
pacitated, then staggered, dazed, and finally removes a –1
Toughness check penalty per minute until fully recovered.
The Healing and Regeneration effects can speed this pro-
cess. Lasting or more serious injuries are handled as com-
plications  (see  Lasting Injuries  in  the  Recovery section
of the Action & Adventure chapter).

Objects, having no Stamina, do not recover from damage
unless they have an effect like Regeneration. Instead, they
must be repaired. See the guidelines under the Technol-
ogy skill when repairing damaged objects.

DEFLECT

DEFENSE

Action: Standard • Range: Ranged
Duration: Instant • Cost: 1 point per rank

You can actively defend for characters other than yourself,
deflecting or diverting attacks against them at a distance,
and may be able to more effectively defend yourself, de-
pending on your rank. See the Defend action in the Ac-
tion  &  Adventure  chapter  for  details. You 

[... truncated ...]
```

**Chunk 22** (`f45e1af7c8dc`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

Effect: Ranged, Progressive Affliction, Resisted by Forti-
tude • 4 points per rank

You  render  the  target  unable  to  breathe.  Targets  fail-
ing  the  Fortitude  resistance  check  against  your  effect
DC become dazed, stunned, and finally incapacitated,
passing out from the lack of oxygen. A failed attempt
to  resist  the  ongoing  effect  of  Suffocation  causes  the
target’s condition to worsen by one degree.

ent than “heat ray” is a descriptor for a Damage effect or
“sticky webbing” is a descriptor for a hindering Affliction;
in  neither  case  does  the  character  need  Summon  Heat
Ray or Summon Webbing to create the desired powers!

SWIMMING

MOVEMENT

Action: Free • Range: Personal
Duration: Sustained • Cost: 1 point per rank

You can swim fast. You have a water speed equal to your
Swimming  rank  –2,  subject  to  the  usual  rules  for  swim-
ming (see the Athletics skill description for details). You
can make Athletics checks to swim as routine checks. This
power does not allow you to breathe underwater (for that
see Immunity, page 165).

TELEPORT

MOVEMENT

Action: Move • Range: Rank
Duration: Instant • Cost: 2 points per rank

You can move instantly from place to place without cross-
ing the distance in between. You can teleport yourself and
up  to  50  lbs.  (mass  rank  0)  of  additional  mass  a  distance
rank equal to your effect rank as a move action. Unwilling
passengers  get  a  Dodge  resistance  check  to  avoid  being
taken along.

You can only teleport to places you can accurately sense
or know especially well (in the GM’s judgment). You re-
tain  your  position  and  relative  velocity  when  you  tele-
port. So if you are falling when you teleport, you are still
falling at the same speed when you arrive at your desti-
nation.

Teleport is meant for use on or around a planet. For things
like traveling to distant planets or stars, apply the Space
Travel  effect  of  Movement  as  a  “hyperjump”  or  similar
power.
EXTRAS

Accurate: You don’t need to know or accurately sense your
destination to teleport there, just be able to generally de-
scribe it, such as “inside the capitol building lobby” or “atop
the  Emerald  Tower’s  roof.”  If  the  destination  isn’t  in  your
Teleport range, nothing happens. +1 cost per rank.

SUPER-SPEED

Effect: Enhanced Initiative, Quickness, Speed • 3 points
per rank

You are fast! Each rank of Super-Speed gives you the
effects  of  Imp

[... truncated ...]
```

**Chunk 23** (`fc4ed8309dc8`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

EXTRAS

Action: This extra reduces the action required for you to
use Healing. You cannot use Healing more than once per
turn  regardless. To  heal  multiple  subjects  at  once,  apply
the Area modifier. +1 cost per rank.

Affects Objects: Your Healing can also “heal” damage to
non-living  subjects.  You  make  a  Healing  check  against
the subject’s worst damage condition, as normal. +1 cost
per rank.

Area: Healing with this extra grants the same benefit to all
subjects in the affected area. Area Empathic Healing (see
this power’s Flaws) is an unwise combination, as the heal-
er takes on all of the damage conditions of the affected
subjects at once! +1 cost per rank.

Energizing: You can heal the fatigued and exhausted con-
ditions as well as damage conditions: DC 10, one degree of
success for fatigued, two degrees of success for exhausted.
However, you take on the removed conditions and cannot
use  Healing  to  eliminate  your  own  fatigue  (although  you
can still use hero points to recover from them). If the Heal-
ing check fails, you must wait the normal recovery time or
use extra effort to try again. +1 cost per rank.

Perception: Applied to Ranged Healing (following), Per-
ception Ranged Healing does not require an attack check
to “touch” the subject. +1 cost per rank.

Persistent: Your  Healing  can  remove  even  Incurable  ef-
fects (see the Incurable modifier). Flat +1 point.

Ranged:  Ranged  Healing  requires  an  attack  check  to
“touch” the subject with the Healing effect. The GM may
waive the check for a willing subject holding completely
still, but the subject is defenseless that round, making it an
unwise decision in the midst of combat. +1 cost per rank.

recover from it normally. You can use Healing and Regen-
eration to cure your own conditions. You can have the Res-
urrection modifier for Healing, but if you successfully use
it, you die! This may not be as bad as it seems if you have
Immortality, allowing you to return to life (see the Immor-
tality effect for details). –1 cost per rank.

Limited: Examples of ways in which Healing may be Lim-
ited include: One Type of Damage (such as energy or blud-
geoning  damage),  Objects  (in  conjunction  with  Affects
Objects), Others (you can’t use Healing on yourself), or Self
(you can only use Healing on yourself). –1 cost per rank.

Temporary:  The  benefits  of  your  Healing  are  temporary,
lasting for one hour. The subject the

[... truncated ...]
```

**Chunk 24** (`fe13616b260d`):

```
CHAPTER 6: POWERS

153

CREATE

CONTROL

Action: Standard • Range: Ranged
Duration: Sustained • Cost: 2 points per rank

You  can  form  solid  objects  essentially  out  of  nowhere.
They may be made of solidified energy, “hardened” water
or  air,  transmuted  bulk  matter,  ice,  stone,  or  some  other
medium, depending on the effect’s descriptors.

You  can  form  any  simple  geometric  shape  or  common
object (such as a cube, sphere, dome, hammer, lens, disk,
etc.). The GM has final say on whether or not a particular
object  is  too  complex  for  this  effect.  Generally,  your  ob-
jects  can’t  have  any  moving  parts  more  complex  than  a
hinge. They can be solid or hollow, opaque or transparent,
as  you  choose  when  you  use  the  effect,  limited  by  your
descriptors and the Gamemaster’s judgment.

You  can  create  an  object  with  a  maximum  volume  rank
equal to your effect rank and Toughness equal to your ef-
fect rank. Created objects can be damaged or broken like
ordinary objects. They also vanish if you stop maintaining
them. You can repair any damage to a created object at will
by using your effect again (essentially “re-creating” the ob-
ject). Your created objects are stationary once you have cre-
ated them, although other effects can move them. Assume
a created object has a mass rank equal to its volume rank.
OBJECTS, COVER, AND CONCEALMENT

A created object can provide cover or concealment (if the
object is opaque) just like a normal object. Cover provided
by a created object can block incoming attacks, but blocks
outgoing attacks as well. Attacks hitting the covering ob-
ject  damage  it  normally  (see  Damaging  Objects,  page
244). Indirect effects can bypass the cover a created object
provides just like any other cover (see the Indirect modi-
fier). The Selective modifier allows you to vary the cover
and concealment your objects provide.

You can trap a target inside a large enough hollow ob-
ject (a cage or bubble, for example). This requires both
an attack check against the target’s Dodge and a Dodge
resistance  check  against  the  effect’s  rank.  A  trapped

HOOD: CREATE VS. SUMMON

Create  and  Summon  are  similar  effects:  both  “create”
things out of nowhere. So when should a character have
one and not the other?

Generally, Create makes inanimate objects, while Sum-
mon  conjures  creatures  of  some  sort,  capable  of  inde-
pendent  action  (albeit  limited  in  the  case  of  mindless
creatures  like  ro

[... truncated ...]
```

---

## Concept: Area Damage

Chunk count: 1
Receives actions: ['act_0312']

### Chunk texts

**Chunk 1** (`25d04efd242a`):

```
CHAPTER 6: POWERS

187

ply to at least one rank, and may apply to as many ranks as
the effect has. The change in cost and effect applies only
to the ranks with the modifier; the unmodified ranks have
their normal cost and effect.

Example:  Caliber’s  micro-rockets  are  a  Damage  7
effect. They also explode on impact, for a Burst Area
Damage  effect,  but  the  Area  Damage  is  only  rank
4. So the first 4 ranks of the Caliber’s Damage effect
have the Burst Area modifier, costing 1 point more (or
3 per rank). The remaining 3 ranks have their usual
cost (2 per rank). Caliber makes a normal ranged at-
tack check against the main target for his micro-rock-
et launcher; if he hits, the target has to resist Damage
7, and everyone within the area around the target re-
sists Damage 4 (the Area Damage). Even if he misses,
the main target has to resist the Area Damage 4, since
the micro-rocket explodes close by! In Caliber’s busi-
ness, it pays to cover your bases...

MODIFIERS

Some modifiers, rather than increasing or decreasing an ef-
fect’s cost per rank, have a flat value in power points, noted
as flat in the modifier’s header. For example, the Subtle extra
costs only 1 or 2 points, depending on how subtle the effect
is. Likewise, the Activation flaw has a flat value of –1 or –2
points, depending on how long the power takes to activate.

Flat-value modifiers are applied to the final cost of an effect,
after its cost per rank and total cost for its number of ranks
is determined. So, for example, if an effect costs 2 points per
rank, with +1 per rank for extras and –2 per rank for flaws.
It has a final adjusted cost of (2 + 1 – 2) or 1 point per rank.
With 8 ranks, it costs 8 power points. If the same effect also
has a flat-value extra costing 2 points and a flat-value flaw
worth –1 point, then you add 2 to the final cost and sub-
tract 1, for a total of (8 points for the effect + 2 points for the
flat extra – 1 point for the flat flaw) or 9 power points.
modified cost + flat extra value -
flat flaw value

tion). When  an  effect  is  used  against  a  corporeal  target,
the effect’s rank is equal to the rank of this extra, up to a
maximum of the effect’s full rank. Characters with lower
ranks  1–3  of  Insubstantial  do  not  require  this  extra  for
their effects to work on the physical world, although they
can apply it to their Strength rank to allow them to exert
some Strength while Insubstantial.

FLAT • 1 OR 2 POINTS

An  effect  with  this  extra  wo

[... truncated ...]
```

---

## Concept: Area Nullify

Chunk count: 1
Receives actions: ['act_0267']

### Chunk texts

**Chunk 1** (`b054d3b34f13`):

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

---

## Concept: Armor

Chunk count: 1
Performs actions: ['act_0373']

### Chunk texts

**Chunk 1** (`c9e9523951b6`):

```
CHAPTER 7: GADGETS & GEAR

219

ITEM

EFFECT

GRENADES

DC

COST

Fragmentation

Ranged Burst Area Damage 5

Smoke

Flash-bang

Sleep gas

Tear gas

Dynamite

Plastic explosive

Ranged Cloud Area Concealment Attack 4

Ranged Burst Area Dazzle 4

Ranged Cloud Area Sleep 4*

Ranged Cloud Area Affliction 4*

Ranged Burst Area Damage 5

Ranged Burst Area Damage 10

* = See individual descriptions for more information.

15

14

14

14

14

15

20

15

12

16

12

16

15

30

Suppressor: A suppressor muffles the noise of a ballistic
weapon, giving it Subtle 1 and making it difficult (DC 20)
for normal hearing to detect it.

Targeting Scope: A targeting scope gives a weapon the
benefits  of  the  Improved  Aim  advantage,  doubling  the
normal benefits of aiming.

Fragmentation  grenade:  A  common  military  grenade
that sprays shrapnel in all directions.

Smoke grenade: A smoke grenade fills an area with thick
smoke  (colored  as  desired)  providing  total  concealment
to all visual senses.

Flash-bang  grenade:  A  flash-bang  grenade  gives  off  a
bright flash and a loud bang that can render targets tem-

porarily blind and deaf. A flash grenade affects only vision
and costs 12 points.

Sleep gas grenade: This grenade releases a gas with an
Affliction (Sleep) effect.

Tear gas grenade: This type of grenade releases a cloud
of  gas  that  irritates  the  eyes  and  lungs,  causing  tempo-
rarily blindness and nausea (an Affliction with dazed and
visually impaired, stunned and visually disabled, and inca-
pacitated effects).

Dynamite: A common explosive. The damage on the ta-
ble is for a single stick of dynamite. Each doubling of the
amount of explosive increases Damage rank by 1.

Plastic explosive: Another common explosive, which can
be worked into different shapes. The damage listed is for
a 1-lb block. Each doubling of the amount of explosive in-
creases Damage rank by 1.

ARMOR

With so many weapons and super-powered attacks around, characters may need armor to protect them. Some heroes
are innately tough enough to stand up to a lot of punishment, while others rely on their high Dodge and Parry ranks.
Others choose to wear armor, ranging from ancient metal armors to modern composites or ultra-modern battlesuits.

Armor provides a Protection effect, a bonus to Toughness. Like other equipment, armor bonuses do not stack with other
armor or effect bonuses, only the highest bonus applies, one of the reasons why tough heroes rarely, if ever, wear armor.
Tou

[... truncated ...]
```

---

## Concept: Array

Chunk count: 20
Performs actions: ['act_0319']
Receives actions: ['act_0079']

### Chunk texts

**Chunk 1** (`1081db3c43af`):

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

**Chunk 2** (`13ce58f9b33f`):

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

**Chunk 3** (`17270869c240`):

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

**Chunk 4** (`19a54c3b3576`):

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

**Chunk 5** (`1b8011530852`):

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

**Chunk 6** (`3e277f7add29`):

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

**Chunk 7** (`44f0396c2518`):

```
CHAPTER 6: POWERS

163

Insight  check.  Senses  with  the  Counters  Illusion  effect
(see Senses) automatically detect illusions. If any viewer
successfully uncovers an illusion and communicates this
fact to others, they gain another Insight check with a +5
circumstance bonus. Circumstances may grant additional
modifiers to the Insight check to uncover an illusion, de-
pending on how convincing it is.

Maintaining an active illusion (such as a fighting creature)
requires a standard action each round, but maintaining a
static illusion (one that doesn’t move or interact) is only a
free action.

EXTRAS

Illusion is a broad-ranging effect, usable for a number of
different things. A few common considerations for Illu-
sion include the following.

Independent: Your active illusions only require a free action
to maintain, rather than a standard action. +1 cost per rank.

Selective:  You  choose  who  perceives  your  Illusion  and
who doesn’t. +1 cost per rank.

For illusions so realistic they are capable of inflicting dam-
age, add a Linked Perception Range Damage effect. At the
GM’s discretion, this effect can even be made into a Linked
Array  with  a  variety  of  alternate  attack  effects,  allowing
your illusionist to inflict conditions other than damage on
targets. Keep in mind the attack effects all need to be per-
ception range to match the range of Illusion.

Illusion  can  alter  a  subject’s  appearance,  providing  an
essentially impenetrable disguise—at least until some-
one  makes  a  successful  check  to  see  through  the  illu-
sion.  However,  for  just  the  ability  to  alter  appearance,
use the Morph effect, which is generally more effective
than Illusion Limited to Appearance.

The  default  Illusion  effect  is  perceptible  to  anyone  or
anything  (including  machines)  as  if  it  were  real.  Some
illusions exist solely in the mind, like projected psychic
hallucinations. This type of Illusion has the Resistible by
Will flaw and the Selective extra, since the illusionist can
choose whether or not to project the illusion into a par-
ticular subject’s mind, and therefore decides who can or
cannot perceive the illusion. This is a net +0 modifier, for
the same base cost.
MY ALLY, MY ENEMY

A common Illusion trick is to switch the appearances of
an  enemy  and  an  ally,  causing  a  foe’s  teammate  to  at-
tack  that  enemy  by  mistake. You  can  generally  handle
this with an opposed check of Illusion and Insight; if you
win, the tar

[... truncated ...]
```

**Chunk 8** (`6717e2899e27`):

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

**Chunk 9** (`685941d4ae65`):

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

**Chunk 10** (`8558df91a0a1`):

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

**Chunk 11** (`85cc7f979174`):

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

**Chunk 12** (`8ad0833a1563`):

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

**Chunk 13** (`aa943c38ef67`):

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

**Chunk 14** (`b511fe78f53a`):

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

**Chunk 15** (`c0c1858f03fe`):

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

**Chunk 16** (`cfadcb33d64b`):

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

**Chunk 17** (`e087f7a0b70b`):

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

**Chunk 18** (`eab98ce0e1fc`):

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

**Chunk 19** (`fd5ed2485118`):

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

**Chunk 20** (`138e63aeed36`):

```
CHAPTER 6: POWERS

189

Arrays—collections of Alternate Effects—are one of the more complex and important constructs in MUTANTS & MASTERMINDS
and require some special care in terms of their creation and use. Players should take these things into account when
creating characters with arrays, and Gamemasters should consider them when approving such characters and dealing
with them in play.

The main reason for the Alternate Effect modifier is to allow a degree of flexibility in terms of a character’s power effects
within the cost restrictions laid down by having a finite number of power points. It’s based on the assumption that a wide
range of powers has a diminishing return in terms of value, since characters can only use so many effects at once. A power
with various “settings,” usable one at a time, is more valuable than a power with only one, but not as valuable as various
effects all usable at the same time.

However, Alternate Effect can be abused to try and squeeze the most “efficiency” out of a character’s power points, gain-
ing the most effects for the lowest cost. The guidelines for Alternate Effects are intended to help limit this somewhat, but
there is no way they can eliminate the possibility entirely and still provide all the benefits of flexibility they’re intended to
offer. Some Gamemaster oversight is therefore necessary when it comes to the creation and use of arrays.

Before giving a character Alternate Effects, it is wise to ask, “Is an array really needed for this concept?” Some concepts,
such as a variety of different attacks, clearly call for an array. Others, like a power with a few rarely used stunts, may not call
for an array. Such a power may be better served by acquiring such occasional stunts through extra effort and the spend-
ing of hero points rather than the creation of a permanent set of Alternate Effects. That is what the power stunts rules are
for, after all: so you do not have to fill up character sheets with minor Alternate Effects a hero will rarely ever use.

If you decide an array is appropriate, the first thing is to determine its overall theme and associated descriptors. Is it an ar-
ray of different attacks, like a “weapons array” of a battlesuit? Is it a collection of regular power stunts for a themed power
like earth control, or spells for magic? Is it a series of alternate forms for a metamorph? And so forth. Arrays should have
some unifying theme beyond “all the powers I want my hero to have,” and Gamemasters s

[... truncated ...]
```

---

## Concept: Assessment

Chunk count: 1
Performs actions: ['act_0045']

### Chunk texts

**Chunk 1** (`e5eb32b8480c`):

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

---
