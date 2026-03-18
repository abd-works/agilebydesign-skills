# Hypothesis concept review – batch 33

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

## Concept: Rank

Chunk count: 2
Performs actions: ['act_0241']

### Chunk texts

**Chunk 1** (`706d511e685d`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

both be Insubstantial and make an attack to make others
Insubstantial. +0 or +1 cost per rank.

suffer any damage from landing after a jump, so long as it
is within your maximum distance.

Continuous:  Extending  the  effect’s  duration  to  continu-
ous allows you to remain Insubstantial until you choose to
return to your corporeal form. +1 cost per rank.

Innate: Use this modifier if your character’s form is natu-
rally  or  innately  Insubstantial,  particularly  if  the  effect  is
permanent in duration. Flat +1 point.

Precise: This modifier allows you to selectively make some
portions of your body insubstantial while keeping others
substantial (or vice versa). This allows you to do things like
reach through a wall, solidify your hand to pick up an ob-
ject  or  tap  someone  on  the  shoulder  (or  punch  them  in
the face), and become incorporeal again to withdraw it on
the following round. Flat +1 point.

Progressive:  You  can  assume  lower  ranked  forms  of  In-
substantial, but you must progress through them in order
to reach the higher-ranked ones. For example if you have
Progressive Insubstantial 3, you can assume fluid, gaseous,
or energy forms, but to assume energy form, you must first
progress through fluid and gaseous, becoming less and less
substantial. Since you can only activate the effect once per
turn, it takes you three turns to get there. +0 cost per rank.

Reaction: Becoming Insubstantial is normally a free action,
meaning  you  can’t  switch  to  an  Insubstantial  form  when
surprised or otherwise unable to take action. At the GM’s
option, applying the Action extra to use Insubstantial as a
reaction allows you to switch forms “reflexively” in response
to such hazards, even if it is not your turn. +1 cost per rank.

Subtle:  This  extra  makes  your  Insubstantial  nature  less
noticeable  to  observers.  Rank  1  requires  a  Perception
check (DC 20) to detect that you are Insubstantial, while 2
ranks mean you look entirely normal in Insubstantial form
(which may cause opponents to waste effort on you, not
knowing  you  are  immune  to  their  attacks,  for  example).
Flat +1 or 2 points.

FLAWS

Absent Strength: This flaw applies only to rank 1 Insub-
stantial and removes your effective Strength while in that
form, leaving you with limited ability to affect the physical
world like the higher ranks of the effect. Flat –1 point.

Permanent: You are always Insubstantial; you

[... truncated ...]
```

**Chunk 2** (`cf5b8ba8408b`):

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

---

## Concept: Raven

Chunk count: 1
Performs actions: ['act_0020']

### Chunk texts

**Chunk 1** (`301ee8a15809`):

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

---

## Concept: Ray

Chunk count: 2

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

**Chunk 2** (`bb3e97c13b71`):

```
CHAPTER 4: SKILLS
CHAPTER 4: SKILLS

CHAPTER 4: SKILLS

people are favorable or indifferent toward heroes, but a
specific circumstance or complication may call for a dif-
ferent attitude.

You  can  improve  others’  attitudes  with  a  DC  15  Persua-
sion  check.  Success  improves  the  subject’s  attitude  by
one  step,  while  every  two  additional  degrees  of  success
improve it by another step (so two steps at three degrees,
three  steps  at  five  degrees,  and  so  forth).  Failure  means
no change, and more than a degree of failure worsens the
subject’s attitude by one step! In the case of a hostile sub-
ject, they may outright attack or otherwise interfere with
you if their attitude worsens.

ATTITUDES

ATTITUDE

EFFECT

Hostile

Will take risks to attack
or interfere with you.

Unfavorable

Will insult, mislead,
or otherwise cause you trouble.

Indifferent

Favorable

Helpful

Acts as socially expected
towards you.

Will chat, advise,
and offer limited help.

Will take risks to
help or protect you.

Persuading someone is at least a standard action, usually
quite a bit longer. The GM decides if you can persuade at
all once a conflict has broken out! Even if the initial check
succeeds,  the  other  character  can  only  be  persuaded  so
far;  you  can  try  again  in  the  same  scene,  but  you  check
against the subject’s initial attitude, and may end up wors-
ening it rather than improving it!

Example:  The  heroes  must  convince  the  imperi-
ous King of Atlantis that the surface world is not
responsible  for  recent  attacks  against  his  king-
dom  in  order  to  avert  a  war.  The  king’s  attitude
is  unfavorable  towards  these  surface-world  in-
terlopers  to begin with. The team’s spokesperson
makes  a  Persuasion  attempt  and  gets  a  check
result  of  22,  a  success  with  two  degrees  total.
That  shifts  the  king’s  attitude  one  step,  to  indif-
ferent. He’s inclined to continue negotiating with
the heroes and willing to place the assault on the
surface world on-hold for the time-being. The he-
roes try to convince the king further, but any ad-
ditional checks need at least the same degree of
success as the first to get his attitude to favorable,
where he is willing to call off the attack, and more
than one degree of failure on any check moves his
attitude to hostile, where he orders the intruders
arrested and the attack to begin at once!

way:  you  find  a  new  approach  to  your  argument,  new
evidence appears,

[... truncated ...]
```

---

## Concept: Reaching

Chunk count: 1
Performs actions: ['act_0264']

### Chunk texts

**Chunk 1** (`3739eabb7a65`):

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

---

## Concept: Reaction Damage

Chunk count: 9

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

**Chunk 2** (`14dd371ce972`):

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

**Chunk 3** (`442f2e5a5a37`):

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

**Chunk 4** (`685941d4ae65`):

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

**Chunk 5** (`8ad0833a1563`):

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

**Chunk 6** (`aa943c38ef67`):

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

**Chunk 8** (`d329357e5091`):

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

## Concept: Readying

Chunk count: 1

### Chunk texts

**Chunk 1** (`9136b6d87e68`):

```
CHAPTER 8: ACTION & ADVENTURE

247

ground  speed  minus  one  rank,  if  you  choose.  If  you  fail,
you are still grabbed.

GRAB

You  attempt  to  grab  a  target.  Make  an  attack  check
against the target. If successful, the target makes a resis-
tance check against your Strength (or the rank of a grab-
bing effect) using the better of Strength or Dodge. If you
win with one degree of success, the target is restrained
(immobile  and  vulnerable). Two  or  more  degrees  leave
your  opponent  bound  (defenseless,  immobile,  and  im-
paired).  You  can  attempt  to  improve  an  existing  hold
with another grab action on a following turn. Any result-
ing  degrees  of  success  are  cumulative,  but  if  you  lose,
the target escapes.

You  are  hindered  and  vulnerable  while  grabbing  and
holding an opponent. You can maintain a successful grab
as a free action each turn, but cannot perform other ac-
tions requiring the use of your grabbing limb(s) while do-
ing so. Since maintaining a grab is a free action, you can
take a standard action to inflict your Strength damage to
a grabbed target on subsequent turns after the grab is es-
tablished.

You can drag a restrained or bound target along with you
when  you  move.  The  target  gets  a  Strength  resistance
check  against  your  Strength.  If  it  fails,  you  move  and  the
target moves along with you. If the target resists, you are
immobilized that turn unless you release your hold on the
target.

You can end a grab (releasing your target) as a free action.
If you are unable to take the free action maintain the hold,
the target is automatically released. A target can attempt
to escape from a grab as a move action (see Escape).

MOVE

You can move up to your normal speed rank in any move-
ment mode available to you as a move action. Normally
this is rank 0 ground speed for most people (up to 30 feet).
If  you  choose  to  move  twice  on  your  turn  (taking  two
move actions) then you move your speed rank each time.
You can make a DC 15 Athletics check as a free action to
run faster: one or more degree of success increases your
ground speed rank by +1 for one round.

READY

Readying lets you prepare to take an action later, after you
would normally act on your initiative, but before your ini-
tiative on your next turn. Readying is a standard action, so
you can move as well.

If you come to your next turn and have not yet performed
your readied action, you don’t get to take the readied ac-
tion, y

[... truncated ...]
```

---

## Concept: Rebound

Chunk count: 1
Performs actions: ['act_0212']

### Chunk texts

**Chunk 1** (`cf5b8ba8408b`):

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

---

## Concept: Reflect

Chunk count: 2
Receives actions: ['act_0207', 'act_0208', 'act_0227', 'act_0228']

### Chunk texts

**Chunk 1** (`ba29424008f5`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

FLAWS

Limited: You must specify a reasonably common effect
(or set of uncommon effects) that keeps you from recov-
ering from death, such as beheading, cremation, a stake
through the heart, and so forth. Even then, if the effect is
somehow removed or reversed (e.g. the stake is removed
from your corpse) you may still be able to come back. -1
cost per rank.

IMMUNITY

DEFENSE

Action: None • Range: Personal
Duration: Permanent • Cost: 1 point per rank

You are immune to certain effects, automatically succeeding
on  any  resistance  check  against  them. You  assign  ranks  of
Immunity to various effects to gain immunity to them (with
more extensive effects requiring more ranks). These assign-
ments are permanent. Examples include the following:

•

•

•

•

•

•

1  rank:  aging,  disease,  poison,  one  environmental
condition  (cold,  heat,  high  pressure,  radiation,  or
vacuum), one type of suffocation (breathe normally
underwater or in an alien atmosphere, for example),
starvation and thirst, need for sleep, or a rare power
descriptor (such as your own powers, a close sibling’s
powers, etc.).

2 ranks: critical hits, suffocation effects (no need to
breathe  at  all),  or  an  uncommon  power  descriptor
(such as chemical, gravitic, necromantic, etc.).

5 ranks: alteration effects, sensory Affliction effects,
emotion  effects,  entrapment  (grabbing,  snares,  or
bonds), fatigue effects, interaction skills, or a particu-
lar  Damage  effect,  descriptor  (such  as  bullets,  cold,
electricity, falling, fire, magic, radiation, sonic, etc.)

10 ranks: a common power descriptor (such as all ef-
fects with cold, electricity, fire, radiation, or weather
descriptors,  for  example),  life  support  (includes  im-
munity  to  disease,  poison,  all  environmental  condi-
tions, suffocation, and starvation and thirst).

20  ranks:  a  very  common  power  descriptor  (blud-
geoning or energy, for example).

30 ranks: All effects resisted by Fortitude, All effects
resisted by Will.

•

80  ranks:  All  effects  resisted  by  Toughness  (the
equivalent of 40 ranks of Impervious Toughness).

Some Immunity effects are a matter of degree. For exam-
ple, “immunity to cold” can range from the environmen-
tal effects of cold (described under The Environment) to
cold damage, to complete immunity to all effects with the
“cold”  descriptor. The  first  requires  only  1  rank,  and  pro-
vides no resistance to othe

[... truncated ...]
```

**Chunk 2** (`f1bc1ad153ee`):

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

---

## Concept: Regeneration

Chunk count: 28
Receives actions: ['act_0204', 'act_0270', 'act_0425', 'act_0436']

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

**Chunk 5** (`301534069c2d`):

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

**Chunk 6** (`3df9e8cdc695`):

```
CHAPTER 8: ACTION & ADVENTURE
CHAPTER 8: ACTION & ADVENTURE

CHAPTER 8: ACTION & ADVENTURE

is designed to emulate the superhero comic books, so characters generally bounce back pretty fast
from taking serious beatings, and there is little differentiation between getting punched through a brick wall and shot-up
with a .45 caliber (or, for that matter, set on fire or electrocuted). Realistically, any or all of these things should result in
severe injuries that take a considerable amount of time to heal; in the comics, most characters just shake it off and are all
better by the next scene.

If you want to include lasting or more serious injuries in your game, or just in a particular story, they are better handled
as complications (see the Complications section in The Basics chapter for details). This is largely how the comics handle
them; most of the time, heroes bounce back from the effects of combat but, occasionally, a character suffers a serious and
significant injury—such as a broken arm or head trauma—that plays a role in the story later on. Handle this like any other
GM-imposed complication: award the player a hero point when it comes into play, and apply the effects of the complication
to the story. Use the conditions defined in The Basics chapter as an idea of the complications facing an injured character.

DEATH

Character death is a relatively rare happenstance in the comic books. Technically, it’s not so much rare as it is temporary. The
tendency of comic book characters to return from the dead has become so commonplace it is cliché, with various stories
and characters poking fun at it.

The MUTANTS & MASTERMINDS rules make character death a similarly rare occurrence. Characters generally only acquire the dying
condition after being incapacitated and suffering further harm, which usually means someone is actively trying to kill them.
Even then, dying characters have opportunities to stabilize and stave off death. It takes a second active effort to kill a dying
character outright, so accidental death due to a single bad die roll is all but impossible for the major characters in a series.

Note that none of this applies to minions, who can be killed simply with a successful attack and a declaration of intent to
do so. While heroes in a four-color or mainstream style game generally refrain from killing, minions can get mowed down
by the dozens in gritty Iron Age style games. The Gamemaster can also kill off supporting characters as desired to suit t

[... truncated ...]
```

**Chunk 7** (`442f2e5a5a37`):

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

**Chunk 8** (`685941d4ae65`):

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

**Chunk 9** (`6be13e770e51`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

Constructs  suffer  damage  like  inanimate  objects  (see
the  Damage  effect  in  the  Powers  chapter  for  details).
Constructs  do  not  recover  from  damage.  Instead,  they
must be repaired. See the Technology skill description for
guidelines on repairing damaged objects.

ZOMBIE

STR
2

STA
-

AGL
-1

DEX
-1

FGT
1

INT
-

AWE
-1

POWERS

Undead: Immunity 30 (Fortitude effects), Protection 3

OFFENSE

PL2

PRE
-

Constructs  with  Regeneration  are  self-repairing  (see  the
Regeneration effect in the Powers chapter).

INITIATIVE –1

Attack +1

Close, Damage 2

The  following  are  some  typical  constructs  for  MUTANTS  &
MASTERMINDS,  most  likely  to  show  up  as  a  villain’s  minions
. Individually, they’re no match for most heroes, but large
numbers of them can keep characters busy and even wear
them down with a lucky attack or two.

PL5

PRE
-

ROBOT

STR
5

STA
-

AGL
-1

DEX
-1

FGT
0

INT
-

AWE
0

SKILLS

Close Combat (Unarmed)  4 (+4)

POWERS

Armor: Protection 10, Impervious 6 • 16 points

Robot: Immunity 30 (Fortitude effects) • 30 points

DEFENSE

DODGE

PARRY

WILL

0

1

Immune

FORTITUDE

Immune

TOUGHNESS

ABILITIES

POWERS

–30

33

0

SKILLS

DEFENSES

TOTAL

STR
16

STA
-

AGL
0

DEX
0

FGT
0

INT
-

AWE
0

POWERS

Armor: Protection 12, Impervious  • 24 points

Giant: Growth 16, Continuous, Permanent, Innate  • 33 points

Robot: Immunity 30 (Fortitude) • 30 points

3

0

1

4

PL8

PRE
-

OFFENSE

OFFENSE

INITIATIVE –1

INITIATIVE +0

Attack +4

Close, Damage 5

Attack +0

Close, Damage 16

DEFENSE

DODGE

PARRY

WILL

0

0

FORTITUDE

Immune

TOUGHNESS

10

Immune

DEFENSE

DODGE

PARRY

WILL

–5

–5

Immune

FORTITUDE

Immune

TOUGHNESS

16

ABILITIES

POWERS

–24

46

0

SKILLS

DEFENSES

TOTAL

2

1

25

ABILITIES

POWERS

–30

87

0

SKILLS

DEFENSES

TOTAL

0

0

57

```

**Chunk 10** (`6c8715df5e97`):

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

**Chunk 11** (`75f616f43b9d`):

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

**Chunk 13** (`919d7063d0ae`):

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

**Chunk 14** (`a67593d532fb`):

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

**Chunk 15** (`aa5babc5f423`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

As with the Feature effect, a Feature extra should be sig-
nificant  enough  to  be  worth  at  least  1  power  point  and
not solely based on the power’s descriptors. So, for exam-
ple, a fiery Ranged Damage effect does not need a Feature
to ignite fires; doing so is part of its “fire” descriptor and
can be equally advantageous and problematic. A Ranged
Damage effect that consistently “brands” its target with a
visible and traceable mark, on the other hand, is an effect
with an added Feature.

HOMING

FLAT • 1 POINT PER RANK

This modifier grants a ranged effect an additional oppor-
tunity to hit. If an attack check with a Homing effect fails, it
attempts to hit again on the start of your next turn, requir-
ing only a free action to maintain and allowing you to take
other actions, including making another attack. Each rank
in Homing grants the effect one additional attack check,
but it still only gets one check per round.

The  Homing  effect  uses  the  same  accurate  sense  as  the
original attack to “track” its target, so concealment effec-
tive against that sense may confuse the effect and cause
it to miss. If a Homing attack misses due to concealment,
it  has  lost  its “lock”  on  the  target  and  does  not  get  any
further  chances  to  hit.  You  can  take  Senses  Linked  to
the Homing effect, if desired (to create things like radar-
guided or heat-seeking missiles, for example). If a Homing
attack  is  countered  before  it  hits,  it  loses  any  remaining
chances to hit. The same is true if it hits a different target.

+1 COST PER RANK

A defense with this modifier is highly resistant. Any effect
with a resistance difficulty modifier equal to or less than
half the Impervious rank (rounded up) has no effect. So,
for  example,  Impervious Toughness  9  ignores  any  Dam-
age with a rank of 5 or less. Penetrating effects can over-
come  Impervious  Resistance  (see  the  Penetrating  extra
description).

Impervious is primarily intended for Toughness resistance
checks, to handle characters immune to a certain thresh-
old  of  damage,  but  it  can  be  applied  to  other  defenses
with  the  GM’s  permission,  to  reflect  characters  with  cer-
tain reliable capabilities in terms of resisting particular ef-
fects or hazards.

+1 COST PER RANK

Effects have a standard duration: instant, sustained, con-
tinuous,  or  permanent.  See  Duration  at  the  start  of  this
chapter for details.

[... truncated ...]
```

**Chunk 16** (`aa943c38ef67`):

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

**Chunk 17** (`ab9b367b750f`):

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

**Chunk 18** (`b511fe78f53a`):

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

**Chunk 19** (`bc6e8d2fe577`):

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

**Chunk 20** (`c87ce883452a`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

FLAWS

Limited  to  One  Type:  Your  Quickness  applies  to  only
physical or mental tasks, not both. –1 cost per rank.

Limited to One Task: Your Quickness applies to only one
particular  task,  such  as  reading,  mathematical  calcula-
tions, and so forth. –2 cost per rank.

DEFENSE

Action: None • Range: Personal
Duration: Permanent • Cost: 1 point per rank

You recover quickly from damage. Remove penalties to
your  Toughness  checks  due  to  damage  equal  to  your
Regeneration rank each minute. You then recover other
damage  conditions  equal  to  your  Regeneration  rank
each minute, starting from your most severe condition.
Spread  this  recovery  out  evenly  over  a  minute  (10  ac-
tion  rounds).  So  with  Regeneration  5,  you  remove  a  –1
Toughness penalty every other round (every round with
Regeneration 10, and up to a –2 penalty per round with
Regeneration 20).

Characters  with  no  Stamina  do  not  heal  (see  Absent
Abilities in the Abilities chapter). One or more ranks of
Regeneration overcome this. An absent Stamina character
with Regeneration 1 recovers at a normal rate; additional
Regeneration ranks speed up that rate.
EXTRAS

Persistent:  You  can  regenerate  even  Incurable  damage
conditions (see the Incurable modifier). +1 cost per rank.
FLAWS

Source: Your Regeneration only works when you have ac-
cess  to  a  particular  source  to  replenish  yourself,  such  as
blood, electricity, sand, scrap metal, sunlight, and so forth.
–1 cost per rank.

SENSORY

Action: Free • Range: Rank
Duration: Sustained • Cost: 1–5 points per rank

You can displace one or more of your senses over a dis-
tance, perceiving as if you were at that location, up to 60
feet away. Each additional rank increases your range one
distance rank, so rank 2 is 120 feet, rank 3 is 250 feet, and
so  on.  Remote  Sensing  overrides  your  normal  sense(s)
while  you  are  using  it.  Subjects  observed  via  Remote
Sensing can “feel” it with an Insight check (DC 10 + rank).

You can make Perception checks normally using your dis-
placed senses, taking the normal action to do so. To search
a  large  area  for  someone  or  something,  use  the  search

Quickness,  like  many  power  effects,  is  not  especially
realistic;  it  allows  you  to  do  things  like  disassemble
an  entire  car  as  a  free  action  at  a  high  enough  rank
(around  rank  13-14),  but  doesn’t  have  any  effect  on
how  many 

[... truncated ...]
```

**Chunk 21** (`cf5b8ba8408b`):

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

**Chunk 22** (`d329357e5091`):

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

**Chunk 23** (`d4cad3e10e05`):

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

**Chunk 24** (`d5fc086574e9`):

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

**Chunk 25** (`da1c0758b454`):

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

**Chunk 26** (`dd5713402cfd`):

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

**Chunk 27** (`e6cd24549519`):

```
CHAPTER 6: POWERS

145

ACTION

RANGE

DURATION

COST

Instant

Varies

Instant

Sustained

Sustained

Permanent

Sustained

Sustained

Instant

Instant

Instant

Sustained

Sustained

Sustained

Sustained

Instant

Instant

Sustained

Sustained

Permanent

Permanent

Sustained

Sustained

Sustained

Instant

Fort. or Will

1 per rank

—

See description

Toughness

—

—

—

—

—

Toughness

Fort. or Will

—

—

Strength

—

—

Toughness

Toughness

—

—

—

—

—

—

—

—

2 per rank

1 per rank

4 per rank

2 per rank

2 per rank

2 per rank

1 per rank

2 per rank

1 per rank

3 per rank

2 per rank

1 per rank

See description

4 per rank

2 per rank

As base trait

1-2 per rank

1 per rank

1 per rank

2 per rank

1 per rank

2 per rank

2 per rank

Standard

Varies

Standard

Free

Free

None

Free

Standard

Standard

Standard

Standard

Standard

Standard

Free

Free

Reaction

Standard

Free

Close

Varies

Ranged

Personal

Rank

Personal

Personal

Ranged

Close

Ranged

Ranged

Close

Perception

Personal

Personal

Close

Ranged

Personal

Standard

Rank

Personal

Personal

Personal

Personal

Personal

Close

Personal

Personal

Personal

Personal

Personal

None

None

Free

Free

Free

Standard

Standard

None

None

Free

Free

Free

Standard

Standard

Free

Standard

NAME

Affliction

Alternate Form

Blast

TYPE

Attack

Varies

Attack

Burrowing

Movement

Sensory

Sensory

Sensory

Control

Attack

Attack

Defense

Control

Control

General

General

Attack

Attack

General

Control

General

General

Movement

Defense

General

General

Control

Defense

Defense

General

Sensory

Movement

Control

Attack

Attack

General

Attack

Sensory

General

Control

Communication

Comprehend

Concealment

Create

Damage

Dazzle

Deflect

Duplication

Element Control

Elongation

Energy Absorption

Energy Aura

Energy Control

Enhanced Trait

Environment

Extra Limbs

Feature

Flight

Force Field

Growth

Healing

Illusion

Immortality

Immunity

Insubstantial

Invisibility

Leaping

Luck Control

Magic

Mental Blast

Mimic

Mind Control

Mind Reading

Morph

Move Object

Movement

Nullify

Power-Lifting

Protection

Quickness

Regeneration

Remote Sensing

Perception

Sustained

Awareness

1-5 per rank

Permanent

Permanent

Sustained

Sustained

Instant

Instant

Instant

Instant

Reaction

Standard

Standard

Perception

Ranged

Perception

Move

Personal

Sustained

Perception

Instant

Perception

Sustained

Personal

Ranged

Personal

Ra

[... truncated ...]
```

**Chunk 28** (`f1bc1ad153ee`):

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

---

## Concept: Remote

Chunk count: 1
Receives actions: ['act_0273']

### Chunk texts

**Chunk 1** (`7419fe5693f8`):

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

---

## Concept: Remote Sensing

Chunk count: 10
Receives actions: ['act_0272']

### Chunk texts

**Chunk 1** (`0f75307c0dea`):

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

**Chunk 2** (`3c75d5b04a0e`):

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

**Chunk 3** (`3e277f7add29`):

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

**Chunk 4** (`685941d4ae65`):

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

**Chunk 5** (`6e58428e1e90`):

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

**Chunk 6** (`7419fe5693f8`):

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

**Chunk 7** (`9c7fcc5049c4`):

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

**Chunk 8** (`c1c422470246`):

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

**Chunk 9** (`c87ce883452a`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

FLAWS

Limited  to  One  Type:  Your  Quickness  applies  to  only
physical or mental tasks, not both. –1 cost per rank.

Limited to One Task: Your Quickness applies to only one
particular  task,  such  as  reading,  mathematical  calcula-
tions, and so forth. –2 cost per rank.

DEFENSE

Action: None • Range: Personal
Duration: Permanent • Cost: 1 point per rank

You recover quickly from damage. Remove penalties to
your  Toughness  checks  due  to  damage  equal  to  your
Regeneration rank each minute. You then recover other
damage  conditions  equal  to  your  Regeneration  rank
each minute, starting from your most severe condition.
Spread  this  recovery  out  evenly  over  a  minute  (10  ac-
tion  rounds).  So  with  Regeneration  5,  you  remove  a  –1
Toughness penalty every other round (every round with
Regeneration 10, and up to a –2 penalty per round with
Regeneration 20).

Characters  with  no  Stamina  do  not  heal  (see  Absent
Abilities in the Abilities chapter). One or more ranks of
Regeneration overcome this. An absent Stamina character
with Regeneration 1 recovers at a normal rate; additional
Regeneration ranks speed up that rate.
EXTRAS

Persistent:  You  can  regenerate  even  Incurable  damage
conditions (see the Incurable modifier). +1 cost per rank.
FLAWS

Source: Your Regeneration only works when you have ac-
cess  to  a  particular  source  to  replenish  yourself,  such  as
blood, electricity, sand, scrap metal, sunlight, and so forth.
–1 cost per rank.

SENSORY

Action: Free • Range: Rank
Duration: Sustained • Cost: 1–5 points per rank

You can displace one or more of your senses over a dis-
tance, perceiving as if you were at that location, up to 60
feet away. Each additional rank increases your range one
distance rank, so rank 2 is 120 feet, rank 3 is 250 feet, and
so  on.  Remote  Sensing  overrides  your  normal  sense(s)
while  you  are  using  it.  Subjects  observed  via  Remote
Sensing can “feel” it with an Insight check (DC 10 + rank).

You can make Perception checks normally using your dis-
placed senses, taking the normal action to do so. To search
a  large  area  for  someone  or  something,  use  the  search

Quickness,  like  many  power  effects,  is  not  especially
realistic;  it  allows  you  to  do  things  like  disassemble
an  entire  car  as  a  free  action  at  a  high  enough  rank
(around  rank  13-14),  but  doesn’t  have  any  effect  on
how  many 

[... truncated ...]
```

**Chunk 10** (`d4cad3e10e05`):

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

## Concept: Removable

Chunk count: 27
Receives actions: ['act_0367']

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

**Chunk 2** (`1081db3c43af`):

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

**Chunk 3** (`19a54c3b3576`):

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

**Chunk 5** (`1d151f074127`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

feature and require characters to pay for it if their charac-
ters have such a costume. Otherwise characters have to
make do with ordinary clothing (which may be damaged
or destroyed when they use their powers).

Some devices are otherwise normal equipment with spe-
cial properties. Magical items, normal equipment imbued
with  magical  properties,  are  examples.  Magical  weap-
ons  may  have  greater  damage  bonuses  or  grant  attack
bonuses  while  magical  armor  imposes  no  penalties  and
provides  greater  protection.  Such  enchantments  move
archaic weapons and armor from the realm of mundane
equipment to devices. The same is true of equipment us-
ing super-alloys, bulletproof cloth, and other wonders of
super-science.

WEAPONS

Weapons are common devices, ranging from super-pow-
ered versions of ordinary weapons like swords, bows, or
guns  (see  Enhanced  Equipment)  to  more  exotic  weap-
ons  like  magic  wands  or  alien  power  rings.  A  weapon
device  usually  has  one  or  more  attack  effects  but  may
provide  virtually  any  effect  the  player  wants  to  include.
Weapons often have several different attacks as Alternate
Effects. One example is an array of magic rings, each with
its own effect, but only usable one at a time.

The full range of devices MUTANTS & MASTERMINDS characters
can create and use is limited solely by your imagination.
Essentially any item with a power is considered a device.
Players and GMs may well come up with devices beyond
those  described  here.  Use  the  guidelines  in  this  chapter
and in the Powers chapter to handle any new devices and
their capabilities.

INVENTING

Characters with the Inventor advantage can create inven-
tions,  temporary  devices. To  create  an  invention,  the  in-
ventor defines its effects and its cost in power points. This
cost is used for the necessary skill checks, and determines
the time required to create the invention. Inventions are
subject to the same power level limits as other effects in
the series.

First,  the  inventor  must  design  the  invention.  This  is  a
Technology skill check the GM should make in secret. The
DC is 10 + the invention’s total power point cost, including
all modifiers except Removable, which does not apply to
inventions, as they are temporary by nature.

Designing an invention requires an hour’s work per power
point of the invention’s cost. You can make a routi

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

**Chunk 7** (`44458c4fcb7e`):

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

**Chunk 8** (`685941d4ae65`):

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

**Chunk 9** (`7b2254220623`):

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

**Chunk 10** (`80099a87d308`):

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

**Chunk 11** (`8558df91a0a1`):

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

**Chunk 12** (`8757660124bd`):

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

**Chunk 13** (`87f598748db8`):

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

**Chunk 14** (`9b8b75c1b5e7`):

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

**Chunk 15** (`9c685bbd4830`):

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

**Chunk 16** (`ab9b367b750f`):

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

**Chunk 17** (`bc6e8d2fe577`):

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

**Chunk 18** (`c0c1858f03fe`):

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

**Chunk 19** (`cfadcb33d64b`):

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

**Chunk 20** (`d329357e5091`):

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

**Chunk 21** (`d4cad3e10e05`):

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

**Chunk 22** (`db8b2bdf371a`):

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

**Chunk 23** (`dcdc4c459ab6`):

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

**Chunk 24** (`e087f7a0b70b`):

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

**Chunk 25** (`eab98ce0e1fc`):

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

**Chunk 26** (`ebca8c9dc40a`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

From blaster rifles to anti-gravity belts, teleportation rings, and battlesuits, heroes and villains develop all manner of gad-
gets. Villains are forever coming up with doomsday machines and fiendish deathtraps while heroes use all sorts of gear
to aid them in their fight for justice. This chapter looks at various sorts of devices and equipment in MUTANTS & MASTERMINDS
game terms. It also describes vehicles, headquarters, and constructs, ranging from zombie minions to giant robots.

DEVICES

A device is an item that provides a particular power effect or set of effects. While devices are typically creations of ad-
vanced science, they don’t have to be. Many heroes and villains have magical devices such as enchanted weapons and
armor, magical talismans, wands and staves of power, and so forth. Some devices are products of alien technology so
advanced they might as well be magical, or focuses of psychic or cosmic power beyond the understanding of both
magic and science. All devices work the same way in game terms, regardless of their origin or descriptors.

Generally speaking, devices are powers with the Removable flaw applied to them (see Removable in the Powers chapter),
meaning the power is external to the character. Take away the device, and the wielder loses the ability to use those powers.
So if an armored hero loses access to his battlesuit, for example, he also loses access to the powers tied-up in it. The same
is the case of a hero loses a cosmic ring, magic helmet, or alien artifact, which is why Removable is a flaw for those powers.

Just like other powers, devices cost power points (albeit reduced some by the Removable flaw). Characters who want to
have and use a device on a regular basis have to pay power points to have it, just like having any other power. The device
becomes a part of the character’s abilities. If the device is lost, stolen, or destroyed, the character can replace it, given
time, since the device is considered a permanent part of the character. Only a re-allocation of the character’s power
points will change this, and Gamemasters should allow characters to re-allocate power points spent on a Removable
power if it is somehow permanently lost.

In other cases, characters may make temporary use of a device. Most devices are usable by anyone able to operate
them, in which case characters may loan devices to each other, or may pick up and use someone else’s device (or even
steal a

[... truncated ...]
```

**Chunk 27** (`ffb72d59f44c`):

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
