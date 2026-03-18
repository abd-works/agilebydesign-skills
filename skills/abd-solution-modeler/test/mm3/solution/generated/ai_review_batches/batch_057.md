# Hypothesis concept review – batch 57

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

## Concept: Therefore Unabl

Chunk count: 1

### Chunk texts

**Chunk 1** (`7a6d568a6006`):

```
CHAPTER 1: THE BASICS
CHAPTER 1: THE BASICS

CHAPTER 1: THE BASICS

hand” for talking about a group of basic conditions that
go together in a particular circumstance, much like a pow-
er is a collection of basic effects.

The individual conditions making up a combined condi-
tion can be resolved individually. For example, if an effect
that removes the dazed condition is used on a staggered
character (who is dazed and hindered), then the character
is no longer dazed, only hindered. Similarly, if an effect im-
poses a condition that supersedes part of the combined
condition, only that part changes. So an effect that stuns a
staggered character means the character is now stunned
(superseding  dazed)  and  hindered.  Similarly,  an  effect
that immobilizes a staggered character leaves the target
dazed and immobile (superseding the hindered element
of the combined condition).

•

•

•

•

•

•

•

Asleep:  While  asleep,  a  character  is  defenseless,
stunned,  and  unaware.  A  hearing  Perception  check
with  three  or  more  degrees  of  success  wakes  the
character and removes all these conditions, as does
any sudden movement (such as shaking the sleeping
character) or any effect allowing a resistance check.

Blind:  The  character  cannot  see.  Everything  ef-
fectively  has  full  visual  concealment  from  him.  He
is  hindered,  visually  unaware,  and  vulnerable,  and
may be impaired or disabled for activities where vi-
sion is a factor.

Bound: A bound character is defenseless, immobile,
and impaired.

Deaf: The  character  cannot  hear,  giving  everything
total  auditory  concealment  from  him.  This  may  al-
low  for  surprise  attacks  on  the  unaware  character
(see  Surprise  Attack  in  the  Action  &  Adventure
chapter). Interaction with other characters is limited
to  sign-language  and  lip-reading  (see  Interaction
Skills in Chapter 3).

Dying: A dying character is incapacitated (defense-
less, stunned, and unaware) and near death. When
the  character  gains  this  condition,  immediately
make  a  Fortitude  check  (DC  15).  If  the  check  suc-
ceeds,  nothing  happens. With  two  degrees  of  suc-
cess,  the  character  stabilizes,  removing  this  condi-
tion. If the check fails, the character remains dying.
Three  or  more  total  degrees  of  failure  mean  the
character  dies:  so  three  failed  Fortitude  checks  or
one or two checks adding up to three degrees. Dy-
ing  characters  make  a  Fortitude  check  each  round
unt

[... truncated ...]
```

---

## Concept: These

Chunk count: 24
Performs actions: ['act_0366']

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

**Chunk 2** (`03f345278ec9`):

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

**Chunk 4** (`115dd3a349cb`):

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

