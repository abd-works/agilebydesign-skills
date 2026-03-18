# Hypothesis concept review – batch 11

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

## Concept: Disarm

Chunk count: 2
Performs actions: ['act_0147']
Receives actions: ['act_0156']

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

**Chunk 2** (`f6ef830f7b6b`):

```
CHAPTER 4: SKILLS

127

goes off. For every two full degrees of success, the explo-
sive deals +5 damage to the structure. Failure means the
explosive does not go off as planned, while more than one
degree of failure means the charge goes off while you are
setting it! In all cases, the explosive deals normal damage
to all other targets.

You  can  make  an  explosive  device  more  difficult  to  dis-
arm. To do so, choose a disarm difficulty class before mak-
ing  your  check  to  set  the  detonator. Your  DC  to  set  the
detonator  is  the  desired  disarm  DC.  Failure  means  the
explosive fails to go off as planned. Two or more degrees
of failure mean the explosive goes off as the detonator is
being installed!

Disarming an explosive also requires a Technology check.
The DC is usually 10, unless the person who set the deto-
nator chose a higher disarm DC (previously). If you fail the
check, you do not disarm the explosive. With more than a
degree of failure, the explosive goes off. Setting or disarm-
ing a detonator is a standard action.
INVENTING

If you have the Inventor advantage (see the Advantages
chapter),  you  can  use  Technology  to  create  inventions,
temporary devices. See Inventing, page 211, for details.

SECURITY

You  can  use  Technology  to  disarm  or  sabotage  various
security devices, including locks, traps, and sensors. This
takes  at  least  a  minute,  possibly  longer,  at  the  GM’s  dis-
cretion.  The  GM  makes  your  Technology  check  secretly
so you don’t necessarily know right away if you have suc-
ceeded. The Gamemaster sets the DC of the check based
on the level of security:

Simple lock or home alarm system

Quality lock or home alarm system

Business and corporate security

High security: branch bank vault, museum

Very high security: bank headquarters
vault, medium prison

Maximum security: highly secure prison

Super-max security: super-prison

MODIFIERS

Preventing your tampering
 from being noticed.

DC

10

15

20

25

30

35

40

+5

Failure  on  your  skill  check  means  nothing  happens,  but
you can keep trying. More than one degree of failure sets
off the security or trap, if it is possible to do so.

128

```

---

## Concept: Disguise

Chunk count: 2
Receives actions: ['act_0257']

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

**Chunk 2** (`f41e7b13c82a`):

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

## Concept: Disruption

Chunk count: 1
Performs actions: ['act_0079']

### Chunk texts

**Chunk 1** (`cfadcb33d64b`):

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

---

## Concept: Disruption Attacks

Chunk count: 1

### Chunk texts

**Chunk 1** (`cfadcb33d64b`):

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

---

## Concept: Dodge

Chunk count: 89
Performs actions: ['act_0081', 'act_0413', 'act_0414', 'act_0429']
Receives actions: ['act_0011', 'act_0104', 'act_0112', 'act_0120', 'act_0154']...

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

**Chunk 3** (`068f6ea2c39b`):

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

**Chunk 4** (`086d54227650`):

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

**Chunk 5** (`0b30704b97a2`):

