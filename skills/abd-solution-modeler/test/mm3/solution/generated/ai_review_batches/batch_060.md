# Hypothesis concept review – batch 60

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

## Concept: Unarmed Combat Maneuvers

Chunk count: 1

### Chunk texts

**Chunk 1** (`2df9d8dcc068`):

```
CHAPTER 4: SKILLS
CHAPTER 4: SKILLS

CHAPTER 4: SKILLS

a standing long-jump of 10 feet, a vertical jump of 4 feet,
and a standing vertical jump of 2 feet on a routine basis.

DISTANCE (IN FEET)

Running Long-Jump

Athletics check result

Standing Long-Jump

Running Vertical Jump

Standing Vertical Jump

Athletics check result,
divided by 2

Athletics check result,
divided by 5

Athletics check result,
divided by 10

RUNNING

You can make a DC 15 Athletics check as a free action to
run faster: one or more degree of success increases your
ground speed rank by +1 for one round.

SWIMMING

DC

+5

+5

+5

MODIFIERS

Rescuing another character who cannot swim

Rough or choppy water

+1 speed rank (up to your full ground speed)

+10

Stormy or turbulent water

Fighting

You’re trained with a particular type of close attack, giv-
ing  you  a  bonus  to  your  attack  checks  with  it  equal  to
your  skill  rank  (see  Attack  Check  in  The  Basics  and  in
the  Action  &  Adventure  chapter).  Each  close  attack  is
a separate Close Combat skill with its own rank, and en-
compasses  a  single  weapon  or  power,  although  an  ar-
ray may be considered one power, at the Gamemaster’s
discretion  (see  Arrays  in  the  Powers  chapter  for  more
information).

A  successful  DC  10  Athletics  check  allows  you  to  swim
your ground speed rank minus 2 as a move action. If the
check fails, you make no progress through the water dur-
ing the action. With more than one degree of failure, you
go  under.  If  underwater,  you  must  hold  your  breath  to
avoid drowning (see page 238).

So  a  hero  might  have  Close  Combat:  Swords,  but  Close
Combat: Melee Weapons is too broad. Close Combat: Un-
armed  is  an  option,  meaning  skill  with  unarmed  strikes
like punches and kicks. However, this bonus does not ap-
ply to other forms of unarmed combat maneuvers, includ-
ing, but not limited to, grabbing or tripping.

```

---

## Concept: Unaware

Chunk count: 1

### Chunk texts

**Chunk 1** (`b551e66974e2`):

```
CHAPTER 1: THE BASICS

17

•

•

•

•

•

•

•

•

•

•

Disabled:  A  disabled  character  is  at  a  –5  circum-
stance  penalty  on  checks.  If  the  penalty  applies  to
specific  checks,  they  are  added  to  the  name  of  the
condition,  such  as  Attack  Disabled,  Fighting  Dis-
abled, Perception Disabled, and so forth. Debilitated,
if it applies to the same trait(s), supersedes disabled.

Fatigued: Fatigued characters are hindered. Characters
recover from a fatigued condition after an hour of rest.

Hindered: A hindered character moves at half normal
speed (–1 speed rank). Immobile supersedes hindered.

Immobile: Immobile characters have no movement
speed and cannot move from the spot they occupy,
although they are still capable of taking actions un-
less prohibited by another condition.

Impaired:  An  impaired  character  is  at  a  –2  circum-
stance penalty on checks. If the impairment applies
to  specific  checks,  they  are  added  to  the  name  of
the condition, such as Attack Impaired, Fighting Im-
paired, Perception Impaired, and so forth. If it applies
to the same trait(s), disabled supersedes impaired.

Normal: The character is unharmed and unaffected
by other conditions, acting normally.

Stunned: Stunned characters cannot take any actions,
including free actions

Transformed: Transformed  characters  have  some  or
all of their traits altered by an outside agency. This may
range from a change in the character’s appearance to
a complete change in trait ranks, even the removal of
some  traits  and  the  addition  of  others!  The  primary
limit  on  the  transformed  condition  is  the  character’s
power point total cannot increase, although it can ef-
fectively decrease for the duration of the transforma-
tion,  such  as  when  a  powerful  superhero  is  turned
into an otherwise powerless mouse or frog (obviously
based on considerably fewer power points).

Unaware: The character is completely unaware of his
surroundings, unable to make interaction or Percep-
tion checks or perform any action based on them. If
the  condition  applies  to  a  specific  sense  or  senses,
they  are  added  to  the  name  of  the  condition,  such
as visually unaware, tactilely unaware (or numb), and
so forth. Subjects have full concealment from all of a
character’s unaware senses.

Vulnerable:  Vulnerable  characters  are  limited  in
their  ability  to  defend  themselves,  halving  their  ac-
tive defenses (round up the final value). Defenseless
su

[... truncated ...]
```

