# Hypothesis concept review – batch 28

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

## Concept: Nullify

Chunk count: 1
Receives actions: ['act_0345']

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

## Concept: Objects

Chunk count: 7
Performs actions: ['act_0116', 'act_0199', 'act_0221', 'act_0261', 'act_0421']
Receives actions: ['act_0221', 'act_0305', 'act_0307']

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

**Chunk 2** (`44458c4fcb7e`):

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

**Chunk 3** (`72dc60c2e6cf`):

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

**Chunk 5** (`c46c64c84f63`):

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

**Chunk 6** (`d1e949b40c7a`):

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

**Chunk 7** (`fc4ed8309dc8`):

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

## Concept: Obscure

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

## Concept: Observation

Chunk count: 1

### Chunk texts

**Chunk 1** (`dcdc4c459ab6`):

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

## Concept: Offense

Chunk count: 8

### Chunk texts

**Chunk 1** (`1a59d1dc4a9a`):

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

**Chunk 2** (`60fdef9305c6`):

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

**Chunk 3** (`6805431193d6`):

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

**Chunk 4** (`919d7063d0ae`):

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

**Chunk 5** (`aa943c38ef67`):

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

**Chunk 6** (`c8f8dadd6203`):

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

**Chunk 7** (`dd5713402cfd`):

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

**Chunk 8** (`eab98ce0e1fc`):

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

## Concept: Overcome

Chunk count: 31

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

**Chunk 3** (`14dd371ce972`):

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

**Chunk 4** (`17270869c240`):

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

**Chunk 6** (`267bbd73af09`):

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

**Chunk 7** (`301534069c2d`):

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

**Chunk 8** (`3e277f7add29`):

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

**Chunk 9** (`43d5c758bf78`):

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

**Chunk 11** (`685941d4ae65`):

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

**Chunk 12** (`75f616f43b9d`):

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

**Chunk 13** (`80099a87d308`):

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

**Chunk 14** (`85cc7f979174`):

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

**Chunk 15** (`8757660124bd`):

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

**Chunk 16** (`8ad0833a1563`):

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

**Chunk 17** (`997bf2eca013`):

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

**Chunk 18** (`aa943c38ef67`):

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

**Chunk 19** (`ac75d3f2b9e6`):

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

**Chunk 20** (`b511fe78f53a`):

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

**Chunk 21** (`bc6e8d2fe577`):

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

**Chunk 22** (`c1c422470246`):

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

**Chunk 24** (`db8b2bdf371a`):

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

**Chunk 27** (`dd71074ce318`):

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

**Chunk 28** (`e087f7a0b70b`):

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

**Chunk 29** (`e17d1554782d`):

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

**Chunk 30** (`f47cb1a00aa5`):

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

**Chunk 31** (`ffc525f7d497`):

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

## Concept: Paladin

Chunk count: 1
Receives actions: ['act_0024']

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

## Concept: Paragon

Chunk count: 2

### Chunk texts

**Chunk 1** (`1631a649fb6e`):

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

**Chunk 2** (`a8c6225b93ed`):

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

---

## Concept: Parry

Chunk count: 65
Performs actions: ['act_0011']
Receives actions: ['act_0064', 'act_0172', 'act_0429']

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

**Chunk 2** (`042be12e9222`):

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

**Chunk 3** (`04f4880a6e63`):

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

**Chunk 9** (`238fc7bd4809`):

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

**Chunk 10** (`267bbd73af09`):

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

**Chunk 11** (`2b9b77a24290`):

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

**Chunk 12** (`301534069c2d`):

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

**Chunk 13** (`301ee8a15809`):

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

**Chunk 14** (`3c75d5b04a0e`):

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

**Chunk 15** (`442f2e5a5a37`):

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

**Chunk 16** (`481ffcf3c778`):

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

**Chunk 17** (`60fdef9305c6`):

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

**Chunk 18** (`634190f2dd84`):

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

**Chunk 19** (`6717e2899e27`):

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

**Chunk 20** (`6805431193d6`):

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

**Chunk 21** (`6be13e770e51`):

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

**Chunk 22** (`6c8715df5e97`):

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

**Chunk 23** (`6d18f5cb0ab3`):

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