```
CHAPTER 1: THE BASICS

15

+/-2 for bonus/penalty
+/-5 for major bonus/penalty

Sometimes  characters  work  together  and  help  each  other
out. In this case, one character (usually the one with the high-
est bonus) is considered the leader of the effort and makes
the check normally, while each helper makes the same type
of check using the same trait(s) against DC 10. The helpers’ in-
dividual degrees of success (and failure!) are added together
to achieve the final outcome of the assistance.

Success grants the leader a +2 circumstance bonus. Three
or more total degrees of success grant a +5 circumstance
bonus.  One  degree  of  failure  provides  no  modifier,  but
two or more impose a –2 circumstance penalty!

The GM sets the limit on how many characters can help as
part of a team check. Regardless of the number of help-
ers, the leader’s bonus cannot be more than +5 (for three
or more total degrees of success) nor the penalty greater
than –2 (for two or more total degrees of failure).

Team Check = +2 circumstance bonus
for one total degree of success
+5 circumstance bonus for three or more total degrees of success
-2 circumstance penalty for two or more total degrees of failure

An  attack  check  determines  whether  or  not  you  hit  an
opponent  in  combat  with  an  attack.  It  is  a  d20  roll  plus
your bonus with that particular attack, usually based off
of  Fighting  or  Dexterity  and  appropriate  modifiers,  like
the Close and Ranged Combat skills. The difficulty is your
target’s  defense  class:  Parry  for  close  attacks,  Dodge  for
ranged attacks. Certain attacks may target other defenses.
If  you  equal  or  exceed  your  target’s  defense  class  result,
your attack hits. Otherwise, you miss.

Attack Check = d20 + attack bonus +
modifiers vs. defense class

A natural 20 on an attack check (where the die comes up
20) always hits and may be a critical hit (see Critical Hits in
the Action & Adventure chapter). A natural 1 on an attack
check (where the die comes up 1) always misses, regardless
of the check total. This differs from normal checks and re-
flects the variable and unpredictable nature of combat.

A  resistance  check  is  an  attempt  to  resist  different  ef-
fects, ranging from damage and injury to traps, poisons,
and various power effects. A resistance check is a d20 roll
+  the  appropriate  defense  (typically  Dodge,  Fortitude,
Toughness, or Will).

Resistance Check = d20 + defense bonus +
modifiers vs. hazard’s D

[... truncated ...]
```

**Chunk 6** (`1094aa03eba1`):

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

**Chunk 7** (`138e63aeed36`):

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

**Chunk 8** (`14dd371ce972`):

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

**Chunk 9** (`19a54c3b3576`):

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

**Chunk 10** (`1a59d1dc4a9a`):

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

**Chunk 11** (`1b8011530852`):

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

**Chunk 12** (`238fc7bd4809`):

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

**Chunk 13** (`25d04efd242a`):

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

**Chunk 14** (`267bbd73af09`):

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

**Chunk 15** (`2b9b77a24290`):

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

**Chunk 16** (`2f5c20c3ef2c`):

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

**Chunk 17** (`301534069c2d`):

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

**Chunk 18** (`301ee8a15809`):

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

**Chunk 19** (`3c75d5b04a0e`):

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

**Chunk 20** (`40cf06e030f1`):

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

**Chunk 21** (`43d5c758bf78`):

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

**Chunk 22** (`442f2e5a5a37`):

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

**Chunk 23** (`481ffcf3c778`):

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

**Chunk 24** (`5ec359de437f`):

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

**Chunk 25** (`60fdef9305c6`):

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

**Chunk 26** (`634190f2dd84`):

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

**Chunk 27** (`661dd344a1d2`):

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

**Chunk 28** (`6805431193d6`):

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

**Chunk 29** (`685941d4ae65`):

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

**Chunk 30** (`6be13e770e51`):

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

**Chunk 31** (`6c8715df5e97`):

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

**Chunk 32** (`6d18f5cb0ab3`):

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

**Chunk 33** (`714405399e02`):

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

**Chunk 34** (`75f616f43b9d`):

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

**Chunk 35** (`7b2254220623`):

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

**Chunk 36** (`80099a87d308`):

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

**Chunk 37** (`803cb2a8c272`):

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

**Chunk 38** (`82504504b374`):

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

**Chunk 39** (`84157ccb1121`):

