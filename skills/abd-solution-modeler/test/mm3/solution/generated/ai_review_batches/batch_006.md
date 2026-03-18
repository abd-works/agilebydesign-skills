# Hypothesis concept review – batch 6

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

## Concept: Character

Chunk count: 27
Performs actions: ['act_0123', 'act_0129', 'act_0152', 'act_0360']

### Chunk texts

**Chunk 1** (`02d77d753dd0`):

```
CHAPTER 1: THE BASICS
CHAPTER 1: THE BASICS

CHAPTER 1: THE BASICS

is one degree of success, just as a result of 8 is one degree
of failure.

There is no limit to the number of degrees a check may have,
although more than two degrees of failure rarely matters,
and some degrees of success may have no further effect be-
yond a certain point (once you have succeeded as well as
is possible in a given situation). For example, failure on an
Acrobatics check to balance means you wobble and spend
that  turn  maintaining  your  balance,  but  don’t  move. Two
degrees of failure mean you lose your balance and fall! After
that point, further degrees of failure don’t really matter.

In cases where a single degree of success or failure is suffi-
cient, the rules simply specify “success” or “failure” without
giving a degree.

Specific types of graded checks—notably skill and resis-
tance checks—give specific results for degrees of success
and failure in their descriptions.

Some circumstances make checks easier or harder, result-
ing in a bonus or penalty to the check. Characters in a fa-
vorable situation are said to have a circumstance bonus
for the check, while those in a disadvantageous situation
are said to be have a circumstance penalty.

As  a  general  rule,  apply  a  modifier  of  plus  or  minus  2  if
the character is at a minor bonus or minor penalty, and
a modifier of plus or minus 5 if the character is at a major
bonus or major penalty for the check:

Technically,  circumstance  modifiers  could  apply  to  ei-
ther the check result of the difficulty class of a check, af-
fecting the character’s performance, or making the task
itself  easier  or  harder.  If  you  want  to  differentiate  be-
tween circumstance modifiers that affect performance
versus those that modify the difficulty of a task, feel free
to  do  so.  MUTANTS  &  MASTERMINDS  applies  circumstance
modifiers directly to the check result because it is easier
to deal with them consistently, and the game effect is
the same: the chance of success changes.

Circumstance  modifiers  are  another  useful  Gamemas-
ter  tool  for  handling  a  lot  of  the  variables  that  come
up  during  game  play.  Specific  examples  are  discussed
throughout  the  rules  for  various  types  of  checks.  One
example includes the following:
TOOLS

Some  tasks  require  tools.  If  tools  are  needed,  the  spe-
cific items are mentioned in the description of the task
or skill. If you don’t have the appropria

[... truncated ...]
```

**Chunk 2** (`03bc5d87aec7`):

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

**Chunk 3** (`115dd3a349cb`):

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

**Chunk 4** (`1d151f074127`):

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

**Chunk 5** (`25d04efd242a`):

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