**Chunk 5** (`1a59d1dc4a9a`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

267

On this and the following two pages, are a collection of twenty-one characters for use in all MUTANTS & MASTERMINDS games.
The characters range from the average man-on-the-street (Bystander) to highly trained soldiers and criminals. Many
of these characters fit into support roles, scientists, reporters, and street informants the heroes may go to in order to
get questions answered, while others are combatants. None of these characters will be a threat to PL10 characters, but
they’re often encountered in groups, which makes them more of a threat.

These characters are intended to be used when the GM needs a fairly common type of character that’s either around
to help or harm the character in some way depending on your series. They’re also meant to represent a wide range of
characters of that type. So, you can use the Police Officer to represent an actual police officer, but it could also be used
as the basis for a detective, highly-trained security professional, or bodyguard.

If you don’t see exactly the archetype you need, find something close and make a few changes. That should get you
close enough to keep the game moving quickly.

CIVILIANS

BYSTANDER

Scientists are specialists in their chosen field. This arche-
type  can  be  used  as  anything  from  an  archaeologist  to
zoologist, or for anything with a lot of knowledge about a
particular subject, such as a professor.

PL0

STR  0,  STA  0,  AGL  0,  DEX  0,  FGT  0,  INT  0,  AWE  0,  PRE  0.
Equipment:  cell  phone.  Advantages:  Equipment  1.  Skills:
Expertise:  Choose  One  4  (+4),  Expertise:  Current  Events  2  (+2),
Expertise:  Pop  Culture  2  (+2).  Offense:  Init  +0,  Unarmed  +0
(Damage 0). Defense: Dodge 0, Parry 0, Fort 0, Tou 0, Will 0. Totals:
Abilities 0 + Powers 0 + Advantages 1 + Skills 4 + Defenses 0 = 5

The bystander represents the everyday people that popu-
late the world. The sort of character a supervillain or other
criminal might take hostage or otherwise endanger. Cus-
tomize the bystander by choosing an expertise such as a
profession or trade skill.

REPORTER

PL1

STR  0,  STA  0,  AGL  0,  DEX  0,  FGT  0,  INT  2,  AWE  2,  PRE  1
Equipment: Camera, computer, digital recorder, smart-phone.
Advantages:  Contacts,  Equipment  1.  Skills:  Deception  4
(+5),  Expertise:  Current  Events  4  (+6),  Expertise:  Pop  Culture
2  (+4),  Expertise:  Streetwise  2  (+4),  Expertise:  Writing  4  (+6),
Investigation  2  (

[... truncated ...]
```

**Chunk 6** (`442f2e5a5a37`):

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

**Chunk 7** (`489d1a2f08e9`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

257

The MUTANTS & MASTERMINDS Damage effect makes it rela-
tively difficult to kill someone outright; the target has to
first be incapacitated, then further damage causes them
to become dying and potentially die. If you want to up
the level of lethality in your game, you can apply some
or all of the following options:

•

•

•

•

•

•

Allow attackers to “go for the kill” when they attack.
In this case, incapacitating the target also results in
their condition becoming dying.

Use minion characters and have a “taken out” result
against them equal the minion being killed rather
than simply incapacitated.

Have  certain  kinds  of  attacks—such  as  guns,  fire,
or lasers—always count as “going for the kill” when
they are used.

Add dying to the third degree conditions an Afflic-
tion effect may impose.

Have four or more degrees of failure on a resistance
check against Damage (and Afflictions that cause
the  dying  condition)  result  in  immediate  death.
This  is  a  particularly  harsh  option  to  impose,  but
heroes still gain the benefit of hero points to help
them avoid this fate.

Make  conditions  suffered  from  a  killing  attack
slower to recover: one condition per hour or even
per day. This emphasizes their seriousness. Also see
the Lasting Injuries sidebar in the Recovery sec-
tion of Chapter 8.

encourages  this  kind  of  narrative
structure  by  awarding  hero  points  for  defeats,  capture,
and similar complications suffered by the heroes. Essen-
tially, the more the heroes struggle early on in the game,
the more resources (in this case, hero points) they have to
overcome the villain later .

Defeat in the comics isn’t a serious problem, since it usu-
ally just results in the heroes facing another obstacle, like
a deathtrap, rather than ending the story. Some players,
however,  don’t  care  for  the  idea  of  defeat,  even  when
there  is  some  kind  of  reward  for  it. This  may  come  from
other RPGs, where defeat has much more serious conse-
quences, up to and including the death of the heroes! It
can also come from associating any kind of defeat or set-
back with “losing the game.” These players may overreact
to potential defeats in the game.

The best way of handling this is to discuss it with your play-
ers. Point out that an early defeat by the villain is not neces-
sarily  a “loss,”  but  a  complication,  and  that  they  earn  hero
points  for  complications,  leading  up  

[... truncated ...]
```

**Chunk 8** (`4e205a3c2745`):

```
CHAPTER 4: SKILLS

117

The  bonus  from  a  Close  Combat  skill  applies  only  to  at-
tack checks with the particular attack, not to defenses. For
a broader bonus to attack checks that is less than simply
raising  Fighting  rank,  see  the  Close  Attack  advantage  in
the Advantages chapter.

DECEPTION

Presence • Interaction

Deception is the skill of getting others to believe what you
want them to believe. It covers things like acting, bluffing,
fast-talk, trickery, and subterfuge.

Deception takes as long as it takes to spin-out your story.
Uses of Deception in action rounds are generally standard
actions, although you can attempt to deceive as a move
action by taking a –5 penalty to your check.

BLUFFING

Make  a  Deception  check  to  tell  a  believable  lie  or  get
someone do go along with you.

A  bluff  is  usually  opposed  by  the  target’s  Deception  or
Insight  check.  Favorable  and  unfavorable  circumstances
weigh  heavily  on  the  outcome.  Two  circumstances  can
work against you: the deception is hard to believe, or what
you  ask  goes  against  the  target’s  self-interest,  nature,  or
personality.

If it’s important, you can distinguish between a deception
that  fails  because  the  target  doesn’t  believe  it  and  one
that fails because it asks too much. For instance, if the tar-
get gets a +10 bonus to resistance because the deception
demands serious risk, and the resistance check succeeds
by 10 or less, then the target doesn’t so much see through
the deception as prove reluctant to go along with it. If the
target’s Insight check succeeds by 11 or more, he has seen
through  the  deception,  and  would  have  refused  even  if
it had not placed unusual demands on him (that is, even
without the +10 modifier).

MODIFIER

The target wants
to believe you.

The deception is believable
and doesn’t affect the target
much either way.

The deception is a little hard
to believe or puts the target at
some kind of risk.

The deception is difficult
to believe or entails
a serious risk.

The deception is way
out there, almost too
incredible to consider.

–5

+0

+5

+10

+20

There are a number of factors to consider when choosing skills for your MUTANTS & MASTERMINDS character.

VS. TALENT

In game terms there’s no difference between a character who has ranks in a skill because of extensive training and an-
other whose skill ranks represent a natural talent or aptitude for the skill. Both are considered “trained” in the skill in
game te

[... truncated ...]
```

**Chunk 9** (`6802eda7b562`):

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

**Chunk 10** (`6805431193d6`):

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

**Chunk 11** (`73f84062d601`):

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

**Chunk 12** (`80d802c96f20`):

```
CHAPTER 7: GADGETS & GEAR

221

SIZE (RANK)

EXAMPLES

STRENGTH

TOUGHNESS

DEFENSE

Awesome

Colossal

Space transport

Passenger jet

Gargantuan

Semi, yacht, private jet

Huge

Large

Medium

Stretch limo, SUV, tank

Car, small truck

Motorcycle

TRAIT

Size

Strength

Speed

COST

1 point per size category

1 point per +1 Strength

movement effect cost

Toughness

1 point per +1 Toughness

Defense

Features

Powers

1 point per +1 Defense

1 point per feature

power cost (see Chapter 5)

modes of movement (air, ground, and water, for example)
pay full cost for the most expensive and can acquire the
others as Alternate Effects (see the Alternate Effect modi-
fier in the Powers chapter).
DEFENSE

A vehicle’s size determines its base Defense, which is used
to determine the Defense Class to hit the vehicle with at-
tacks. For sizes larger than medium, this is a penalty, mak-
ing it easier to target the vehicle, even to the point where
attackers  can  hit  it  as  a  routine  check. You  can “buy  off”
the Defense penalty applied to a vehicle for 1 equipment
point per –1 penalty removed.

TOUGHNESS

Size category determines a vehicle’s base Toughness rank,
used  for  Toughness  resistance  checks.  You  can  increase
a vehicle’s Toughness over the base rank for its size for 1
equipment point per Toughness rank.

20

16

12

8

4

0

15

13

11

9

7

5

–12

–8

–4

–2

–1

0

•

•

•

•

•

•

Alarm: The vehicle has an alarm system that goes off
when an unauthorized access or activation attempt
is made. A Technology check (DC 20) can overcome
the alarm. For each additional equipment point, the
DC increases by 5.

Caltrops: A vehicle may be equipped with a dispenser
for caltrops, spikes meant to damage tired. Activating
the dispenser is a standard action. Caltrops automati-
cally blow out the tires of ordinary vehicles that run over
them  (consider  such  vehicles  “minions”).  Heroes  and
villains can make DC 13 Toughness checks for their ve-
hicles; tires are Toughness 3. One degree of failure slows
the vehicle, while two degrees of failure immobilize it.

Hidden  Compartments:  The  vehicle  has  hidden
compartments or cargo areas holding up to a tenth
of the vehicle’s medium load in cargo. A Perception
check (DC 20) allows the searcher to find the hidden
compartment. For each additional equipment point,
the DC increases by 5.

Navigation System: The vehicle is equipped with a
navigation system that grants a +5 circumstance bo-
nus on skill checks relate

[... truncated ...]
```

**Chunk 13** (`952d6212a75a`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

Audio  Recorder: These  tiny  digital  recorders  (about  the
size  of  a  deck  of  playing  cards)  can  record  up  to  eight
hours  of  audio  and  can  be  connected  to  a  computer  to
download the digital recording.

Video  Camera:  A  hand-held  camera  that  records  video
and audio on tape or digitally, with a capacity of about 6
hours of footage. Video cameras cost 2 points, since they
effectively double as audio recorders as well.

sion goggles must have at least a little light to operate. A
cloudy night provides sufficient ambient light, but a pitch-
black cave or a sealed room doesn’t. For situations of total
darkness, the goggles come with an infrared illuminator
that, when switched on, operates like a flashlight visible
only to the wearer (or anyone else with IR vision).

Parabolic Microphone: This apparatus has a gun-like mi-
crophone with an attached set of headphones. A parabol-
ic mike provides a +5 equipment bonus to listening Per-
ception checks that overcomes some or all of the penalty
for listening to sounds at a distance, through walls, etc.

This equipment is most often used by criminals or to catch
criminals.

Handcuffs: Handcuffs are restraints designed to lock two
limbs—normally the wrists—of a prisoner together. They
fit any medium or small humanoid. Handcuffs can only be
placed on a defenseless or unresisting target. Steel cuffs
have Toughness 9 and are DC 20 to escape using Sleight
of Hand (or Technology to pick the lock).

Lock Release Gun: This small, pistol-like device automati-
cally disables and opens cheap and average mechanical
locks operated by standard keys as a routine check. It does
not affect other locks.

Restraints: Similar to handcuffs are plastic restraints, used in
cases where authorities need to restrain a large number of
people and cuffs are impractical. They are generally Tough-
ness 5 or so and DC 20 to escape with Sleight of Hand but
cannot be removed except by cutting or breaking them.

Heroes often use surveillance gear to keep tabs on crimi-
nals and their activities.

Binoculars: Standard binoculars allow the user to make visu-
al Perception checks at a greater distance, or with a reduced
penalty  for  distance,  effectively  providing  a  +5  equipment
bonus that overcomes some or all of the distance penalty.

Concealable Microphone: A tiny receiver usable as a lis-
tening device. It has a broadcast range of about a mi

[... truncated ...]
```

**Chunk 14** (`9aad078a59d7`):

```
CHAPTER 3: ABILITIES
CHAPTER 3: ABILITIES

Everyone has certain basic abilities: how strong, fast, smart, and clever they are. These abilities influence most things
your character does. Stronger characters can lift greater weights, more agile characters have better balance, tougher
characters can soak up more damage, and so forth.

characters have eight basic abilities: Strength (Str), Stamina (Sta), Dexterity (Dex), Agility (Agl),
Fighting (Ftg), Intellect (Int), Awareness (Awe), and Presence (Pre). Strength, Dexterity, Agility and Stamina are physical
abilities, whereas Fighting, Intellect, Awareness, and Presence are mental abilities. Each above-average ability pro-
vides a bonus on certain die rolls; while below average abilities apply a penalty.

Each ability has a rank associated with it, based on how above or below average it is. Abilities start at rank 0, the baseline
average for an adult human being. They can go as low as –5 (truly terrible) and as high as 20, with higher values reserved
for truly cosmic beings and forces.

The ability rank is added to, or subtracted from, die rolls when your character does something related to that ability. For
example, your Strength rank affects the amount of damage you do when punching someone. Your Intellect rank comes
into play when you roll skills based on Intellect, and so forth. Sometimes your rank is used to calculate another value, such
as when you use your Agility to determine how good you are at avoiding harm with your reflexes (your Dodge defense).

You  choose  your  hero’s  ability  ranks  by  spending  power
points  on  them.  Increasing  an  ability  rank  by  1  costs  2
power points, so putting two points into Strength, for ex-
ample, raises it from 0 to 1. Remember a rank of 0 is av-
erage,  2  is  a  fair  amount  of  talent  or  natural  ability,  3  is
exceptional, 4 extraordinary, and so forth. (See the Ability
Benchmarks table for guidelines.)

You can also lower one or more of your character’s ability
ranks from the starting value of 0. Each rank you lower an
ability gives you an additional two power points to spend
elsewhere.  You  cannot  lower  an  ability  rank  below  –5,
which is itself a serious deficiency.

Ability Cost = 2 power points
per +1 to an ability rank.

Gain 2 bonus power points
per -1 to an ability rank.

RANK

–5

–4

–3

–2

–1

0

1

2

3

4

5

6

7

8

10

13

15

20

Completely inept or disabled

Weak; infant

Younger child

Child, elderly, impaired

Below averag

[... truncated ...]
```

**Chunk 15** (`ab446868e7fe`):

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

**Chunk 16** (`ba29424008f5`):

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

**Chunk 17** (`c51168f2be2c`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

* = See individual descriptions for more information.

Trucks  include  pick-ups,  sport  utility
vehicles (SUVs), vans, and similarly
sized vehicles.

Tanks are heavily armed
and  armored  vehicles.
The standard tank has
Tough-
Impervious
ness  12  and  comes
equipped  with  a  can-
non  (Ranged  Damage  10,
Burst Area 6) and a heavy machine
gun (Ranged Multiattack Damage 6). It
takes a move action to get into or out
of a  tank, and another move action
to start it up.

APCs or Armored Personnel Car-
riers,  are  designed  for  carry-
ing  troops.  They  come  with
a  smaller  cannon  (Ranged
Damage  6,  Burst  Area  4),
Impervious  Toughness  8,
and are set up so soldiers on
board can fire their personal
weapons  from  behind  the
cover of the APC’s armor.

Water vehicles range from small boats and outboards to
massive sea-going ships.

Cutters are used by the Coast Guard and the Navy. They’re
often equipped with light machine guns (Ranged Multiat-
tack Damage 6).

Destroyers  are  main  naval  ships,  carrying  heavy  guns
(Ranged Damage 10, Burst Area 8).

Battleships have massive gun batteries (Ranged Damage
13, Burst Area 9) and heavy armor.

Submarines are equipped with torpedoes (Ranged Dam-
age  8,  Burst  Area  5)  and  often  ballistic  missiles  (Ranged
Burst  Area  Damage  15  or  higher,  not  included  in  listed
cost).

Air vehicles are all capable of flight, some of them at very
high speeds.

Military  helicopters  are  equipped  with  machine  guns
(Ranged  Multiattack  Damage  6)  and  rockets  (Ranged
Damage 9, Burst Area 6).

Fighter  jets  have  machine  guns  (Ranged  Multiattack
Damage  6)  and  air-to-air  missiles  (Ranged  Damage  11,
Burst Area 8, Homing 6).

Bombers may have machine guns and missiles, but also
have powerful bombs (Burst Area Damage 12 or higher)
they can drop on targets.

Space  vehicles  are  intended  for  use  outside  the  atmo-
sphere, some of them for interplanetary or even interstel-
lar travel. Generally space vehicles are found in the pos-
session of alien civilizations, although the GM may choose
to allow some organizations and individuals on Earth to
have space vehicles.

Space fighters are armed with blaster cannons (Ranged
Damage 10).

Space cruisers have larger beam weapons (Ranged Dam-
age 12) and often energy torpedoes (Ranged Damage 12,
Burst Area 10, Homing 8).

Space  battleships  have  the  most  massive  weapons:

[... truncated ...]
```

**Chunk 18** (`c53b199f9ade`):

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

**Chunk 19** (`c8f8dadd6203`):

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

**Chunk 20** (`d421725a8d2c`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

270

Welcome to Emerald City, Storm City, the City of Destiny,
City  on  the  Albian,  Red,  and  Bronze  Rivers,  City  of  the
Three Hills… a city in crisis. Emerald City is a thriving Pa-
cific Northwest metropolis, a port city known as a home
to hardy pioneers for well over a century and a half. The
people of E.C. need their pioneer spirit, too, since the city
has also become the focus of world-changing events.

them superhuman powers. Many of these so-called “storm-
ers” were driven mad or freakishly mutated, and turned to
lives  of  crime.  Others  sought  to  protect  Emerald  City  from
this new onslaught. The Silver Storm shattered the unity of
the  Chamber,  and  brought  the  truth  to  light.  No  longer  a
sleepy Pacific town, Emerald City is a hub of high-tech, alien
activity, and superhuman struggle—a city in need of heroes.

HISTORY

GEOGRAPHY

Starting out as a trapping and mill-town in the Pacific North-
west,  the  jewel  that  became  known  as  Emerald  City  had  a
reputation as a quiet, safe place, until recently. The city was
largely free of crime, at least on the surface. That was because
of  a  criminal  conspiracy  known  as  the  Chamber,  which  set
Emerald City up as a safe place for other criminals to lay-low
and disappear for a while. Let places like Freedom City be-
come battlefields, they reasoned. They would maintain a low
profile and a safe haven. It worked, too, until the Silver Storm.

An explosion along Emerald City’s famed Yellow Brick Row
shopping district unleashed a spreading cloud of nanotech-
nology  that  transformed  many  of  those  it  touched,  giving

Emerald City is located in the Pacific Northwest, centered
on a sheltered inner peninsula jutting into the Albian River,
with access to Malory Bay and chains of islands, built upon
three main hills, modest in size compared to the mountain-
ous terrain in the surrounding area, but still fairly steep. The
city has since spread across the inlet to the western or outer
peninsula and along the south of the riverbank eastward as
well as pushing south towards the mountains.

The Downtown area of the city is towards the waterfront,
the  early  center  of  Emerald  City’s  livelihood  and  activity.
Down  below  is  the  Undercity,  a  preserved  19th  century
section of the city turned into a tourist attraction. The Riv-

271

erfront stretches along the south shore of the Albian River.
Royal Hill, the northernmost o

[... truncated ...]
```

**Chunk 21** (`db250ced1e81`):

```
CHAPTER 3: ABILITIES
CHAPTER 3: ABILITIES

CHAPTER 3: ABILITIES

Over  the  course  of  play,  your  hero’s  ability  ranks  may
change for the following reasons:

•

•

Some power effects raise or lower ability ranks (see
the Powers chapter).

You can improve ability ranks permanently by spend-
ing  earned  power  points  on  them,  but  you  cannot
increase  an  ability  rank  above  the  limits  set  by  the
series’ power level (see Power Level, page 24).

Whenever  an  ability  rank  changes,  all  traits  associated
with  the  ability  change  as  well.  So  if  you  increase  your
character’s Agility, his Agility-based skills and Dodge de-
fense  also  increase.  Likewise,  if  the  hero’s  Agility  bonus
decreases, his Agility-based skills and Dodge suffer.

If one of your hero’s ability ranks drops below –5 for any
reason, that ability is said to be debilitated and the char-
acter  suffers  more  serious  effects  than  just  a  penalty  to
certain traits and rolls, as follows:

•

•

•

•

Debilitated  Strength,  Agility,  or  Dexterity  means
the  hero  collapses:  defenseless,  immobilized,  and
stunned (although still conscious and aware).

Debilitated  Stamina  means  the  hero  is  dying,  and
suffers  a  –5  modifier  on  Fortitude  checks  to  avoid
death on top of it.

Debilitated  Fighting  means  the  hero  is  dazed  and
defenseless, and cannot make close attacks.

Debilitated
Intellect,  Awareness,  or  Presence
means the hero is unaware and remains so until re-
stored to at least a –5 rank in the ability.

Debilitated  ability  ranks  usually  result  from  a  power  af-
fecting  your  character.  Ability  ranks  cannot  be  lowered
any further once they are debilitated.

Rather  than  having  a  rank  of  –5  in  a  given  ability,  some
things  or  creatures  actually  lack  an  ability  altogether.
These  beings  automatically  fail  any  check  requiring  the
absent ability. The additional effects of  an  absent ability
are as follows:

•

•

Strength:  A  creature  with  no  Strength  is  incapable
of exerting any physical force, either because it has
no physical form (like an incorporeal ghost) or simply
can’t move (like a tree).

Stamina: A creature with no Stamina has no physical
body (like a ghost) or is not a living being (such as a
robot or other construct). Creatures with no Stamina
suffer  and  recover  from  damage  like  inanimate  ob-
jects  (see  Damaging  Objects  under  the  Damage

```

**Chunk 22** (`ebca8c9dc40a`):

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

**Chunk 24** (`ffc525f7d497`):

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

## Concept: Thieves

Chunk count: 1
Receives actions: ['act_0510']

### Chunk texts

**Chunk 1** (`d421725a8d2c`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

270

Welcome to Emerald City, Storm City, the City of Destiny,
City  on  the  Albian,  Red,  and  Bronze  Rivers,  City  of  the
Three Hills… a city in crisis. Emerald City is a thriving Pa-
cific Northwest metropolis, a port city known as a home
to hardy pioneers for well over a century and a half. The
people of E.C. need their pioneer spirit, too, since the city
has also become the focus of world-changing events.

them superhuman powers. Many of these so-called “storm-
ers” were driven mad or freakishly mutated, and turned to
lives  of  crime.  Others  sought  to  protect  Emerald  City  from
this new onslaught. The Silver Storm shattered the unity of
the  Chamber,  and  brought  the  truth  to  light.  No  longer  a
sleepy Pacific town, Emerald City is a hub of high-tech, alien
activity, and superhuman struggle—a city in need of heroes.

HISTORY

GEOGRAPHY

Starting out as a trapping and mill-town in the Pacific North-
west,  the  jewel  that  became  known  as  Emerald  City  had  a
reputation as a quiet, safe place, until recently. The city was
largely free of crime, at least on the surface. That was because
of  a  criminal  conspiracy  known  as  the  Chamber,  which  set
Emerald City up as a safe place for other criminals to lay-low
and disappear for a while. Let places like Freedom City be-
come battlefields, they reasoned. They would maintain a low
profile and a safe haven. It worked, too, until the Silver Storm.

An explosion along Emerald City’s famed Yellow Brick Row
shopping district unleashed a spreading cloud of nanotech-
nology  that  transformed  many  of  those  it  touched,  giving

Emerald City is located in the Pacific Northwest, centered
on a sheltered inner peninsula jutting into the Albian River,
with access to Malory Bay and chains of islands, built upon
three main hills, modest in size compared to the mountain-
ous terrain in the surrounding area, but still fairly steep. The
city has since spread across the inlet to the western or outer
peninsula and along the south of the riverbank eastward as
well as pushing south towards the mountains.

The Downtown area of the city is towards the waterfront,
the  early  center  of  Emerald  City’s  livelihood  and  activity.
Down  below  is  the  Undercity,  a  preserved  19th  century
section of the city turned into a tourist attraction. The Riv-

271

erfront stretches along the south shore of the Albian River.
Royal Hill, the northernmost o

[... truncated ...]
```

---

## Concept: This Approach

Chunk count: 1

### Chunk texts

**Chunk 1** (`63430f7e2ad6`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

scale  opens  up  larger  potential  threats. You  can  destroy
entire worlds at these levels to demonstrate what the he-
roes are up against, whereas such a threat would wipe out
an entire smaller scale setting.

SETTING

The setting is where and when the series takes place. Is it
the modern-day, medieval times, the wild west, or the far
future solar system? Each of the following settings has its
positives  and  negatives,  and  each  is  suited  to  particular
types of games.

MODERN

Most of the time, a MUTANTS & MASTERMINDS series is set in a
version of our modern world. This approach is the easiest
one by far, since there isn’t as much you have to make up.
You don’t have to explain to your players where New York
City is, for example.

If  your  M&M  game  is  set  in  the  modern-day  world,  you
may want to choose a particular city or area as the heroes’
home base. Even a truly global team needs some place to
call home, such as an orbiting satellite or the top floors of
a skyscraper.

A fun option can be to use your home city (or one near-
by) as the setting for your series. It offers a familiar locale
along  with  the  fun  of  having  superheroes  and  villains
duke it out around your local landmarks!

Many comics and series feature heroes that live in fictional
cities, places that don’t exist in the real world but are often
remarkably similar to various real world cities. You can do
something similar in your own series, perhaps based on
the place where you live.

Of course, your modern setting is not necessarily the mod-
ern universe: with parallel Earths, yours could be like the
real world, but with whatever changes you want.

The Golden Age of comics began in the 1930s and MU-
can easily be set any time in the past
seventy-five years. Players can take the roles of “mystery
men”  and  the  first  superheroes,  fighting  against  gang-
sters and the forces of the Axis in World War II. They can
be  government  agents  or  patriotic  heroes  during  the
Cold  War  with  Russia,  or  counter-culture  rebels  during
the 1960s.

But  nothing  says  you  can’t  go  farther  back  in  history  if
you  want.  Comic  books  have  told  stories  about  heroes
from nearly every time period. There’s World War I and the
American Revolutionary War. The Wild West offers cowboy
heroes,  Native  American  shaman,  and  steam-tech  weird
science. Medieval heroes could face evil wizards, goblins,
and monsters. You c

[... truncated ...]
```

---

## Concept: This Minion

Chunk count: 1

### Chunk texts

**Chunk 1** (`3a7f34326ad9`):

```
CHAPTER 5: ADVANTAGES
CHAPTER 5: ADVANTAGES

CHAPTER 5: ADVANTAGES

move  one  of  the  following  conditions  from  an  ally  with
whom you can interact: dazed, fatigued, or stunned.

LUCK

FORTUNE, RANKED (1/2 PL)

Once per round, you can choose to re-roll a die roll, like
spending a hero point (see Hero Points, page 20), includ-
ing adding 10 to re-rolls of 10 or less. You can do this a
number  of  times  per  game  session  equal  to  your  Luck
rank, with a maximum rank of half the series power level
(rounded down). Your Luck ranks refresh when your hero
points “reset”  at  the  start  of  an  adventure. The  GM  may
choose to set a different limit on ranks in this advantage,
depending on the series.

Generally speaking, languages are not terribly important
in comic book superhero stories except as background col-
or or occasional plot complications. Gamemasters should
allow  players  with  characters  fluent  in  other  languages
the occasional opportunity to show them off or put them
to good use. If you specifically set up the language barrier
as an obstacle by confronting the heroes with a language
they cannot possibly understand, that should count as a
complication and be worth a hero point.

COMBAT

MINION

GENERAL, RANKED

You can draw a weapon from a holster or sheath as a free
action, rather than a move action.

You have a follower or minion. This minion is an indepen-
dent  character  with  a  power  point  total  of  (advantage
rank x 15). Minions are subject to the normal power level
limits, and cannot have minions themselves. Your minions
(if capable of independent thought) automatically have a
helpful attitude toward you. They are subject to the nor-
mal rules for minions (see page 245).

Minions do not earn power points. Instead, you must spend
earned  power  points  to  increase  your  rank  in  this  advan-
tage to improve the minion’s power point total and traits.
Minions also do not have hero points. Any lost minions are
replaced in between adventures with other followers with
similar abilities at the Gamemaster’s discretion.

ACTION

COMBAT

When taking a standard action and a move action you can
move both before and after your standard action, provid-
ed the total distance moved isn’t greater than your normal
movement speed.

COMBAT

When  you  make  a  power  attack  (see  Maneuvers,  page
250)  you  can  take  a  penalty  of  up  to  –5  on  your  attack
bonus and add the same number (up to +5) to the effect
bonus of your attack.

[... truncated ...]
```

---

## Concept: Though

Chunk count: 1
Performs actions: ['act_0471']

### Chunk texts

**Chunk 1** (`d421725a8d2c`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

270

Welcome to Emerald City, Storm City, the City of Destiny,
City  on  the  Albian,  Red,  and  Bronze  Rivers,  City  of  the
Three Hills… a city in crisis. Emerald City is a thriving Pa-
cific Northwest metropolis, a port city known as a home
to hardy pioneers for well over a century and a half. The
people of E.C. need their pioneer spirit, too, since the city
has also become the focus of world-changing events.

them superhuman powers. Many of these so-called “storm-
ers” were driven mad or freakishly mutated, and turned to
lives  of  crime.  Others  sought  to  protect  Emerald  City  from
this new onslaught. The Silver Storm shattered the unity of
the  Chamber,  and  brought  the  truth  to  light.  No  longer  a
sleepy Pacific town, Emerald City is a hub of high-tech, alien
activity, and superhuman struggle—a city in need of heroes.

HISTORY

GEOGRAPHY

Starting out as a trapping and mill-town in the Pacific North-
west,  the  jewel  that  became  known  as  Emerald  City  had  a
reputation as a quiet, safe place, until recently. The city was
largely free of crime, at least on the surface. That was because
of  a  criminal  conspiracy  known  as  the  Chamber,  which  set
Emerald City up as a safe place for other criminals to lay-low
and disappear for a while. Let places like Freedom City be-
come battlefields, they reasoned. They would maintain a low
profile and a safe haven. It worked, too, until the Silver Storm.

An explosion along Emerald City’s famed Yellow Brick Row
shopping district unleashed a spreading cloud of nanotech-
nology  that  transformed  many  of  those  it  touched,  giving

Emerald City is located in the Pacific Northwest, centered
on a sheltered inner peninsula jutting into the Albian River,
with access to Malory Bay and chains of islands, built upon
three main hills, modest in size compared to the mountain-
ous terrain in the surrounding area, but still fairly steep. The
city has since spread across the inlet to the western or outer
peninsula and along the south of the riverbank eastward as
well as pushing south towards the mountains.

The Downtown area of the city is towards the waterfront,
the  early  center  of  Emerald  City’s  livelihood  and  activity.
Down  below  is  the  Undercity,  a  preserved  19th  century
section of the city turned into a tourist attraction. The Riv-

271

erfront stretches along the south shore of the Albian River.
Royal Hill, the northernmost o

[... truncated ...]
```

---

## Concept: Three

Chunk count: 1

### Chunk texts

**Chunk 1** (`7a6d568a6006`):

```
CHAPTER 1: THE BASICS
CHAPTER 1: THE BASICS

CHAPTER 1: THE BASICS

hand” for talking about a group of basic conditions that
go together in a particular circumstance, much like a pow-
er is a collection of basic effects.

The individual conditions making up a combined condi-
tion can be resolved individually. For example, if an effect
that removes the dazed condition is used on a staggered
character (who is dazed and hindered), then the character
is no longer dazed, only hindered. Similarly, if an effect im-
poses a condition that supersedes part of the combined
condition, only that part changes. So an effect that stuns a
staggered character means the character is now stunned
(superseding  dazed)  and  hindered.  Similarly,  an  effect
that immobilizes a staggered character leaves the target
dazed and immobile (superseding the hindered element
of the combined condition).

•

•

•

•

•

•

•

Asleep:  While  asleep,  a  character  is  defenseless,
stunned,  and  unaware.  A  hearing  Perception  check
with  three  or  more  degrees  of  success  wakes  the
character and removes all these conditions, as does
any sudden movement (such as shaking the sleeping
character) or any effect allowing a resistance check.

Blind:  The  character  cannot  see.  Everything  ef-
fectively  has  full  visual  concealment  from  him.  He
is  hindered,  visually  unaware,  and  vulnerable,  and
may be impaired or disabled for activities where vi-
sion is a factor.

Bound: A bound character is defenseless, immobile,
and impaired.

Deaf: The  character  cannot  hear,  giving  everything
total  auditory  concealment  from  him.  This  may  al-
low  for  surprise  attacks  on  the  unaware  character
(see  Surprise  Attack  in  the  Action  &  Adventure
chapter). Interaction with other characters is limited
to  sign-language  and  lip-reading  (see  Interaction
Skills in Chapter 3).

Dying: A dying character is incapacitated (defense-
less, stunned, and unaware) and near death. When
the  character  gains  this  condition,  immediately
make  a  Fortitude  check  (DC  15).  If  the  check  suc-
ceeds,  nothing  happens. With  two  degrees  of  suc-
cess,  the  character  stabilizes,  removing  this  condi-
tion. If the check fails, the character remains dying.
Three  or  more  total  degrees  of  failure  mean  the
character  dies:  so  three  failed  Fortitude  checks  or
one or two checks adding up to three degrees. Dy-
ing  characters  make  a  Fortitude  check  each  round
unt

[... truncated ...]
```

---

## Concept: Three Artifacts

Chunk count: 1

### Chunk texts

**Chunk 1** (`d421725a8d2c`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

270

Welcome to Emerald City, Storm City, the City of Destiny,
City  on  the  Albian,  Red,  and  Bronze  Rivers,  City  of  the
Three Hills… a city in crisis. Emerald City is a thriving Pa-
cific Northwest metropolis, a port city known as a home
to hardy pioneers for well over a century and a half. The
people of E.C. need their pioneer spirit, too, since the city
has also become the focus of world-changing events.

them superhuman powers. Many of these so-called “storm-
ers” were driven mad or freakishly mutated, and turned to
lives  of  crime.  Others  sought  to  protect  Emerald  City  from
this new onslaught. The Silver Storm shattered the unity of
the  Chamber,  and  brought  the  truth  to  light.  No  longer  a
sleepy Pacific town, Emerald City is a hub of high-tech, alien
activity, and superhuman struggle—a city in need of heroes.

HISTORY

GEOGRAPHY

Starting out as a trapping and mill-town in the Pacific North-
west,  the  jewel  that  became  known  as  Emerald  City  had  a
reputation as a quiet, safe place, until recently. The city was
largely free of crime, at least on the surface. That was because
of  a  criminal  conspiracy  known  as  the  Chamber,  which  set
Emerald City up as a safe place for other criminals to lay-low
and disappear for a while. Let places like Freedom City be-
come battlefields, they reasoned. They would maintain a low
profile and a safe haven. It worked, too, until the Silver Storm.

An explosion along Emerald City’s famed Yellow Brick Row
shopping district unleashed a spreading cloud of nanotech-
nology  that  transformed  many  of  those  it  touched,  giving

Emerald City is located in the Pacific Northwest, centered
on a sheltered inner peninsula jutting into the Albian River,
with access to Malory Bay and chains of islands, built upon
three main hills, modest in size compared to the mountain-
ous terrain in the surrounding area, but still fairly steep. The
city has since spread across the inlet to the western or outer
peninsula and along the south of the riverbank eastward as
well as pushing south towards the mountains.

The Downtown area of the city is towards the waterfront,
the  early  center  of  Emerald  City’s  livelihood  and  activity.
Down  below  is  the  Undercity,  a  preserved  19th  century
section of the city turned into a tourist attraction. The Riv-

271

erfront stretches along the south shore of the Albian River.
Royal Hill, the northernmost o

[... truncated ...]
```

---

## Concept: Three Ranks

Chunk count: 1

### Chunk texts

**Chunk 1** (`9c685bbd4830`):

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

---

## Concept: Throwing

Chunk count: 1

### Chunk texts

**Chunk 1** (`bb3e97c13b71`):

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

## Concept: Thugs

Chunk count: 1
Performs actions: ['act_0134']

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

## Concept: Thunder

Chunk count: 1

### Chunk texts

**Chunk 1** (`6890e166bca9`):

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

---