```
CHAPTER 8: ACTION & ADVENTURE
CHAPTER 8: ACTION & ADVENTURE

CHAPTER 8: ACTION & ADVENTURE

Now the remaining smugglers get to go. They draw their guns and shoot at you!

The GM rolls attack checks against the heroes. Two smugglers shoot at Ultramarine and three shoot at Princess, but they both
have Impervious Toughness 8. Since the smugglers’ guns can’t hurt them, the GM does not bother rolling the attack checks. The
remaining two shoot at Rook, but one is impaired and the other blind, so they both miss by a mile.

Rook, you easily avoid the clumsy shots, especially from the guys dazzled by the flash bomb. Princess, Ultramarine, a
couple of stray shots ricochet off of you harmlessly.
ROUND 2

That brings us back to the top of the order. Princess?

Princess: I’m going to punch-out one of the smugglers! “Hey, watch the couture, boys!”

GM: Roll an unarmed attack check.

Princess: Rolls, gets a natural 20. A critical hit!

GM: Glances at Princess’ Strength of 12, and the +5 critical hit DC modifier, making the Toughness resistance DC (15 + 12 + 5)
or 32. No way the smuggler can succeed.

Wow! You send the guy flying right off the deck and into the drink! Sploosh!

Then, suddenly…

The GM rolls an attack check against Princess, getting a 15 result. Normally this would miss her Dodge defense of 18, but this is
a surprise attack, so Princess is vulnerable and her Dodge is halved to 4, rather than 8, making the DC a 14.

…a steel mesh net launches out of the doorway of the control cabin of the ship. Princess, give me a Dodge resistance
check.

Princess: Rolls a 5 for a total of 13. Um… 13?

GM: Compares it against the DC of 19. Two degrees of failure.

…the net wraps around you tightly, leaving you immobilized and defenseless, Princess.

From out of the control cabin lumbers a massive armored figure in red and silver, one arm ending in a lobster-like servo-
claw.

Ultramarine: Trawler!

GM: In Trawler’s voice. Who did you think was running this operation, heroes? Now back off!

Ultramarine: Is it my turn?

GM: No. It would be, but you delayed until after Rook, remember? Rook, it’s your turn, then Ultramarine and the smug-
glers.

Rook: I don’t think my weapons will do much against Trawler’s armor. Can I help Princess get free from the net?

GM: Your throwing talons might help cut through it.

Rook: Okay, I’ll do that.

GM: Since the net is immobile, do you want to roll or make a routine check?

Rook: If I roll, I get a damage bonus, right? The GM nods. Okay, I’l

[... truncated ...]
```

**Chunk 40** (`8558df91a0a1`):

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

**Chunk 41** (`85cc7f979174`):

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

**Chunk 42** (`8757660124bd`):

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

**Chunk 43** (`87f598748db8`):

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

**Chunk 44** (`8d5f5f31a27f`):

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

**Chunk 45** (`9136b6d87e68`):

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

**Chunk 46** (`919d7063d0ae`):

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

**Chunk 47** (`92b89ee67633`):

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

**Chunk 48** (`9575430bef02`):

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

**Chunk 49** (`997bf2eca013`):

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

**Chunk 50** (`9aad078a59d7`):

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

**Chunk 51** (`9b4ab26032fa`):

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

**Chunk 52** (`9b8b75c1b5e7`):

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

**Chunk 53** (`9c7fcc5049c4`):

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

**Chunk 54** (`a67593d532fb`):

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

**Chunk 55** (`a8c6225b93ed`):

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

**Chunk 56** (`a92e401b2501`):

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

**Chunk 57** (`a9a5f596da97`):

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

**Chunk 58** (`aa943c38ef67`):

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

**Chunk 59** (`ab9b367b750f`):

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

**Chunk 60** (`ac75d3f2b9e6`):

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

**Chunk 61** (`b511fe78f53a`):

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

**Chunk 62** (`b6064e74b184`):

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

**Chunk 63** (`b95c26d52ee0`):

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

**Chunk 64** (`bc6e8d2fe577`):

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

**Chunk 65** (`c0c1858f03fe`):

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

**Chunk 66** (`c1c422470246`):

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

**Chunk 67** (`c53b199f9ade`):

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

**Chunk 68** (`c8f8dadd6203`):

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

**Chunk 69** (`c9e9523951b6`):

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

**Chunk 70** (`cefb93c1d699`):

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

**Chunk 71** (`cfadcb33d64b`):

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

**Chunk 72** (`d1e949b40c7a`):

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

**Chunk 73** (`d5fc086574e9`):

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

**Chunk 74** (`da1c0758b454`):

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

**Chunk 75** (`db250ced1e81`):

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

**Chunk 76** (`db54782984cc`):

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

**Chunk 77** (`db8b2bdf371a`):

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

**Chunk 78** (`dd5713402cfd`):

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

**Chunk 79** (`e05fc680a484`):

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

**Chunk 80** (`e087f7a0b70b`):

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

**Chunk 81** (`e17d1554782d`):

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

**Chunk 82** (`e53b2f1b3ca2`):

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

**Chunk 83** (`e5eb32b8480c`):

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

**Chunk 84** (`eab98ce0e1fc`):

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

**Chunk 85** (`f1bc1ad153ee`):

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