**Chunk 6** (`2c3d57c2a1b3`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

WEAPON

EFFECT

CRITICAL

COST

Brass Knuckles

Club

Knife

Pepper Spray

Stun Gun

Battleaxe

Sword

Spear

Warhammer

Chain

Chainsaw

Nunchaku

Whip

Damage 1, bludgeoning

Damage 2, bludgeoning

Damage 1, piercing

Close Visual Dazzle 4, chemical

Affliction 5, electrical

Damage 3, slashing

Damage 3, slashing

Damage 3, piercing

Damage 3, bludgeoning

Damage 2, Imp. Grab, Imp. Trip, Reach 2

Damage 6, slashing

Damage 2, bludgeoning

Imp. Grab, Imp. Trip, Reach 3

20

20

19-20

20

20

20

19-20

19-20

20

20

20

19-20

20

1

2

2

2

5

3

4

4

3

6

6

3

5

Category: Melee weapons are categorized as simple, ar-
chaic, and exotic.

Effect: The effect a hit with the weapon causes, typically
Damage,  although  some  modern  melee  weapons  have
other effects. The effect has the normal cost given in the
Powers chapter. The effect may also have certain descrip-
tors, such as bludgeoning or slashing, for defining things
like resistance or vulnerability to certain effects.

Critical: The threat range for a critical hit with the weap-
on. Some weapons have a larger threat range than others.
Increasing a weapon’s threat range by 1 costs 1 point, like
the Improved Critical advantage.

Cost: This is the weapon’s cost in points. Characters pay
this cost from their equipment points to have a weapon of
this type as part of their regular equipment.

Brass Knuckles: Pieces of molded metal fitting over the
fingers, brass knuckles add +1 damage to your unarmed
strikes. They include similar items like armored gauntlets.

Club: Any of a number of blunt weapons used to strike,
including  nightsticks,  batons,  light  maces,  quarterstaffs,
and  similar  bludgeoning  weapons.  A  particularly  light
club might be only Damage 1.

Knife: A bladed weapon with a length less than 18 inches
or  so. This  includes  daggers,  stilettos,  sais,  switchblades,
bowie knives, and hunting knives, among others.

Pepper Spray: A liquid sprayed in a target’s face at close
range to blind them.

Stun Gun: A stun gun hits its target with a surge of elec-
tricity,  an  Affliction  that  can  daze,  stun,  and  potentially
incapacitate.

Battleaxe: A heavy-bladed axe that can be wielded with
one or two hands.

Sword:  A  blade  between  18  and  30  or  more  inches  in
length,  single  or  double-edged.  It  includes  longswords,
katanas, sabers, scimitars, and similar weapons.

Spear: A bladed pole-arm

[... truncated ...]
```

**Chunk 7** (`33e0c08724ff`):

```
CHAPTER 4: SKILLS
CHAPTER 4: SKILLS

Heroes sneak into the closely guarded lairs of criminal masterminds, infiltrate alien computer systems, and build devices
beyond the understanding of modern science. They can piece together obscure clues to a villain’s latest plot, run along
tightropes, and pilot vehicles through obstacle courses, all in a day’s work. In MUTANTS & MASTERMINDS, they do so through
the use of various skills, described in this chapter.

Skills are learned abilities, a combination of training (the skill) and natural talent (an ability rank). Each skill has a rank,
used as a bonus to the die roll when using the skill. To make a skill check, roll:

d20 + skill rank + ability modifier + miscellaneous modifiers

Your rank in a skill, based on the points you have invested
in that skill. If you have ranks in a skill you’re considered
trained  in  that  skill. You  can  use  some  skills  even  if  you
don’t have any ranks in them, known as using a skill un-
trained. Some skills may not be used untrained.

If  you  roll  a  20  on  the  die  when  making  a  check  you’ve
scored  a  critical  success.  Determine  the  degree  of  suc-
cess  normally  and  then  increase  it  by  one  degree.  This
can turn a low-level success into something more signifi-
cant, but more importantly, it can turn a failure into a full-
fledged success!

Each  skill  has  an  ability  modifier  applied  to  the  skill’s
checks. Each skill’s ability modifier is noted in its descrip-
tion and on the Skills table. If you use a skill untrained, the
ability modifier still applies to the skill check.

Miscellaneous modifiers to skill checks include modifiers
for circumstances, and bonuses from advantages or pow-
ers, among others.

The higher the total, the better the result. You’re usually look-
ing  for  a  total  that  equals  or  exceeds  a  particular  difficulty
class (DC), which may be based on another character’s traits.

Give your hero skill ranks by spending power points: 2 skill
ranks per power point. Skill ranks do not all need to be as-
signed to the same skill. You can split them between differ-
ent  skills.  Characters  can  perform  some  tasks  without  any
training,  using  only  raw  talent  (as  defined  by  their  ability
ranks), but skilled characters are better at such things. Those
with  the  right  combinations  of  skills  and  advantages  can
even hold their own against super-powered opponents.

Skill Cost = 1 power point per
2 skill ranks.

When y

[... truncated ...]
```

**Chunk 8** (`34cb0222a3bd`):

```
CHAPTER 1: THE BASICS
CHAPTER 1: THE BASICS

provides a framework for your imagination. It has rules to help determine what happens in your
stories and to resolve conflicts between characters and the challenges they face. With it, you can experience adventure
as a hero fighting against the forces of evil! Any adventure you can imagine is possible.

Like all games, MUTANTS & MASTERMINDS has rules. This chapter looks at the basic rules of the game and how they work,
giving you the foundation upon which the rest of the game is built.

uses a standard, or “core,” game me-
chanic to resolve actions. Whenever a character attempts
an action with a chance of failure, do the following:

•

•

•

Roll a twenty-sided die (or d20).

Add any relevant modifiers (for game traits like abili-
ties, skills, powers, or circumstances) to the number
rolled.

Compare  the  total  to  a  number  called  a  difficulty
class (abbreviated DC).

If the result equals or exceeds the difficulty class (set by the
GM  based  on  the  circumstances),  the  effort  succeeds.  If
the result is lower than the difficulty class, it fails.

This simple mechanic is used for nearly everything in MU-
MASTERMINDS, with variations based on what modi-
fiers are made to the roll, what determines the difficulty
class, and the exact degree of success and failure. Remem-
ber...

d20 + modifiers vs. difficulty class

... and you understand how to play most of the game!

One of the players in a MUTANTS & MASTERMINDS game takes
the  role  of  Gamemaster  (abbreviated  GM).  The  Game-
master is responsible for running the game—a combina-
tion  of  writer,  director,  and  referee.  The  GM  creates  the
adventures for the heroes, portrays the villains and sup-
porting characters, describes the world to the players, and
decides the outcome of the heroes’ actions based on the
roll of the die and the guidelines given in the rules. It’s a
big  job,  but  also  a  rewarding  one,  since  the  Gamemas-
ter gets to develop the world and all the characters in it,
along with inventing fun and exciting stories.

If  you’re  going  to  be  the  Gamemaster,  you  should  read
through this whole book carefully. You should have a firm
grasp of the rules, since you’re expected to interpret them
for the players to help decide what happens in the game.
You’ll  also  help  the  players  develop  their  own  heroes,
making sure they fit into the world and have potential for
exciting stories in their own right.

The other play

[... truncated ...]
```

**Chunk 9** (`3788ea99174b`):

```
CHAPTER 7: GADGETS & GEAR

211

Example:  Makeshift  needs  to  whip  up  a  mind-
shielding  device  to  confront  Gepetto,  who  has
seized control of his teammates. Immunity to Mind
Control (a common Affliction effect) cost 5 power
points, so the Technology check is DC 15 (10 + 5)
and takes 5 hours. Makeshift’s skill bonus is +15, so
he succeeds automatically. The construction check
is  also  DC  15  (10  +  the  device’s  cost).  It  takes  20
hours. Makeshift again succeeds automatically on
the  check.  However,  that’s  25  hours  total  to  build
the  mind-shield,  and  Gepetto  plans  to  send  his
new “puppets” into action in just a few hours. Even
taking a –15 check penalty to cut the time to one-
eighth only takes it down to just over three hours.
Makeshift needs that device right now, so he’s go-
ing to need to speed things up....

you speed up the process any further by taking a check
penalty.  You  can  use  a  jury-rigged  invention  again  by
spending another hero point.

Example:  Needing  to  get  the  mind  shield  device
ready  right  away,  Makeshift’s  player  decides  to
spend a hero point to jury-rig it. He skips the design
step  altogether  and  reduces  construction  time  to
5 rounds (just under a minute). The DC of the con-
struction check increases to 20, but still well within
Makeshift’s skill; the player only needs to roll a 5 or
better. He rolls a 25 result on the check and, a min-
ute later, Makeshift has a makeshift mind-shield he
hopes will protect him from Gepetto’s power long
enough to try and free his teammates from the vil-
lain’s influence.

DEVICES

MISHAPS

An inventor can choose to spend a hero point to jury-rig a
device; ideal for when a particular device is needed right
now.  When  jury-rigging  a  device,  skip  the  design  check
and  reduce  the  time  of  the  construction  check  to  one
round  per  power  point  of  the  device’s  cost,  but  increase
the DC of the check by +5. The inventor makes the check
and, if successful, has use of the device for one scene be-
fore it burns out, falls apart, blows up, or otherwise fails.
You can’t jury-rig an invention as a routine check, nor can

At  the  GM’s  discretion,  three  or  more  degrees  of  failure,
or a natural roll of 1, on any required inventing skill check
may result in some unexpected side-effect or mishap. Ex-
actly  what  depends  heavily  on  the  invention.  Inventing
mishaps can become a source of adventure ideas and put
the heroes in some diff

[... truncated ...]
```

**Chunk 10** (`3df9e8cdc695`):

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

**Chunk 12** (`714405399e02`):

```
CHAPTER 3: ABILITIES
CHAPTER 3: ABILITIES

CHAPTER 3: ABILITIES

The  exception  is  Toughness,  which  can  only  be  increased
above your base Stamina rank using advantages and pow-
ers, not by direct spending of power points. This reflects that
greater-than-normal Toughness is virtually always some sort
of special ability. See the Advantages and Powers chapters
for various options for improving Toughness, notably the De-
fensive Roll advantage and the Protection effect.

Dodge and Parry defenses require a measure of action to
be fully effective. Limits on your mobility, focus, and reac-
tion time adversely affect them. If you are vulnerable, your
Dodge  and  Parry  defense  ranks  are  halved  (divide  their
normal values by 2 and round up), and if you are defense-
less, they are both reduced to 0!

One  use  of  defenses  is  determining  a  defense  class,  or
the  difficulty  class  to  affect  a  target  with  a  particular  at-
tack. This  is  the  appropriate  defense,  plus  10,  just  like  a
routine  check  (indeed,  it  is  essentially  a  measure  of  the
character’s “routine” defense). So hitting a character with
a ranged attack goes against Dodge defense, giving the
attack a DC of (Dodge + 10). Similarly, affecting someone
with a mental power goes against Will defense, with a DC
of (Will + 10), and so forth. This is referred to as “targeting”
a defense, such as “targets Dodge” or “targets Will”.

The main defense class traits are Dodge, Parry, and Will.

Defenses  are  also  used  to  measure  the  ability  to  over-
come certain effects, involving a resistance check of the
defense plus a die roll against a difficulty class determined
by the effect or hazard. So you might make a Fortitude re-
sistance check for your hero to overcome a toxin, for ex-
ample, or a Dodge resistance check to avoid a trap just as
it is triggered, and so on. This is referred to as “resisting,”
such as “resisted by Fortitude” or “resisted by Dodge”.

The  main  resistance  check  traits  are  Dodge,  Fortitude,
Toughness, and Will.

When  things  start  happening  quickly,  MUTANTS  &  MASTER-
characters use their initiative bonuses to determine
who goes first. Each character involved in a conflict makes
a check of d20 + initiative modifier, which is:

Initiative Modifier = Agility + Advantages
(Improved Initiative) + Power Modifiers

Characters then act in initiative order, from highest to low-
est. For details see the Action & Adventure chapter.

```

**Chunk 13** (`7973bfe6a35b`):

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

**Chunk 14** (`7a6d568a6006`):

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

**Chunk 15** (`7db012c9a682`):

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

**Chunk 16** (`80099a87d308`):

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

**Chunk 17** (`800b98bbc634`):

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

**Chunk 18** (`83acf5380dc1`):

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

**Chunk 19** (`9136b6d87e68`):

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

**Chunk 20** (`a92e401b2501`):

```
CHAPTER 5: ADVANTAGES
CHAPTER 5: ADVANTAGES

Heroes are more than just skilled, they often have amazing advantages, beyond the abilities of ordinary people. In MU-
MASTERMINDS, advantages often allow heroes to “break the rules,” gaining access to and doing things most people
cannot, or simply doing them better.

Advantages are rated in ranks and bought with power points, just like abilities and skills. Advantages cost 1 power point
per rank. Some advantages have no ranks and are acquired only once, effectively at rank 1.
Advantage Cost = 1 power point per advantage rank

Each advantage’s description explains the benefit it provides. It also says if the advantage can be acquired in ranks and
the effects of doing so. Such advantages are listed as “Ranked” alongside the advantage name. Ranks in a advantage are
noted with a number after the advantage’s name, such as “Defensive Roll 2” (for a character who has taken two ranks
in the Defensive Roll advantage), just like skill and power ranks. If there is a maximum number of ranks a character can
take, it’s listed in parentheses after the word “Ranked” in the advantage’s heading.

Advantages are categorized as one of four types:

•

•

•

•

Combat  Advantages  are  useful  in  combat  and  of-
ten modify how various combat maneuvers are per-
formed.

Fortune  Advantages  require  and  enhance  the  use
of hero points.

General Advantages provide special abilities or bo-
nuses not covered by the other categories.

Skill Advantages offer bonuses or modifications to
skill use.

Each advantage is listed by name, type, and if the advan-
tage is available in multiple ranks, followed by a descrip-
tion of the advantage’s benefits. The effects of additional
ranks  of  the  advantage  (if  any)  are  noted  in  the  text  of
each advantage. In some cases a advantage’s description
mentions  the  normal  conditions  for  characters  who  do
not have the advantage for comparison.

COMBAT

When you make an accurate attack (see Maneuvers, page
249) you can take a penalty of up to –5 on the effect modi-
fier of the attack and add the same number (up to +5) to
your attack bonus.

SKILL

You can use your Acrobatics bonus or movement speed
rank in place of Deception to feint and trick in combat as if
your skill bonus or speed rank were your Deception bonus
(see the Deception skill description). Your opponent op-
poses the attempt with Acrobatics or Insight (whichever
is better).

ATTACK

COMBAT

When you make an all-out attack (s

[... truncated ...]
```

**Chunk 21** (`ae82f9b088df`):

```
CHAPTER 5: ADVANTAGES

137

LITERACY

Characters are assumed to be literate in their native language and any other language they know. At the GM’s discretion,
characters may have to spend an additional Languages rank to be literate in a language with a different alphabet or style
of writing from the character’s native language (such as Arabic, Japanese kanji or Russian Cyrillic for an English speaker).
Completely illiterate characters are faced with a potential Disability complication during the game.

level limits, like other uses of hero points. Multiple uses of
Inspire do not stack, only the highest bonus applies.

JACK-OF-ALL-TRADES

SKILL

GENERAL

You can go from prone to standing as a free action with-
out the need for an Acrobatics skill check.

INTERPOSE

GENERAL

Once  per  round,  when  an  ally  within  range  of  your  nor-
mal movement is hit by an attack, you can choose to place
yourself between the attacker and your ally as a reaction,
making  you  the  target  of  the  attack  instead. The  attack
hits  you  rather  than  your  ally,  and  you  suffer  the  effects
normally. You cannot use this advantage against area ef-
fects or perception range attacks, only those requiring an
attack check.

INVENTOR

SKILL

You can use the Technology skill to create inventions. See
Inventing, page 211, for details.

You can use any skill untrained, even skills or aspects of
skills  that  normally  cannot  be  used  untrained,  although
you must still have proper tools if the skill requires them.

LANGUAGES

SKILL, RANKED

You  can  speak  and  understand  additional  languages.
With one rank in this advantage, you know an additional
language. For each additional rank, you double your ad-
ditional  known  languages:  two  at  rank  2,  four  at  rank  3,
eight at rank 4, etc. So a character with Languages 7 is flu-
ent in 64 languages! Characters are assumed to be fluent
in any languages they know, including being able to read
and write in them.

For the ability to understand any language, see the Com-
prehend effect in the Powers chapter.

FORTUNE

Your presence reassures and lends courage to your allies.
As  a  standard  action,  you  can  spend  a  hero  point  to  re-

138

```

**Chunk 22** (`b551e66974e2`):

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

**Chunk 23** (`c87ce883452a`):

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

**Chunk 24** (`c9e9523951b6`):

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

**Chunk 25** (`ebca8c9dc40a`):

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

**Chunk 26** (`f62657e080ad`):

```
CHAPTER 8: ACTION & ADVENTURE

245

A successful attack has some effect on the target. Typical-
ly this is an effect from the Powers chapter, such as Dam-
age or Affliction. The effect has a rank, used to determine
a difficulty class for the target’s resistance check.

Resistance Difficulty = effect rank + 10

The target of the attack makes a resistance check against
the effect to determine what, if anything, happens.

Some  effects  are  not  resisted  just  once,  but  multiples
times. The later resistance checks represent how fast the
target is able to “shake off” the effect. Make a resistance
check  for  the  target  of  an  ongoing  effect  at  the  end  of
each  of  the  target’s  turns.  A  successful  check  ends  the
effect  and  removes  conditions  imposed  by  it.  A  failure
means  the  effect’s  conditions  persist,  as  given  in  the  ef-
fect’s description.

Example: Captain Thunder was hit by a Affliction
effect, leaving him blinded. At the end of his turn,
he makes a Fortitude resistance check against the
effect’s  DC  to  try  and  shake  it  off,  but  missed  the
check  by  2.  His  next  turn,  still  blind,  he  stumbles
and tries to strike the foe taunting him. At the end
of his turn, he makes another resistance check. Suc-
cess! He ends the Affliction effect and removes the
blinded condition. Next turn, the villain had better
watch out!

A  failed  resistance  check  against  an  attack  imposes  one
or more conditions on the target, depending on the type
of effect and the degree of failure. See the effect descrip-
tion and the Conditions section of The Basics chapter for
more on the various conditions.

ACTIONS

The  most  common  actions  characters  take  during  con-
flicts  are  listed  and  described  here.  The  GM  should  use
these as guidelines for dealing with unusual actions play-
ers may choose for their characters, basing them on the
existing action descriptions.

AID

If you are in position to attack an opponent, you can at-
tempt to aid an ally engaged in melee with that oppo-
nent as a standard action. This is like a team check (see
Team  Checks  in  The  Basics  chapter): You  make  an  at-
tack check against DC 10. If you succeed, you don’t actu-
ally hit or affect the opponent, but success grants your
ally  gains  a  +2  circumstance  bonus  on  an  attack  check
against  that  opponent  or  a  +2  circumstance  bonus  to

Defense  against  that  opponent  (your  choice)  until  the
end  of  your  ally’s  next 

[... truncated ...]
```

**Chunk 27** (`fc4ed8309dc8`):

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

## Concept: Character Death

Chunk count: 1

### Chunk texts

**Chunk 1** (`3df9e8cdc695`):

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

---

## Concept: Check Required

Chunk count: 4

### Chunk texts

**Chunk 1** (`17270869c240`):

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

**Chunk 2** (`9c685bbd4830`):

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

**Chunk 3** (`d2a75d4d379e`):

```
CHAPTER 6: POWERS

197

fects separately, apply this flaw to each of them, requiring
separate actions for each.

FLAT • -1 POINT PER RANK

If Activation is not automatic, apply the Check Required
flaw to the entire power as well and have the player make
the necessary check in order to activate the power. If the
check fails, the power does not activate, and the character
has to take the activation action to try again.

The Activation flaw does allow permanent effects that are
part of a power to be turned off, but only if the power as a
whole is deactivated. It does not affect the other aspects
of permanent duration, including the inability to improve
the effect with extra effort. The GM should decide if allow-
ing a permanent effect to have an Activation is appropri-
ate based on the specific effect and any others it is com-
bined with in the power.

Example:  Stonewall  has  the  power  to  turn  into
a  super-strong  rock-form.  This  is  a  combination
of  the  Enhanced  Strength,  Impervious  Protec-
tion,  and  Power-Lifting  effects.  Stonewall’s  player
applies  the  Activation  flaw  to  the  power,  saying
Stonewall has to concentrate and take a standard
action  to  assume  his  rock-form.  That  reduces  the
total cost of all three effects by 2 power points and
means  unless  Stonewall  takes  a  standard  action
to activate his rock-form, he cannot use any of the
power’s  effects,  even  including  permanent  ones
like Protection.

An effect with this flaw requires a check of some sort—usually
a skill check—with a base difficulty of 10, +1 for each addition-
al rank in Check Required. If the check fails, the effect doesn’t
work, although the action required to use it is expended (so
attempting to activate a standard action effect takes a stan-
dard action whether the check is successful or not).

If the check succeeds, the character gains the use of 1 ef-
fect rank per point the check exceeds the DC. Thus a check
result of 14 allows the character to use up to 4 ranks of the
effect.  If  a  lesser  rank  of  the  effect  doesn’t  do  anything,
then it’s the same as failing the check.

The required check occurs as part of the action to use the
effect and provides no benefit other than helping to ac-
tivate it. Normal modifiers apply to the check, and if you
are unable to make the required check for any reason, the
effect doesn’t work.

A natural 1 rolled on the check means it fails automatical-
ly, regardless of the check result. So there is always

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

## Concept: Check To Revive

Chunk count: 1

### Chunk texts

**Chunk 1** (`d5441abe7f45`):

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

---

## Concept: Checks

Chunk count: 2

### Chunk texts

**Chunk 1** (`dd71074ce318`):

```
CHAPTER 1: THE BASICS
CHAPTER 1: THE BASICS

CHAPTER 1: THE BASICS

As you can see, once you break it down, checks are actual-
ly fairly simple. All the Gamemaster has to say in response
to the player’s declaration is: “Okay, roll a Fighting check
to hit the villain,” letting the rest of the description stand
as what happens. Whether or not the hero is successful in
stopping the trap depends on the outcome of the attack
against the bad guy.

Of course, if the villain is expecting the hero, there might be
another trap, such as part of the catwalk rigged to fall away
under him, leaving him dangling above the acid vat and at
the villain’s mercy! In that case, the GM would respond to
the  player’s  description: “You  smash  through  the  skylight
and swing over to the catwalk, but when you do...” and go
on to describe what follows. The rest of the hero’s intended
action(s) are null and void, because things don’t always go
as planned when you’re dealing with cunning supervillains!

Checks are used to resolve all outcomes in MUTANTS & MAS-
TERMINDS,  so  once  you  understand  the  basic  concept,  the
rest is easy. For detailed examples of how to use checks in
the game and their effects, see the Action & Adventure
chapter.

If  you  roll  a  20  on  the  die  when  making  a  check  you’ve
scored a critical success. Determine the degree of success
normally and then increase it by one degree. This can turn
a low-level success into something more significant, but
more importantly, it can turn a failure into a full-fledged
success! A critical success with an attack check is called a
critical hit, discussed later in this chapter and in the Ac-
tion & Adventure chapter.

Checks are made against a difficulty class or DC, a num-
ber set by the GM, which your check must equal or exceed
to achieve success. So for a task with a DC of 15 you must
roll a check total of 15 or greater to succeed. In some cas-
es, the results of a check vary based on how much higher
or lower the result is than the DC, known as its degree of
success or failure.

DIFFICULTY (DC)

EXAMPLE (SKILL USED)

Very easy (0)

Notice something in plain sight
(Perception)

Easy (5)

Climb a knotted rope (Athletics)

Average (10)

Tough (15)

Challenging (20)

Formidable (25)

Heroic (30)

Super-heroic (35)

Nigh-impossible (40)

Hear an approaching security
guard (Perception)

Disarm an explosive
(Technology)

Swim against a strong current
(Athletics)

Climb a wet, slippery rock-face
(Athletics)

Overcome 

[... truncated ...]
```

**Chunk 2** (`e47577e0b729`):

```
CHAPTER 4: SKILLS

123

trying to perceive. So hearing a noise from 50 feet away is a
–5 modifier to your Perception check, for example.

The GM usually makes Perception checks secretly so you
don’t know whether there was nothing to notice or you
simply failed to notice it. The common sorts of Perception
checks are:
HEARING

Make a check against a DC based on how loud the noise
is or against an opposed Stealth check. Normal conversa-
tion is DC 0, a soft noise DC 10. Listening through a door
is +5 DC, +15 for a solid wall. While you’re asleep, hearing
something well enough to wake up is +10 DC.
SEEING

Make a check against a DC based on how visible the ob-
ject is or against an opposed Stealth check. Something in
plain sight is DC 0, while something subtle or easily over-
looked may be DC 5, 10 or more. Visual perception is also
used to detect someone in disguise (see the Deception
skill) or to notice a concealed object (see the Sleight of
Hand skill).

You  can  make  Perception  checks  involving  other  sense
types as well (see the Powers chapter for more on sense

types).  Noticing  something  obvious  to  a  sense  is  DC  0.
Less obvious things are DC 10 or so, hidden things DC 20
or more, and discerning details requires at least three de-
grees of success, as usual.

You can make a Perception check every time you have the
opportunity to notice something new. As a move action,
you  can  attempt  to  notice  something  you  failed  (or  be-
lieve you failed) to notice previously.

Various  sensory  effects  provide  modifiers  on  Perception
checks (see the Powers chapter for details).

Presence • Interaction

You’re skilled in dealing with people, from etiquette and
social  graces  to  a  way  with  words  and  public  speaking,
all of which helps to get your point across, make a good
impression, negotiate, and generally win people over to
your way of seeing things.

In negotiations, all participants roll Persuasion checks to
see  who  gains  the  advantage.  Opposed  checks  also  re-
solve  cases  where  two  advocates  plead  opposing  cases
before a third party.

Non-player  characters  each  have  an  initial  attitude  to-
wards you or your cause. The GM chooses the character’s
initial attitude based on circumstances. Most of the time,

124

```

---

## Concept: Chi Mastery

Chunk count: 1

### Chunk texts

**Chunk 1** (`6717e2899e27`):

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

---

## Concept: Clans

Chunk count: 0
Receives actions: ['act_0478']

### Chunk texts

---

## Concept: Close Attack

Chunk count: 14

### Chunk texts

**Chunk 1** (`17270869c240`):

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

**Chunk 3** (`301534069c2d`):

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

**Chunk 4** (`3e277f7add29`):

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

**Chunk 5** (`481ffcf3c778`):

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

**Chunk 7** (`a67593d532fb`):

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

**Chunk 9** (`cfadcb33d64b`):

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

**Chunk 10** (`d329357e5091`):

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

**Chunk 11** (`d5fc086574e9`):

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

**Chunk 12** (`db8b2bdf371a`):

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

**Chunk 13** (`dd5713402cfd`):

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

**Chunk 14** (`e087f7a0b70b`):

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

## Concept: Close Combat

Chunk count: 28
Receives actions: ['act_0159']

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

**Chunk 2** (`0b483461d2f8`):

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

**Chunk 4** (`2df9d8dcc068`):

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

**Chunk 5** (`301ee8a15809`):

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

**Chunk 6** (`473141849a66`):

```
CHAPTER 5: ADVANTAGES
CHAPTER 5: ADVANTAGES

CHAPTER 5: ADVANTAGES

COMBAT

You  can  make  grab  attacks  with  only  one  arm,  leaving
the other free. You can also maintain the grab while using
your other hand to perform actions. You are not vulner-
able while grabbing (see Grabbing in the Action & Ad-
venture chapter).

COMBAT

Your grab attacks are particularly difficult to escape. Op-
ponents  you  grab  suffer  a  –5  circumstance  penalty  on
checks to escape.

COMBAT, RANKED

You have a +4 bonus to your initiative checks per rank in
this advantage.

COMBAT

You have no penalty to attack checks to hit an object held
by another character (see Smash in the Action & Adven-
ture chapter).

COMBAT

You  have  no  penalty  to  your  attack  check  to  trip  an  op-
ponent and they do not get the opportunity to trip you.
When  making  a  trip  attack,  make  an  opposed  check  of
your Acrobatics or Athletics against your opponent’s Ac-

robatics  or  Athletics,  you  choose  which  your  opponent
uses to defend, rather than the target choosing (see Trip
in the Action & Adventure chapter). This is a good martial
arts advantage for unarmed fighters.

SKILL

You ignore the circumstance penalty for using skills with-
out proper tools, since you can improvise sufficient tools
with whatever is at hand. If you’re forced to work without
tools at all, you suffer only a –2 penalty.

COMBAT, RANKED

When  wielding  an  improvised  close  combat  weapon—
anything from a chair to a telephone pole or entire car—
you use your Close Combat: Unarmed skill bonus for at-
tack checks with the “weapon” rather than relying on your
general Close Combat skill bonus. Additional ranks in this
advantage give you a +1 bonus to Damage with impro-
vised weapons per rank. Your maximum Damage bonus is
still limited by power level, as usual.

INSPIRE

FORTUNE, RANKED (5)

You can inspire your allies to greatness. Once per scene, by
taking a standard action and spending a hero point, allies
able to interact with you gain a +1 circumstance bonus per
Inspire rank on all checks until the start of your next round,
with a maximum bonus of +5. You do not gain the bonus,
only  your  allies  do.  The  inspiration  bonus  ignores  power

```

**Chunk 7** (`4e205a3c2745`):

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

**Chunk 8** (`5610c4e8f961`):

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

**Chunk 9** (`60fdef9305c6`):

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

**Chunk 10** (`6717e2899e27`):

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

**Chunk 11** (`6805431193d6`):

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

**Chunk 12** (`6be13e770e51`):

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

**Chunk 13** (`818544ba2429`):

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

**Chunk 14** (`8d5f5f31a27f`):

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

**Chunk 15** (`919d7063d0ae`):

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

**Chunk 16** (`94d3158e4b6b`):

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

**Chunk 17** (`9575430bef02`):

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

**Chunk 18** (`997bf2eca013`):

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

**Chunk 19** (`9b4ab26032fa`):

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

**Chunk 20** (`ab9b367b750f`):

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

**Chunk 21** (`b511fe78f53a`):

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

**Chunk 22** (`c0c1858f03fe`):

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

**Chunk 23** (`cfadcb33d64b`):

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

**Chunk 24** (`da1c0758b454`):

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

**Chunk 26** (`dd71074ce318`):

```
CHAPTER 1: THE BASICS
CHAPTER 1: THE BASICS

CHAPTER 1: THE BASICS

As you can see, once you break it down, checks are actual-
ly fairly simple. All the Gamemaster has to say in response
to the player’s declaration is: “Okay, roll a Fighting check
to hit the villain,” letting the rest of the description stand
as what happens. Whether or not the hero is successful in
stopping the trap depends on the outcome of the attack
against the bad guy.

Of course, if the villain is expecting the hero, there might be
another trap, such as part of the catwalk rigged to fall away
under him, leaving him dangling above the acid vat and at
the villain’s mercy! In that case, the GM would respond to
the  player’s  description: “You  smash  through  the  skylight
and swing over to the catwalk, but when you do...” and go
on to describe what follows. The rest of the hero’s intended
action(s) are null and void, because things don’t always go
as planned when you’re dealing with cunning supervillains!

Checks are used to resolve all outcomes in MUTANTS & MAS-
TERMINDS,  so  once  you  understand  the  basic  concept,  the
rest is easy. For detailed examples of how to use checks in
the game and their effects, see the Action & Adventure
chapter.

If  you  roll  a  20  on  the  die  when  making  a  check  you’ve
scored a critical success. Determine the degree of success
normally and then increase it by one degree. This can turn
a low-level success into something more significant, but
more importantly, it can turn a failure into a full-fledged
success! A critical success with an attack check is called a
critical hit, discussed later in this chapter and in the Ac-
tion & Adventure chapter.

Checks are made against a difficulty class or DC, a num-
ber set by the GM, which your check must equal or exceed
to achieve success. So for a task with a DC of 15 you must
roll a check total of 15 or greater to succeed. In some cas-
es, the results of a check vary based on how much higher
or lower the result is than the DC, known as its degree of
success or failure.

DIFFICULTY (DC)

EXAMPLE (SKILL USED)

Very easy (0)

Notice something in plain sight
(Perception)

Easy (5)

Climb a knotted rope (Athletics)

Average (10)

Tough (15)

Challenging (20)

Formidable (25)

Heroic (30)

Super-heroic (35)

Nigh-impossible (40)

Hear an approaching security
guard (Perception)

Disarm an explosive
(Technology)

Swim against a strong current
(Athletics)

Climb a wet, slippery rock-face
(Athletics)

Overcome 

[... truncated ...]
```

**Chunk 27** (`e53b2f1b3ca2`):

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

**Chunk 28** (`eab98ce0e1fc`):

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

## Concept: Close Duration

Chunk count: 6

### Chunk texts

**Chunk 1** (`2f5c20c3ef2c`):

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

**Chunk 2** (`40cf06e030f1`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

This section describes the various power effects available in MUTANTS & MASTERMINDS. They are listed in alphabetical order.

ATTACK

Action: Standard • Range: Close
Duration: Instant • Cost: 1 point per rank

TYPE

You can impose some debilitating condition or conditions
on a target by making a close attack. You set the conditions
your  Affliction  causes  at  each  degree  when  you  acquire  it
and they may not be changed. Higher degree conditions re-
place lower degree conditions and do not stack with them.
See the possible conditions for each degree under the Af-
fliction Resistance Check table. The target resists with For-
titude or Will defense (chosen when you take the effect):

Fortitude or Will vs.
DC [Affliction rank + 10]

Success: No effect.

Failure  (one  degree):  The  target  is  dazed,  entranced,
fatigued,  hindered,  impaired,  or  vulnerable  (choose
one). Potential descriptors include coughing or sneez-
ing,  creeping  mental  influence,  drowsiness,  euphoria,
fear, itchiness, lethargy, nausea, pain, or tipsiness.

Failure (two degrees): The target is compelled, defense-
less,  disabled,  exhausted,  immobile,  prone,  or  stunned
(choose  one).  Potential  descriptors  include  agonizing
pain, confusion, ecstasy, momentary emotional or men-
tal influence, paralysis, seizure, terror, or vomiting.

Failure  (three  degrees):  The  target  is  asleep,  con-
trolled,  incapacitated,  paralyzed,  transformed  or  un-
aware (choose one).

The target of an Affliction makes a resistance check at the
end of each of his turns to remove first and second degree
conditions. Third  degree  conditions  require  a  minute  of
recovery time or outside aid, such as the Treatment skill or
Healing effect (DC 10 + rank).

The exact nature and descriptors of the Affliction are up
to you, chosen when you acquire the effect, with the GM’s
approval;  some  examples  are  provided,  but  feel  free  to
make up your own.

EXTRAS

Alternate Resistance: Some Afflictions may be initially re-
sisted by Dodge, representing the need for quick reaction

Action • Range
Duration • Cost

Name: What the effect is called.

Type: The type of effect.

Action: The action required to use the effect: standard,
move, free, reaction, or none.

Range: The range at which the effect operates: person-
al, close, ranged, perception, or rank.

Duration: The effect’s duration: instant, concentration,
sustained, continuous, or perm

[... truncated ...]
```

**Chunk 3** (`44458c4fcb7e`):

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

**Chunk 4** (`7f148070d8bb`):

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

**Chunk 5** (`a9a5f596da97`):

```
CHAPTER 6: POWERS

161

Levitation: You can only move vertically, straight up and
down, and not side to side, although you can allow your-
self to be carried along in the direction of the wind hori-
zontally. –1 cost per rank.

Platform: Your Flight is reliant on some sort of platform on
which  you  stand  or  sit.  If  you  fail  a  resistance  check  while
flying,  or  you  are  grabbed  by  someone  standing  on  the
ground, you’re knocked or pulled off your platform and can-
not fly. You can regain the use of your flying platform by reac-
tivating your Flight effect on your next turn. –1 cost per rank.

Wings: You have wings that allow you to fly, but they run
the risk of being fouled or restrained, which prevents you
from flying. If you are immobilized, restrained, or bound,
you cannot fly. You can regain the use of your wings by
reactivating  your  Flight  effect  once  you  are  no  longer
affected  by  the  aforementioned  conditions.  –1  cost
per rank.

GROWTH

GENERAL

Action: Free • Range: Personal
Duration: Sustained • Cost: 2 points per rank

You can temporarily increase your size, gaining Strength
and  Stamina  at  the  cost  of  becoming  a  bigger,  heavier,
less agile target, unable to maneuver through small spac-
es. Growth modifiers are restricted by power level limits.

Each  rank  of  Growth  adds  1  rank  to  your  Strength  and
Stamina  (constructs  add  1  rank  to  Strength  and Tough-
ness if they lack Stamina) and adds 1 rank to your mass.
Every  two  ranks  adds  a  +1  bonus  to  Intimidation.  Every
8 ranks adds 1 to your Speed. Every rank of Growth sub-
tracts 1 from your Stealth checks. Every 2 ranks (rounded
up) subtracts 1 from your Dodge and Parry defenses. Ev-
ery  4  ranks  of  Growth  increases  your  size  rank  by  1  (or-
dinary humans start out at size rank –2, between 3 and
6  feet  tall).  So  at  Growth  8,  you  have  +8  Strength  and
Stamina,  +4  to  Intimidation,  +1  Speed,  but  -8  to
Stealth,  –4  Dodge  and  Parry,  and  you  are  size
rank 0 (around 30 feet tall). Increases to your
Strength and Stamina also improve related
traits like your Strength Damage, Forti-
tude, and Toughness.
EXTRAS

Permanent:
Permanent
Growth,  typically  with  In-
nate, suits giant-sized char-
acters  and  creatures  that
are a fixed larger size. +0 cost
per rank.

HEALING

GENERAL

Action: Standard • Range: Close
Duration: Instant • Cost: 2 points per rank

You can heal Damage conditions by touching a subject
and taking 

[... truncated ...]
```

**Chunk 6** (`b60c97b07a3c`):

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

## Concept: Cold

Chunk count: 2
Performs actions: ['act_0210']

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

**Chunk 2** (`e17d1554782d`):

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

---

## Concept: Combat

Chunk count: 7

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

**Chunk 2** (`3a7f34326ad9`):

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

**Chunk 3** (`473141849a66`):

```
CHAPTER 5: ADVANTAGES
CHAPTER 5: ADVANTAGES

CHAPTER 5: ADVANTAGES

COMBAT

You  can  make  grab  attacks  with  only  one  arm,  leaving
the other free. You can also maintain the grab while using
your other hand to perform actions. You are not vulner-
able while grabbing (see Grabbing in the Action & Ad-
venture chapter).

COMBAT

Your grab attacks are particularly difficult to escape. Op-
ponents  you  grab  suffer  a  –5  circumstance  penalty  on
checks to escape.

COMBAT, RANKED

You have a +4 bonus to your initiative checks per rank in
this advantage.

COMBAT

You have no penalty to attack checks to hit an object held
by another character (see Smash in the Action & Adven-
ture chapter).

COMBAT

You  have  no  penalty  to  your  attack  check  to  trip  an  op-
ponent and they do not get the opportunity to trip you.
When  making  a  trip  attack,  make  an  opposed  check  of
your Acrobatics or Athletics against your opponent’s Ac-

robatics  or  Athletics,  you  choose  which  your  opponent
uses to defend, rather than the target choosing (see Trip
in the Action & Adventure chapter). This is a good martial
arts advantage for unarmed fighters.

SKILL

You ignore the circumstance penalty for using skills with-
out proper tools, since you can improvise sufficient tools
with whatever is at hand. If you’re forced to work without
tools at all, you suffer only a –2 penalty.

COMBAT, RANKED

When  wielding  an  improvised  close  combat  weapon—
anything from a chair to a telephone pole or entire car—
you use your Close Combat: Unarmed skill bonus for at-
tack checks with the “weapon” rather than relying on your
general Close Combat skill bonus. Additional ranks in this
advantage give you a +1 bonus to Damage with impro-
vised weapons per rank. Your maximum Damage bonus is
still limited by power level, as usual.

INSPIRE

FORTUNE, RANKED (5)

You can inspire your allies to greatness. Once per scene, by
taking a standard action and spending a hero point, allies
able to interact with you gain a +1 circumstance bonus per
Inspire rank on all checks until the start of your next round,
with a maximum bonus of +5. You do not gain the bonus,
only  your  allies  do.  The  inspiration  bonus  ignores  power

```

**Chunk 4** (`481ffcf3c778`):

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

**Chunk 5** (`4eeee75475f7`):

```
CHAPTER 5: ADVANTAGES
CHAPTER 5: ADVANTAGES

CHAPTER 5: ADVANTAGES

applies to when you acquire it and the GM must approve
it. You can take Ultimate Effort multiple times, each time,
it  applies  to  a  different  check. This  advantage  may  not
be  used  after  you’ve  rolled  the  die  to  determine  if  you
succeed.

The following are some potential Ultimate Efforts. The GM
is free to add others suitable to the series.

•

•

•

Ultimate Aim: When  you  take  a  standard  action  to
aim an attack (see Aim, page 246), you can spend a
hero point to apply a 20 result to the attack check on
the following round. Since the Ultimate Aim bonus is
not a natural 20, it also does not qualify as an auto-
matic or critical hit.

Ultimate Resistance: You can spend a hero point to
apply a 20 result to a resistance check with one de-
fense determined when you acquire this advantage.

Ultimate Skill: You can spend a hero point to apply a
20 result to checks with a particular skill.

COMBAT

You are especially attuned to danger. You are not vulnera-
ble when surprised or otherwise caught off-guard. You are
still made vulnerable by effects that limit your mobility.

COMBAT

If you take the defend action (see Defend in the Action
&  Adventure  chapter)  and  successfully  defend  against
a  close  weapon  attack,  you  can  make  a  disarm  attempt
against the attacker immediately as a reaction. The disarm
attempt  is  carried  out  normally,  including  the  attacker
getting the opportunity to disarm you.

COMBAT

If you take the defend action (see Defend in the Action
&  Adventure  chapter)  and  successfully  defend  against
a close weapon attack, you can make an attack against
the attacker’s weapon immediately as a reaction. This re-
quires an attack check and inflicts normal damage to the
weapon if it hits (see Smash in the Action & Adventure
chapter).

WELL-INFORMED

SKILL

You are exceptionally well-informed. When encountering
an individual, group, or organization for the first time, you
can make an immediate Investigation or Persuasion skill
check to see if your character has heard something about
the subject. Use the guidelines for gathering information
in the Investigation skill description to determine the lev-
el of information you gain. You receive only one check per
subject  upon  first  encountering  them,  although  the  GM
may allow another upon encountering the subject again
once significant time has passed.

```

**Chunk 6** (`a92e401b2501`):

```
CHAPTER 5: ADVANTAGES
CHAPTER 5: ADVANTAGES

Heroes are more than just skilled, they often have amazing advantages, beyond the abilities of ordinary people. In MU-
MASTERMINDS, advantages often allow heroes to “break the rules,” gaining access to and doing things most people
cannot, or simply doing them better.

Advantages are rated in ranks and bought with power points, just like abilities and skills. Advantages cost 1 power point
per rank. Some advantages have no ranks and are acquired only once, effectively at rank 1.
Advantage Cost = 1 power point per advantage rank

Each advantage’s description explains the benefit it provides. It also says if the advantage can be acquired in ranks and
the effects of doing so. Such advantages are listed as “Ranked” alongside the advantage name. Ranks in a advantage are
noted with a number after the advantage’s name, such as “Defensive Roll 2” (for a character who has taken two ranks
in the Defensive Roll advantage), just like skill and power ranks. If there is a maximum number of ranks a character can
take, it’s listed in parentheses after the word “Ranked” in the advantage’s heading.

Advantages are categorized as one of four types:

•

•

•

•

Combat  Advantages  are  useful  in  combat  and  of-
ten modify how various combat maneuvers are per-
formed.

Fortune  Advantages  require  and  enhance  the  use
of hero points.

General Advantages provide special abilities or bo-
nuses not covered by the other categories.

Skill Advantages offer bonuses or modifications to
skill use.

Each advantage is listed by name, type, and if the advan-
tage is available in multiple ranks, followed by a descrip-
tion of the advantage’s benefits. The effects of additional
ranks  of  the  advantage  (if  any)  are  noted  in  the  text  of
each advantage. In some cases a advantage’s description
mentions  the  normal  conditions  for  characters  who  do
not have the advantage for comparison.

COMBAT

When you make an accurate attack (see Maneuvers, page
249) you can take a penalty of up to –5 on the effect modi-
fier of the attack and add the same number (up to +5) to
your attack bonus.

SKILL

You can use your Acrobatics bonus or movement speed
rank in place of Deception to feint and trick in combat as if
your skill bonus or speed rank were your Deception bonus
(see the Deception skill description). Your opponent op-
poses the attempt with Acrobatics or Insight (whichever
is better).

ATTACK

COMBAT

When you make an all-out attack (s

[... truncated ...]
```

**Chunk 7** (`b2722c49426d`):

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