**Chunk 24** (`714405399e02`):

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

**Chunk 25** (`75f616f43b9d`):

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

**Chunk 26** (`803cb2a8c272`):

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

**Chunk 27** (`8558df91a0a1`):

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

**Chunk 28** (`85cc7f979174`):

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

**Chunk 29** (`8757660124bd`):

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

**Chunk 30** (`8d5f5f31a27f`):

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

**Chunk 31** (`9136b6d87e68`):

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

**Chunk 32** (`919d7063d0ae`):

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

**Chunk 33** (`9575430bef02`):

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

**Chunk 34** (`997bf2eca013`):

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

**Chunk 35** (`9b4ab26032fa`):

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

**Chunk 36** (`9b8b75c1b5e7`):

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

**Chunk 37** (`a67593d532fb`):

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

**Chunk 38** (`a8c6225b93ed`):

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

**Chunk 39** (`a92e401b2501`):

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

**Chunk 40** (`a9a5f596da97`):

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

**Chunk 41** (`aa943c38ef67`):

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

**Chunk 42** (`ab9b367b750f`):

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

**Chunk 43** (`b511fe78f53a`):

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

**Chunk 44** (`b95c26d52ee0`):

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

**Chunk 45** (`bc6e8d2fe577`):

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

**Chunk 46** (`c0c1858f03fe`):

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

**Chunk 47** (`c53b199f9ade`):

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

**Chunk 48** (`c8f8dadd6203`):

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

**Chunk 49** (`c9e9523951b6`):

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

**Chunk 50** (`cefb93c1d699`):

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

**Chunk 51** (`cfadcb33d64b`):

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

**Chunk 52** (`d1e949b40c7a`):

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

**Chunk 53** (`d5fc086574e9`):

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

**Chunk 54** (`da1c0758b454`):

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

**Chunk 55** (`db54782984cc`):

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

**Chunk 56** (`db8b2bdf371a`):

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

**Chunk 57** (`dd5713402cfd`):

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

**Chunk 58** (`e05fc680a484`):

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

**Chunk 59** (`e087f7a0b70b`):

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

**Chunk 60** (`e17d1554782d`):

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

**Chunk 61** (`e53b2f1b3ca2`):

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

**Chunk 62** (`eab98ce0e1fc`):

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

**Chunk 63** (`f1bc1ad153ee`):

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

**Chunk 64** (`f97fb5b16662`):

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

**Chunk 65** (`ffc525f7d497`):

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

## Concept: Patenting

Chunk count: 0
Performs actions: ['act_0517']

### Chunk texts

---

## Concept: Penetrating

Chunk count: 27
Receives actions: ['act_0196', 'act_0330', 'act_0407']

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

**Chunk 2** (`1094aa03eba1`):

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

**Chunk 3** (`14dd371ce972`):

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

**Chunk 6** (`373c8323a9b6`):

```
CHAPTER 6: POWERS

149

Spread throughout this section are boxes like this one,
providing  examples  of  some  of  the  most  common
powers  found  amongst  superhero  characters  to  give
you a “menu” of pre-fabricated powers to choose from
when  creating  your  own  heroes  (and  villains)  in  MU-
MASTERMINDS.  Sample  powers  are  presented  on
the Power Effects table in italics.

Each power is presented in the following format:

NAME

Effect(s): Modifier(s) • Cost

Name: What the power is called. Feel free to mod-
ify the name to suit how you’re using the power.

Effects: The power’s effect or effects are listed by
name.

Modifiers:  Any  modifiers  applying  to  the  effect
are  listed  with  it.  If  a  power  has  multiple  effects,
each is listed with its applicable modifiers.

Cost: Lastly, the power’s cost is given. This is a cost
per rank of the power if it has a ranked effect, oth-
erwise it is a flat cost in power points. Some pow-
ers may have a flat cost for the initial power, plus a
cost per rank for additional ranks.

Effect: Varies, Activation • effects total –1 or 2 points

isting degrees on the target. For example, if you hit a target
and impose a vulnerable condition (one degree), then at-
tack again and get one degree on the effect, you impose
the Affliction’s second degree condition. +1 cost per rank.

Extra  Condition:  Your  Affliction  imposes  an  additional
condition per degree of success. So with one application of
this extra, your Affliction imposes two conditions—such as
dazed  and  hindered,  or  impaired  and  vulnerable—rather
than just one. With two applications, it imposes three con-
ditions,  and  so  forth.  Since  mutually  incompatible  condi-
tions  are  largely  wasted,  Afflictions  with  this  extra  often
have the Limited Degree flaw as well. +1 cost per rank.

Progressive: This modifier causes an Affliction to increase
incrementally  without  any  effort  from  you.  If  the  target
fails  a  resistance  check  to  end  the  Affliction,  it  not  only
persists, but increases in effect by one degree! So a target
affected by the first degree of a Progressive Affliction who
fails to resist progresses to the second degree of the effect
at the start of his next round. A successful resistance check
still ends the Affliction, as usual. +2 cost per rank.

FLAWS

Instant Recovery: Similar to the Reversible extra (see p.
196),  the  target  of  an  Affliction  effect  with  this  modifier
recovers  automatically,  no  c

[... truncated ...]
```

