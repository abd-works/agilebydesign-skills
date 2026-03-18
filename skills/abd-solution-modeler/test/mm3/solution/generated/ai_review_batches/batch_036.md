# Hypothesis concept review – batch 36

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

## Concept: Security System

Chunk count: 10

### Chunk texts

**Chunk 1** (`03bc5d87aec7`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

The headquarters is equipped with an automatic system
for  detecting  and  extinguishing  fires.  Any  large  open
flame  sets  the  system  off  (beware,  fire-using  heroes!).  It
functions as a Nullify Fire 5 effect. A computer-controlled
fire prevention system can be programmed to ignore cer-
tain sources of fire or the system can be placed on manual
control (requiring someone to throw a switch in order to
activate it).

GARAGE

A garage houses ground vehicles and includes a ramp, el-
evator, or other access to move vehicles in and out, facili-
ties for repairing and maintaining vehicles, and a sliding
access door.
GROUNDS

In addition to the actual building(s) of the headquarters, it
has a considerable area of land surrounding it. An HQ can
have  surrounding  land  of  one  size  category  larger  than
the structure at no cost, without having this feature. Hav-
ing it allows for grounds up to three size categories larger
than the structure, so a large mansion headquarters could
have a colossal area of land.

If the headquarters has features like Defense System and
Security System, they also extend over the grounds (with
fences, sensors, weapon emplacements, and so forth).

GYM

A  gym  consists  of  weight-training  and  other  exercise
machines,  space  for  working  out,  stretching,  and  similar
exercises, and all the necessary amenities (lockers, show-
ers, etc.). Some HQs may incorporate the gym feature into
the combat simulator, for a multi-purpose training room.
A gym may also include a pool (heated or unheated, good
for  aquatic  characters),  possibly  even  connected  to  an
outside  body  of  water,  to  the  base’s  dock,  or  both  at  no
additional cost.

HANGAR

A hangar houses air and space vehicles. It includes a hatch
and/or runway for the vehicles to launch and facilities for
repairing and maintaining flying vehicles. For some HQs
the launch facilities of the hangar may require a long tun-
nel or other access to the outside.

These are cells for holding prisoners, usually temporarily,
although  some  headquarters  might  have  more  perma-
nent holding facilities. The cells are equipped with Nul-
lify devices (ranked at the HQ power level) or their basic
Toughness is increased by 50%, which option should be
agreed  upon  by  both  player  and  GM  (both  options  for
two  features).  Heroes  use  holding  cells  to  contain  cap-
tured villains until th

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

**Chunk 3** (`1081db3c43af`):

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

**Chunk 4** (`1af862ab5396`):

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

**Chunk 5** (`75c6a0d7757a`):

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

**Chunk 6** (`8ad0833a1563`):

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

**Chunk 7** (`ab446868e7fe`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

SEA-BASE

Gamemasters can use the following sample headquarters
as ready-made lairs for supervillains while players can use
them as bases for their heroes.

Size: Gargantuan Toughness: 14 Features: Communications,
Computer, Concealed, Dock, Fire Prevention System, Isolated,
Living Space, Power System, Security System • 16 points.

SKYSCRAPER (5 FLOORS)

Size:  Medium  Toughness:  8  Features:  Communications,
Computer,  Concealed,  Garage,  Gym,  Living  Space,  Power
System, Security System • 10 points.

Size:  Large  Toughness:  10  Features:  Communications,
Computer,  Defense  System,  Fire  Prevention  System,  Gym,
Hangar,  Infirmary,  Laboratory,  Library,  Living  Space,  Power
System, Security System, Workshop • 17 points.

MOON-BASE

Size:  Awesome Toughness:  20  Features:  Combat  Simulator,
Communications, Computer, Defense System, Fire Prevention
Isolated,
System,  Gym,  Hangar,  Holding  Cells,
Laboratory, Living Space, Power System, Security System (DC
25), Teleport (Affects Others), Workshop • 28 points.

Infirmary,

Size:  Huge  Toughness:  10  Features:  Communications,
Computer,  Concealed,  Dock,  Garage,  Gym,  Hangar,  Infirmary,
Laboratory,  Library,  Living  Space,  Power  System,  Security
System, Workshop • 19 points.

Size:  Colossal  Toughness:  20  Features:  Combat  Simulator,
Communications, Computer, Defense System, Fire Prevention
System,  Gym,  Hangar,  Holding  Cells,
Isolated,
Laboratory,  Living  Space,  Power  System,  Security  System,
Teleport (Affects Others) • 25 points.

Infirmary,

Size:  Huge  Toughness:  14  Features:  Communications,
Computer, Concealed, Defense System, Garage, Holding Cells,
Isolated,  Laboratory,  Library,  Living  Space,  Power  System,
Security System • 19 points.

Size: Medium Toughness: 10 Features: Concealed, Dual-Size
(Huge),  Laboratory,  Library,  Living  Space,  Security  System,
Workshop • 12 points.

Size:  Large  Toughness:  12  Features:  Combat  Simulator,
Communications,  Computer,  Concealed,  Defense  System,  Fire
Prevention System, Garage, Gym, Holding Cells, Infirmary, Living
Space, Power System, Security System, Workshop • 22 points.

Armored robots, humanlike androids, even magically-animated golems or zombies are all examples of constructs, non-
living things capable of acting on their own to one degree or another, carrying out pre-programmed instructions, or
even possessing independent th

[... truncated ...]
```

**Chunk 8** (`d5fc086574e9`):

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

**Chunk 9** (`dcdc4c459ab6`):

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

**Chunk 10** (`eab98ce0e1fc`):

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

## Concept: Selective

Chunk count: 22
Performs actions: ['act_0182', 'act_0267']
Receives actions: ['act_0209', 'act_0333']

### Chunk texts

**Chunk 1** (`068f6ea2c39b`):

```
CHAPTER 6: POWERS

191

•

•

ter of the burst. This immunity does not apply to other
effects, nor does it extend to anyone else: for that, ap-
ply the Selective extra. If the user wants to be affected
at the same time, increase cost per rank by +1. An ex-
ample would be a Close Burst Area Healing effect that
included the user along with everyone else in the area.
This is the equivalent of the +1 Affects Others modifier.

Ranged:  A  ranged  area  effect  can  be  placed  any-
where within the effect’s range, extending to fill the
area’s volume from the origin point.

Perception: A perception area effect can be placed
anywhere  the  user  can  accurately  perceive.  Percep-
tion area effects neither require an attack check nor
allow a Dodge resistance check, although targets still
get a normal resistance check against the effect. Per-
ception  area  effects  are  blocked  by  either  conceal-
ment or cover; choose one when acquiring the effect.
For concealment, if the attacker can’t accurately per-
ceive a target in the area, it is unaffected. Thus even
heavy smoke or darkness can block the effect. Effects
blocked by cover are much like conventional area ef-
fects:  solid  barriers  interfere  with  the  effect,  even  if
they are transparent, but the effect ignores conceal-
ment like darkness, shadows, or smoke. Only targets
behind total cover are unaffected.

Example: Mastermind has a Burst Area Affliction, al-
lowing him to seize control of the minds of everyone
in  the  affected  area.  He  must  be  able  to  accurately
perceive a target to control it; an invisible foe or one
out of his line of sight, for example, would be unaffect-
ed, even if they were within the area of the burst. On
the other hand, targets behind a glass wall or invisible
force field are affected, since Mastermind can perceive
them. Conversely, Fear-Master has a Burst Area Afflic-
tion as well—his fear-inducing gas. Targets behind a
solid barrier (such as on the other side of that glass
wall or invisible shield) are unaffected, but the unseen
or concealed target is, even though Fear-Master can’t
perceive him, since the gas still reaches them.

ATTACK

+0 COST PER RANK

This  extra  applies  to  personal  range  effects,  making
them into attack effects. Examples include Shrinking and
Teleport, causing a target to shrink or teleport away, re-
spectively.  Unlike  most  extras,  the  effect’s  cost  does  not
change, although it does work differently.

The  effect  no  longer  works

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

**Chunk 4** (`1094aa03eba1`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

Example:  Captain  Thunder  has  the  ability  to  hurl
thunderbolts  that  shock  their  targets  with  electric-
ity and deafen them with powerful claps of thunder.
This  is  a  Ranged  Damage  effect  (lightning),  cost-
ing 2 points per rank, Linked to a Ranged Affliction
(deafening thunder), costing 2 points per rank. The
combined effect costs 4 points per rank.Since both
effects  are  ranged  and  require  a  standard  action
to use, so does the combined effect. Since Damage
requires a Toughness check and Affliction requires a
Dodge check, the target checks against them sepa-
rately, making a Toughness resistance check against
the damage of the lightning and a Dodge check to
avoid being deafened by the thunder. Since the two
effects are Linked, Captain Thunder cannot throw a
lightning  bolt  without  the  deafening  thunderclap,
nor can he attempt to merely deafen a target with-
out  also  hitting  them  with  lightning!  (To  do  these
things,  Cap  might  take  the  stand-alone  effects  as
Alternate Effects.)

+1 COST PER RANK

A Multiattack effect allows you to hit multiple targets, or a
single target multiple times, in the same standard action.
Multiattack  can  apply  to  any  effect  requiring  an  attack
check. There are three ways in which a Multiattack effect
can be used:

To  use  a  Multiattack  against  a  single  target,  make  your
attack check normally. If successful, increase the attack’s
resistance check DC by +2 for two degrees of success, and
+5  for  three  or  more. This  circumstance  bonus  does  not
count against power level limits.

If  an  Impervious  Resistance  would  ignore  the  attack  be-
fore any increase in the DC, then the attack still has no ef-
fect as usual; a volley of multiple shots is no more likely to
penetrate Impervious Resistance than just one.

You can use Multiattack to hit multiple targets at once by
“walking” or “spraying” the Multiattack across an arc. Roll
one  attack  check  per  target  in  the  arc. You  suffer  a  pen-
alty to each check equal to the total number of targets. So
making a Multiattack against five targets is a –5 penalty
to each attack check. If you miss one target, you may still
attempt to hit the others.

by  your  covering  attack  at  the  cost  of  being  automati-
cally  attacked  by  it;  make  a  normal  attack  check  to  hit
that opponent.

FLAT • 1 POINT PER RANK

Your effect overcomes Impervious Resistance to a deg

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

**Chunk 6** (`301534069c2d`):

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

**Chunk 7** (`3e277f7add29`):

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

**Chunk 8** (`437f5039e60f`):

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

**Chunk 9** (`44f0396c2518`):

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

**Chunk 11** (`6e58428e1e90`):

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

**Chunk 12** (`72dc60c2e6cf`):

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

**Chunk 13** (`8757660124bd`):

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

**Chunk 14** (`9b4ab26032fa`):

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

**Chunk 15** (`afba8b4a5938`):

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

**Chunk 16** (`b054d3b34f13`):

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

**Chunk 17** (`cf5b8ba8408b`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

Effect: Damage, Reaction • 4 points per rank

Effect: Ranged Damage • 2 points per rank

You can surround your body with an aura of damaging
energy or some similar effect. Anyone you touch or that
touches you must make a Toughness resistance check
against your aura’s Damage rank. You can turn your aura
on and off at will as a free action. If your Aura damages
some targets but not others, apply the Selective or Lim-
ited modifiers (depending on whether or not the selec-
tivity is under your control).

Reduced Trait: One or more of your traits is lowered while
others  are  enhanced. This  flaw  is  worth  as  many  points
as  the  reduction  in  the  affected  trait(s).  So,  for  example,
if you lose Intellect while you gain in Strength, treat the
value  of  the  lost  Intellect  ranks  as  the  value  of  the  flaw.
As with all flaws, the effect must still cost at least 1 power
point. Flat –points equal to the lowered trait.

You can generate and project a type of energy, such as
cold, electricity, fire, kinetic force, magnetism, radiation,
or  even  cosmic  energy,  in  a  damaging  blast  (see  the
Blast power).

Energy Control is further defined by the addition of Alter-
nate Effects (see Alternate Effects, page 188), expand-
ing what you can do with your control. For example, Cold
Control  might  let  you  lower  the  surrounding  tempera-
ture (Environment – Cold) or trap targets in ice (Affliction,
see  the  Snare  version).  Magnetic  Control  could  let  you
manipulate metallic objects (Limited Move Object) while
Electrical Control lets you generate an electrical pulse to
overload electronics (Burst Area Nullify Electronics). Add
as many Alternate Effects to your Energy Control as you
can afford, and consider some additional ones as options
for power stunts (see Powers Stunts, page 20).

CONTROL

Action: Standard • Range: Rank
Duration: Sustained • Cost: 1–2 points per rank

You  can  change  the  environment  in  an  area:  raising  or
lowering  the  temperature,  creating  light,  causing  rain,
and so forth (see The Environment in the Action & Ad-
venture chapter for details).

Your  Environment  affects  a  30  foot  radius  around  you
at rank 1. Each additional rank moves the radius up one
distance rank, for a reach of approximately 2,000 miles at
rank  20,  sufficient  to  alter  the  environment  of  an  entire
continent!

Each of the following is a separate Environment effect. If
you 

[... truncated ...]
```

**Chunk 18** (`d4cad3e10e05`):

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

**Chunk 19** (`e17d1554782d`):

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

**Chunk 20** (`f1bc1ad153ee`):

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

**Chunk 21** (`fc4ed8309dc8`):

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

**Chunk 22** (`fe13616b260d`):

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

## Concept: Sense

Chunk count: 47
Receives actions: ['act_0276', 'act_0281', 'act_0282', 'act_0323', 'act_0338']

### Chunk texts

**Chunk 1** (`5731b0e9cb2f`):

```
CHAPTER 6: POWERS

177

1-4 RANKS

Senses  in  MUTANTS  &  MASTERMINDS  are  broken  down  into
sense types, used as descriptors for sensory effects. Here
are  the  traits  of  normal  human  senses,  for  use  when
modifying them with the options from Senses:

VISUAL

Normal  vision  is  ranged  (with  a  –1/10  feet  modifier),
acute (able to distinguish fine details) and accurate (able
to pinpoint the locations of things).
AUDITORY

Normal hearing is ranged  (with  a –1/10  feet modifier),
acute  (able  to  pick  up  details  like  differences  in  tone),
and radius (able to pick up on sounds coming from any
direction). Normal hearing is not accurate.

OLFACTORY

Normal  human  olfactory  senses,  which  lump  together
smell  and  taste  for  descriptor  purposes,  are  fairly  lim-
ited. Ordinary human olfactory senses are neither acute
nor accurate. The sense of smell is a radius sense, how-
ever, able to pick up on scents coming from any direc-
tion. Its “range” is quite limited, however, effectively only
close, except for especially strong scents.

TACTILE

The normal sense of touch is, by definition, close range.
It is accurate (in that you know the location of anything
you  can  touch)  and  radius  (in  that  you  can  feel  things
from any surface of your body).

MENTAL

In MUTANTS & MASTERMINDS terms, the “sixth sense” or men-
tal  sense  type  is  fairly  crude  in  normal  humans,  lim-
ited essentially to interactions with the Insight skill and
awareness of mental effects used directly on you. Thus it
is close range and has none of the Sense qualities.

horizon and physical barriers between you and the sub-
ject, unless it also Penetrates Concealment.

1 RANK

You can see in the infrared portion of the spectrum, allow-
ing you to see heat patterns. Darkness does not provide
concealment  for  objects  differing  in  temperature  from
their  surroundings.  If  you  have  the Track  effect,  you  can
track warm creatures by the faint heat trails they leave be-
hind. The Gamemaster is the final judge on how long the
trail remains visible.
VISION

1 RANK

You can view extremely small things. You can make Per-
ception checks to see tiny things nearby. Cost is 1 rank for
dust-sized  objects,  2  ranks  for  cellular-sized,  3  ranks  for
DNA and complex molecules, 4 ranks for atomic-sized. The
GM  may  require  an  Expertise  skill  check  to  understand
and interpret what you see.

4 RANKS

A sense with this trait is unaffected by concealment from

[... truncated ...]
```

**Chunk 2** (`5ec359de437f`):

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

**Chunk 3** (`02269b6c9ef6`):

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

**Chunk 4** (`0f75307c0dea`):

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

**Chunk 5** (`14dd371ce972`):

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

**Chunk 6** (`17270869c240`):

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

**Chunk 7** (`19a54c3b3576`):

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

**Chunk 8** (`2b9b77a24290`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

TYPE

ACTION

RANGE

DURATION

COST

Sensory

General

General

Attack

Attack

None

Move

Free

Standard

Standard

Personal

Personal

Personal

Ranged

Ranged

Permanent

Sustained

Sustained

Instant

Instant

—

—

—

Fortitude

Dodge

Movement

Free

Personal

Sustained

—

Standard

Standard

Standard

Free

Free

Move

Standard

Standard

Standard

Close

Ranged

Close

Instant

Instant

Sustained

Personal

See description

Personal

Sustained

Rank

Close

Personal

Close

Instant

Sustained

Sustained

Toughness

Fortitude

—

—

—

—

—

—

Instant

Fort. or Will

1 per rank

8 per rank

2 per rank

2 per rank

3 per rank

1 per rank

1 per rank

4 per rank

2 per rank

3 per rank

1 per rank

2 per rank

2-5 per rank

7 per rank

1 per rank

NAME

Senses

Shapeshift

Shrinking

Sleep

Snare

Speed

Strike

Suffocation

Summon

Attack

Attack

Control

Super-Speed

See description

Movement

Movement

Control

General

Attack

Swimming

Teleport

Transform

Variable

Weaken

RANGE

Each  effect  has  a  default  range,  which  may  be  changed
by modifiers.

•

•

•

•

•

Personal: The effect works only on you, the user.

Close: The effect can target anyone or anything you
touch. Touching an unwilling subject requires an un-
armed attack check against the subject’s Parry.

Ranged:  The  effect  works  at  a  distance,  limited  by
perception  and  path  and  requiring  a  ranged  attack
check against the subject’s Dodge defense. A ranged
effect has a short range of (rank x 25 feet), a medium
range  of  (rank  x  50  feet)  and  a  long  range  of  (rank
x 100 feet). Ranged attack checks at medium range
suffer  a  –2  circumstance  penalty,  while  ranged  at-
tacks at long range suffer a –5 circumstance penalty.
See the Action & Adventure chapter for details.

Perception: The effect works on any target you can
perceive  with  an  accurate  sense,  without  any  need
for an attack check. If you cannot accurately perceive
the target, you cannot affect it.

Rank:  The  effect’s  range  or  area  of  effect  is  deter-
mined by its rank, as given in its description.

DURATION

so.  If  you  are  incapable  of  taking  the  necessary  ac-
tion, or simply choose not to, the effect ends.

Sustained: You can keep a sustained effect going by
taking  a  free  action  each  round  to  do  so.  If  you  are
incapable  of  taking  the  necessary  action,  or  simply
choose not to, the effect ends.

C

[... truncated ...]
```

**Chunk 9** (`301534069c2d`):

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

**Chunk 10** (`3c75d5b04a0e`):

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

**Chunk 11** (`3e277f7add29`):

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

**Chunk 12** (`43d5c758bf78`):

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

**Chunk 13** (`442f2e5a5a37`):

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

**Chunk 14** (`44f0396c2518`):

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

**Chunk 15** (`634190f2dd84`):

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

**Chunk 16** (`661dd344a1d2`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

the  round  in  which  the  duration  ends.  So,  for  example,
an instant duration Affliction only lasts one round, while
a  sustained  duration  Affliction  lasts  until  no  longer  sus-
tained. –1 cost per rank.

Limited Degree: Your Affliction is limited to no more than
two degrees of effect. With two applications of this modi-
fier, it is limited to no more than one degree of effect. –1
cost per rank.

BURROWING

MOVEMENT

Action: Free • Range: Personal
Duration: Sustained • Cost: 1 point per rank

You can burrow through the ground, leaving a tunnel be-
hind if you choose. You move through soil and sand at a
speed rank equal to your Burrowing rank, minus 5. So Bur-
rowing 8, for example, lets you move through the ground
at speed rank 3 (around 16 MPH). Burrowing through hard
clay and packed earth reduces speed one additional rank.
Burrowing through solid rock reduces it by two additional
ranks. The tunnel you leave behind is either permanent or
collapses behind you immediately (your choice when you
begin burrowing each new tunnel).

Note  that  Burrowing  differs  from  the  Permeate  effect  of
Movement, which allows you to pass through an obstacle
like the ground at your normal speed without disturbing
it at all (see Movement for details).
EXTRAS

Penetrating:  Normally,  the  hardness  of  the  ground  af-
fects  only  the  speed  at  which  you  burrow.  At  the  GM’s
discretion, some super-hard materials may be considered
Impervious to Burrowing, in which case this extra allows
you to dig through them. 1 point per rank.

Ranged: This extra either allows you to create tunnels at a
greater distance (without having to be at the end-point of
the tunnel as it forms) or, in conjunction with Affects Oth-
ers, allows you to grant the Burrowing effect to someone
else at a distance. Doing both requires two applications of
the extra. +1 or 2 cost per rank.

FLAWS

Limited:  Burrowing  may  be  limited  to  certain  circum-
stances  or  materials,  such  as  only  loose  sand  and  soil

BLAST

Effect: Ranged Damage • 2 points per rank

You  can  make  a  damaging  ranged  attack.  It  might  be
a  blast  of  energy,  a  projectile  (arrow,  bullet,  throwing
blade, etc.), or some similar effect. You make a ranged
attack  check  against  the  target’s  Dodge  defense.  The
attack’s damage equals your power rank and the target
makes a Toughness resistance check against it.

(leaving  the  character  una

[... truncated ...]
```

**Chunk 17** (`6805431193d6`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

1), Assault Rifle +5 (Ranged Damage 5, Multiattack). Defense:
Dodge  5,  Parry  5,  Fort  5, Tou  5/2, Will  1.  Totals:  Abilities 20 +
Powers 0 + Advantages 11 + Skills 9 + Defenses 8 = 48

This archetype covers the typical infantryman or enlisted
soldier. Specialists and officers have appropriate addition-
al training (and skills).

PL4

STR  0,  STA  1,  AGL  1,  DEX  0,  FGT  2,  INT  3,  AWE  2,  PRE  4
Equipment: Bulletproof vest (+4 Toughness vs. Ballistic), heavy
pistol,  cell  phone.  Advantages:  Benefit  5  (Millionaire,  Status:
Crime  Lord),  Connected,  Equipment  3,  Well-informed.  Skills:
Expertise: Criminal 8 (+11), Expertise: Streetwise 6 (+9), Expertise:
Current  Events  2  (+5),  Intimidation  6  (+10),  Perception  2  (+4),
Persuasion 4 (+8), Ranged Combat: Pistols 4 (+4). Offense: Init
+1, Unarmed +2 (Damage 0), heavy pistol +4 (Ranged Damage
4).  Defense:  Dodge  3,  Parry  3,  Fort  3,  Tou  5/1,  Will  5.  Totals:
Abilities 26 + Powers 0 + Advantages 10 + Skills 16 + Defenses 8 = 60

Sitting  on  top  of  the  criminal  underworld  are  the  crime
lords. These are men and women who’ve come up through
the ranks and now run the show. Physically a crime lord
is  no  match  for  a  hero,  but  their  connections,  resources,
and  knowledge  of  the  underworld  can  be  problematic.
The crime lord presented here is a fairly small fish; Game-
masters should make any changes needed to increase the
crime lord’s power and influence for the series.

CRIMINAL

PL2

STR  1,  STA  0,  AGL  2,  DEX  1,  FGT  1,  INT  1,  AWE  0,  PRE  1
Equipment: Leather jacket (+1 Toughness), light pistol, knife,
cell phone. Advantages: Equipment 2. Skills: Athletics 4 (+5),
Expertise:  Choose  One  4  (+5),  Expertise:  Streetwise  4  (+5),
Expertise:  Current  Events  2  (+3),  Perception  4  (+4),  Stealth
6  (+8),  Technology  4  (+5),  Vehicles  4  (+5).  Offense:  Init  +2,
Unarmed  +1  (Damage  1),  Knife  +1  (Damage  2,  Crit.  19-20),
Pistol +1 (Ranged Damage 3). Defense: Dodge 3, Parry 3, Fort
2, Tou 1/0, Will 0. Totals: Abilities 14 + Powers 0 + Advantages 2 +
Skills 16 + Defenses 5 = 37

This  archetype  represents  run-of-the-mill  career  crimi-
nals. Gamemasters should shuffle the criminal’s skill ranks
around to specialize as needed.

PL2

STR  1,  STA  0,  AGL  2,  DEX  1,  FGT  1,  INT  1,  AWE  0,  PRE  1
Equipment: Leather jacket (+1 Toughness), light pistol, knife,
cell phone. Advantag

[... truncated ...]
```

**Chunk 18** (`7419fe5693f8`):

```
CHAPTER 6: POWERS

175

use  perception  ranged  effects  via  your  Remote  Sensing.
Despite the built-in limitation, this is an extra, since it al-
lows you to use your Remote Sensing to observe subjects
in relative safety. +1 cost per rank.

Simultaneous:  You  can  use  both  Remote  Sensing  and
your normal senses at the same time, perceiving two lo-
cales like “translucent” overlays of each other. This means
you’re more capable of taking physical action while also
using  your  Remote  Sensing,  although  the  effect  still  re-
quires its normal duration to maintain. You are not vulner-
able while using your Remote Sensing. +1 cost per rank.

Subtle: Remote Sensing already has a degree of subtlety. Ap-
plying 1 rank of Subtle to Remote Sensing increases the DC
to notice the effect to 20 + rank or makes it noticeable only to
a particular unusual sense (with the usual DC 10 + rank per-
ception check). Subtle 2 makes Remote Sensing completely
unnoticeable, as usual. Flat +1 point per rank of Subtle.
FLAWS

Feedback:  With  this  flaw,  damaging  attacks  directed  at
where you displaced your senses can affect you. Your sen-
sory-point is considered to have partial cover from attacks
and you use your Remote Sensing rank as your Toughness
defense against any successful attack. The feedback may
be psychosomatic in nature or due to some sort of disrup-
tion  caused  by  an  assault  on  the  point  where  you  have
redirected your senses. Note that sensory effects already
work on you via Remote Sensing and this flaw doesn’t ap-
ply to them. –1 cost per rank.

Medium: You  require  a  medium  for  your  Remote  Sens-
ing, such as shadows, flames, mirrors, open water, televi-
sion screens, and so forth. You can only perceive locations
where your chosen medium exists. –1 cost per rank.

Noticeable: Remote Sensing with this flaw has an easily
noticeable display, like a glowing set of eyes or a phantom
image of your face, head, or body at the location you are
observing. This manifestation cannot be used for commu-
nication, however (for that, take the Communication ef-
fect). Flat –1 point.

Sense-Dependent:  Remote  Sensing  is  already  Sense-
Dependent  and  cannot  apply  this  flaw.  Another  effect
might potentially have the flaw Remote-Sensing Depen-
dent, such as an Affliction that targets only remote view-
ers observing a target or an area as a means of blocking or
deterring them.

SENSES

SENSORY

Action: None • Range: Personal
Duration: Permanent • Co

[... truncated ...]
```

**Chunk 19** (`75f616f43b9d`):

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

**Chunk 20** (`765269f2e7c2`):

```
CHAPTER 6: POWERS

169

Subtle:  As  a  mental  sensory  effect,  Mind  Reading  has  a
degree  of  subtlety,  only  noticeable  to  the  subject  or  to
characters  with  an  appropriate  mental  sense,  such  as
Mental  Awareness  (see  the  Senses  effect).  Subtle  Mind
Reading is less detectable, requiring a DC 20 Perception
check  for  either  type  of  character  to  sense  it,  while  two
ranks  of  the  Subtle  modifier  makes  your  Mind  Reading
completely undetectable. Flat +1 or 2 points.

FLAWS

Close: Applied to Ranged Mind Reading, Close Mind Read-
ing requires a close attack check to touch an unwilling tar-
get and physical contact throughout the effect’s duration;
breaking contact ends the effect. –1 cost per rank.

Feedback: You suffer Feedback if a subject you are reading
is harmed, using your Mind Reading rank as the resistance
check  bonus  against  the  damage.  Additionally,  you  may
suffer Feedback at the GM’s discretion from reading or ex-
periencing  particularly  traumatic  or  emotionally-charged
thoughts of memories from the subject. –1 cost per rank.

Limited by Language: You can only understand the sub-
ject’s thoughts or memories if you share a common lan-
guage. –1 cost per rank.

Limited to Emotions: You can only read or probe for emo-
tions and emotional associations, not coherent thoughts
or memories. –1 cost per rank.

Limited to Sensory Link: If you have the Sensory Link extra
and this flaw, you can only tap into a subject’s senses, you
cannot read their thoughts or memories. –1 cost per rank.

Limited to Surface Thoughts: You can only read surface
thoughts and cannot achieve higher degrees of contact.
–1 cost per rank.

Ranged: Ranged Mind Reading requires a ranged attack
check in addition to the effect’s normal resistance check.
–1 cost per rank.

Sense-Dependent: Your Mind Reading is dependent on
a  sense  other  than  just  having  to  accurately  sense  the
target, such as needing to see his expressions (Sight-De-
pendent), hear him speak (Hearing-Dependent), smell his
changes in biochemistry (Scent-Dependent), and so forth.
Alternately, it may be dependent on first being in Mental
Communication with the target (see Communication). –1
cost per rank.

MORPH

GENERAL

Action: Free • Range: Personal
Duration: Sustained • Cost: 5 points per rank

You can alter your appearance. Your traits do not change;
your new form is merely a cosmetic change. You gain a +20
bonus to Deception checks to disguise yourself as the fo

[... truncated ...]
```

**Chunk 21** (`7b2254220623`):

```
CHAPTER 6: POWERS

181

SNARE

Effect:  Ranged,  Cumulative  Affliction,  Extra  Condition,
Resisted by Dodge, Limited Degree • 3 points per rank

You can restrain a target with bonds of ice, glue, web-
bing, bands of energy, and so forth (whatever suits your
descriptors). The target makes a Dodge resistance check
against your effect DC. One degree of failure leaves the
target hindered and vulnerable, while two results in the
target becoming defenseless and immobilized. There is
no additional effect for three or more degrees of failure.

The resistance check to break out of a Snare is based on
Damage (including Strength Damage) or Sleight of Hand,
either breaking the effect or slipping out of it. This is part of
the power’s Alternate Resistance, with no change in cost.

Mental Link: You  have  a  mental  link  with  your  minions,
allowing you to communicate with them and issue orders
telepathically like the Communication Link effect (see the
Senses effects in this chapter). Flat +1 point.

Multiple  Minions:  You  can  summon  more  than  one
minion. Each application of this extra doubles your total
number of minions. So, for example, with Summon 6, you
summon a single 90-point minion. With Multiple Minions
1, you can summon two 90-point minions, with Multiple
Minions  2,  four  minions,  and  so  forth.  It  requires  a  stan-
dard action to summon each minion unless you also have
the Horde extra (see previous). +2 cost per rank.

STRIKE

Effect: Damage • 1 point per rank

You  inflict  additional  damage  in  close  combat.  Your
Strike  either  substitutes  for  your  Strength  damage  or
adds  to  it,  if  it  is  Strength-based,  see  the  Damage  ef-
fect for details. It might be claws, energy fields, focused
striking  strength,  or  something  similar,  depending  on
your  descriptors.  Close  combat  weapons  are  either
equipment or this power with the Removable flaw. See
the Gadgets & Gear chapter (following) for more infor-
mation.

Sacrifice: When you are hit with an effect requiring a resis-
tance check, you can spend a hero point to shift it to one
of your minions instead. The minion must be within range
of the effect and a viable target. Needless to say, this is not
a particularly heroic ability. In fact, the GM may wish to re-
strict  it  to  villains  or  non-player  characters  (in  which  case
a hero earns a hero point when a villain uses this extra to
avoid an effect by sacrificing a minion). Flat +1 point.

Variable  Type:  Minions  a

[... truncated ...]
```

**Chunk 22** (`800b98bbc634`):

```
CHAPTER 8: ACTION & ADVENTURE

237

less than ideal conditions. This section details some of the
hazards heroes may face.

FALLING

Criminals  often  lurk  in  the  darkness,  and  many  crimes
take  place  at  night.  Most  cities  are  lit  well  enough,  but
sometimes  heroes  run  into  areas  where  it’s  difficult  to
see. Poorly lit areas provide concealment. Characters with
Counters Concealment (Darkness) Senses or other appro-
priate Senses effects can ignore concealment penalties for
poor lighting.

Intense  heat  and  cold  wear  down  characters,  while  pro-
longed exposure to the elements can be extremely dan-
gerous.

Characters in hot or cold conditions must make Fortitude
checks (DC 10, +1 per previous check) to avoid becoming
fatigued.  Fatigued  characters  who  fail  a  check  become
exhausted, then incapacitated, at which point the charac-
ter’s condition becomes dying after another failed Forti-
tude check.

How  often  characters  have  to  make  Fortitude  checks  de-
pends on the conditions. Once an hour for uncomfortable
heat or cold (a hot summer day or cold winter day), once
per 10 minutes for intense heat or cold (a blazing desert or
arctic conditions), once a minute for extreme heat or cold
like the edge of a volcano or an arctic winter storm. Checks
are made at the end of each period of exposure. Truly in-
tense heat or cold—such as a blast furnace or touching liq-
uid nitrogen—inflicts direct damage like an attack.

Characters with the appropriate Immunity do not need to
make Fortitude checks for extreme temperatures.

Heroes  can  go  without  water  for  a  day.  After  this,  they
need to make a Fortitude check (DC 10, +1 per previous
check) each hour to avoid a level of fatigue. Heroes can go
without food for three days. After this, they must make a
Fortitude check (DC 10, +1 per previous check) each day
to  avoid  fatigue.  The  character  cannot  recover  until  he
gets  water  or  food.  Heroes  with  Immunity  to  Starvation
can go an unlimited time without food or water.

Characters can hold their breath for ten rounds (one min-
ute) plus a number of rounds equal to twice their Stamina.
After that time they must make a Fortitude check (DC 10)
each round to continue holding their breath. The DC in-
creases  by  +1  for  each  previous  success.  Failure  on  the
Fortitude  check  means  the  character  becomes  incapaci-
tated . On the following round the character is dying. A dy-
ing character cannot stabilize until

[... truncated ...]
```

**Chunk 23** (`83acf5380dc1`):

```
CHAPTER 7: GADGETS & GEAR

209

using the device beyond that, he must pay power points
to make the device part of his regular abilities. Otherwise
the GM can simply rule that the device is lost, reclaimed
by its owner, runs out of power, breaks down, or whatever,
and is therefore no longer accessible. Characters with the
Inventor  and  Artificer  advantages  can  create  temporary
devices for use in an adventure.

Gamemasters  may  require  characters  to  spend  a  hero
point to make temporary use of a device that doesn’t be-
long to them, similar to performing a power stunt without
suffering fatigue. This helps to limit the loaning and tem-
porary use of devices.

A  common  staple  of  comic  books  is  the  battlesuit,  also
known  as  power-armor.  It  is  an  advanced  suit  of  tech-
nological  (sometime  magical)  armor,  giving  the  wearer
various powers. Battlesuits commonly grant the following
powers:

•

•

•

Armor:  Protection  is  the  foundation  power  for  a
battlesuit. Whether it is armor plating, metallic mesh,
flexible  ballistic  material,  or  some  combination  of
these and other cutting-edge technologies, a battle-
suit  protects  its  wearer  from  damage.  Some  battle-
suits provide Impervious Protection and some have
Sustained  Protection  in  the  form  of  built-in  force
fields or the like.

Attacks:  Battlesuits  are  typically  equipped  with
some kind of weapon or weapons, based around var-
ious attack effects, particularly Damage. A battlesuit
with an array of weapons may have a primary attack
effect and several others as Alternate Effects (see the
Alternate Effect modifier in the Powers chapter).

Immunity: A part of the protection a battlesuit offers
is  a  sealed  environment,  offering  Immunity  to  vari-
ous conditions and hazards.

•  Movement:  After  defense  and  offense,  battlesuits
typically allow the wearer to get around, whether it’s
hydraulic-assisted  Leaping,  boot-jets  or  anti-gravity
repulsion for Flight, turbines for Swimming, or some

other movement effect.

•

Sensors:  Battlesuits  often  come
equipped with a suite of sensors providing
Senses. Darkvision, direction sense (pos-
sibly from a global positioning system),
infrared vision, radio, time sense (from
a  chronometer),  and  ultra-hearing  are
all common battlesuit sensors.

•  Strength: A battlesuit might have ser-
vomotors  or  other  mechanisms  to  mag-
nify  the  wearer’s  Strength. This  is  typically  a
combination of Enhanced Stren

[... truncated ...]
```

**Chunk 24** (`85cc7f979174`):

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

**Chunk 25** (`872471930ea9`):

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

**Chunk 26** (`8757660124bd`):

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

**Chunk 27** (`9b8b75c1b5e7`):

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

**Chunk 28** (`9c685bbd4830`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

FLAWS

NAME

COST

Activation

–1-2 flat points

Effect requires a move (1 point) or standard (2 points) action to activate.

Check Required

–1 flat per rank

Must succeed on a check to use effect.

Concentration

–1 per rank

Sustained effect becomes concentration duration.

Diminished Range

–1 flat per rank

Reduces short, medium, and long ranges for the effect.

Distracting

Fades

Feedback

Grab-Based

–1 per rank

–1 per rank

–1 per rank

–1 per rank

Increased Action

–1-3 per rank

Limited

Noticeable

Permanent

Quirk

–1 per rank

–1 flat point

–1 per rank

Vulnerable while using effect.

Effect loses 1 rank each time it is used.

Suffer damage when your effect’s manifestation is damaged.

Effect requires a successful grab attack to use.

Increases action required to use effect.

Effect loses about half its effectiveness.

Continuous or permanent effect is noticeable.

Effect cannot be turned off or improved with extra effort.

–1 flat per rank

A minor flaw attached to an effect. The opposite of a Feature.

Reduced Range

–1-2 per rank

Effect’s range decreases.

Removable

Resistible

Sense-Dependent

Side Effect

Tiring

Uncontrolled

Unreliable

–1-2/5 flat points

Effect can be taken away from the user.

–1 per rank

–1 per rank

–1-2 per rank

–1 per rank

–1 per rank

–1 per rank

Effect gains a resistance check.

Target must be able to perceive the effect for it to work.

Failing to use the effect causes a problematic side effect.

Effect causes a level of fatigue when used.

You have no control over the effect.

Effect only works about half the time (roll of 11 or more).

Example: A spellcaster has Senses 4 (Detect Magic,
Ranged,  Acute,  Analyze)  with  Expertise:  Magic
Check Required 4. The player needs to make a DC
13 skill check (10 + 3 additional ranks) to success-
fully cast the spell, followed by the normal Percep-
tion check to pick up on anything present, and per-
haps another Expertise check to interpret what the
character senses.

Skill checks an effect may require include:

Acrobatics: Suitable for effects requiring a measure
of coordination or complex maneuvering.

Deception:  Good  for  effects  intended  to  deceive,
particularly sensory effects like Concealment or Illu-
sion, and disguise or form-altering effects like Morph.

Expertise:  An  Expertise  skill  check  might  represent
having  to  know  something  about  the  subject  of  the
effect or having to kno

[... truncated ...]
```

**Chunk 29** (`a67593d532fb`):

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

**Chunk 30** (`ab9b367b750f`):

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

**Chunk 31** (`ac75d3f2b9e6`):

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

**Chunk 32** (`b511fe78f53a`):

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

**Chunk 33** (`b60c97b07a3c`):

```
CHAPTER 6: POWERS

179

Effect: Variable (assumed forms), Move Action • 8 points
per rank

You  can  transform  into  different  forms,  gaining  the
physical  traits  (abilities,  skills,  advantages,  and  pow-
ers) of the assumed form. You gain (Shapeshift rank x 5)
power points worth of traits. You can also redistribute
points spent on your own physical traits (lowering your
Strength to apply those points elsewhere, for example).
You are limited to the inherent traits of the forms you
assume and do not gain new mental traits, even if that
form possesses them.

Shapeshift is often further Limited by the specific types
of forms the character can assume, such as Limited to
Animals or Limited to Machines.

ter’s perceptions are unreliable, the sense appears to work,
but the character gets the wrong information. For this rea-
son, the GM should make all reliability checks for Senses
in secret, just informing the player of what the character
does (or does not) notice. –1 cost per rank.

SHRINKING

GENERAL

Action: Free • Range: Personal
Duration: Sustained • Cost: 2 points per rank

You can temporarily decrease your size, becoming smaller,
harder to see — and hit — at the cost of losing Strength
and  speed.  Every  4  ranks  of  Shrinking  reduces  your  size
rank by 1 (normal humans are size rank –2 by default) and
each reduction in size rank subtracts 1 from your Strength
and every two reductions in size rank subtract 1 from your
ground speed rank. Add half your Shrinking rank (rounded
down)  to  your  active  defenses.  Add  your  Shrinking  rank
as a bonus to Stealth checks, since you are harder to spot,
but apply half your rank (rounded down) as a penalty to In-
timidation checks (hard to be imposing when you’re tiny).
Shrinking modifiers are restricted by power level limits.

So  at  Shrinking  12,  you  are  size  rank  –5  (about  6  inches
tall),  and  have  a  +6  bonus  to  active  defenses  and  +12
Stealth bonus, but –3 Strength, –1 speed, and –6 Intimida-
tion penalties.
EXTRAS

Atomic: At Shrinking 20 (and size rank –7), you can shrink
down to the molecular or even atomic level, allowing you
to pass through solid objects by slipping between their at-
oms. It takes at least a full turn to do so, possibly longer for
larger objects. You’re effectively immune to damage and
many effects at this scale, since you are essentially shifted
out of the ordinary universe. The GM decides if a particular
effect can reach you at the atomic level. If you have 

[... truncated ...]
```

**Chunk 34** (`b95c26d52ee0`):

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

**Chunk 35** (`bc6e8d2fe577`):

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

**Chunk 36** (`c0c1858f03fe`):

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

**Chunk 37** (`c84a4002269b`):

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

**Chunk 38** (`cefb93c1d699`):

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

**Chunk 39** (`d329357e5091`):

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

**Chunk 40** (`d4cad3e10e05`):

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

**Chunk 41** (`d5fc086574e9`):

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

**Chunk 42** (`dcdc4c459ab6`):

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

**Chunk 43** (`dd5713402cfd`):

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

**Chunk 44** (`e087f7a0b70b`):

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

**Chunk 45** (`e17d1554782d`):

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

**Chunk 46** (`eab98ce0e1fc`):

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

**Chunk 47** (`ffb72d59f44c`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

-1 OR -2 COST PER RANK

An effect has a range of close, ranged, or perception. De-
creasing  an  effect’s  range  by  one  step  (from  ranged  to
close, for example) is worth 1 point per rank. Some effects
have  their  range  determined  by  rank. To  change  the  ef-
fect’s range, increase or decrease its rank; this flaw does
not apply. Effects that are close range by default cannot
further decrease their range.

REMOVABLE

FLAT • -1 OR -2 POINTS PER 5 POINTS

Removable applies to the power as a whole and not in-
dividual effects, although it may apply to a power with
only  one  effect.  The  flaw  is  worth  –1  point  (–2  points
for  Easily  Removable)  per  5  total  power  points  of  the
power’s final cost, rounded up, after applying extras and
flaws to its effects.

A removable power may only be removed when you are
both stunned and defenseless, essentially unable to resist,
and  cannot  be  removed  during  action  time. This  means
opponents can generally only remove the power after de-
feating you (leaving you incapacitated) or through some
sort of scheme outside of a conflict, such as a plot to break
into your headquarters and steal a device kept there, for
example.

An  easily  removable  power  can  be  taken  away  with  a
disarm  or  grab  action  (see  the  Action  &  Adventure
chapter). This typically represents some sort of handheld

device (such as a weapon, magic wand, remote control,
or the like) or some worn item easily snatched from you,
like a hat or cloak.

Removable applies to the power as a whole and not indi-
vidual effects, although it may apply to a power with only
one effect. The flaw is worth –1 point (–2 points for Easily
Removable) per 5 total power points of the power’s final
cost, after applying extras and flaws to its effects.

Example:  Ultramarine’s  armor  provides  Veronica
with  a  number  of  effects,  including  Damage,  En-
hanced  Strength,  Flight,  Protection,  and  Senses.
The total power point cost of all the armors effects
is 98 points, including extras and flaws applied to
those effects. Dividing the total cost by 5 is 20. So
the Removable flaw reduces the cost of the Ultra-
marine  armor  by  20  points,  from  98  to  78  power
points. However the armor can be taken away, dis-
abled, and so forth, and the player receives no hero
points for a complication when it happens due to
the nature of the flaw.

Removable  devices  can  be  damaged,  possib

[... truncated ...]
```

---

## Concept: Sense Of Smell

Chunk count: 1

### Chunk texts

**Chunk 1** (`5731b0e9cb2f`):

```
CHAPTER 6: POWERS

177

1-4 RANKS

Senses  in  MUTANTS  &  MASTERMINDS  are  broken  down  into
sense types, used as descriptors for sensory effects. Here
are  the  traits  of  normal  human  senses,  for  use  when
modifying them with the options from Senses:

VISUAL

Normal  vision  is  ranged  (with  a  –1/10  feet  modifier),
acute (able to distinguish fine details) and accurate (able
to pinpoint the locations of things).
AUDITORY

Normal hearing is ranged  (with  a –1/10  feet modifier),
acute  (able  to  pick  up  details  like  differences  in  tone),
and radius (able to pick up on sounds coming from any
direction). Normal hearing is not accurate.

OLFACTORY

Normal  human  olfactory  senses,  which  lump  together
smell  and  taste  for  descriptor  purposes,  are  fairly  lim-
ited. Ordinary human olfactory senses are neither acute
nor accurate. The sense of smell is a radius sense, how-
ever, able to pick up on scents coming from any direc-
tion. Its “range” is quite limited, however, effectively only
close, except for especially strong scents.

TACTILE

The normal sense of touch is, by definition, close range.
It is accurate (in that you know the location of anything
you  can  touch)  and  radius  (in  that  you  can  feel  things
from any surface of your body).

MENTAL

In MUTANTS & MASTERMINDS terms, the “sixth sense” or men-
tal  sense  type  is  fairly  crude  in  normal  humans,  lim-
ited essentially to interactions with the Insight skill and
awareness of mental effects used directly on you. Thus it
is close range and has none of the Sense qualities.

horizon and physical barriers between you and the sub-
ject, unless it also Penetrates Concealment.

1 RANK

You can see in the infrared portion of the spectrum, allow-
ing you to see heat patterns. Darkness does not provide
concealment  for  objects  differing  in  temperature  from
their  surroundings.  If  you  have  the Track  effect,  you  can
track warm creatures by the faint heat trails they leave be-
hind. The Gamemaster is the final judge on how long the
trail remains visible.
VISION

1 RANK

You can view extremely small things. You can make Per-
ception checks to see tiny things nearby. Cost is 1 rank for
dust-sized  objects,  2  ranks  for  cellular-sized,  3  ranks  for
DNA and complex molecules, 4 ranks for atomic-sized. The
GM  may  require  an  Expertise  skill  check  to  understand
and interpret what you see.

4 RANKS

A sense with this trait is unaffected by concealment from

[... truncated ...]
```

---

## Concept: Sensory Link

Chunk count: 1
Performs actions: ['act_0256']
Receives actions: ['act_0256']

### Chunk texts

**Chunk 1** (`765269f2e7c2`):

```
CHAPTER 6: POWERS

169

Subtle:  As  a  mental  sensory  effect,  Mind  Reading  has  a
degree  of  subtlety,  only  noticeable  to  the  subject  or  to
characters  with  an  appropriate  mental  sense,  such  as
Mental  Awareness  (see  the  Senses  effect).  Subtle  Mind
Reading is less detectable, requiring a DC 20 Perception
check  for  either  type  of  character  to  sense  it,  while  two
ranks  of  the  Subtle  modifier  makes  your  Mind  Reading
completely undetectable. Flat +1 or 2 points.

FLAWS

Close: Applied to Ranged Mind Reading, Close Mind Read-
ing requires a close attack check to touch an unwilling tar-
get and physical contact throughout the effect’s duration;
breaking contact ends the effect. –1 cost per rank.

Feedback: You suffer Feedback if a subject you are reading
is harmed, using your Mind Reading rank as the resistance
check  bonus  against  the  damage.  Additionally,  you  may
suffer Feedback at the GM’s discretion from reading or ex-
periencing  particularly  traumatic  or  emotionally-charged
thoughts of memories from the subject. –1 cost per rank.

Limited by Language: You can only understand the sub-
ject’s thoughts or memories if you share a common lan-
guage. –1 cost per rank.

Limited to Emotions: You can only read or probe for emo-
tions and emotional associations, not coherent thoughts
or memories. –1 cost per rank.

Limited to Sensory Link: If you have the Sensory Link extra
and this flaw, you can only tap into a subject’s senses, you
cannot read their thoughts or memories. –1 cost per rank.

Limited to Surface Thoughts: You can only read surface
thoughts and cannot achieve higher degrees of contact.
–1 cost per rank.

Ranged: Ranged Mind Reading requires a ranged attack
check in addition to the effect’s normal resistance check.
–1 cost per rank.

Sense-Dependent: Your Mind Reading is dependent on
a  sense  other  than  just  having  to  accurately  sense  the
target, such as needing to see his expressions (Sight-De-
pendent), hear him speak (Hearing-Dependent), smell his
changes in biochemistry (Scent-Dependent), and so forth.
Alternately, it may be dependent on first being in Mental
Communication with the target (see Communication). –1
cost per rank.

MORPH

GENERAL

Action: Free • Range: Personal
Duration: Sustained • Cost: 5 points per rank

You can alter your appearance. Your traits do not change;
your new form is merely a cosmetic change. You gain a +20
bonus to Deception checks to disguise yourself as the fo

[... truncated ...]
```

---

## Concept: Shapeshift

Chunk count: 1

### Chunk texts

**Chunk 1** (`b60c97b07a3c`):

```
CHAPTER 6: POWERS

179

Effect: Variable (assumed forms), Move Action • 8 points
per rank

You  can  transform  into  different  forms,  gaining  the
physical  traits  (abilities,  skills,  advantages,  and  pow-
ers) of the assumed form. You gain (Shapeshift rank x 5)
power points worth of traits. You can also redistribute
points spent on your own physical traits (lowering your
Strength to apply those points elsewhere, for example).
You are limited to the inherent traits of the forms you
assume and do not gain new mental traits, even if that
form possesses them.

Shapeshift is often further Limited by the specific types
of forms the character can assume, such as Limited to
Animals or Limited to Machines.

ter’s perceptions are unreliable, the sense appears to work,
but the character gets the wrong information. For this rea-
son, the GM should make all reliability checks for Senses
in secret, just informing the player of what the character
does (or does not) notice. –1 cost per rank.

SHRINKING

GENERAL

Action: Free • Range: Personal
Duration: Sustained • Cost: 2 points per rank

You can temporarily decrease your size, becoming smaller,
harder to see — and hit — at the cost of losing Strength
and  speed.  Every  4  ranks  of  Shrinking  reduces  your  size
rank by 1 (normal humans are size rank –2 by default) and
each reduction in size rank subtracts 1 from your Strength
and every two reductions in size rank subtract 1 from your
ground speed rank. Add half your Shrinking rank (rounded
down)  to  your  active  defenses.  Add  your  Shrinking  rank
as a bonus to Stealth checks, since you are harder to spot,
but apply half your rank (rounded down) as a penalty to In-
timidation checks (hard to be imposing when you’re tiny).
Shrinking modifiers are restricted by power level limits.

So  at  Shrinking  12,  you  are  size  rank  –5  (about  6  inches
tall),  and  have  a  +6  bonus  to  active  defenses  and  +12
Stealth bonus, but –3 Strength, –1 speed, and –6 Intimida-
tion penalties.
EXTRAS

Atomic: At Shrinking 20 (and size rank –7), you can shrink
down to the molecular or even atomic level, allowing you
to pass through solid objects by slipping between their at-
oms. It takes at least a full turn to do so, possibly longer for
larger objects. You’re effectively immune to damage and
many effects at this scale, since you are essentially shifted
out of the ordinary universe. The GM decides if a particular
effect can reach you at the atomic level. If you have 

[... truncated ...]
```

---

## Concept: Shockwave

Chunk count: 1
Receives actions: ['act_0054']

### Chunk texts

**Chunk 1** (`685941d4ae65`):

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

---

## Concept: Shrinking

Chunk count: 1
Performs actions: ['act_0283']

### Chunk texts

**Chunk 1** (`b60c97b07a3c`):

```
CHAPTER 6: POWERS

179

Effect: Variable (assumed forms), Move Action • 8 points
per rank

You  can  transform  into  different  forms,  gaining  the
physical  traits  (abilities,  skills,  advantages,  and  pow-
ers) of the assumed form. You gain (Shapeshift rank x 5)
power points worth of traits. You can also redistribute
points spent on your own physical traits (lowering your
Strength to apply those points elsewhere, for example).
You are limited to the inherent traits of the forms you
assume and do not gain new mental traits, even if that
form possesses them.

Shapeshift is often further Limited by the specific types
of forms the character can assume, such as Limited to
Animals or Limited to Machines.

ter’s perceptions are unreliable, the sense appears to work,
but the character gets the wrong information. For this rea-
son, the GM should make all reliability checks for Senses
in secret, just informing the player of what the character
does (or does not) notice. –1 cost per rank.

SHRINKING

GENERAL

Action: Free • Range: Personal
Duration: Sustained • Cost: 2 points per rank

You can temporarily decrease your size, becoming smaller,
harder to see — and hit — at the cost of losing Strength
and  speed.  Every  4  ranks  of  Shrinking  reduces  your  size
rank by 1 (normal humans are size rank –2 by default) and
each reduction in size rank subtracts 1 from your Strength
and every two reductions in size rank subtract 1 from your
ground speed rank. Add half your Shrinking rank (rounded
down)  to  your  active  defenses.  Add  your  Shrinking  rank
as a bonus to Stealth checks, since you are harder to spot,
but apply half your rank (rounded down) as a penalty to In-
timidation checks (hard to be imposing when you’re tiny).
Shrinking modifiers are restricted by power level limits.

So  at  Shrinking  12,  you  are  size  rank  –5  (about  6  inches
tall),  and  have  a  +6  bonus  to  active  defenses  and  +12
Stealth bonus, but –3 Strength, –1 speed, and –6 Intimida-
tion penalties.
EXTRAS

Atomic: At Shrinking 20 (and size rank –7), you can shrink
down to the molecular or even atomic level, allowing you
to pass through solid objects by slipping between their at-
oms. It takes at least a full turn to do so, possibly longer for
larger objects. You’re effectively immune to damage and
many effects at this scale, since you are essentially shifted
out of the ordinary universe. The GM decides if a particular
effect can reach you at the atomic level. If you have 

[... truncated ...]
```

---

## Concept: Shroud

Chunk count: 0

### Chunk texts

---

## Concept: Side Effect

Chunk count: 1
Performs actions: ['act_0346']
Receives actions: ['act_0346']

### Chunk texts

**Chunk 1** (`87f598748db8`):

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

---

## Concept: Sidekick

Chunk count: 1

### Chunk texts

**Chunk 1** (`2f722833852f`):

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

---

## Concept: Simian

Chunk count: 0
Receives actions: ['act_0522']

### Chunk texts

---