**Chunk 86** (`f45e1af7c8dc`):

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

**Chunk 87** (`f97fb5b16662`):

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

**Chunk 88** (`fe13616b260d`):

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

**Chunk 89** (`ffc525f7d497`):

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

## Concept: Dodge Dc

Chunk count: 1
Performs actions: ['act_0418']

### Chunk texts

**Chunk 1** (`84157ccb1121`):

```
CHAPTER 8: ACTION & ADVENTURE
CHAPTER 8: ACTION & ADVENTURE

CHAPTER 8: ACTION & ADVENTURE

Now the remaining smugglers get to go. They draw their guns and shoot at you!

The GM rolls attack checks against the heroes. Two smugglers shoot at Ultramarine and three shoot at Princess, but they both
have Impervious Toughness 8. Since the smugglers’ guns can’t hurt them, the GM does not bother rolling the attack checks. The
remaining two shoot at Rook, but one is impaired and the other blind, so they both miss by a mile.

Rook, you easily avoid the clumsy shots, especially from the guys dazzled by the flash bomb. Princess, Ultramarine, a
couple of stray shots ricochet off of you harmlessly.
ROUND 2

That brings us back to the top of the order. Princess?

Princess: I’m going to punch-out one of the smugglers! “Hey, watch the couture, boys!”

GM: Roll an unarmed attack check.

Princess: Rolls, gets a natural 20. A critical hit!

GM: Glances at Princess’ Strength of 12, and the +5 critical hit DC modifier, making the Toughness resistance DC (15 + 12 + 5)
or 32. No way the smuggler can succeed.

Wow! You send the guy flying right off the deck and into the drink! Sploosh!

Then, suddenly…

The GM rolls an attack check against Princess, getting a 15 result. Normally this would miss her Dodge defense of 18, but this is
a surprise attack, so Princess is vulnerable and her Dodge is halved to 4, rather than 8, making the DC a 14.

…a steel mesh net launches out of the doorway of the control cabin of the ship. Princess, give me a Dodge resistance
check.

Princess: Rolls a 5 for a total of 13. Um… 13?

GM: Compares it against the DC of 19. Two degrees of failure.

…the net wraps around you tightly, leaving you immobilized and defenseless, Princess.

From out of the control cabin lumbers a massive armored figure in red and silver, one arm ending in a lobster-like servo-
claw.

Ultramarine: Trawler!

GM: In Trawler’s voice. Who did you think was running this operation, heroes? Now back off!

Ultramarine: Is it my turn?

GM: No. It would be, but you delayed until after Rook, remember? Rook, it’s your turn, then Ultramarine and the smug-
glers.

Rook: I don’t think my weapons will do much against Trawler’s armor. Can I help Princess get free from the net?

GM: Your throwing talons might help cut through it.

Rook: Okay, I’ll do that.

GM: Since the net is immobile, do you want to roll or make a routine check?

Rook: If I roll, I get a damage bonus, right? The GM nods. Okay, I’l

[... truncated ...]
```

---

## Concept: Doing Good

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

**Chunk 2** (`079ee72c1633`):

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

**Chunk 3** (`1631a649fb6e`):

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

**Chunk 4** (`5e2f6b7f48fe`):

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

**Chunk 5** (`919d7063d0ae`):

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

**Chunk 6** (`a67593d532fb`):

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

---

## Concept: Doused In Chemicals

Chunk count: 1

### Chunk texts

**Chunk 1** (`6793b6d4a926`):

