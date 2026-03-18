# Hypothesis concept review – batch 8

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

## Concept: Cost Per Rank

Chunk count: 11

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

**Chunk 3** (`138e63aeed36`):

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

**Chunk 4** (`25d04efd242a`):

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

**Chunk 5** (`7ade13289c0f`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

use of a tiring effect. In essence, the power requires extra
effort  in  order  to  use  it  (see  Extra  Effort,  page  19). This
makes Tiring a useful flaw for creating an effect you can
only use with extra effort.

Tiring is often applied to just some ranks of an effect to rep-
resent a higher level of the effect, usable only through extra
effort. For example, a hero might have a rank 12 Damage
effect, but routinely use only 8 ranks of it. The remaining
4 ranks are Tiring, so using them quickly fatigues the hero.

A Tiring effect can be combined with extra effort, but the
fatigue stacks, causing a minimum of two levels of fatigue
per use.

-1 COST PER RANK

You have no control over an effect with this flaw. Instead,
the Gamemaster decides when and how it works (essen-
tially  making  it  a  plot  device). This  flaw  is  best  suited  for
mysterious powers out of the characters’ direct control or
effects the GM feels more comfortable having under direct,
rather than player, control.

-1 COST PER RANK

An Unreliable effect doesn’t work all the time. Roll a die
each round before you use or maintain the effect. On a
10 or less, it doesn’t work this round, but you’ve still used
the action the effect requires. You can roll again on the
following  round  to  see  if  it  works,  although  you  must
take  the  normal  action  needed  to  activate  the  effect
again. Spending a hero point on your reliability roll al-

lows you to succeed automatically (since the roll is then
at least an 11).

Alternately,  instead  of  having  a  reliability  roll,  you  can
choose to have five uses where your effect works normal-
ly, then it stops working altogether until you can “recover”
it in some way (see the Fades flaw for more on this). The
GM may allow you to spend a hero point to automatically
recover a spent Unreliable power.

Powers  that  are  only  occasionally  unreliable  (less  than
about 50% of the time) are better handled as complica-
tions (see Complications, page 30).

One possible application of the Unreliable flaw is to re-
flect weapons or equipment that occasionally run out of
ammunition or “jam” or “crash” and must be reloaded or
reset in some way. It really only applies to effects where
this happens fairly often, as given in the Unreliable flaw
description. Large ammo or fuel capacities, which only
occasionally run out or inconvenience the character, are
better handled as descriptors and occasiona

[... truncated ...]
```

**Chunk 6** (`82504504b374`):

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

**Chunk 7** (`87f598748db8`):

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

**Chunk 8** (`9c685bbd4830`):

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

**Chunk 9** (`aa5babc5f423`):

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

**Chunk 10** (`bfdbb051d926`):

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

**Chunk 11** (`ffb72d59f44c`):

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

## Concept: Costume

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

## Concept: Cover

Chunk count: 2
Performs actions: ['act_0428']
Receives actions: ['act_0262']

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

**Chunk 2** (`db54782984cc`):

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

---

## Concept: Create

Chunk count: 17
Performs actions: ['act_0320']
Receives actions: ['act_0340']

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

**Chunk 2** (`138e63aeed36`):

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

**Chunk 4** (`179f10a90f72`):

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

**Chunk 5** (`27cd3f53557a`):

```
CHAPTER 6: POWERS ........ 143
POWERS ..... 143
Power Costs ...........................143
Power Descriptors...............143
TYPES ................. 144
WORK ..... 145
Effect Checks ........................145
Effect Parameters ................145
Countering Effects ..............147
EFFECTS ............ 149
Affliction .................................149
Burrowing ..............................151
Communication ...................151
Comprehend.........................152
Concealment ........................153
Create ......................................154
Damage ..................................156
Deflect .....................................157
Elongation .............................158
Enhanced Trait .....................158
Environment .........................159
Extra Limbs ............................160
Feature ....................................160
Flight ........................................161
Growth ....................................162
Healing ....................................162
Illusion .....................................163
Immortality ...........................164
Immunity ...............................165
Insubstantial .........................166
Leaping ...................................167
Luck Control ..........................167
Mind Reading .......................169
Morph......................................170
Move Object .........................171
Movement .............................172
Nullify ......................................173
Protection ..............................174

INTRODUCTION .....................5
```

**Chunk 6** (`2f722833852f`):

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

**Chunk 9** (`82504504b374`):

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

**Chunk 10** (`85cc7f979174`):

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

**Chunk 11** (`8757660124bd`):

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

**Chunk 12** (`c7946753c154`):

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

**Chunk 13** (`db8b2bdf371a`):

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

**Chunk 14** (`dd5713402cfd`):

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

**Chunk 15** (`e17d1554782d`):

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

**Chunk 16** (`e6cd24549519`):

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

**Chunk 17** (`fe13616b260d`):

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

## Concept: Crime Fighter

Chunk count: 5

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

**Chunk 2** (`a25964ce768c`):

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

**Chunk 3** (`d4cad3e10e05`):

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

**Chunk 4** (`e05fc680a484`):

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

**Chunk 5** (`ffc525f7d497`):

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

## Concept: Critical Hits

Chunk count: 9

### Chunk texts

**Chunk 1** (`0b30704b97a2`):

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

**Chunk 2** (`8757660124bd`):

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

**Chunk 3** (`997bf2eca013`):

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

**Chunk 4** (`9c9f9b5a490d`):

```
CHAPTER 1: THE BASICS
CHAPTER 1: THE BASICS

CHAPTER 1: THE BASICS

not even on your turn. Reactions don’t count against your
normal  allotment  of  actions  and  you  can  react  as  often
as the circumstances dictate, but only when they dictate.

Heroes  run  into  their  share  of  difficulties  in  their  work.
One way MUTANTS & MASTERMINDS measures this is with dif-
ferent  conditions.  They  are  shorthand  for  the  different
game modifiers imposed by things from power effects to
injuries or fatigue. So, for example, “vulnerable” is a condi-
tion where a hero’s active defenses are reduced. An oppo-
nent grabbing them or an entangling mass of glue might
make heroes vulnerable, or they might be made vulner-
able by a foe’s cunning combat maneuver or being caught
off-guard. The game effect is the same (the hero’s active
defenses  are  reduced),  so  it  is  easier  to  just  refer  to  the
overall condition as “vulnerable” and describe the differ-
ent situations that cause it.

This section describes the different conditions that can af-
fect characters in MUTANTS & MASTERMINDS. If multiple condi-
tions apply, use all of their effects. Some conditions super-
sede other, lesser, conditions, as given in their descriptions.

Each  basic  condition  describes  a  single  game  modifier.
They are the “building blocks” of conditions, much as ef-
fects  are  the  basic  building  blocks  of  powers.  Indeed,
many  power  effects  reference  these  basic  conditions  in

the descriptions of what they do. See the Powers chapter
for details.

•

•

•

•

•

Compelled: A compelled character is directed by an
outside force, but struggling against it; the character
is limited to free actions and a single standard action
per turn, with both types of action being chosen by
another, controlling character. As usual, this standard
action  can  be  traded  for  a  move  action.  Controlled
supersedes compelled.

Controlled:  A  controlled  character  has  no  free  will;
the character’s actions each turn are dictated by an-
other, controlling, character.

Dazed:  A  dazed  character  is  limited  to  free  actions
and a single standard action per turn, although the
character may use that action to perform a move, as
usual. Stunned supersedes dazed.

Debilitated: The character has one or more abilities
lowered below –5. (See Debilitated Abilities in the
Abilities chapter.)

Defenseless: A defenseless character has active de-
fense  bonuses  of  0.  Attackers  can  make  a

[... truncated ...]
```

**Chunk 5** (`a67593d532fb`):

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

**Chunk 6** (`b511fe78f53a`):

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

**Chunk 9** (`db8b2bdf371a`):

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

## Concept: Cryptic

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

## Concept: Cumulative Affliction

Chunk count: 9

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

**Chunk 4** (`6717e2899e27`):

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

**Chunk 5** (`685941d4ae65`):

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

**Chunk 6** (`85cc7f979174`):

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

**Chunk 7** (`c1c422470246`):

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

**Chunk 8** (`dd5713402cfd`):

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

**Chunk 9** (`ffc525f7d497`):

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

## Concept: Current Events

Chunk count: 4

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

**Chunk 3** (`60fdef9305c6`):

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

**Chunk 4** (`6805431193d6`):

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

---

## Concept: Cybernetic

Chunk count: 1

### Chunk texts

**Chunk 1** (`45ba36bcd3d5`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

265

More  than  a  few  comic  books  speculate  about  the  fu-
ture. There are science fiction comics aplenty, along with
super-hero stories set at different points in Earth’s future.

A near future setting may be quite similar to the modern-
day, with the addition of some new technology and the
new problems that come with it. For example there may
be flying cars, cybernetic and genetic modifications, and
advances  in  computer  technology  along  with  increases
in crime and urban decay. Heroes can stalk the streets of
dark, towering cities trying to protect the innocent where
a corrupt legal system has failed.

Some  future  comic  stories  are  set  following  a  terrible
catastrophe  that  has  all  but  destroyed  civilization.  In  a
setting  like  this  the  heroes  may  be  the  last  survivors  of
ordinary  humanity,  or  super-powered  mutants,  trained
super-soldiers (perhaps intended as weapons in the Last
War), or even cyborgs or aliens. Their adventures tend to
revolve around protecting pockets of civilization from ma-
rauding  mutants  and  keeping  ambitious  warlords  from
conquering the world or destroying innocent people.

Far future settings feature faster-than-light space travel, al-
lowing heroes to visit (or come from) any of dozens or even
hundreds  of  different  worlds.  A  team  made  up  of  heroes
from  these  different  worlds  could  band  together  to  pro-
tect the interstellar government from hostile alien invaders
while also dealing with disasters, space pirates, and crimi-
nal  cartels.  Or  a  group  can  explore  the  unknown  reaches
of space on board a starship, encountering would-be con-
querors, despots, raiders, and other villains along the way.

STYLE

Just as comics themselves span the stylistic gamut from
lighthearted  adventure  to  intricately  plotted,  grim  mo-
rality  plays,  so  can  a  MUTANTS  &  MASTERMINDS  series  vary  in
style. Once a style of play is established, it’s up to the GM
to  maintain  it.  That  means  creating  adventures  and  en-
counters suited to that style and encouraging the players
to get into the style’s mindset and run their characters ac-
cordingly. Styles run along a spectrum from light to dark:

LIGHT

The light style is simple and straightforward. The heroes
are the good guys and the villains are usually bad through
and  through  (with  a  few  misunderstood  souls  in  need
of help). Problem solving is a matter of eith

[... truncated ...]
```

---

## Concept: Damage

Chunk count: 96
Performs actions: ['act_0088', 'act_0167', 'act_0311', 'act_0314', 'act_0370']...
Receives actions: ['act_0102', 'act_0166', 'act_0167', 'act_0195', 'act_0224']...

### Chunk texts

**Chunk 1** (`042be12e9222`):

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

**Chunk 3** (`05327100448d`):

```
CHAPTER 7: GADGETS & GEAR

231

sentient magic item. They cannot undertake physical ac-
tions on their own, although they may be able to control
other  constructs.  They  cannot  move  or  exert  force,  and
automatically  fail  Strength  and  Agility  checks.  They  can
have Dexterity, used for manipulating remotes and such.

A construct can buy up one of its nonexistent ability ranks
by spending power points; +1 rank per 2 power points, as
usual, but starting at a rank of –5. This gives the construct
the normal use of that ability. Note a construct with Intel-
lect  but  no  Presence  is  intelligent  but  non-sentient  (not
self-aware) and a construct needs a rank in both Strength
and  Agility  to  be  able  to  move  and  act  physically.  Con-
structs cannot buy Stamina, since creatures with Stamina
are, by definition, not constructs.

Like inanimate objects, constructs have a Toughness rank,
which measures their ability to resist damage. A construct
starts out at Toughness 0 and can increase its rank using
the Protection effect. A mobile construct can even have
the Defensive Roll advantage.

SKILLS

Constructs can have skills just like characters at the same
cost.  However,  constructs  cannot  have  skills  based  on
abilities they lack.

Constructs can have advantages at the same cost as other
characters. Some advantages are less useful or even use-

less to constructs and, like skills, constructs cannot have
advantages requiring abilities they lack.
POWERS

Constructs can have various power effects, like other char-
acters. Some effects are less useful or even useless to con-
structs  and  the  GM  has  final  say  as  to  whether  or  not  a
particular effect can be assigned to a construct. Power ef-
fects are often aspects of a construct’s makeup or design,
such as built-in armor (Protection), weapons (Damage), or
sensors (Sense).

SIZE

Constructs larger or smaller than medium must pay pow-
er points for Innate and Permanent Growth or Shrinking.

A construct’s owner can give it orders verbally or through
any other means the construct understands. Command-
ing a construct is a move action. Constructs follow orders
to the best of their ability. Non-intelligent constructs do
exactly  as  they’re  told,  without  creativity  or  initiative,
while  intelligent  constructs  have  the  ability  to  interpret
and improvise. An owner can also give a construct a series
of basic orders for it to fulfill, such as “stay and guard this
place and attack anyon

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

**Chunk 6** (`19a54c3b3576`):

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

**Chunk 7** (`1a59d1dc4a9a`):

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

**Chunk 8** (`1b8011530852`):

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

**Chunk 9** (`1d915e6497ab`):

```
CHAPTER 6: POWERS

147

each  other  they  must  have  opposed  descriptors.  For  ex-
ample, light and darkness powers can counter each other
as can heat and cold, water and fire, and so forth. In some
cases,  such  as  magical  or  mental  effects,  powers  of  the
same descriptor can also counter each other. The GM is the
final arbiter as to whether or not an effect with a particular
descriptor can counter another. The Nullify effect (see page
173) can counter any effect of a particular descriptor!

her water powers. The GM agrees the two powers
should be able to counter each other, so he asks Si-
ren’s player to make a Water Control effect check,
while he makes a Fire Control effect check for White
Knight.  Siren’s  player  rolls  a  result  of  26  while  the
GM rolls a result of 19 for White Knight. Siren suc-
cessfully counters the flame blast, which fizzles out
in a gout of steam.

To counter an effect, you must take the ready action (see
page 248). In doing so, you wait to complete your action
until  your  opponent  tries  to  use  a  power.  You  may  still
move, since ready is a standard action.

You must be able to use the readied effect as a standard
action or less. Effects usable as a reaction do not require
a ready action; you can use them to counter at any time.
Effects  requiring  longer  than  a  standard  action  cannot
counter during action rounds (although they may be able
to counter ongoing effects, see the following section).

If an opponent attempts to use a power you are able to
counter,  use  your  countering  effect  as  your  readied  ac-
tion. You and the opposing character make effect checks
(d20 + rank). If you win, your two powers cancel each oth-
er out and there is no effect from either. If the opposing
character  wins,  your  attempt  to  counter  is  unsuccessful.
The opposing effect works normally.

Example: Siren, goddess of the seas, is fighting the
White  Knight.  The  hate-mongering  villain  hurls  a
blast of white-hot fire (a Ranged Damage effect).
Having prepared an action, Siren’s player says she
wants  to  counter  White  Knight’s  fire  blast  with

You can also use one power to counter the ongoing effect
of another, or other lingering results of an instant effect
(like flames ignited by a fiery Damage effect). This requires
a  normal  use  of  the  countering  effect  and  an  opposed
check, as above. If you are successful, you negate the ef-
fect (although the opposing character can attempt to re-
establish 

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

**Chunk 11** (`25d04efd242a`):

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

**Chunk 12** (`27cd3f53557a`):

```
CHAPTER 6: POWERS ........ 143
POWERS ..... 143
Power Costs ...........................143
Power Descriptors...............143
TYPES ................. 144
WORK ..... 145
Effect Checks ........................145
Effect Parameters ................145
Countering Effects ..............147
EFFECTS ............ 149
Affliction .................................149
Burrowing ..............................151
Communication ...................151
Comprehend.........................152
Concealment ........................153
Create ......................................154
Damage ..................................156
Deflect .....................................157
Elongation .............................158
Enhanced Trait .....................158
Environment .........................159
Extra Limbs ............................160
Feature ....................................160
Flight ........................................161
Growth ....................................162
Healing ....................................162
Illusion .....................................163
Immortality ...........................164
Immunity ...............................165
Insubstantial .........................166
Leaping ...................................167
Luck Control ..........................167
Mind Reading .......................169
Morph......................................170
Move Object .........................171
Movement .............................172
Nullify ......................................173
Protection ..............................174

INTRODUCTION .....................5
```

**Chunk 13** (`2c3d57c2a1b3`):

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

**Chunk 15** (`373c8323a9b6`):

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

**Chunk 16** (`3a7f34326ad9`):

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

**Chunk 17** (`3c75d5b04a0e`):

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

**Chunk 18** (`3df9e8cdc695`):

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

**Chunk 19** (`43d5c758bf78`):

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

**Chunk 20** (`44458c4fcb7e`):

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

**Chunk 21** (`473141849a66`):

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

**Chunk 22** (`489d1a2f08e9`):

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

**Chunk 24** (`60fdef9305c6`):

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

**Chunk 25** (`634190f2dd84`):

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

**Chunk 26** (`6717e2899e27`):

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

**Chunk 27** (`6802eda7b562`):

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

**Chunk 32** (`6e58428e1e90`):

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

**Chunk 33** (`72dc60c2e6cf`):

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

**Chunk 35** (`7663d2fb489a`):

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

**Chunk 36** (`7973bfe6a35b`):

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

**Chunk 37** (`7ade13289c0f`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

use of a tiring effect. In essence, the power requires extra
effort  in  order  to  use  it  (see  Extra  Effort,  page  19). This
makes Tiring a useful flaw for creating an effect you can
only use with extra effort.

Tiring is often applied to just some ranks of an effect to rep-
resent a higher level of the effect, usable only through extra
effort. For example, a hero might have a rank 12 Damage
effect, but routinely use only 8 ranks of it. The remaining
4 ranks are Tiring, so using them quickly fatigues the hero.

A Tiring effect can be combined with extra effort, but the
fatigue stacks, causing a minimum of two levels of fatigue
per use.

-1 COST PER RANK

You have no control over an effect with this flaw. Instead,
the Gamemaster decides when and how it works (essen-
tially  making  it  a  plot  device). This  flaw  is  best  suited  for
mysterious powers out of the characters’ direct control or
effects the GM feels more comfortable having under direct,
rather than player, control.

-1 COST PER RANK

An Unreliable effect doesn’t work all the time. Roll a die
each round before you use or maintain the effect. On a
10 or less, it doesn’t work this round, but you’ve still used
the action the effect requires. You can roll again on the
following  round  to  see  if  it  works,  although  you  must
take  the  normal  action  needed  to  activate  the  effect
again. Spending a hero point on your reliability roll al-

lows you to succeed automatically (since the roll is then
at least an 11).

Alternately,  instead  of  having  a  reliability  roll,  you  can
choose to have five uses where your effect works normal-
ly, then it stops working altogether until you can “recover”
it in some way (see the Fades flaw for more on this). The
GM may allow you to spend a hero point to automatically
recover a spent Unreliable power.

Powers  that  are  only  occasionally  unreliable  (less  than
about 50% of the time) are better handled as complica-
tions (see Complications, page 30).

One possible application of the Unreliable flaw is to re-
flect weapons or equipment that occasionally run out of
ammunition or “jam” or “crash” and must be reloaded or
reset in some way. It really only applies to effects where
this happens fairly often, as given in the Unreliable flaw
description. Large ammo or fuel capacities, which only
occasionally run out or inconvenience the character, are
better handled as descriptors and occasiona

[... truncated ...]
```

**Chunk 38** (`7b2254220623`):

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

**Chunk 39** (`7ed36e3d5075`):

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

**Chunk 40** (`7f148070d8bb`):

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

**Chunk 41** (`80099a87d308`):

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

**Chunk 42** (`800b98bbc634`):

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

**Chunk 43** (`803cb2a8c272`):

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

**Chunk 44** (`81d16734de2e`):

```
CHAPTER 7: GADGETS & GEAR

217

Ranged  weapons  include  both  thrown  and  projectile
weapons.  Thrown  weapons  are  Strength-based,  adding
the wielder’s Strength rank to their Damage rank. Projec-
tile weapons include bows, crossbows, and guns as well
as energy weapons like lasers and blasters. Their Damage
is generally not Strength-based.

Like melee weapons, ranged weapons have category, ef-
fect,  critical,  and  cost  traits.  Ranged  weapon  categories
are  Projectile  Weapons,  Energy  Weapons,  Heavy  Weap-
ons, and Thrown Weapons.

Holdout  pistol:  A  low-caliber,  easily  concealed  pistol,
typically used as a back-up or secondary weapon.

Light pistol: A common handgun, found in the hands of
police officers and criminals alike.

Heavy  pistol:  A  high-caliber  handgun,  usually  used  by
those who want a lot of stopping power.

Machine pistol: A small automatic weapon, usable in one
hand.

Submachine gun: Compact automatic weapons that fire
pistol  ammunition,  submachine  guns  are  common  mili-
tary weapons, also used by criminals with access to more
serious firepower.

Shotgun: A shotgun can fire shot, which does Damage 5
with Accurate 1 due to the spread, but Limited to Dam-
age 3 against targets with Protection. It can also load solid
slugs, which inflict the same damage, but without the Ac-
curate bonus or the Limit on Damage.

Assault rifle: Rifles designed for military-use capable of
both single-fire and automatic fire.

Sniper rifle: Rifles designed for long-range use, typically
in conjunction with a powerful scope or targeting system.

Bow: Although outdated, some heroes and villains favor the
bow as a weapon and it can be quite effective in the right
hands. A bow-wielding character may have various “trick” ar-
rows with different powers, typically handled as devices.

Crossbow: Similar to a bow, and used for the same reasons.

Blaster pistol: A pistol that fires a coherent bolt of energy.

Blaster rifle: A larger rifle-sized weapon that fires a more
powerful bolt of energy.

Taser: A compressed-air weapon firing a pair of darts. On
impact  they  release  a  powerful  electrical  charge,  for  an
Affliction effect that can daze, stun, or incapacitate (For-
titude resistance, DC 15).

Flamethrower: A flamethrower shoots a stream or arc of
fire Damage as Cone or Line Area and can switch between
settings as an Alternate Effect.

Grenade  launcher:  A  grenade  launcher  fires  various
types of grenades out a greater distance, gener

[... truncated ...]
```

**Chunk 45** (`821fc06edf41`):

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

**Chunk 46** (`83acf5380dc1`):

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

**Chunk 47** (`84157ccb1121`):

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

**Chunk 48** (`8558df91a0a1`):

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

**Chunk 49** (`85cc7f979174`):

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

**Chunk 50** (`8757660124bd`):

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

**Chunk 51** (`87f598748db8`):

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

**Chunk 52** (`8d5f5f31a27f`):

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

**Chunk 53** (`919d7063d0ae`):

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

**Chunk 54** (`93337a63364b`):

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

**Chunk 55** (`9575430bef02`):

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

**Chunk 56** (`997bf2eca013`):

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

**Chunk 57** (`9b4ab26032fa`):

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

**Chunk 58** (`9b8b75c1b5e7`):

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

**Chunk 59** (`a67593d532fb`):

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

**Chunk 60** (`a9a5f596da97`):

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

**Chunk 61** (`aa5babc5f423`):

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

**Chunk 62** (`aa943c38ef67`):

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

**Chunk 63** (`ab9b367b750f`):

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

**Chunk 64** (`ac75d3f2b9e6`):

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

**Chunk 65** (`b95c26d52ee0`):

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

**Chunk 66** (`ba29424008f5`):

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

**Chunk 67** (`bfdbb051d926`):

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

**Chunk 68** (`c0c1858f03fe`):

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

**Chunk 69** (`c1c422470246`):

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

**Chunk 70** (`c51168f2be2c`):

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

**Chunk 71** (`c53b199f9ade`):

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

**Chunk 72** (`c73e4c4738ad`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

•

•

Divine powers come from a higher being, essentially
a  god  or  gods.  Divine  power  is  generally  limited  to
the  god(s)  areas  of  influence  and  may  be  morally
aligned, available only to wielders with an allegiance
to that divinity.

Extradimensional  powers  originate  outside  the
home  dimension  of  the  setting,  from  other  planes
or dimensions of existence. Some extradimensional
powers  are  scientific  while  others  are  downright
mystical,  or  even  beyond  into  realms “man  was  not
meant to know.”

•

•

•  Magical powers draw upon magical energies, how-
ever they might be defined in the setting. Typically,
there  is  some  sort  of “magical  energy”  in  existence
that magicians and magical creatures draw upon for
their  powers  and  effects.  Note  that  powers  with  a
magical source are not necessarily “spells,” although
they might be; a dragon’s breath might use magic to
power it, or it might be biological, depending on the
descriptors applied to it (in other words, how it’s de-
fined in terms of the setting).

•  Moral  powers  come  from  an  abstract  morality  or
ideal,  essentially  from  an  allegiance  to  that  ideal.
Whether or not the moral power is aware and capa-
ble of interaction is up to the GM and the specifica-
tions of the setting; it’s the character’s belief in that
ideal that matters so far as the power is concerned.
“Good” and “evil” are common abstract moral sourc-
es of powers, but others may include chaos, law, an-
archy, order, justice, balance, neutrality, reason, and
so forth.

Psionic powers are powers of the mind, coming from
the psyche of the wielder (or perhaps from the Col-
lective  Unconscious,  which  acts  as  a “wellspring”  of
psionic power). This power source is associated with
classic “mental” powers like telepathy and telekinesis,
although effects like Mind Reading and Move Object
can also come from other sources.

Technological powers are the result of technology,
machines and technological devices. Although tech-
nological  power  sources  often  involve  Devices  or
Equipment, they don’t necessary have to; a techno-
logical  power  may  be  a  permanent  implant,  for  ex-
ample,  without  the  limitations  of  a  Device,  but  still
technological  (and  affected  by  things  keyed  to  the
technological descriptor).

MEDIUM

A power’s medium is what the power uses to accomplish its
effect(s). Often, a power’s source and me

[... truncated ...]
```

**Chunk 73** (`c8f8dadd6203`):

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

**Chunk 74** (`c9e9523951b6`):

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

**Chunk 75** (`cf5b8ba8408b`):

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

**Chunk 76** (`cfadcb33d64b`):

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

**Chunk 77** (`d329357e5091`):

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

**Chunk 78** (`d5fc086574e9`):

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

**Chunk 79** (`d7e831fa5f41`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

In many instances, players come up with creative uses for their characters’ descriptors. This should be encouraged and,
generally speaking, allowed freely so long as those uses don’t spoil the game. So if a fire-using character wants to use
a tiny amount of his flame blast power to light some candles, or the electrical-controlling character wants to use some
of his power output to act as a living battery to jump-start a car, go for it. In the latter case you might want to call for a
Technology skill check to make sure the character gets the terminals and the voltage right, but most of the time it’s bet-
ter to just let the trick go through and give the character a chance to shine.

Creative uses of descriptors with no real game effect are freebies: no extra effort or hero points needed. Situations
where creative uses of descriptors have a significant game effect can be handled as power stunts: pick the effect that
best suits the desired outcome and treat it as an Alternate Effect of the power the hero wants to use, with descrip-
tors assigned as appropriate. If an electrical-controlling hero wants to use his power like a living defibrillator to save
a heart-attack victim, for example, that can be a Healing power stunt. The hero uses extra effort (and possibly a hero
point) and gets a one-shot use of Healing to stabilize the dying victim.

While  descriptors  are  generally  applied  to  powers  when
those  powers  are  defined  (that  is,  when  a  character  is
created),  in  some  cases,  certain  descriptors  may  be  left
unspecified  and  defined  during  play.  This  can  either  be
because nobody thought to define the descriptor in ad-
vance, or it was deliberately left vague, to be filled-in later.

So, for example, a particular heroine might not know the
origin or source of her powers, and her player doesn’t want
to know, leaving them a mystery for later development in
the game. The GM agrees and so the heroine’s powers have
no  origin  or  source  descriptors.  Instead,  the  GM  chooses
them, which isn’t known until the heroine is subject to an
anti-magical field and discovers her powers don’t work! The
GM awards the player a hero point for the unexpected set-
back and now the source of the heroine’s powers is known,
although their origin still remains a mystery….

Applying descriptors in play gives you a lot of flexibility,
letting you handle certain things “on the fly” rather than
having 

[... truncated ...]
```

**Chunk 80** (`db250ced1e81`):

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

**Chunk 81** (`db54782984cc`):

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

**Chunk 82** (`db8b2bdf371a`):

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

**Chunk 83** (`dc5f9b168c4e`):

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

**Chunk 84** (`dcdc4c459ab6`):

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

**Chunk 85** (`dd5713402cfd`):

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

**Chunk 86** (`de33a93804de`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

Although some heroes and villains rely solely on their skills and advantages, most are set apart by their superhuman
powers. MUTANTS & MASTERMINDS characters can lift tanks, fly through the air, throw lightning from their hands, shoot lasers
from their eyes, or any number of other amazing things. This chapter describes these and many other powers and how
you can create your own.

Players spend power points on various powers for their heroes, like acquiring skills or other traits. A power is made up of
one or more effects, possibly with different modifiers, which increase or decrease the cost of the effects.

Effects can be used to create any number of different powers. A hero with the Concealment effect (see page 153) could use
it to create a power called Blending, Blur, Cloak, Invisibility, Shadowmeld, or anything else appropriate to the character you
wish to play. It’s all a matter of how powerful the effect is and what modifiers have been placed on it to increase or decrease
its performance. Another way to think of it is that this book is filled with effects, but your character sheet is filled with powers.

Power  effects  are  acquired  in  ranks,  like  ranks  for  other
traits. The more ranks an effect has, the greater its effect.
Each effect of a power has a standard cost per rank.

MODIFIERS

Modifiers  change  how  an  effect  works,  making  it  more
effective  (an  extra)  or  less  effective  (a  flaw).  Modifiers
have ranks, just like other traits. Extras increase a power’s
cost while flaws decrease it. Some modifiers increase an
effect’s cost per rank, others apply an unchanging cost to
the power’s total; these are called flat modifiers. For more
information see Modifiers, on page 187.

The  final  cost  of  a  power  is  determined  by  base  effect
costs,  modified  by  extras  and  flaws,  multiplied  by  the
power’s rank, with flat modifiers applied to the total cost.

Power Cost = ((base effect costs + extras -
flaws) x rank) + flat modifiers

The rules in this chapter explain what the various powers do,
that is, what their game effects are, but it is left up to the play-
er and Gamemaster to apply descriptors to define exactly
what a power is and what it looks (and sounds, and feels) like
to observers beyond just a collection of game effects.

A power’s descriptors are primarily for color. It’s more inter-
esting and clear to say a hero has a “Flame Blast” or “Light-
ning  Bolt”  power  than  a  gene

[... truncated ...]
```

**Chunk 87** (`e087f7a0b70b`):

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

**Chunk 88** (`e17d1554782d`):

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

**Chunk 89** (`e53b2f1b3ca2`):

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

**Chunk 90** (`e6cd24549519`):

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

**Chunk 91** (`eab98ce0e1fc`):

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

**Chunk 92** (`f1bc1ad153ee`):

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

**Chunk 93** (`f45e1af7c8dc`):

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

**Chunk 94** (`f97fb5b16662`):

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

**Chunk 95** (`fc4ed8309dc8`):

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

**Chunk 96** (`ffb72d59f44c`):

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

## Concept: Danger Sense

Chunk count: 8

### Chunk texts

**Chunk 1** (`301534069c2d`):

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

**Chunk 2** (`813c952ca178`):

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

**Chunk 3** (`872471930ea9`):

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

**Chunk 4** (`ab9b367b750f`):

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

**Chunk 5** (`ac75d3f2b9e6`):

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

**Chunk 6** (`b95c26d52ee0`):

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

**Chunk 7** (`bc6e8d2fe577`):

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

**Chunk 8** (`cefb93c1d699`):

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

---