**Chunk 7** (`43d5c758bf78`):

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

**Chunk 8** (`442f2e5a5a37`):

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

**Chunk 9** (`661dd344a1d2`):

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

**Chunk 11** (`685941d4ae65`):

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

**Chunk 12** (`75f616f43b9d`):

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

**Chunk 13** (`7ed36e3d5075`):

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

**Chunk 14** (`7f148070d8bb`):

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

**Chunk 15** (`8757660124bd`):

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

**Chunk 16** (`997bf2eca013`):

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

**Chunk 17** (`aa5babc5f423`):

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

**Chunk 18** (`ab9b367b750f`):

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

**Chunk 19** (`afba8b4a5938`):

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

**Chunk 20** (`b95c26d52ee0`):

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

**Chunk 21** (`bc6e8d2fe577`):

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

**Chunk 22** (`c1c422470246`):

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

**Chunk 23** (`d329357e5091`):

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

**Chunk 24** (`d4cad3e10e05`):

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

**Chunk 25** (`db8b2bdf371a`):

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

**Chunk 26** (`dc5f9b168c4e`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

WEAPON

EFFECT

CRITICAL

COST

Holdout pistol

Light pistol

Heavy pistol

Machine pistol

Submachine gun

Shotgun

Assault Rifle

Sniper Rifle

Bow

Crossbow

Blaster pistol

Blaster rifle

Taser

Ranged Damage 2

Ranged Damage 3

Ranged Damage 4

Ranged Multiattack Damage 3

Ranged Multiattack Damage 4

Ranged Damage 5*

Ranged Multiattack Damage 5

Ranged Damage 5

Ranged Damage 3

Ranged Damage 3

Ranged Damage 5

Ranged Damage 8

Ranged Affliction 5*

Flamethrower

Cone or Line Area Damage 6

Grenade Launcher

Burst Area Ranged Damage 5

Rocket Launcher

Ranged Damage 10, Burst Area 7

Bolos

Boomerang

Javelin

Shuriken

Ranged Snare 3*

Ranged Damage 1

Ranged Damage 2

Ranged Multiattack Damage 1

* = See individual descriptions for more information.

20

20

20

20

20

20

20

19-20

20

19-20

20

20

20

—

—

20

20

20

20

20

4

6

8

9

12

10

15

11

6

7

10

16

10

13

15

27

6

2

4

3

also  Penetrating,  to  help  overcome  Impervious  armor
Protection,  although  the  rocket’s  Damage  typically  does
most of that work. Most rocket launchers can fire only one
or two shots before they must be reloaded (standard ac-
tion, meaning the launcher cannot fire that turn).

Bolos: A set of weighted cords intended to entangle an
opponent  with  a  Snare  Affliction  that  hinders  and  im-
pedes, then renders the target defenseless and immobile.
See Snare in the Powers chapter for details.

Boomerang: A common throwing weapon for heroes, a
thrown boomerang returns to the thrower’s hand, ready
to be thrown again on the next round (less a Feature and
more a special descriptor). Boomerang wielders often use
this  property  of  the  weapon  to  feint,  allowing  for  an  at-
tack against a vulnerable target on the return arc on the
attacker’s next turn.

Javelin: Light, flexible spears intended to be thrown. Jav-
elins can also be used in melee combat.

Shuriken: Flat metal stars or spikes for throwing. Shuriken
can be thrown in groups as a Multiattack. Although they
are  thrown  weapons,  shuriken  are  not  Strength-based,
being too light.

The following accessories can be added to the projectile
weapons in this section. Each is considered a feature cost-
ing 1 equipment point.

Laser Sight: A laser sight projects a non-damaging laser
beam showing where the weapon is aimed. This grants a
Accurate 1 to the weapon it’s attached, which grants a +2
bonus on attack c

[... truncated ...]
```

**Chunk 27** (`e087f7a0b70b`):

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

## Concept: Perception

Chunk count: 87
Performs actions: ['act_0137', 'act_0138', 'act_0139', 'act_0155', 'act_0398']...
Receives actions: ['act_0136', 'act_0241', 'act_0275', 'act_0277']

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

**Chunk 2** (`068f6ea2c39b`):

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

**Chunk 3** (`0b483461d2f8`):

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

**Chunk 9** (`1af862ab5396`):

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

**Chunk 10** (`1b8011530852`):

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

**Chunk 11** (`238fc7bd4809`):

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

**Chunk 12** (`267bbd73af09`):

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

**Chunk 13** (`2b9b77a24290`):

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

**Chunk 14** (`2ec68f50f56a`):

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

**Chunk 15** (`2f722833852f`):

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

**Chunk 18** (`3f5cd9a1056e`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

253

It’s that simple. Note that, practically speaking, a major cir-
cumstance modifier effectively shifts a check up or down
a  degree  of  difficulty,  as  shown  on  the  Difficulty  Class
Examples  table.  Likewise,  a  major  modifier  effectively
changes the degree of a graded check by one (see Grad-
ed Checks in Chapter 1).

Routine checks reflect that some tasks and situations are
so  trivial  it  is  not  worth  having  a  player  roll  a  check.  It
would be illogical for the character to have a real chance
of failing at the task, since failure should be rare enough
to constitute a complication in that situation. Examples in-
clude things like a competent driver handling a car under
ordinary conditions or a trained professional performing
the routine tasks of a job.

Routine checks save time, because you do not need to ask
players  for  a  check  for  every  single  thing  their  characters
do, but they also provide valuable guidelines for when you
should ask the players for a check while running the game.
They  set  a  threshold  for  the  Difficulty  of  certain  actions.
When coming up with Difficulty Classes for your adventure,
keep the routine check rule in mind. If the DC is low enough
that anyone can succeed as a routine check, then it may be
too low, or the action may not be worth assigning a check.

Take Perception, for example. If you decide it is a DC 10
Perception  check  to  pick  up  on  some  clue  or  bit  of  in-
formation in the adventure, that Difficulty is low enough
that anyone with an unimpaired (0 or higher) Awareness
can succeed at the task as a routine check. Assuming the
information is also important to the plot, you might be
better off to simply tell the players their characters no-
tice  it  without  calling  for  a  check.  If  there  needs  to  be
a  chance  of  failure,  then  set  a  higher  Difficulty  for  the
check. Of course, If the situation is stressful—such as the
midst of combat—then a routine check is not an option,
and  a  lower  DC  can  provide  heroes  with  a  reasonably
high chance of success with just a small chance of failure
for dramatic purposes.

“TELL ME HOW IT HAPPENS...”

Sometimes  it’s  a  good  idea  to  make  checks  secretly,  so
the players don’t necessarily know the result. This is usu-
ally  the  case  for  any  sort  of  check  where  the  characters
don’t  immediately  know  whether  they’ve  succeeded  or
failed. For example, Perce

[... truncated ...]
```

**Chunk 19** (`437f5039e60f`):

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

**Chunk 20** (`4e205a3c2745`):

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

**Chunk 21** (`5459e29a0535`):

```
CHAPTER 8: ACTION & ADVENTURE
CHAPTER 8: ACTION & ADVENTURE

CHAPTER 8: ACTION & ADVENTURE

though you can move (move action) and then attack (stan-
dard  action)  or  attack  and  then  move,  you  cannot  move
half  your  distance,  attack,  and  then  move  the  other  half
unless you have some special trait that allows you to do so.

At the end of your turn, you should:

•

End any effects that last “until the end of your turn”.

•  Make  any  necessary  resistance  checks  to  recover

You  can  use  extra  effort  in  order  to  take  an  additional
standard or move action on your turn (see Extra Effort on
page 19).

•

from ongoing effects.

Inform the Gamemaster and other players that your
turn is finished, allowing the next character in the ini-
tiative order to go.

In MUTANTS & MASTERMINDS game terms, a challenge is an action or series of actions where players are called upon to make
checks of their characters’ traits, but which do not involve direct conflict, such as fighting. Some challenges are quick
and involve only a single character, such as a hero making a daring leap or acrobatic maneuver, while others are more
involved and require the efforts of a whole team, such as clearing all of the people out of a burning building or search-
ing the entire city (or world!) for an escaped criminal.

The challenges given in this section are by no means the only possible ones. They simply cover the major “building
blocks” Gamemasters can use to create challenges in their own games and offer examples. Feel free to come up with
your own challenges to test the heroes’ abilities and give the players an opportunity to come up with clever plans of
their own.

Challenges may or may not involve initiative checks, de-
pending on the nature of the challenge.

If all of the characters get a turn and it does not particu-
larly matter who goes first, then the Gamemaster can dis-
pense with initiative for the challenge. For example, if the
heroes  all  have  to  leap  across  a  chasm,  then  it  is  a  chal-
lenge they must all complete, and it does not particularly
matter which of them goes first or last in doing so (since
their actions are all virtually simultaneous).

With other challenges, it does matter who goes first, par-
ticular when the challenge is timed in some fashion. So,
for example, if the GM determines that part of a burning
building will collapse after the first round, initiative may
be  checked  to  see  which  heroes  go  before  the  collapse
a

[... truncated ...]
```

**Chunk 22** (`5731b0e9cb2f`):

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

**Chunk 23** (`5ec359de437f`):

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

**Chunk 24** (`5f561d435c81`):

```
CHAPTER 4: SKILLS

125

DC

15

20

25

15 + rank

Ropes

Handcuffs

Straightjacket

Power Effect

Escaping from a grab is an Acrobatics or Athletics check.
See Grab in the Conflict section and Contorting, previ-
ously, for details.

Minor feats of sleight of hand, such as making a coin or
playing card “vanish,” have a DC of 10 unless an observer
is focused on noticing what you are doing. When you per-
form this skill under observation, your check is opposed
by  the  observer’s  Perception  check  to  see  if  they  notice
the trick.
STEALING

To covertly take something from another person make a
Sleight of Hand check (DC 20). Your target makes a Per-
ception check and notices the attempt if his check result
beats  yours,  whether  you  succeed  in  taking  the  object
or not.

You can also make a Sleight of Hand check to plant a small
object on someone, slip something into their pocket, drop
something into their drink, place a tiny radio tracer on them,
and so forth. To plant the object, you must get a check result
of  20  or  higher,  regardless  of  the  opponent’s  check  result.
The opponent notices the attempt if his check result beats
yours, whether you succeed in planting the item or not.

Example:  The  Rubber-Bandit  is  robbing  a  muse-
um of some of its valuables when a security guard
passes  by  while  making  his  rounds.  The  bouncing
Bandit has no fear of the rent-a-cop, so he decides
to have some fun. He has Skill Mastery for his Stealth
and,  unsurprisingly,  the  guard  doesn’t  notice  him
slither closer, but then the Rubber-Bandit decides to
try and steal the guard’s gun without being noticed.
Bandit has Sleight of Hand +12 and adds that to the
roll of a die. A whopping 19 plus 12 for a total of 31!
The guard, with a Perception skill of only +5, doesn’t
have a prayer of noticing his gun being eased out of
its holster, but the GM rolls anyway and gets a total
of 20. A good roll, but no enough.

STEALTH

Agility

You’re skilled in going unnoticed. While using Stealth, you
can  move  at  your  speed  rank  minus  1  with  no  penalty.
Faster than that, up to your full speed, you take a –5 cir-
cumstance penalty to your Stealth checks.

126

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

**Chunk 27** (`6717e2899e27`):

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

**Chunk 29** (`6c8715df5e97`):

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

**Chunk 30** (`706d511e685d`):

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

**Chunk 31** (`7419fe5693f8`):

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

**Chunk 32** (`7420eccba7af`):

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

**Chunk 33** (`765269f2e7c2`):

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

**Chunk 34** (`7a6d568a6006`):

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

**Chunk 35** (`803cb2a8c272`):

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

**Chunk 36** (`813c952ca178`):

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

**Chunk 37** (`818544ba2429`):

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

**Chunk 38** (`8558df91a0a1`):

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

**Chunk 39** (`86e82163c6b8`):

```
CHAPTER 4: SKILLS
CHAPTER 4: SKILLS

CHAPTER 4: SKILLS

HIDING

OPERATING

If you have cover or concealment, make a Stealth check,
opposed by an observer’s Perception check, to hide and
go unnoticed.

If  others  are  aware  of  your  presence,  you  can’t  use
Stealth  to  remain  undetected.  You  can  run  around  a
corner so you are out of sight and then use Stealth, but
others know which way you went. You can’t hide at all if
you have absolutely no cover or concealment, since that
means you are standing out in plain sight. Of course, if
someone isn’t looking directly at you (you’re sneaking up
from behind, for example), then you have concealment
relative to that person.

A  successful  Deception  or  Intimidation  check  can  give
you the momentary distraction needed to make a Stealth
check  while  people  are  aware  of  you. When  others  turn
their attention from you, make a Stealth check if you can
reach  cover  or  concealment  of  some  kind.  (As  a  general
guideline, any such cover has to be within 1 foot for every
rank you have in Stealth.) This check, however, is at a –5
penalty because you have to move quickly.
TAILING

You  can  use  Stealth  to  tail  someone  at  your  normal
speed.  This  assumes  you  have  some  cover  or  conceal-
ment (crowds of people, shadows, fog, etc.). If the subject
is worried about being followed, he can make a Percep-
tion  check  (opposed  by  your  Stealth  check)  every  time
he  changes  course  (goes  around  a  street  corner,  exits  a
building,  and  so  on).  If  he  is  unsuspecting,  he  only  gets
one Perception check for the scene. If the subject notices
you, make a Deception check, opposed by Insight. If you
succeed, you manage to pass off your presence as coinci-
dence and can continue tailing. A failed Deception check,
or being noticed a second time, means the subject knows
something is up and reacts accordingly.

Most  routine  operations  of  technological  equipment
don’t require a skill check and can be done untrained. Us-
ing an unfamiliar device does require a check, with the DC
determined by how foreign or unusual the device is, from
simple (DC 10) to highly advanced (DC 25 or more).
BUILDING

The difficulty and time required to make an item depends
on its complexity, as shown on the Building Items table. If
your Technology check succeeds, you have made the item
after the necessary time. If the check fails, you did not pro-
duce a usable end result, and any time and materials are
wast

[... truncated ...]
```

**Chunk 40** (`872471930ea9`):

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

**Chunk 41** (`885a404994e2`):

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

**Chunk 42** (`8ad0833a1563`):

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

**Chunk 43** (`8d5f5f31a27f`):

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

**Chunk 44** (`919d7063d0ae`):

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

**Chunk 45** (`94d3158e4b6b`):

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

**Chunk 46** (`952d6212a75a`):

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

**Chunk 47** (`9575430bef02`):

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

**Chunk 48** (`997bf2eca013`):

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

**Chunk 49** (`9a2865ac841b`):

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

**Chunk 50** (`9b4ab26032fa`):

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

**Chunk 51** (`9b8b75c1b5e7`):

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

**Chunk 52** (`9c7fcc5049c4`):

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

**Chunk 53** (`aa5babc5f423`):

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

**Chunk 54** (`aa943c38ef67`):

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

**Chunk 55** (`ab9b367b750f`):

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

**Chunk 56** (`ac75d3f2b9e6`):

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

**Chunk 57** (`afba8b4a5938`):

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

**Chunk 58** (`b2722c49426d`):

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

**Chunk 59** (`b511fe78f53a`):

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

**Chunk 60** (`b53c348dec5d`):

```
CHAPTER 6: POWERS

193

•

Indirect  4:  The  effect  can  originate  from  any  point
and aim in any direction, including towards you
(hitting a target in front of you from behind, for ex-
ample).

INNATE

FLAT • 1 POINT

An effect with this modifier is an innate part of your na-
ture  and  unaffected  by  Nullify  (see  the  Nullify  effect  in
this  chapter).  Gamemasters  should  exercise  caution  in
allowing  the  application  of  Innate;  the  effect  must  be  a
truly inborn or essential trait, such as an elephant’s size or
a ghost’s incorporeal nature. If the effect is not something
normal to the character’s species or type, it probably isn’t
innate.

INSIDIOUS

FLAT • 1 POINT

This  modifier  is  similar  to  the  Subtle  modifier  (later  in
this  section),  except  Insidious  makes  the  result  of  an
effect  harder  to  detect  rather  than  the  effect  itself.  For
example, a target suffering from Insidious Damage isn’t
even aware he’s been damaged. Someone affected by an
Insidious Weaken feels fine until some deficiency makes
it obvious that he’s weaker, and so forth. A target of an
Insidious effect may remain unaware of the danger until
it’s too late!

An  Insidious  effect  is  detectable  either  by  a  DC  20  skill
check  (usually  Perception,  although  skills  like  Expertise,
Insight, or Treatment may apply in other cases) or a par-
ticular unusual sense, such as an Insidious magical effect
noticeable by Detect Magic or Magical Awareness.

Note that Insidious does not make the effect itself harder
to notice; apply the Subtle modifier for that. So it is pos-
sible for an active Insidious effect to be noticeable: the tar-
get can perceive the use of the effect, but not its results:
the effect appears “harmless” or doesn’t seem to “do any-
thing” since the target cannot detect the results.

LINKED

FLAT • 0 POINTS

This modifier applies to two or more effects, linking them
together so they only work in conjunction as one.

The  Linked  effects  must  operate  at  the  same  range.
The  action  required  to  use  the  combined  effects  is  the
longest of its components and they use a single attack
check  (if  one  is  required)  and  resistance  check  (if  both
effects  use  the  same  type  of  check).  If  the  effects  have
different  resistances,  targets  check  against  each  effect
separately.  Different  Alternate  Effects  cannot be  Linked
since they can’t be used at the same time by definition.
Generally, the same effect c

[... truncated ...]
```

**Chunk 61** (`b95c26d52ee0`):

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

**Chunk 62** (`bb3e97c13b71`):

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

**Chunk 63** (`bfdbb051d926`):

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

**Chunk 64** (`c0c1858f03fe`):

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

**Chunk 65** (`c1c422470246`):

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

**Chunk 66** (`c46c64c84f63`):

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

**Chunk 68** (`c7946753c154`):

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

**Chunk 69** (`c87ce883452a`):

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

**Chunk 70** (`c8f8dadd6203`):

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

**Chunk 71** (`d29cce6a9b89`):

```
CHAPTER 4: SKILLS
CHAPTER 4: SKILLS

CHAPTER 4: SKILLS

DC

10

20

Ransack an area to find a certain object.

Notice a secret compartment, simple trap, or an
obscure clue.

25+

Find a well-hidden secret compartment or trap,
or an extremely obscure clue.

To determine how long it takes to search a given area, take
the total area measurement (in square feet, yards, or miles),
find  the  time  measurement  for  that  distance,  and  add  2.
So searching 60 square feet (roughly an 8 ft. by 8 ft. room)
takes the time rank of 60 feet (rank 1), plus 2, or 1 minute
(time rank 3). Searching a square mile takes the time rank of
1 mile (rank 8), plus 2, or two hours (time rank 10).

The DC for an Investigation check to find a concealed ob-
ject is usually opposed by the Stealth or Sleight of Hand
check of the character who hid it.

To collect a piece of evidence for analysis, make an Investi-
gation check (DC 15). If the check succeeds, the evidence
can be analyzed (see the following). If the check fails, an
analysis  can  be  done,  but  with  a  –5  penalty  for  highly
unfavorable  circumstances.  With  more  than  one  degree
of  failure,  the  evidence  is  ruined  and  no  analysis  can  be
done. On the other hand, two or more degrees of success
provide a +2 circumstance bonus to later analysis.

•

•

•

•

You  can  make  an  Investigation  check  to  apply  forensic
knowledge  to  evidence.  This  function  of  Investigation
does not give you clues where none exist. It simply allows
you to extract useful information from evidence and clues
you have found.

The base DC 15, modified by the time elapsed since the
evidence was left, and whether or not the scene was dis-
turbed. Success gives you information based on the clue
(and determined by the GM). Two or more degrees of fail-
ure may provide misleading or confusing evidence, also at
the GM’s discretion.

DC

15

15

TASK

Analyze Evidence

Gather Evidence

You  know  how  to  make  contacts,  collect  gossip  and  ru-
mors, question informants, and otherwise get information
from people.

By  succeeding  at  a  DC  10  Investigation  check  taking  at
least  an  hour,  you  get  a  feel  for  the  major  news  and  ru-
mors  in  an  area.  This  assumes  no  obvious  reasons  exist
why  information  would  be  withheld.  The  degree  of  the
check  result  determines  the  completeness  and  detail  of
the information. Information ranges from general to pro-
tected, and the DC increases accordingly for the

[... truncated ...]
```

**Chunk 72** (`d329357e5091`):

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

**Chunk 74** (`da014c928bec`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

change things to make the outcome more interesting or
more in line with how the game should go. In the above
example,  you  might  decide  the  villain  is  only  dazed  or
stunned  rather  than  being  knocked  out,  momentarily
giving the heroes the upper hand, but not ending the cli-
matic encounter prematurely.

Isn’t this cheating? Well, yes, in a manner of speaking it
is, but it’s “cheating” in order to make the game more in-
teresting and fun for everyone involved. So long as you
don’t alter the outcome of die rolls unfairly or malicious-
ly  and  you  do  it  to  help  ensure  the  game  is  fun,  inter-
esting, and challenging, you shouldn’t have a problem.
Besides,  the  complication  system  of  MUTANTS  &  MASTER-
provides you with the perfect excuse to “cheat” to
help out the heroes’ adversaries from time to time, and
to  compensate  the  players  in  the  process  by  awarding
them hero points, which they, in turn, can use to “cheat”
the fickle die from time to time and ensure their heroes
succeed.

IT

Sometimes you’ll run into a situation the game rules don’t
cover, or that you’re not sure how to handle. In these cases,
feel free to just fake it. Come up with a check you feel suits
the situation and go with it, so you can keep the game mov-
ing rather than getting bogged down in page flipping and
rules arguments. One of the great things about the MUTANTS
& MASTERMINDS system is pretty much everything can be re-
solved with a simple check. So when all else fails, just have a
player make a check with the most appropriate trait (ability,
skill, or power). If the check beats your estimation of the Dif-
ficulty Class, it’s a success. Otherwise, it’s a failure.

You also can fake it when dealing with certain trivial situ-
ations in the game. If there’s an important piece of infor-
mation you want the players to know, don’t bother seeing
if  they  succeed  at  a  Perception  check.  You  can  pretend
to  make  the  checks,  then  ignore  the  results  and  tell  the
players what their heroes find. Likewise,  if  a  power  level
10 hero is going to take out a PL 3 thug, you don’t have
to make all the rolls. Just ask the player to describe how
the hero defeats the hapless thug. It’s pretty much going
to  happen  anyway,  and  there’s  no  reason  why  the  hero
shouldn’t look cool doing it.

The essence of the MUTANTS & MASTERMINDS game system is
actually  quite  simple.  The  vast  majority  of  th

[... truncated ...]
```

**Chunk 75** (`da1c0758b454`):

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

**Chunk 76** (`daeb5804fb93`):

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

**Chunk 77** (`dcdc4c459ab6`):

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

**Chunk 79** (`dd71074ce318`):

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

**Chunk 80** (`e47577e0b729`):

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

**Chunk 81** (`e53b2f1b3ca2`):

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

**Chunk 82** (`e6cd24549519`):

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

**Chunk 83** (`eab98ce0e1fc`):

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

**Chunk 84** (`f41e7b13c82a`):

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

**Chunk 85** (`f97fb5b16662`):

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

**Chunk 86** (`fc4ed8309dc8`):

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

**Chunk 87** (`fd5ed2485118`):

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

---