---

## Concept: Uncanny Dodge

Chunk count: 15
Receives actions: ['act_0274']

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

**Chunk 2** (`267bbd73af09`):

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

**Chunk 3** (`2b979f00a098`):

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

**Chunk 4** (`301534069c2d`):

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

**Chunk 5** (`5610c4e8f961`):

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

**Chunk 6** (`6717e2899e27`):

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

**Chunk 7** (`813c952ca178`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

then  invisible  beings  are  visible  to  you.  For  5  ranks,  the
sense type ignores all Concealment effects, regardless of
descriptor. Concealed subjects seem slightly “off” to you,
enough  to  know  they  are  concealed  to  others. This  trait
does not affect concealment provided by opaque objects,
for that, see Penetrates Concealment.

2 RANKS

A sense type with this trait ignores the Illusion effect; you
automatically succeed on your resistance check against the
illusion if it affects your sense type, realizing that it isn’t real.

1 RANK

This  is  essentially  the  same  as  Counters  Concealment
(Darkness).
DETECT

1-2 RANKS

You can sense a particular item or effect by touch with a
Perception check. Detect has no range and only indicates
the  presence  or  absence  of  something  (being  neither
acute  nor  accurate).  Choose  what  sense  type  your  De-
tect falls under (often mental). For 2 ranks you can detect
things at range (with the normal –1 per 10 feet modifier to
your Perception check).

1 RANK

When you would normally be surprised in combat, make
a Perception check (DC 10): One degree of success means
you’re  not  surprised,  but  can’t  act  during  the  surprise
round  (so  you  don’t  suffer  any  conditions  of  being  sur-
prised), while two or more degrees of success means you
are not surprised and may act during the surprise round
(if any). Failure means you are surprised (although, if you
have  Uncanny  Dodge,  you  are  not  vulnerable).  The  GM
may raise the DC of the Danger Sense check in some cir-
cumstances. Choose a sense type for your Danger Sense.
Sensory effects targeting that sense also affect your Dan-
ger Sense ability and may “blind” it.

2 RANKS

You can see in complete darkness as if it were normal day-
light;  darkness  provides  no  concealment  to  your  vision.

You always know what direction north lies in and can re-
trace your steps through any place you’ve been.

1 RANK

You can accurately and automatically judge distances.
EXTENDED

1 RANK

You  have  a  sense  that  operates  at  greater  than  normal
range.  Your  range  with  the  sense—the  distance  used
to  determine  penalties  to  your  Perception  check—is  in-
creased by a factor of 10. Each additional time you apply
this option, your range increases by an additional factor
of 10, so 1 rank means you have a –1 to Perception checks
per 100 feet, 2 ranks makes it –1 per 1,000 feet, and so 

[... truncated ...]
```

**Chunk 8** (`818544ba2429`):

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

**Chunk 9** (`a67593d532fb`):

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

**Chunk 10** (`a8c6225b93ed`):

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

**Chunk 11** (`ab9b367b750f`):

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

**Chunk 12** (`ac75d3f2b9e6`):

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

**Chunk 13** (`c1c422470246`):

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

**Chunk 14** (`d329357e5091`):

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

**Chunk 15** (`dcdc4c459ab6`):

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

---

## Concept: Undead

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

## Concept: Unfortunately

Chunk count: 1
Performs actions: ['act_0135']

### Chunk texts

**Chunk 1** (`9a2865ac841b`):

```
CHAPTER 4: SKILLS

121

ceed or fail, a target’s true attitude towards you generally
becomes hostile after you attempt an Intimidation check,
even if they go along with you for the moment.

You can use Intimidation in combat as a standard action
to undermine an opponent’s confidence. Make an Intimi-
dation check as a standard action. If it succeeds, your tar-
get is impaired (a –2 circumstance penalty on checks) un-
til the end of your next round. With four or more degrees
of success, the target is disabled (a –5 penalty) until the
end of your next round.

You can intimidate a whole group of minions—who can
all see and hear you—with a single check. If the group has
you at a disadvantage, you suffer the usual circumstance
penalty on your check. Compare your check result against
a single resistance check made by the GM for the entire
group. Your Intimidation check must have the same effect
on every member of the group (that is, you cannot demor-
alize some and coerce others, for example).

Example:  Rocky  is  facing  down  Pack-Rat  in  one
of his many bolt holes around Emerald City when
the big rat commands a pack of his street thieves
to keep Rocky from following him. The gang of kids
steps forward to get in Rocky’s way. Rocky has no
interest in hurting a bunch of kids, so he bellows,
“Get  outta  the  way  or  I’ll  knock  your  blocks  off!”
and his player decides to use Rocky’s routine Intimi-
dation check of 18 to attempt to coerce the entire
group of minions into moving out of his way. The
street kids are all Thugs, so they have a resistance
rank  of  0  (their  Insight  and  Will  ranks  are  tied).
Since Rocky is attempting the same effect on every
member of the group, he makes a single opposed
check. Unfortunately, the GM rolls a 13, which isn’t
enough  to  beat  Rocky’s  18.  The  street  kids  know
Rocky won’t actually hurt them, but they dive out
of the way anyway as Rocky bulls past.”

Intellect • Trained Only

You  know  how  to  search  for  and  study  clues,  gather  in-
formation through interviews and surveillance, and ana-
lyze evidence to help solve crimes. The GM may make In-
vestigation checks for you in secret, so you do not know
exactly what you have found, or if you may have missed
something.

SEARCH

You can search an area for clues, hidden items, traps, and
other details. Perception allows you to immediately notice
things, while an Investigation check allows you to pick up
on details with some effort.

122

```

---

## Concept: Unless

Chunk count: 2
Performs actions: ['act_0191', 'act_0236']

### Chunk texts

**Chunk 1** (`92b89ee67633`):

```
CHAPTER 6: POWERS

165

GENERAL

Action: Free • Range: Personal
Duration: Sustained • Cost: 5 points per rank

pass through solid objects permeable to your type of en-
ergy, but energy resistant barriers, like heavy shielding or
force fields, block your movement.
RANK 4 - INCORPOREAL

You  can  assume  a  less  solid  form,  with  each  Insubstantial
rank becoming progressively less solid. You do not gain the
ability to assume lower-ranked Insubstantial forms at higher
ranks, but you can acquire a lower-ranked form as an Alter-
nate Effect of a higher-ranked one. You can switch between
normal and Insubstantial form at will as a free action once
per  round.  The  default  is  that  substantial  is  your “normal”
form, but the GM may permit you to make Insubstantial your
“normal” form, in which case remaining solid is a sustained
duration for you! Insubstantial offers four ranks of effect:

You  become  an  incorporeal  phantom.  You  can  pass
through solid matter at your normal speed and you have
Immunity to Physical and Energy Damage. Sensory effects
(other than tactile) and those targeting Will still work on
you,  as  do  effects  with  the  Affects  Insubstantial  modi-
fier. Choose one other reasonably common effect or de-
scriptor that works on you while you are incorporeal. You
have no effective Strength and cannot affect the physical
world, except with effects with the Affects Corporeal mod-
ifier. Your sensory effects work normally.

RANK 1 - FLUID

You become a fluid mass. You can flow through any sort of
opening,  under  (or  around)  doors,  through  keyholes  and
pipes,  and  so  forth.  You  cannot  pass  through  watertight
seals. You can automatically flow out of any restraint—such
as a snare or grab—that is not watertight. So you cannot flow
out of a bubble completely enclosing you, for example, but
anything  less  cannot  hold  you. You  can  exert  your  normal
Strength and can still push or carry objects, although your
manual dexterity may be limited (at the GM’s discretion).

A  fluid  character  may  attempt  to  catch  a  falling  person
or  object,  cushioning  the  fall  with  the  character’s  flex-
ible  form. This  requires  a  move  action,  and  reduces  the
falling damage by the cushioning character’s Toughness
bonus (representing flexibility in this case). Both charac-
ters  must  make  resistance  checks  against  the  remaining
damage. Higher rank insubstantial forms—lacking physi-
cal Strength—cannot attempt this.

RANK 2 

[... truncated ...]
```

**Chunk 2** (`c7946753c154`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

jects cannot have their selectivity changed once they are
created. +1 cost per rank.

Stationary:  Your  created  objects  can  hang  immobile
in  the  air. They  resist  being  moved  with  a  Strength  rank
equal to the modifier rank. Unless you have the Tether ex-
tra  or  the  Movable  extra,  you  cannot  move  a  stationary
created object once it’s placed any more than anyone else
can. +0 cost per rank.

Subtle:  This  modifier  either  makes  created  objects  not
noticeable as constructs for 1 rank (they look just like real
objects) or not noticeable at all for 2 ranks (such as objects
composed of invisible force). Flat +1or 2 points.

Tether: You  have  a  connection  to  your  created  objects,
allowing  you  to  exert  your  own  Strength  to  move  them
(provided you are strong enough to do so). Flat 1 point.
FLAWS

Feedback: You may suffer damage when your created ob-
jects are damaged (see the Feedback flaw description for
details). -1 cost per rank.

Permanent:  Permanent  created  objects  last  until  de-
stroyed or nullified. Unlike Continuous Create, you cannot
choose to dismiss such objects; they are truly permanent.
You  cannot  repair  permanent  created  objects  or  other-
wise alter them once they’re created. +0 cost per rank (for
a Sustained effect).

Proportional: Your  created  objects  have  a  total  volume
rank plus Toughness rank equal to your Create rank, rather

than both volume and Toughness up to your rank. So you
can create an object with volume rank 0 and Toughness
equal to your Create rank, vice versa, or anywhere in be-
tween, so long as the sum of the two ranks does not ex-
ceed your Create rank. –1 cost per rank.

DAZZLE

Effect:  Ranged,  Cumulative  Affliction,  Limited  to  One
Sense • 2 points per rank

You can overwhelm one of the target’s senses, chosen
when  you  take  this  effect.  The  target  makes  a  Forti-
tude  or  Will  resistance  check  against  your  effect  DC
(choose one when you acquire the effect). One degree
of failure leaves the sense impaired (–2 penalty). Two
degrees leave it disabled (–5 penalty) while three de-
grees  leave  the  sense  unaware: The  target  automati-
cally fails Perception checks involving the sense, and
everything effectively has total concealment from that
sense.

The target makes a new resistance check at the end of
each  turn  to  recover.  Success  removes  the  condition
imposed by the Dazzle power. Failure 

[... truncated ...]
```

---

## Concept: Unreliable

Chunk count: 1
Performs actions: ['act_0098', 'act_0099']

### Chunk texts

**Chunk 1** (`1b8011530852`):

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

---

## Concept: Untrained Skill

Chunk count: 1
Performs actions: ['act_0000']

### Chunk texts

**Chunk 1** (`94d3158e4b6b`):

```
CHAPTER 4: SKILLS ........... 113
BASICS .................. 113
Acquiring Skills ....................113
WORK ........ 113
Untrained Skill Checks ......113
Interaction Skills ..................114
Manipulation Skills .............114
DESCRIPTIONS..... 114
Acrobatics ..............................115
Athletics ..................................116
Close Combat .......................117
Deception ..............................118
Expertise .................................119
Insight .....................................120
Intimidation ..........................121
Investigation .........................122
Perception .............................123
Persuasion .............................124
Ranged Combat ..................125
Sleight of Hand ....................125
Stealth .....................................126
Technology ............................127
Treatment ..............................129
Vehicles ...................................129

```

---

## Concept: Untrained Skill Checks

Chunk count: 1

### Chunk texts

**Chunk 1** (`94d3158e4b6b`):

```
CHAPTER 4: SKILLS ........... 113
BASICS .................. 113
Acquiring Skills ....................113
WORK ........ 113
Untrained Skill Checks ......113
Interaction Skills ..................114
Manipulation Skills .............114
DESCRIPTIONS..... 114
Acrobatics ..............................115
Athletics ..................................116
Close Combat .......................117
Deception ..............................118
Expertise .................................119
Insight .....................................120
Intimidation ..........................121
Investigation .........................122
Perception .............................123
Persuasion .............................124
Ranged Combat ..................125
Sleight of Hand ....................125
Stealth .....................................126
Technology ............................127
Treatment ..............................129
Vehicles ...................................129

```

---

## Concept: Utility Belt

Chunk count: 1

### Chunk texts

**Chunk 1** (`80099a87d308`):

```
CHAPTER 7: GADGETS & GEAR

215

A  common  piece  of  equipment  for  crime  fighters  and
espionage agents is the utility belt (or bag, pouch, back-
pack, etc.): a collection of useful tools and equipment in
a compact carrying case. A utility belt is an array of Alter-
nate Equipment. Some characters may have a Removable
array of devices instead, allowing for far more unusual ef-
fects than run-of-the-mill equipment.

Note  that  equipment  with  a  cost  of  1  equipment  point
doesn’t  really  need  to  be  acquired  as  Alternate  Equip-
ment,  since  there’s  no  change  in  cost.  Still,  heroes  often
have 1-point items in their utility belts, like flashlights, re-
breathers, and so forth.

By spending hero points you can temporarily add Alter-
nate  Equipment  to  your  utility  belt,  for  those  one-time
items you may need in a pinch.

Feel  free  to  modify  this  example  (adding  or  omitting
items)  to  create  your  own  customized  utility  belts. The
tear gas, as the most expensive effect, has full cost. The
other items cost 1 point each for Alternate Equipment,
making the total equipment point cost of the utility belt
25  equipment  points,  or  5  power  points  (for  5  ranks  of
the Equipment advantage).

WEAPONS

•

Tear Gas Pellets: Ranged Cloud
Area Affliction 4 (Resisted by
Fortitude; Dazed and Vision
Impaired, Stunned and Vision
Disabled, Incapacitated) • 16 points.

•  Bolos: Ranged Cumulative

Affliction 3 (Resisted by Dodge, Overcome by
Damage; Hindered and   Vulnerable, Defenseless and
Immobile), Extra Condition, Limited Degree  • 1 point.

•  Boomerangs: Ranged Damage 1, Strength-based

• 1 point.

•

Explosives: Ranged Burst Area Damage 5 • 1 point.

•  Cutting Torch: Damage 1 Linked to Weaken

Toughness 1 • 1 point.

•

Flash-Bangs: Ranged Burst Area Cumulative
Affliction 4 (Resisted and Overcome by Will; Visually
Impaired, Visually Disabled, Visually Unaware),
Limited to Vision  • 1 point.

•  Pepper Spray: see page 217 • 1 point.

•  Power Knuckles: Damage 4, Strength-based • 1 point.

•

•

Sleep Gas Pellets: Ranged Cloud Area Affliction 3
(Resisted and Overcome by Fortitude; Fatigued,
Exhausted, Asleep) • 1 point.

Smoke Pellets: Ranged Cloud Area Visual
Concealment Attack • 1 point.

Weapons of various sorts are common for both heroes and villains. They range from melee weapons to ranged weapons
like guns and bows and devices like shrink-rays, mind-control helmets and more. Characters who don’t have any offen-
sive pow

[... truncated ...]
```

---

## Concept: Variable

Chunk count: 15
Performs actions: ['act_0301', 'act_0302']
Receives actions: ['act_0299']

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

**Chunk 2** (`2b9b77a24290`):

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

**Chunk 3** (`2f5c20c3ef2c`):

```
CHAPTER 6: POWERS

183

TRANSFORM

CONTROL

Action: Standard • Range: Close
Duration: Sustained • Cost: 2-5 points per rank

You can change objects into other objects, altering their
shape  or  material  composition  in  the  process. You  must
touch  the  chosen  object,  which  requires  a  close  attack
check if the object is held or worn by another character.

What you can transform affects cost per rank:

•

2 points: Transform one thing or substance into one
other thing or substance, such as metal into wood,
iron into glass, or broken objects into repaired ones.

Transform is a powerful effect, particularly in the hands
of a cunning player. To a degree, Transform can dupli-
cate certain other effects, such as trapping a target by
transforming air into a solid material or turning oxygen
into a suffocating gas (both Afflictions). This is perfectly
allowable; use the rules for other effects as guidelines
on how to handle these situations, using Transform rank
to determine resistance DCs.

Keep in mind, however, that Transform has a sustained
duration, which may affect how such “tricks” work (e.g.,
the trap disappears if the character is stunned, the suffo-
cating gas dissipates unless the character concentrates
each round to continue transforming it, etc.). As always,
the GM should use common sense and good judgment.

You  may  wish  to  require  characters  using  Transform
to  acquire  money  (gold,  precious  gems,  etc.)  or  other
permanent  material  goods  to  spend  power  points  on
ranks of the Benefit advantage to reflect this newfound
wealth; otherwise, the goods fade or remain imperma-
nent in some way. (Assuming things like wealth matter
in your series in some way.)

It is possible for Transform to effectively destroy objects:
turning a steel door into water, air, or even rust certain-
ly  removes  it  as  a  barrier.  However,  keep  in  mind  that
Transform  is  normally  sustained;  the  target  isn’t  truly
destroyed unless the effect is continuous, and therefore
irreversible. Even then, the destruction of targets tends
to be all-or-nothing. For an effect capable of wearing-
down  and  eventually  destroying  objects,  use  Weaken
Toughness instead.

Transforming living or otherwise animate beings as op-
posed to inanimate matter requires an effect other than
Transform. To alter a target’s outward appearance only,
go  with  a  Morph  Attack  (see  the  Morph  effect).  For  a
harmful effect that does something like turn the target
to  

[... truncated ...]
```

**Chunk 4** (`44458c4fcb7e`):

```
CHAPTER 6: POWERS

185

Powers  based  off  the Variable  effect  are  obviously  very  flexible,  capable  of  duplicating  a  wide  range  of  other  effects.
Responsibility for controlling Variable effects in the game is placed largely in the hands of both the Gamemaster and
responsible players. To do otherwise would require weighing the effect down with numerous game-system limitations
that would keep it from doing what it is supposed to do: create a wide range of effects.

Keep in mind a Variable effect is not supposed to be “any effect I want.” That kind of unlimited power doesn’t belong in the
hands of player characters, and is better reserved as a plot device for NPCs. A Variable effect can be “any effect within a
given set of parameters,” but it’s up to you and the GM to define those parameters. The limits of power flexibility in MUTANTS
& MASTERMINDS are deliberately set by Variable effects, the use of extra effort, and hero points.

Many  comic  book  heroes  who  appear  to  have  the  power  to “do  anything”  are  actually  using  one  of  these  options  in
terms.  For  example,  a  super-wizard  can  do  practically  anything  with  magic.  However,  generally
speaking, these characters have certain abilities they use all the time (powers they have acquired with power points) and
“stunts” they only do from time to time, essentially power stunts performed with extra effort (and possibly hero points).
This is why the Magic power given later in this chapter, for example, is not a Variable effect: most powers in the game
have the potential to do “stunts” via extra effort, so the “variability” of Magic seen in the comics is already built-in to the
system, with some costs to control it, without having to give players carte blanche to duplicate any effect in the game at
will (which is just likely to slow things down and cause game balance issues).

Variable effects are better reserved for things where it is difficult to cost-out and define everything about a given power in
advance. For example, the ability to shapechange into any animal could be an application of the Morph effect with a long
list of Metamorph options, but listing out every single possible animal form, one at a time, would be tedious to say the
least, especially when a good number of those forms would be superfluous. A Variable effect, with the descriptor “animal
forms” is easier to manage. The player can pre-build certain commonly used animal forms for use during play, but also ha

[... truncated ...]
```

**Chunk 5** (`8d5f5f31a27f`):

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

**Chunk 6** (`9c7fcc5049c4`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

round, which limits its usefulness in responding to the ac-
tions of others. –1 cost per rank.

Ranged: Luck Control normally requires no attack check;
if Ranged, it does. –1 cost per rank.

Resistible: Targets  of  your  Luck  Control  get  a  resistance
check—usually Dodge or Will—to avoid its effects. –1 cost
per rank.

Side Effect: As a particular side effect of Luck Control, if
your  effort  to  alter  luck  fails,  you  suffer  a  setback  with-
out earning a hero point. Effectively the GM gains a “free”
complication against you. –1 or –2 cost per rank.

SENSORY

Effect:  Perception  Ranged,  Cumulative  Affliction,  Re-
sisted by Will • 4 points per rank

You  can  impose  your  will  on  others,  forcing  them  to
obey  your  commands. Targets  failing  a Will  resistance
check against your effect DC first become dazed, then
compelled, as they try to fight off your influence. Finally,
with  three  or  more  degrees  of  effect,  the  target  be-
comes controlled and obeys any commands you give.

Degrees  of  failure  on  resistance  checks  against  Mind
Control are cumulative. You can also apply the Progres-
sive modifier (see the Affliction effect) so your mental
hold  increases  each  time  the  target  fails  a  resistance
check against it!

Action: Standard • Range: Perception
Duration: Sustained • Cost: 2 point per rank

MIMIC

You can read another character’s mind. To use Mind Read-
ing,  make  an  opposed  effect  check  against  the  result  of
the target’s Will check. The degree of success determines
the degree of contact:

1

2

3

4

Surface  thoughts: You  can  read  what  the
target  is  presently  thinking.  Mind  Reading
transcends language; you comprehend the
target’s thoughts whether or not you share
a common language.

Personal thoughts: You can probe deeper
into  the  target’s  mind  for  information. You
can  essentially  ask  any  one  question  and
receive  the  answer  from  the  target’s  mind.
If the target doesn’t know the answer, then
you know that as well.

Memory: You can read the subject’s memo-
ries  and  recollections.  This  allows  you  to
perceive  them  exactly  as  the  target  recalls
them, one memory per round.

Subconscious:  You  can  read  memories
from the target’s subconscious, things even
the  target  does  not  consciously  know. This
might mean repressed or hidden memories,
deep-seated psychological traumas, or even
other personalities.

If  you 

[... truncated ...]
```

**Chunk 7** (`ab9b367b750f`):

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

**Chunk 8** (`b60c97b07a3c`):

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

**Chunk 9** (`c46c64c84f63`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

manoids, animals, machines, and so forth. At rank 4 you
can assume any form of the same mass as your own.

For the ability to change size as well as appearance see the
Growth and Shrinking effects. To take on the other traits of
forms you assume, see the Metamorph extra, following, or
the Variable effect, later in this chapter.
EXTRAS

Attack:  A  Morph  Attack  imposes  a  different  appearance
on  the  target  creature.  Unlike  an  Affliction  that  imposes
the transformed condition, a Morph Attack is entirely cos-
metic: you can’t change the target’s traits other than ap-
pearance. +0 cost per rank.

Metamorph:  Morph  only  changes  your  appearance;  you
still  have  all  the  traits  of  your  normal  form. This  modifier
allows  you  to  have  an  alternate  set  of  traits,  essentially  a
complete  alternate  character  you  change  into,  one  set  of
traits per rank in Metamorph. You can switch between sets
of traits at will, once per round, as a free action. Your other
form(s) must have the same point total as you and are sub-
ject  to  the  same  power  level  limits. They  must  also  have
traits  suitable  to  your  Morph  effect.  For  example,  if  you
can only Morph into humanoid forms, then your alternate
forms all have to be humanoid. All of your forms must have
your full Morph effect as well; those power points cannot
be reallocated. The GM may require certain additional com-
mon traits for all of your forms, particularly mental abilities
and skills, if you retain them. Metamorph is best suited to
characters with defined sets of alternate traits. For a char-
acter able to transform into a virtually unlimited number of
forms with various traits, see the Variable effect later in this
chapter. Flat +1 point per rank of Metamorph.
FLAWS

Resistible: A Morph effect Resistible by Will is most likely
a mental illusion of some sort. Observers who succeed on
the Will  resistance  check  see  you  as  you  truly  are  rather
than in your Morph guise. This is in addition to the usual
Perception check to penetrate your disguise. If you have
the Metamorph extra, then targets that resist your effect
treat you as if you had your normal traits, and not those
granted by your Metamorph form. –1 cost per rank.

CONTROL

Action: Standard • Range: Ranged
Duration: Sustained • Cost: 2 points per rank

You  can  move  objects  at  a  distance  without  touching
them. Move Object has no action/reaction;

[... truncated ...]
```

**Chunk 10** (`c53b199f9ade`):

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

**Chunk 11** (`cb4093e23f62`):

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

**Chunk 12** (`cfadcb33d64b`):

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

**Chunk 13** (`d4cad3e10e05`):

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

**Chunk 14** (`daeb5804fb93`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

mimics  other’s  traits  is  limited  to  the  traits  its
subject(s)  possess;  a  Variable  effect  pro-
viding  you  with  traits  suitable  to  dif-
ferent shapes is limited by the form(s)
you  assume;  a  Variable  effect  pro-
viding  adaptations  is  limited  to  the
stimulus  to  which  it  adapts,  and
so  forth.  This  descriptor  does  not
reduce  the  effect’s  cost  unless  it’s
especially  narrow  or  limiting,  and
the GM is the final arbiter of what con-
stitutes  a  suitable  descriptor  and  which
descriptors are narrow enough to qualify
for a Limited flaw.

The  allocation  of  your  Variable  points  is
sustained,  so  if  you  stop  maintaining  your
Variable  effect  for  any  reason,  your  allo-
cated points “reset” to a “null” state: you lose
any temporary traits and must take the
action  necessary  to  reallocate  your
Variable  points  again  on  your  turn  to
regain  them.  Points  in  a  Continuous
Variable  effect  remain  where  you  set
them  without  maintenance,  unless  the
Variable  effect  itself  is  countered  or  nul-
lified.  Variable  effects  cannot  be  perma-
nent in duration by definition.

EXTRAS

Action: You can change the configuration of
your effect faster, although only a Reaction
Variable  can  change  more  often  than  once
per turn, and then only in response to its trig-
gering  circumstances.  Gamemasters  should
exercise  caution  with  Variable  effects  that
can be reconfigured as a free action or re-
action:  they  not  only  grant  tremendous
flexibility,  they  can  also  slow  down  game
play as the player considers virtually infinite
possibilities for each action using the Variable
effect. Move Action: +1 cost per rank . Free Action: +2 cost
per rank. Reaction: +3 cost per rank.

Affects Others: You can grant effects to someone
else. The subject granted the use of the effect con-
trols  its  configuration,  if  appropriate  for  its  descrip-
tors (although you retain the ability to withdraw use of the
effect altogether whenever you wish). Affects Others Only:
+0 cost per rank. Affects Others or yourself: +1 cost per rank.

Perception: Applied to a Ranged Affects Others Variable,
this extra allows you to grant the benefits of the effect to
any target you can accurately perceive. +1 cost per rank.

Ranged:  A Variable  effect  with  Affects  Others  may  have
the Ranged extra to improve the range at which you can
grant the effect to anoth

[... truncated ...]
```

**Chunk 15** (`dd5713402cfd`):

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

---

## Concept: Variable Effect

Chunk count: 1

### Chunk texts

**Chunk 1** (`44458c4fcb7e`):

```
CHAPTER 6: POWERS

185

Powers  based  off  the Variable  effect  are  obviously  very  flexible,  capable  of  duplicating  a  wide  range  of  other  effects.
Responsibility for controlling Variable effects in the game is placed largely in the hands of both the Gamemaster and
responsible players. To do otherwise would require weighing the effect down with numerous game-system limitations
that would keep it from doing what it is supposed to do: create a wide range of effects.

Keep in mind a Variable effect is not supposed to be “any effect I want.” That kind of unlimited power doesn’t belong in the
hands of player characters, and is better reserved as a plot device for NPCs. A Variable effect can be “any effect within a
given set of parameters,” but it’s up to you and the GM to define those parameters. The limits of power flexibility in MUTANTS
& MASTERMINDS are deliberately set by Variable effects, the use of extra effort, and hero points.

Many  comic  book  heroes  who  appear  to  have  the  power  to “do  anything”  are  actually  using  one  of  these  options  in
terms.  For  example,  a  super-wizard  can  do  practically  anything  with  magic.  However,  generally
speaking, these characters have certain abilities they use all the time (powers they have acquired with power points) and
“stunts” they only do from time to time, essentially power stunts performed with extra effort (and possibly hero points).
This is why the Magic power given later in this chapter, for example, is not a Variable effect: most powers in the game
have the potential to do “stunts” via extra effort, so the “variability” of Magic seen in the comics is already built-in to the
system, with some costs to control it, without having to give players carte blanche to duplicate any effect in the game at
will (which is just likely to slow things down and cause game balance issues).

Variable effects are better reserved for things where it is difficult to cost-out and define everything about a given power in
advance. For example, the ability to shapechange into any animal could be an application of the Morph effect with a long
list of Metamorph options, but listing out every single possible animal form, one at a time, would be tedious to say the
least, especially when a good number of those forms would be superfluous. A Variable effect, with the descriptor “animal
forms” is easier to manage. The player can pre-build certain commonly used animal forms for use during play, but also ha

[... truncated ...]
```

---
