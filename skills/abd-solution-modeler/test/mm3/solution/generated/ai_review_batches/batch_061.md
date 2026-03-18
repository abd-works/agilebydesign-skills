# Hypothesis concept review – batch 61

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

## Concept: Variable Trigger

Chunk count: 1
Receives actions: ['act_0335']

### Chunk texts

**Chunk 1** (`885a404994e2`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

sponse to a particular danger, after a set amount of time,
in  response  to  a  particular  event,  and  so  forth—chosen
when  you  apply  the  modifier.  Once  chosen,  the  trigger
cannot be changed.

The  circumstances  must  be  detectable  by  your  senses.
You can acquire Senses Limited and Linked to Triggered
effects, if desired. Setting the effect requires the same ac-
tion as using it normally.

A Triggered  effect  lying  in  wait  may  be  detected  with  a
Perception check (DC 10 + effect rank) and in some cases
disarmed with a successful skill or power check (such as
Sleight  of  Hand, Technology,  Nullify  or  another  counter-
ing effect) with a DC of (10 + effect rank).

A  Triggered  effect  is  good  for  one  use  per  rank  in  this
modifier. After its last activation, it stops working.

You  can  apply  an  additional  rank  of Triggered  to  have  a
Variable Trigger, allowing you to change the effect’s trig-
ger each time you set it.

FLAT • 1-2 POINTS

You can change the descriptors of an effect with this modi-
fier, varying them as a free action once per round. With rank
1, you can apply any of a closely related group of descrip-
tors,  such  as  weather,  electromagnetic,  temperature,  and
so forth. With rank 2, you can apply any of a broad group,
such  as  any  mental,  magical,  or  technological  descriptor.
The GM decides if a given descriptor is appropriate in con-
junction with a particular effect and this modifier.

FLAWS

The  following  section  lists  available  flaws,  starting  with
the flaw’s name and the amount it reduces effect cost (in
power points per rank or flat value), along with a descrip-
tion of how the flaw modifies effects in game terms.

A flat-value flaw cannot have more ranks than the effect
itself.

FLAT • -1 OR -2 POINTS

A  power  with  this  flaw  requires  an  action  to  prepare  or
activate before any of its effects are usable. If the power
requires a move action to activate, the flaw is –1 point. If
it requires a standard action, it is –2 points. Activation tak-
ing  less  than  a  move  action  is  not  a  flaw,  although  may
qualify as a complication (see the Power Loss complica-
tion for details).

Activation has no effect other than making all of the pow-
er’s  effects  available  for  use. The  effects  themselves  still
require their normal actions to use. You can use a power’s
effects in the same turn as you activate it, provided y

[... truncated ...]
```

---

## Concept: Variable Type

Chunk count: 1
Receives actions: ['act_0287']

### Chunk texts

**Chunk 1** (`c58c7a144f00`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

level

mon  effect  used  to  create
it,  is  subject  to  the  normal
limits,  and
power
cannot  have  minions  of  its
own, either from this effect
or the Minions advantage.

You  can  summon  your
minion  automatically  as  a
standard action; it appears
in  the  nearest  open  space
beside  you.  Minions  have
their  own
initiative  (see
Initiative  in  the  Action  &
Adventure  chapter)  and
act starting on the round
after you summon them.
Summoned
minions
are  dazed,  taking  only
a  standard  action  each
round.  Directing  a  min-
ion  to  do  something  is
a  move  action  for  you,
but  minions  generally
do as they are told until a
task is completed.

You  always  have  the  same
minion  unless  you  apply
the Variable Type modifier,
allowing  you  to  summon
different  minions.  Your
minion  automatically  has
a helpful attitude and does
its best to aid you and obey
your commands.

minions
Incapacitated
disappear.  They
recover
normally  and  you  cannot
summon  an  incapacitated  minion  until  it  has  com-
pletely recovered. Your summoned minions also vanish if
your effect is not maintained, or is countered or nullified.
For  more  information  and  rules  regarding  Minions,  see
page 245.
EXTRAS

Active: Your minions are particularly independent and do
not have the dazed condition, having a full set of actions
each round. +1 cost per rank.

Controlled: Your  minions  all  have  the  controlled  condi-
tion (see Controlled in The Basics chapter). They have no
free will of their own and are completely under your direc-
tion. +1 cost per rank.

Heroic: The creatures you summon are not subject to the
minion rules, but treated like normal non-player charac-
ters. Additionally, they do not have the dazed condition
and take a full set of actions each round. Do not apply the
Active modifier to Heroic minions, as this modifier already
includes it. Gamemasters should be particularly cautious

SLEEP

Effect:  Ranged  Affliction,  Resisted  by  Fortitude  •
2 points per rank

You  cause  a  the  target  to  feel  tremendous  weariness.
Targets  failing  the  Fortitude  resistance  check  against
your effect DC become fatigued, then exhausted, and
finally asleep as they succumb.

Sleep  is  not  normally  cumulative,  but  you  can  apply
the  Cumulative  or  Progressive  modifiers,  making  the
fatigue that much harder for victims to fight off.

about  allowing  this  extra  for  Summon  effects  

[... truncated ...]
```

---

## Concept: Vehicle

Chunk count: 27
Performs actions: ['act_0150', 'act_0374']

### Chunk texts

**Chunk 1** (`80d802c96f20`):

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

**Chunk 2** (`d5441abe7f45`):

```
CHAPTER 4: SKILLS
CHAPTER 4: SKILLS

CHAPTER 4: SKILLS

TREATMENT

can’t  awaken  a  dying  character  without  stabilizing  him
first (see the following).

Intellect • Trained Only • Manipulation • Requires Tools

STABILIZE

You’re trained in treating injuries and ailments. The check
DC and effect of Treatment depend on the task:

DC

10

15

15

15

15

TASK

Diagnose injuries and ailments.

Provide long-term care.

Revive dazed or stunned characters.

Stabilize dying character.

Treat diseases or poisons.

If  you  do  not  have  the  appropriate  medical  equipment
and supplies, you take a –5 circumstance penalty on your
check.  If  your  subject  has  a  particularly  unusual  biology
(an alien, for example) you may also suffer a circumstance
penalty.

You  can  use  the Treatment  skill  on  yourself,  but  only  to
diagnose,  provide  care,  or  treat  disease  or  poison.  You
take a –5 circumstance penalty on checks when treating
yourself.
DIAGNOSIS

You  can  diagnose  injuries  and  ailments  with  an  eye  to-
ward  further  treatment.  This  takes  at  least  a  minute.  At
the GM’s discretion, a successful diagnosis provides a +2
bonus  for  favorable  circumstances  on  further Treatment
checks.

Providing  care  means  treating  an  injured  patient  for  a
day or more. If successful, the patient further reduces the
recovery  time  by  1  rank  (see  Recovery  in  the  Action  &
Adventure chapter). You can provide care for up to your
Treatment rank in patients at one time.
REVIVE

You  can  remove  the  dazed  or  stunned  conditions  from
a  subject  (see  Conditions  in  the  Action  &  Adventure
chapter). The check to revive is a standard action. A suc-
cessful  check  removes  the  condition.  Other  conditions
the patient may have remain, so reviving someone inca-
pacitated due to fatigue still leaves the patient exhaust-
ed, for example, while awakening someone incapacitat-
ed due to damage still leaves the patient staggered. You

As a standard action, a successful Treatment check stabi-
lizes a dying character.

You can treat a character afflicted with a disease or poison.
Each time the character makes a resistance check against
the ailment, you make a Treatment check. One degree of
success provides the patient with a +2 circumstance bo-
nus to the resistance check, three or more degrees of suc-
cess provides a +5 circumstance bonus.

VEHICLES

Dexterity • Trained Only • Manipulation

Use this skill to operate vehicles, from ground v

[... truncated ...]
```

**Chunk 3** (`042be12e9222`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

HOOD: SUPER-SHIELDS

Just as power armor is a device version of otherwise or-
dinary equipment armor, some heroes (and, less often,
villains) have shield devices providing them with great-
er benefits than an ordinary shield.

A shield device may provide Enhanced Dodge and Parry
defenses  like  a  mundane  shield,  or  it  can  grant  ranks
of  Protection  (which  do  stack  with  other  effects,  since
they’re not from equipment), perhaps even Impervious
Protection  for  a “bulletproof”  or “indestructible”  shield.
Such benefits are typically Sustained in duration, requir-
ing some action on the shield-wielder’s part.

A super-shield might even be useful as a weapon, pro-
viding a Damage effect, probably Strength-based. This is
best handled as an Alternate Effect of the shield, mean-
ing you can’t use it both offensively and defensively at
the same time! A hero able to hurl a shield at foes can
even have a Ranged Damage effect with it.

Chain-mail: A shirt of heavy metal chain, often with a coif
(hood) to cover the wearer’s head.

Plate-mail:  This  is  chain-mail  augmented  with  a  metal
breastplate, greaves (leg-guards) and arm-guards.

ARMOR

ARMOR

EFFECT

COST

Leather

Chain-mail

Plate-mail

Full-plate

Undercover shirt

Bulletproof vest

ARCHAIC

Protection 1

Protection 3

Protection 5

Protection 6

MODERN

Protection 2, Limited
to Ballistic, Subtle

Protection 4, Limited
to Ballistic, Subtle

SHIELDS

Small shield

+1 Active Defenses

Medium shield

+2 Active Defenses

Large shield

+3 Active Defenses

1

3

5

6

2

3

2

4

6

Bulletproof  vest:  A  heavier  vest  of  ballistic  armor  worn
by police officers and soldiers.

Full-plate:  A  full  (and  heavy!)  suit  of  articulated  metal
plates, like that worn by medieval knights.

SHIELDS

Modern body armor is common among superheroes and
villains, but even more so among people like police offi-
cers, soldiers, criminal agents, and so forth.

Undercover shirt: A thin shirt of ballistic armor that can
be worn under street clothes.

Small shield: A small hand shield large enough to cover
the wearer’s forearm.

Medium shield: A larger shield covering almost the entire
arm, able to shield a large portion of the torso.

Large shield: A “kite” shield able to cover more than half
of the wielder’s body.

VEHICLES

Not every hero can fly (or teleport, or run at super-speed...). Sometimes heroes make use of other means

[... truncated ...]
```

**Chunk 4** (`0b483461d2f8`):

```
CHAPTER 4: SKILLS
CHAPTER 4: SKILLS

CHAPTER 4: SKILLS

SKILL

Acrobatics

Athletics

Close Combat

Deception

Expertise

Insight

Intimidation

Investigation

Perception

Persuasion

Ranged Combat

Sleight of Hand

Stealth

Technology

Treatment

Vehicles

SKILLS

ABILITY

UNTRAINED?

Agl

Str

Fgt

Pre

Int

Awe

Pre

Int

Awe

Pre

Dex

Dex

Agl

Int

Int

Dex

No

Yes

Yes

Yes

No*

Yes

Yes

No

Yes

Yes

Yes

No

Yes

No

No

No

ACTION

move or free

move

standard

standard

—

free

standard

—

free

—

standard

standard

move

standard

standard

move

A “—” entry in the Action column means using the skill typically takes longer than a standard action. See the skill description for details.
* Some areas of Expertise can be used Untrained. See the entry on Expertise for more information.

Interaction: If “Interaction” is included on the line below
the skill’s name, it is an interaction skill.

Manipulation:  If “Manipulation”  is  included  on  the  line
below the skill’s name, it is a manipulation skill.

Requires Tools: If “Requires Tools” is included on the line
below the skill’s name, you need to have the proper tools
to use the skill. Not having the proper tools is a –5 circum-
stance penalty to the skill check (see Circumstance Modi-
fiers, page 15).

The skill name line is followed by a description of the skill
and how it is used.

Agility • Trained Only

Use Acrobatics to flip, dive, roll, tumble, and perform other
acrobatic maneuvers, as well as keeping your balance un-
der difficult circumstances.
BALANCING

You  can  keep  your  balance  and  move  along  a  precari-
ous  surface  at  your  ground  speed  minus  1  rank  with  a
successful  Acrobatics  check  against  the  surface’s  DC.  A
degree of failure indicates you spend your move action
just maintaining your balance and do not actually move,
while  two  or  more  degrees  of  failure  means  you  lose
your balance and fall.

A yard or more wide

Wide ledge (1-3 ft.)

Narrow ledge (less than 1 ft.)

Balance beam

Tightrope

Surface slightly slippery

Surface very slippery

Surface slightly uneven

Surface very uneven or angled

Move at your normal speed rank

Not vulnerable while balancing

DC

0

5

10

15

20

+2

+5

+2

+5

+5

+5

You are vulnerable while balancing. If you accept a +5 in-
crease to the Acrobatics DC, you are not vulnerable.

If  you  fail  a  resistance  check  while  balancing,  make  an-
other immediate Acrobatics check against the original DC
to avoid 

[... truncated ...]
```

**Chunk 5** (`1081db3c43af`):

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

**Chunk 6** (`13ce58f9b33f`):

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

**Chunk 7** (`17270869c240`):

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

**Chunk 8** (`1a59d1dc4a9a`):

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

**Chunk 9** (`1b8011530852`):

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

**Chunk 10** (`238fc7bd4809`):

```
CHAPTER 3: ABILITIES

107

Here are descriptions of the eight abilities and what they represent.

STRENGTH (STR)

INTELLECT (INT)

Strength measures sheer muscle power and the ability to
apply it. Your Strength rank applies to:

•

Damage dealt by your unarmed and strength-based
attacks.
How far you can jump (based on an Athletics skill check).
The amount of weight you can lift, carry, and throw.
Athletics skill checks.

•
•
•
STAMINA (STA)

Stamina  is  health,  endurance,  and  overall  physical  resil-
ience.  Stamina  is  important  because  it  affects  a  charac-
ter’s ability to resist most forms of damage. Your Stamina
modifier applies to:

•
•

•

Toughness defense, for resisting damage.
Fortitude defense, for resisting effects targeting your
character’s health.
Stamina  checks  to  resist  or  recover  from  things  af-
fecting  your  character’s  health  when  a  specific  de-
fense doesn’t apply.

AGILITY (AGL)

Agility is balance, grace, speed, and overall physical coor-
dination. Your Agility rank applies to:

•

•
•
•

Dodge defense, for avoiding ranged attacks and oth-
er hazards.
Initiative bonus, for acting first in combat.
Acrobatics and Stealth skill checks.
Agility  checks  for  feats  of  coordination,  gross  move-
ment, and quickness when a specific skill doesn’t apply.

DEXTERITY (DEX)

Dexterity  is  a  measure  of  hand-eye  coordination,  preci-
sion, and manual dexterity. Your Dexterity rank applies to:

•
•
•

Attack checks for ranged attacks.
Sleight of Hand and Vehicles skill checks.
Dexterity  checks  for  feats  of  fine  control  and  preci-
sion when a specific skill doesn’t apply.

FIGHTING (FGT)

Fighting  measures  your  character’s  ability  in  close  com-
bat, from hitting a target to ducking and weaving around
any counter-attacks. Your Fighting rank applies to:

•
•

Attack checks for close attacks.
Parry defense, for avoiding close attacks.

Intellect covers reasoning ability and learning. A character
with a high Intellect rank tends to be knowledgeable and
well-educated. Your Intellect modifier applies to:

•

•

Expertise,  Investigation, Technology,  and Treatment
skill checks.
Intellect checks to solve problems using sheer brain-
power when a specific skill doesn’t apply.

AWARENESS (AWE)

While  Intellect  covers  reasoning,  Awareness  describes
common sense and intuition, what some might call “wis-
dom.” A character with a high Intellect and a low Aware-
ness may be an “absent-minded professor” type, smart

[... truncated ...]
```

**Chunk 11** (`4e205a3c2745`):

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

**Chunk 12** (`60fdef9305c6`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

PL4

STR  2,  STA  2,  AGL  1,  DEX  1,  FGT  3,  INT  0,  AWE  1,  PRE  1
Equipment: Bulletproof vest (+4 Toughness vs. Ballistic), light
pistol,  tonfa,  cell  phone,  handcuffs.  Advantages:  Equipment
3.  Skills:  Athletics  3  (+5),  Expertise:  Current  Events  2  (+2),
Expertise:  Streetwise  3  (+3),  Expertise:  Police  Officer  4  (+4),
Insight  4  (+5),  Intimidation  2  (+3),  Investigation  2  (+2),
Perception 4 (+5), Ranged Combat: Pistols 4 (+5), Treatment 2
(+2), Vehicles 4 (+5). Offense: Init +1, Unarmed +3 (Damage 2),
Tonfa +3 (Damage 3), Pistol +5 (Ranged Damage 3). Defense:
Dodge  2,  Parry  4,  Fort  4, Tou  6/2, Will  2.  Totals:  Abilities 22 +
Powers 0 + Advantages 3 + Skills 17 + Defenses 5 = 47

This archetype focuses primarily on uniformed beat cops.
Detectives,  undercover.  and  plainclothes  officers  have
more  ranks  in  Investigate  and  often  in  other  social  skills
like Persuasion and Intimidation.

PL5

STR  2,  STA  2,  AGL  2,  DEX  2,  FGT  4,  INT  0,  AWE  1,  PRE  1
Equipment:  Submachine  gun,  riot  gear  (+4  Toughness),
tonfa,  cell  phone,  handcuffs.  Advantages:  Close  Attack  2,
Equipment 4. Skills: Athletics 3 (+5), Expertise: Current Events
2  (+2),  Expertise:  Streetwise  4  (+4),  Expertise:  Police  Officer  5
(+5), Expertise: Tactics 5 (+5), Intimidation 4 (+5), Perception 2
(+3),  Ranged  Combat:  Submachine  Gun  4  (+6),  Stealth  4  (+6),
Treatment  3  (+3).  Offense:  Init  +2,  Unarmed  +6  (Damage  2),
Tonfa +6 (Damage 3), SMG +6 (Ranged Damage 4, Multiattack).
Defense: Dodge 4, Parry 4, Fort 6, Tou 6/2, Will 3. Totals: Abilities
28 + Powers 0 + Advantages 6 + Skills 18 + Defenses 8 = 60

SWAT  (Special  Weapons  And  Tactics)  squads  are  made
up  of  police  officers  with  special  training  in  squad-level
tactics  and  weapon-use. They  deal  with  serious  criminal
threats, including mutant criminals.

MILITANT

PL4

STR  1,  STA  1,  AGL  1,  DEX  1,  FGT  1,  INT  1,  AWE  1,  PRE  1
Equipment:  Light  pistol,  9  points  of  equipment  as  needed.
Advantages: Equipment 3. Skills: Close Combat: Unarmed 4
(+5), Deception 4 (+5), Expertise: Choose One 3 (+4), Expertise:
Demolitions  6  (+7),  Intimidation  3  (+4),  Ranged  Combat:
Pistol 4 (+5), Technology 4 (+5), Vehicles 4 (+5). Offense: Init
+1,  Unarmed  +5  (Damage  1),  Pistol  +5  (Ranged  Damage  3).
Defense: Dodge 4, Parry 4, Fort 4, Tou 1, Will 2. Totals: Abilities
16 + P

[... truncated ...]
```

**Chunk 13** (`6717e2899e27`):

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

**Chunk 14** (`6802eda7b562`):

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

**Chunk 15** (`6805431193d6`):

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

**Chunk 16** (`6c8715df5e97`):

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

**Chunk 17** (`7420eccba7af`):

```
CHAPTER 1: THE BASICS

13

TASK

SKILL

Sneak up on
someone

Stealth

Perception

Con someone

Deception

Win a car race

Vehicles

Insight

Vehicles

Pretend to be
someone else

Steal a key chain
unnoticed

Deception

Perception

Sleight of Hand

Perception

Win a trivia contest

Expertise

Expertise

Break computer
security

Technology

Technology

OR

DEGREE

OR
THAN ...
(DC 20)

DC+15

DC+10

DC+5

DC

DC–5

DC–10

DC–15

DC–20

Four (Success)

Three (Success)

Two (Success)

One (Success)

One (Failure)

Two (Failure)

Three (Failure)

Four (Failure)

35

30

25

20

15

10

5

0

Some  checks  are  opposed.  They  are  made  against  an-
other character’s check result as the DC. Whoever gets the
higher result wins. An example is trying to bluff someone.
You roll a Deception check, while the GM rolls an Insight
check for your target. If you beat the target’s Insight check
result, you succeed.

For ties on opposed checks, the character with the higher
bonus  wins.  If  the  bonuses  are  the  same,  roll  d20.  On  a
1–10, one character wins, and on an 11–20, victory goes to
the other character; decide which character is “high” and
which is “low” before rolling.

Opposed checks offer the Gamemaster a useful tool for
comparing the efforts of two characters quickly and eas-
ily. This applies not only to skills, but also powers and, in
some cases, abilities. If two or more characters compete
at a particular task, you can resolve it with an opposed
check. The character with the highest check result wins.
Of  course,  you  can  play  things  out  if  you  want,  but
sometimes it’s good to be able to resolve things with a
quick opposed check and move on.

As Gamemaster, if you find yourself without a particular
rule to resolve a conflict or contest between characters,
the opposed check is your friend. Pick the appropriate
skill,  power,  or  ability,  make  checks  for  the  characters
and compare the results to see how they did.

opposing character’s modifier +10, just like the result of
a routine check (previously).

Active defenses in combat, where characters are focusing
on other actions, are generally routine opposition, which
is why attack checks are made against a DC of 10 + the ap-
propriate defense. Active opposed checks in combat are
an  option  when  a  character  goes  on  the  defensive.  See
Defend in the Action & Adventure chapter for details.

In cases where a check is a simple test of one character’s
capability  against  another,  with  no  

[... truncated ...]
```

**Chunk 18** (`8558df91a0a1`):

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

**Chunk 19** (`872471930ea9`):

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

**Chunk 20** (`94d3158e4b6b`):

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

**Chunk 21** (`aa943c38ef67`):

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

**Chunk 22** (`ab9b367b750f`):

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

**Chunk 23** (`b511fe78f53a`):

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

**Chunk 24** (`c0c1858f03fe`):

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

**Chunk 25** (`dcdc4c459ab6`):

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

**Chunk 27** (`eab98ce0e1fc`):

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

## Concept: Victor

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

## Concept: Vision

Chunk count: 16

### Chunk texts

**Chunk 1** (`14dd371ce972`):

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

**Chunk 2** (`301534069c2d`):

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

**Chunk 3** (`43d5c758bf78`):

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

**Chunk 4** (`442f2e5a5a37`):

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

**Chunk 5** (`6805431193d6`):

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

**Chunk 6** (`80099a87d308`):

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

**Chunk 7** (`872471930ea9`):

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

**Chunk 8** (`aa943c38ef67`):

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

**Chunk 9** (`ab9b367b750f`):

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

**Chunk 10** (`ac75d3f2b9e6`):

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

**Chunk 11** (`b95c26d52ee0`):

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

**Chunk 12** (`bc6e8d2fe577`):

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

**Chunk 13** (`d421725a8d2c`):

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

**Chunk 14** (`e17d1554782d`):

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

**Chunk 15** (`eab98ce0e1fc`):

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

**Chunk 16** (`5731b0e9cb2f`):

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

## Concept: Visual Conceal

Chunk count: 1
Performs actions: ['act_0184']

### Chunk texts

**Chunk 1** (`437f5039e60f`):

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

---

## Concept: Visual Concealment

Chunk count: 4

### Chunk texts

**Chunk 1** (`437f5039e60f`):

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

**Chunk 2** (`685941d4ae65`):

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

**Chunk 3** (`92b89ee67633`):

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

**Chunk 4** (`b511fe78f53a`):

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

---

## Concept: Visually Disabled

Chunk count: 6

### Chunk texts

**Chunk 1** (`04f4880a6e63`):

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

**Chunk 2** (`1b8011530852`):

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

**Chunk 3** (`685941d4ae65`):

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

**Chunk 4** (`80099a87d308`):

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

**Chunk 5** (`8757660124bd`):

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

**Chunk 6** (`db8b2bdf371a`):

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

---

## Concept: Vul- Nerable

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

## Concept: Vulnerable

Chunk count: 25
Performs actions: ['act_0521']

### Chunk texts

**Chunk 1** (`04f4880a6e63`):

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

**Chunk 2** (`086d54227650`):

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

**Chunk 4** (`14dd371ce972`):

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

**Chunk 8** (`43d5c758bf78`):

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

**Chunk 10** (`75f616f43b9d`):

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

**Chunk 11** (`7663d2fb489a`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

tures a character has to use and maintain rather than hav-
ing them as passive traits requiring no effort whatsoever.

•

•

•

Insulating Fur: You have a layer of fur that protects
you from intense heat and cold, giving you immunity
to those environments.

Internal Compartment: You can carry a portion of
your carrying capacity inside your body! You have a
pouch  or  compartment  of  some  sort,  able  to  hold
objects with a size rank no greater than 3 less than
your own (size -5 for a normal size rank -2 human).

Iron  Stomach: You  can  eat  anything  that’s  not  toxic
without ill effects, no matter how unpleasant it may be:
spoiled or particularly gross or spicy food, for example.

•  Mimicry: You can imitate almost any sound you’ve
heard, giving you a +10 bonus to Deception checks
to convince others your mimicked sounds are real.

The  Feature  effect  is  intended  to  round  out  various
minor traits and abilities characters might have, but it
is entirely optional and not meant to burden MUTANTS
& MASTERMINDS character design with needless amounts
of detail. It’s for traits with an actual game effect, not
merely  descriptors  or  background  color  (neither  of
which should cost any points). Ultimately, the Game-
master  decides  what  traits  merit  a  rank  (or  more)  of
Feature and what Features are permitted for any given
game or setting, using the examples given here.

If  a  “feature”  is  something  likely  to  come  up  only
occasionally, or even just once, then you are better
off  allowing  it  as  an  aspect  of  the  inspiration  and
power  stunt  rules  (see  the  Characteristics  chap-
ter), charging the player a hero point for the feature
when it comes into play. The player can then choose
whether  or  not  to  use  earned  power  points  to  ac-
quire the Feature as a regular part of the character’s
traits later on.

•

•

•

Quick  Change:  You  can  change  clothes—such  as
into or out of your costume—as a free action. With 2
ranks, you can change into any outfit at will.

Special  Effect: You  have  some  special  effect,  like  a
gust of wind at the right dramatic moment, or ideal
spotlighting, or personal theme music. The GM may
give  you  a  +2  bonus  for  favorable  circumstances
when your special effect is likely to impress people or
otherwise aid you.

Temporal  Inertia:  You  are  somehow  uniquely “an-
chored”  in  the  space-time  continuum,  making  you
immune  to

[... truncated ...]
```

**Chunk 12** (`80099a87d308`):

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

**Chunk 13** (`85cc7f979174`):

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

**Chunk 14** (`8757660124bd`):

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

**Chunk 15** (`9575430bef02`):

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

**Chunk 16** (`9c685bbd4830`):

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

**Chunk 17** (`ac75d3f2b9e6`):

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

**Chunk 19** (`b551e66974e2`):

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

**Chunk 21** (`db8b2bdf371a`):

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

**Chunk 22** (`dcdc4c459ab6`):

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

**Chunk 23** (`e087f7a0b70b`):

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

**Chunk 24** (`e17d1554782d`):

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

**Chunk 25** (`f41e7b13c82a`):

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

## Concept: Weaken

Chunk count: 18
Performs actions: ['act_0305', 'act_0309']
Receives actions: ['act_0303', 'act_0304', 'act_0306']

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

**Chunk 2** (`25d04efd242a`):

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

**Chunk 3** (`2b9b77a24290`):

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

**Chunk 4** (`2f5c20c3ef2c`):

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

**Chunk 5** (`44458c4fcb7e`):

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

**Chunk 6** (`72dc60c2e6cf`):

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

**Chunk 7** (`7973bfe6a35b`):

```
CHAPTER 8: ACTION & ADVENTURE

239

ing  Damage  resisted  by  Fortitude.  At  the  GM’s  discre-
tion,  radiation  exposure  can  lead  to  other  effects,  such
as damage to a hero’s power ranks (causing a temporary
decrease in powers).
VACUUM

The primary hazards of the vacuum of space are lack of air
and exposure to unfiltered ionizing radiation.

On  the  third  round  of  exposure  to  vacuum,  a  character
must  succeed  on  a  Fortitude  check  (DC  20)  each  round
or suffer from aeroembolism (“the bends”). A failed check
means excruciating pain as small air bubbles form in the
creature’s  bloodstream;  the  creature  is  stunned  and  re-
mains so until returned to normal atmospheric pressure.
Two or more degrees of failure impose the incapacitated
condition.

The real danger of vacuum comes from suffocation, though
holding one’s breath in vacuum damages the lungs. A char-
acter who attempts to hold his breath must make a Forti-
tude check (DC 15) every round; the DC increases by 1 each
round, and on a successful check the character loses a rank
of Stamina (from the pressure on the linings of his lungs). If
the check fails, or when the character simply stops holding
his breath, he begins to suffocate: the next round, he be-
comes incapacitated . The following round, he’s dying and
cannot stabilize until returned to a normal atmosphere.

Unfiltered  radiation  bombards  any  character  trapped  in
the vacuum of space without protective gear, see Radia-
tion, previously.

Heroes able to ignore the effects of deep space must have
Immunity to suffocation, vacuum, and radiation, at a mini-
mum. See the Immunity effect in the Powers chapter for
details.

CONFLICTS

A conflict is when two or more characters go up against each other, typically in a fight of some sort. Conflict between
heroes and villains is a prime part of MUTANTS & MASTERMINDS and a big element of the fun, just like the colorful and spec-
tacular fights in the superhero comic books.

ATTACKS

An attack check represents an attempt to hit a target with
an attack. When you make an attack check, roll the die and
add your bonus with that attack. If your result equals or
exceeds  the  target’s  defense,  your  attack  hits  and  may
have some effect.

Attack Check = d20 + attack bonus vs.
defense class

When you make an attack check and get a natural 20 (the
d20 actually shows 20), you automatically hit, regardless
of  your  target’s  defense,  and  you  score  a  threat. The  hit
might also 

[... truncated ...]
```

**Chunk 8** (`80099a87d308`):

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

**Chunk 9** (`800b98bbc634`):

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

**Chunk 10** (`821fc06edf41`):

```
CHAPTER 8: ACTION & ADVENTURE
CHAPTER 8: ACTION & ADVENTURE

CHAPTER 8: ACTION & ADVENTURE

RANK

1

3

4

7

8

9

11

13

14

15

Food poisoning: Affliction conditions typically include impaired and disabled, perhaps also dazed and
stunned for especially severe nausea.

Alcohol: Impaired and disabled are the most common conditions, perhaps dazed and stunned for severe
drunkenness, as for food poisoning.

Pesticides: Common Affliction conditions include impaired and disabled, although a large enough dose
or repeated exposure can also Weaken Stamina, even leading to death.

Chloroform: Affliction with dazed, stunned, and incapacitated effects.

Cobra venom: Typically a Weaken effect against Strength, Agility, or Stamina (sometimes more than one),
with Weaken Stamina potentially lethal, if the victim’s Stamina drops below –5.

Mustard gas: Affliction with impaired, disabled, and incapacitated effects, linked with a Damage effect
resisted by Fortitude.

Poisonous mushrooms: Typically a Fortitude Damage effect. Side-effects might include conditions like
dazed, impaired, or hindered.

Chlorine gas: Affliction with dazed, stunned, and incapacitated effects, linked with a Damage effect re-
sisted by Fortitude.

Curare: Affliction with dazed and hindered, stunned and immobilized, and incapacitated effects, linked
with Weaken Stamina, as the poison can potentially stop the target’s heart.

Cyanide: Fortitude Damage effect.

Nerve gas: Affliction with dazed and impaired, stunned and disabled, and incapacitated effects, linked
with Fortitude Damage.

16+

Alien, supernatural, or super-science toxins

RANK

1-2

3-5

4

6

7

8

10

11

12-14

15

Common colds: Usually nothing more than an impaired condition.

Influenza (including bird flu, swine flu, etc.): Affliction with impaired, disabled, and incapacitated.

Malaria: Affliction with impaired, disabled, and incapacitated.

Typhoid: Affliction with dazed, stunned, and incapacitated.

Rabies: Affliction with impaired, compelled (paranoid and violent behavior), and incapacitated.

Leprosy: Affliction with impaired, disabled, and incapacitated.

AIDS: Weaken Fortitude, leading to other opportunistic infections.

Smallpox: Affliction with hindered and impaired, disabled, and incapacitated linked with Weaken Stamina.

Bubonic  plague:  Affliction  with  dazed  and  hindered,  stunned  and  immobilized,  linked  with  Weaken
Stamina.

Ebola virus: Affliction with dazed, hindered, and impaired; stunned, immobilized, and 

[... truncated ...]
```

**Chunk 11** (`82504504b374`):

```
CHAPTER 6: POWERS

199

be “recovered” in some fashion, such as recharging, rest,
repair, reloading, and so forth. The GM decides when and
how a faded effect recovers, but it should generally occur
outside of combat and take at least an hour’s time. The GM
may  allow  a  hero  to  recover  a  faded  effect  immediately
and completely by spending a hero point.

usable only in certain situations and those usable only on
certain  things.  For  example  Only  While  Singing  Loudly,
Only While Flying, Only on Men (or Women), Only Against
Fire, Not Usable on Yellow Things, and so forth. As a gen-
eral rule, the effect must lose about half its usefulness to
qualify  for  this  modifier.  Anything  less  limiting  is  better
handled as an occasional complication.

FEEDBACK

-1 COST PER RANK

You suffer damage when a manifestation of your effect is
damaged. This  flaw  only  applies  to  effects  with  physical
(or  apparently  physical)  manifestations,  such  as  Create,
Illusion,  or  Summon,  for  example.  If  your  power’s  mani-
festation  is  damaged,  make  a  resistance  check  against
the attack’s damage rank, using your effect’s rank as the
resistance check bonus. For example, if a manifestation of
a rank 10 effect is attacked for damage 12, you must make
a resistance check against damage 12 with a +10 bonus
(the effect’s rank) in place of your normal Toughness.

GRAB-BASED

-1 COST PER RANK

An attack effect with this flaw requires you to successfully
grab a target before using the effect (see Grab, page 248).
This generally applies to an effect that is close range, since
you have to be in close combat to grab anyway. If the ef-
fect’s default range is not close, apply the Close modifier
as well. If you do not succeed on the grab, you cannot use
the effect. If your grab attempt succeeds, the effect occurs
automatically as a reaction.

Example: Lamprey has a draining touch that is a
Grab-Based  Weaken  Strength  effect.  So  the  mon-
strous  villain  has  to  take  a  standard  action  and
make a grab first in order to use it. If his close attack
check hits, the target makes a Dodge or Fortitude
resistance  check  against  Lamprey’s  Strength.  If  it
fails, the target then makes the Fortitude resistance
check against the villain’s Weaken effect to see how
much Strength Lamprey drains away.

This  flaw  is  essentially  a  form  of  Resistible,  with  a  grab
check rather than a regular resistance check (see the Re-
sistible flaw for more).

FLAT • -1

[... truncated ...]
```

**Chunk 12** (`87f598748db8`):

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

**Chunk 13** (`93337a63364b`):

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

**Chunk 14** (`b551e66974e2`):

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

**Chunk 15** (`d1e949b40c7a`):

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

**Chunk 16** (`d421725a8d2c`):

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

**Chunk 17** (`d4cad3e10e05`):

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

**Chunk 18** (`fc4ed8309dc8`):

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

---

## Concept: Weaken Stamina

Chunk count: 3

### Chunk texts

**Chunk 1** (`800b98bbc634`):

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

**Chunk 2** (`821fc06edf41`):

```
CHAPTER 8: ACTION & ADVENTURE
CHAPTER 8: ACTION & ADVENTURE

CHAPTER 8: ACTION & ADVENTURE

RANK

1

3

4

7

8

9

11

13

14

15

Food poisoning: Affliction conditions typically include impaired and disabled, perhaps also dazed and
stunned for especially severe nausea.

Alcohol: Impaired and disabled are the most common conditions, perhaps dazed and stunned for severe
drunkenness, as for food poisoning.

Pesticides: Common Affliction conditions include impaired and disabled, although a large enough dose
or repeated exposure can also Weaken Stamina, even leading to death.

Chloroform: Affliction with dazed, stunned, and incapacitated effects.

Cobra venom: Typically a Weaken effect against Strength, Agility, or Stamina (sometimes more than one),
with Weaken Stamina potentially lethal, if the victim’s Stamina drops below –5.

Mustard gas: Affliction with impaired, disabled, and incapacitated effects, linked with a Damage effect
resisted by Fortitude.

Poisonous mushrooms: Typically a Fortitude Damage effect. Side-effects might include conditions like
dazed, impaired, or hindered.

Chlorine gas: Affliction with dazed, stunned, and incapacitated effects, linked with a Damage effect re-
sisted by Fortitude.

Curare: Affliction with dazed and hindered, stunned and immobilized, and incapacitated effects, linked
with Weaken Stamina, as the poison can potentially stop the target’s heart.

Cyanide: Fortitude Damage effect.

Nerve gas: Affliction with dazed and impaired, stunned and disabled, and incapacitated effects, linked
with Fortitude Damage.

16+

Alien, supernatural, or super-science toxins

RANK

1-2

3-5

4

6

7

8

10

11

12-14

15

Common colds: Usually nothing more than an impaired condition.

Influenza (including bird flu, swine flu, etc.): Affliction with impaired, disabled, and incapacitated.

Malaria: Affliction with impaired, disabled, and incapacitated.

Typhoid: Affliction with dazed, stunned, and incapacitated.

Rabies: Affliction with impaired, compelled (paranoid and violent behavior), and incapacitated.

Leprosy: Affliction with impaired, disabled, and incapacitated.

AIDS: Weaken Fortitude, leading to other opportunistic infections.

Smallpox: Affliction with hindered and impaired, disabled, and incapacitated linked with Weaken Stamina.

Bubonic  plague:  Affliction  with  dazed  and  hindered,  stunned  and  immobilized,  linked  with  Weaken
Stamina.

Ebola virus: Affliction with dazed, hindered, and impaired; stunned, immobilized, and 

[... truncated ...]
```

**Chunk 3** (`bc6e8d2fe577`):

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

---