```
CHAPTER 6: POWERS

203

Descriptors help to bring a collection of effects and modifiers to life, differentiating them from similar (or even identical)
configurations and making them into distinct powers. Although descriptors don’t always have significant game effects
in MUTANTS & MASTERMINDS, they’re perhaps the most important element in providing color and character to the powers
of heroes and villains.

Descriptors do have some affect on game play. In particular, descriptors often govern how certain effects interact
with each other, serving as convenient shorthand to help define an effect’s parameters. For example, Immunity and
Nullify work against effects with specific descriptors; if they were limited solely to things like effect type, it would
leave out a tremendous range of options, like “Immunity to Fire” or “Nullify Mutant Powers,” which are important to
the source material.

Descriptors  come  in  many  different  forms.  The  break-
down in this section is inexact, and deliberately so; some
descriptors fall into more than one category, while others
might not fall into any of these categories, being unique
to  that  particular  character  or  power.  Still,  the  following
are the major types of descriptors suited to MUTANTS & MAS-
powers, and things to consider when creating or
choosing powers for a character.
ORIGIN

A descriptor may relate to the origin of a power, where it
comes  from  or  what  granted  it  to  the  character.  For  ex-
ample, did he gain Speed in a scientific accident or from
years of focused meditation at a secret temple to the God
of Speed? A power’s origin may determine how it interacts
with  other  powers.  Some  powers  with  the  same  origin
might be better suited to counter each other, for example,
or  to  work  in  conjunction,  combining  their  benefits.  Ex-
amples of origin descriptors include:

•

•

•

Accidental powers are the result of random chance
or  accident:  being  struck  by  lightning,  doused  in
chemicals, exposed to exotic radiation, and so forth.
The circumstances of an accidental origin may or may
not  be  something  others  can  duplicate  (although
some are sure to try).

Bestowed powers are granted by an outside agency
of some sort, such as a deity, a technology, an alien
race,  or  another  superhuman. The  process  that  be-
stows  the  powers  can  be  transitory  or  effectively
permanent, barring some sort of plot device or GM-
created setback.

Invented powers are designed and created b

[... truncated ...]
```

---

## Concept: Downtown

Chunk count: 0
Performs actions: ['act_0491']

### Chunk texts

---

## Concept: Drawback

Chunk count: 1

### Chunk texts

**Chunk 1** (`bfdbb051d926`):

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

---

## Concept: Dropping

Chunk count: 1
Performs actions: ['act_0432']

### Chunk texts

**Chunk 1** (`aa72b8f17fa7`):

```
CHAPTER 8: ACTION & ADVENTURE
CHAPTER 8: ACTION & ADVENTURE

CHAPTER 8: ACTION & ADVENTURE

any attack made on you until the start of your next turn.
Add  10  to  any  roll  of  10  or  less  that  you  make  on  these
checks, just as if you spent a hero point (thus ensuring a
minimum  roll  of  11). The  attacker  must  equal  or  exceed
your opposed check result in order to hit you.

DELAY

NO ACTION

When you delay, you choose to take your turn later in the
initiative order. You must delay your entire turn. You can-
not delay if you have already taken an action on your turn,
or if you are unable to take actions.

At any point after any other character in the conflict has
acted,  you  can  choose  to  take  your  turn.  Your  initiative
moves into the new place in the order where you act, and
you take your normal allocation of actions. If you do not
act before your initiative comes up in the next round, your
turn ends, you lose your delayed turn, and your initiative
remains where it is.

Beneficial effects lasting until the end of your turn end
when you choose to delay, but harmful effects that last
until  the  end  of  your  turn  last  until  after  you  act.  Like-
wise, you do not make resistance checks until after you
have taken your turn, so delaying can draw out some ef-
fects.

DISARM

You attempt to knock an item—such as a weapon or de-
vice—out of an opponent’s grasp. Make an attack check

against the defender with a –2 penalty. If you attempt to
disarm with a ranged attack, you are at –5 penalty. If your
attack succeeds, make an opposed check of your attack’s
damage  against  the  defender’s  Strength.  If  you  win,  the
defender dropped the held object. If you made the disarm
unarmed, you can grab the dropped object as a free ac-
tion. If you make a disarm attempt with a melee weapon
and lose the opposed check, the defender may immedi-
ately make an attempt to disarm you as a reaction; make
another opposed damage vs. Strength check. If this dis-
arm attempt fails, you do not, however, get an additional
attempt to disarm the defender.

Dropping a held item is a free action (although dropping
or  throwing  an  item  with  the  intention  of  hitting  some-
thing with it is a standard attack action).

Dropping  to  a  prone  position  is  a  free  action,  although
getting up requires a move action (see Stand).

ESCAPE

You attempt to escape from a successful grab (see Grab).
Make  a  check  of  your  Athletics  or  Acrobatics  against
the  rou

[... truncated ...]
```

---

## Concept: Duplication

Chunk count: 1
Receives actions: ['act_0198']

### Chunk texts

**Chunk 1** (`7f148070d8bb`):

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

---
