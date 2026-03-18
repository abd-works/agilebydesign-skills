# Hypothesis concept review – batch 26

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

## Concept: Metamorph

Chunk count: 1
Receives actions: ['act_0258']

### Chunk texts

**Chunk 1** (`c46c64c84f63`):

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

---

## Concept: Mimic

Chunk count: 1
Performs actions: ['act_0253']
Receives actions: ['act_0253']

### Chunk texts

**Chunk 1** (`9c7fcc5049c4`):

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

---

## Concept: Mind Control

Chunk count: 1
Receives actions: ['act_0251']

### Chunk texts

**Chunk 1** (`9c7fcc5049c4`):

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

---

## Concept: Mind Read

Chunk count: 1
Receives actions: ['act_0439']

### Chunk texts

**Chunk 1** (`3f5cd9a1056e`):

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

---

## Concept: Mind Reading

Chunk count: 11
Performs actions: ['act_0255']
Receives actions: ['act_0254']

### Chunk texts

**Chunk 1** (`19a54c3b3576`):

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

**Chunk 3** (`27cd3f53557a`):

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

**Chunk 4** (`5731b0e9cb2f`):

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

**Chunk 5** (`634190f2dd84`):

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

**Chunk 6** (`765269f2e7c2`):

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

**Chunk 8** (`a74c30c36b5b`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

appropriate type of check, a Difficulty Class, and make a
roll to see if the character succeeds or not! It’s that simple.

RANK

Every trait in MUTANTS & MASTERMINDS —abilities, skills, pow-
ers, and so forth—has an associated rank, a value telling
you how strong (or weak) that trait is. Ranks run from –5
(very  weak)  all  the  way  up  to  20  (incredibly  strong)  or
more. You can rate virtually any trait by its rank. With the
correspondence of rank and measure, you can rate virtu-
ally  anything—distance,  weight,  time,  and  so  forth—by
rank.

Every  task—from  making  an  attack  to  avoiding  harm  to
figuring out a gadget—has a Difficulty Class or DC, a value
that tells you how hard that task is to perform. DCs range
from  0  (automatic,  so  easy  it’s  not  worth  rolling)  to  40
(nearly impossible).
CHECKS

Actions in MUTANTS & MASTERMINDS are all resolved through
checks, a roll of a 20-sided die, plus a modifier. If the total
of the check equals or exceeds the Difficulty Class, the ac-
tion is a success. If it doesn’t, then it’s a failure.

Beneficial conditions apply a +2 bonus on the check (+5
for very highly beneficial), adverse conditions impose a –2
penalty (–5 for highly adverse). This is true whether you’re
trying to use a skill, make an attack, use a power, or what
have you.

Avoiding  an  effect  is  a  resistance  check,  with  a  Difficulty
Class of 10 + the effect’s modifier or rank. A successful re-
sistance means you avoid the effect, a failed check means
you suffer some (or all) of the effect.

THAT’S IT!

That’s the core of MUTANTS & MASTERMINDS: roll d20 + rank and
modifiers vs. a Difficulty Class. If you understand that, you
can do pretty much anything in the game. The rest is just
detail. When in doubt, or whenever you want to speed the
game along, just have a player make a check of the appro-
priate trait rank against a DC based on how difficult the
task is and you can’t really go wrong.

Part of the Gamemaster’s job is to make sure the game
is fair and balanced, so everyone can have a good time
and all the heroes have an equal chance of doing some

255

fun and exciting things in the course of the adventure. It
can be tricky sometimes, but MUTANTS & MASTERMINDS gives
you  tools  for  balancing  the  traits  of  the  heroes  against
different  challenges  and  handling  problems  that  may
come up.

While MUTANTS & MASTERMINDS presents a fairly complete and
balanced game 

[... truncated ...]
```

**Chunk 9** (`c1c422470246`):

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

**Chunk 10** (`c73e4c4738ad`):

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

**Chunk 11** (`c84a4002269b`):

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

---

## Concept: Minions

Chunk count: 1
Performs actions: ['act_0286']
Receives actions: ['act_0285']

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

## Concept: Modifiers

Chunk count: 1
Receives actions: ['act_0441']

### Chunk texts

**Chunk 1** (`a74c30c36b5b`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

appropriate type of check, a Difficulty Class, and make a
roll to see if the character succeeds or not! It’s that simple.

RANK

Every trait in MUTANTS & MASTERMINDS —abilities, skills, pow-
ers, and so forth—has an associated rank, a value telling
you how strong (or weak) that trait is. Ranks run from –5
(very  weak)  all  the  way  up  to  20  (incredibly  strong)  or
more. You can rate virtually any trait by its rank. With the
correspondence of rank and measure, you can rate virtu-
ally  anything—distance,  weight,  time,  and  so  forth—by
rank.

Every  task—from  making  an  attack  to  avoiding  harm  to
figuring out a gadget—has a Difficulty Class or DC, a value
that tells you how hard that task is to perform. DCs range
from  0  (automatic,  so  easy  it’s  not  worth  rolling)  to  40
(nearly impossible).
CHECKS

Actions in MUTANTS & MASTERMINDS are all resolved through
checks, a roll of a 20-sided die, plus a modifier. If the total
of the check equals or exceeds the Difficulty Class, the ac-
tion is a success. If it doesn’t, then it’s a failure.

Beneficial conditions apply a +2 bonus on the check (+5
for very highly beneficial), adverse conditions impose a –2
penalty (–5 for highly adverse). This is true whether you’re
trying to use a skill, make an attack, use a power, or what
have you.

Avoiding  an  effect  is  a  resistance  check,  with  a  Difficulty
Class of 10 + the effect’s modifier or rank. A successful re-
sistance means you avoid the effect, a failed check means
you suffer some (or all) of the effect.

THAT’S IT!

That’s the core of MUTANTS & MASTERMINDS: roll d20 + rank and
modifiers vs. a Difficulty Class. If you understand that, you
can do pretty much anything in the game. The rest is just
detail. When in doubt, or whenever you want to speed the
game along, just have a player make a check of the appro-
priate trait rank against a DC based on how difficult the
task is and you can’t really go wrong.

Part of the Gamemaster’s job is to make sure the game
is fair and balanced, so everyone can have a good time
and all the heroes have an equal chance of doing some

255

fun and exciting things in the course of the adventure. It
can be tricky sometimes, but MUTANTS & MASTERMINDS gives
you  tools  for  balancing  the  traits  of  the  heroes  against
different  challenges  and  handling  problems  that  may
come up.

While MUTANTS & MASTERMINDS presents a fairly complete and
balanced game 

[... truncated ...]
```

---

## Concept: Moon

Chunk count: 0
Performs actions: ['act_0453']

### Chunk texts

---

## Concept: Morph

Chunk count: 1
Receives actions: ['act_0259', 'act_0260']

### Chunk texts

**Chunk 1** (`c46c64c84f63`):

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

---

## Concept: Morph Attack

Chunk count: 1

### Chunk texts

**Chunk 1** (`c46c64c84f63`):

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

---

## Concept: Motivation

Chunk count: 28

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

**Chunk 4** (`1631a649fb6e`):

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

**Chunk 5** (`19a54c3b3576`):

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

**Chunk 9** (`5e2f6b7f48fe`):

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

**Chunk 11** (`7f0cf6f57819`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

GOALS

How would you describe your hero’s personality? While
heroes  tend  to  share  a  desire  to  use  their  powers  for
good and uphold the law, they also show a diverse range
of attitudes. One hero may be dedicated to the ideals of
truth,  justice,  and  equality  while  another  is  a  vigilante
willing to break the law in order to ensure justice is done.
Some heroes are forthright and cheerful while others are
grim and unrelenting. Consider your hero’s attitudes and
personality traits. Don’t overlook the effect of Motivation
on  your  hero’s  personality  and  vice  versa  (see  Motiva-
tion, previously).

Finally, what are your hero’s goals? All heroes want things
like peace and justice to one degree or another, but what
other  things  does  your  hero  want?  One  hero  may  want
to  find  his  long-lost  family  while  another  may  want  to
avenge a terrible wrong done to her in the past. A mon-
strous or alien hero may seek acceptance and a new home
on Earth, while a teen hero may want to live up to the leg-
acy of a mentor or predecessor. Giving your hero a goal
beyond simply “doing good” can help give the character
more  depth  and  provide  opportunities  for  roleplaying
and complications during the game. Don’t overlook it.

The Gamemaster awards heroes power points at the end of each MUTANTS & MASTERMINDS story. This represents the experi-
ence and confidence the heroes have gained, along with other factors contributing to an improvement in their abilities,
skills, and powers.

Generally, heroes each receive 1 power point for a successfully completed adventure that lasts for one game session.
If the heroes overcame especially powerful foes or difficult challenges, the GM can increase the power point award to
2 points. For adventures lasting more than one game session, the heroes should get 1 power point per session, plus a
possible power point at the end if they did particularly well.

Gamemasters may vary the rate of advancement by awarding more power points per adventure, allowing heroes to
increase in power faster, which may suit certain styles of play. The Gamemaster also may choose not to award a power
point for an adventure in which the heroes did especially poorly, such as failing to defeat a villain’s major scheme or al-
lowing many innocent people to suffer harm they could have prevented.

Players can spend their heroes’ awarded power points in-betwee

[... truncated ...]
```

**Chunk 12** (`818544ba2429`):

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

**Chunk 16** (`a67593d532fb`):

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

**Chunk 17** (`a8c6225b93ed`):

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

**Chunk 18** (`c8f2e2af058e`):

```
CHAPTER 2: SECRET ORIGINS

71

mankind, he or she may also become a hero for the
same reason.

•  Motivation—Recognition:  Some  Gadgeteers  want
their genius recognized not just by other  scientists,
but by millions of adoring fans.

•  Motivation—Responsibility:  The  Gadgeteer  often
feels it’s only right to use his or her incredible intel-
ligence to help others.

•  Motivation—Thrills:  Gadgeteers  love  to  push  the
limit and live on the edge of scientific research, so it
only makes sense that they might like dressing up in
tights and taking on the role of a hero.

•

•

Quirk—Psychological Problems: Perhaps the Gad-
geteer’s  devices  have  slowly  been  poisoning  his
or  her  mind,  or  biofeedback  caused  by  improperly
functioning cybernetics or other mechanical systems
have  caused  the  Gadgeteer  to  exhibit  some  sort  of
mental problem.

Relationship:  Gadgeteers  often  have  a  number  of
important  people  in  their  life,  either  family,  loved
ones, other researchers, or employees who like to get
into trouble.

The Martial Artist has honed his skills in unarmed combat
to  bridge  the  physical  gap  between  him  and  his  super-
powered  associates.  In  fact,  some  Martial  Artists  display
feats  that  seem  impossible  by  normal  standards—and
may have a mystical origin.
ABILITIES

Roll 1d20 once and record the result.

1-6

7-14

Finesse and Control: Your speed and reflexes
almost too fast to be human.

Mystic Endowment: You have unlocked your
body’s potential by cultivating your inner energy.

15-20

Strength and Power: You have trained your body
close to human perfection.

CONTROL

STRENGTH
3
STAMINA
3

AGILITY
7
DEXTERITY
5

FIGHTING
13
INTELLECT
0

AWARENESS
5
PRESENCE
0

ENDOWMENT

STRENGTH
3

AGILITY
5

FIGHTING
12

AWARENESS
6

STAMINA
3

DEXTERITY
5

INTELLECT
1

PRESENCE
1

POWER

AGILITY
6
DEXTERITY
4

STRENGTH
4
STAMINA
4

FIGHTING
12
INTELLECT
1

AWARENESS
4
PRESENCE
1

Agile Feint, Defensive Roll 4, Improved Initiative, Power Attack,
Takedown

Take the advantages listed above, then roll 1d20 once and
record the result.

1-6

Armed Fighter: You are an expert with exotic
weapons.

7-13 Wealthy: You are well connected and rich.

14-20

Well Traveled: You have walked the world righting
wrongs and challenging senseis.

FIGHTER

Equipment 2 (select one weapon), Improvised Weapon, Quick
Draw

WEALTHY

Benefit 3 (Millionaire), Connected

TRAVELED

Contacts, Languages 1 (Choose One), Tracking, Well-informed

If you rolle

[... truncated ...]
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

**Chunk 20** (`cefb93c1d699`):

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

**Chunk 21** (`cfadcb33d64b`):

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

**Chunk 22** (`d4cad3e10e05`):

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

**Chunk 23** (`db8b2bdf371a`):

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

**Chunk 25** (`e17d1554782d`):

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

**Chunk 26** (`e5eb32b8480c`):

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

**Chunk 28** (`f8e903dbf3d7`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

*If you rolled Vampire for Abilities, then you have Abilities
44, Powers 73, and Defenses 17; otherwise, you have Abili-
ties 62, Powers 52, and Defenses 20.

•  Motivation—Acceptance:  The  Supernatural  Crea-

ture is usually an outcast.

•  Motivation—Doing  Good:  Some  Supernatural
Creatures  attempt  to  go  against  the  grain  and  use
their powers for good.

•

•

•

Power Loss: Some Supernatural Creatures only have
their powers at night, or lose their powers when on
holy  ground  or  when  they  assume  human  form...  if
they have one.

Quirk—Angst:  The  Supernatural  Creature  often
feels great anguish over its lost humanity.

Reputation:  Most  humans  regard  Supernatural
Creatures with fear and hatred as a result of folklore
and myth.

•  Weakness:  Supernatural  Creatures  may  be  vulner-
able to holy weapons. Others may be unable to func-
tion in sunlight.

TOTEM

AVIAN

STRENGTH
4
STAMINA
6

AGILITY
8
DEXTERITY
4
CARNIVORAN

STRENGTH
7
STAMINA
6

AGILITY
5
DEXTERITY
2
PACHYDERM

STRENGTH
12
STAMINA
7
REPTILE

AGILITY
2
DEXTERITY
2

FIGHTING
8
INTELLECT
0

AWARENESS
4
PRESENCE
0

FIGHTING
10
INTELLECT
0

AWARENESS
3
PRESENCE
1

FIGHTING
5
INTELLECT
0

AWARENESS
3
PRESENCE
3

The Totem is a superhero whose powers are closely tied to
a particular animal. The Totem may have acquired its pow-
ers  through  an  accident  of  science,  an  invocation  of  the
animal spirits, or may even be an exceptional, self-aware
animal. Totem heroes tend to be as varied as the animals
they represent, and they can resemble other archetypes
such as the Martial Artist, Warrior, and Powerhouse.
ABILITIES

STRENGTH
10
STAMINA
8

AGILITY
4
DEXTERITY
3

FIGHTING
6
INTELLECT
1

AWARENESS
2
PRESENCE
0

Roll 1d20 once and record the result

Roll  on  both  the  Behavioral  Advantages  table  and  the
Social Advantages table.

1-4

Arthropod: Your totem is a spider, scorpion, wasp,
or even an insect swarm.

5-8

Avian: Your totem is a bird like a falcon or owl.

9-14

15-17

18-20

Carnivoran: Your totem is a carnivore from the
canine, lupine, or feline family.

Pachyderm: Your totem is a massive, thick-hided
mammal, such as an elephant or rhinoceros.

Reptile: Your totem is a reptile, such as a crocodile,
lizard, or snake.

ARTHROPOD

Roll 1d20 once and record the result.

1-4

5-8

9-12

Active: You are in constant motion.

Catch and Hold: You like to grab hold of your prey.

Mystic: Yo

[... truncated ...]
```

---

## Concept: Move

Chunk count: 27
Receives actions: ['act_0411']

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

**Chunk 2** (`0b30704b97a2`):

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

**Chunk 5** (`17270869c240`):

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

**Chunk 6** (`1af862ab5396`):

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

**Chunk 7** (`2b979f00a098`):

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

**Chunk 9** (`5b37523dc91b`):

```
CHAPTER 4: SKILLS

115

ledge, tumbling through obstacles, and so forth. The GM
sets the DC. Success means you accomplish the maneu-
ver,  while  failure  means  you  do  not,  and  two  or  more
degrees  of  failure  usually  means  you  slip  and  end  up
prone (and may suffer additional effects, depending on
the stunt). A successful acrobatic maneuver may provide
you a circumstance bonus on certain follow-up actions,
if the GM sees fit.

STANDING

You can make a DC 20 Acrobatics check to go from prone
to standing as a free action rather than a move action. A
failed check means you remain prone.

TUMBLING

You can make an Acrobatics check (DC 5) to lessen dam-
age from a fall, reducing the damage by 1 per degree. A
fall reduced to rank 0 damage does no damage and you
quickly roll to your feet as a free action. Otherwise, you are
prone at the end of a fall.

DC

5

15

20

30

TASK

Lessen damage from a fall (–1 per degree)

Acrobatic maneuver

Move from prone to
standing as a free action

Contort to fit through a tight space

ATHLETICS

Strength

Use Athletics for physical feats like climbing, jumping, rid-
ing animal mounts, and swimming.

CLIMBING

With a successful Athletics check, you can climb along a
slope,  wall,  or  other  steep  incline  at  your  ground  speed
rank minus 2 as a move action. A perfectly smooth, flat,
vertical surface can’t be climbed without the Wall-crawl-
ing effect of Movement (see the Powers chapter).

A failed Athletics check indicates you make no progress,
and  two  or  more  degrees  of  failure  means  you  fall  from
whatever  height  you  attained  (unless  you  are  secured
with a safety harness or other equipment). Make an Ath-

If  you  want  your  hero  to  jump  tens,  hundreds,  thou-
sands of feet, or even miles, look to the Leaping effect
in the Powers chapter.

letics check to catch yourself (DC equal to the initial check
+ 10). Someone else within arm’s reach can also make an
Athletics check to catch you with the same DC. If your at-
tempt to catch someone else gets more than one degree
of failure, you fall as well.

A ladder

A knotted rope

A rope

An uneven surface, like a rock-face

A rough surface, like a brick wall

An air duct, chimney, or other area
where you can brace against two
opposite walls

A corner where you can brace
against perpendicular walls

Climb of less than 10 feet total

Surface slightly slippery

Surface very slippery

+1 speed rank (up to your full speed)

Not vulnerable while climb

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

**Chunk 11** (`6b20869c8bc9`):

```
CHAPTER 8: ACTION &
ADVENTURE ................... 235
ROUNDS ........... 235
Initiative ..................................235
Action Types .........................235
Standard Action...................235
Move Action ..........................235
Free Action ............................236
Reaction .................................236
No Action ...............................236
Taking Your Turn ..................236
CHALLENGES .................. 237
Environmental Hazards ....237
CONFLICTS ...................... 240
Attacks ....................................240
Defenses .................................245
Actions ....................................246
Aid .........................................246
Aim ........................................246
Attack ...................................246
Charge .................................246
Command ...........................246
Crawl ....................................246
Defend .................................246
Delay ....................................247
Disarm .................................247
Drop an Item ......................247
Drop Prone ..........................247
Escape ..................................247
Grab ......................................248
Move .....................................248
Ready....................................248
Recover ................................248
Smash ..................................248
Stand ....................................248
Trip ........................................248
Maneuvers .............................248
Accurate Attack .................249
All-out Attack .....................249
Defensive Attack ................249
Demoralize .........................249
Feint ......................................249
Finishing Attack .................249
Power Attack ......................250

Slam Attack ........................250
Surprise Attack ...................251
Team Attack ........................251
Recovery ..............................251
GAME ..... 253
Assigning Difficulties .........253
```

**Chunk 12** (`74ebb15a5905`):

```
CHAPTER 5: ADVANTAGES

131

ADVANTAGE

Accurate Attack

All-out Attack

Chokehold

Close Attack

Defensive Attack

Defensive Roll

Evasion

Fast Grab

EFFECT

Trade effect DC for attack bonus.

Trade active defense for attack bonus.

Suffocate an opponent you have successfully grabbed.

+1 bonus to close attack checks per rank.

Trade attack bonus for active defense bonus.

+1 active defense bonus to Toughness per rank.

Circumstance bonus to avoid area effects.

Make a free grab check after an unarmed attack.

Favored Environment

Circumstance bonus to attack or defense in an environment.

Grabbing Finesse

Improved Aim

Improved Critical

Improved Defense

Improved Disarm

Improved Grab

Improved Hold

Improved Initiative

Improved Smash

Improved Trip

Substitute Dex for Str when making grab attacks.

Double circumstance bonuses for aiming.

+1 to critical threat range with an attack per rank.

+2 bonus to active defense when you take the defend action.

No penalty for the disarm action.

Make grab attacks with one arm. Not vulnerable while grabbing.

–5 circumstance penalty to escape from your holds.

+4 bonus to initiative checks per rank.

No penalty for the smash action.

No penalty for the trip action.

Improvised Weapon

Use Unarmed Combat skill with improvised weapons, +1 damage bonus.

Move-by Action

Power Attack

Precise Attack

Prone Fighting

Quick Draw

Ranged Attack

Redirect

Set-up

Takedown

Throwing Mastery

Uncanny Dodge

Weapon Bind

Weapon Break

Move both before and after your standard action.

Trade attack bonus for effect bonus.

Ignore attack check penalties for either cover or concealment.

No penalties for fighting while prone.

Draw a weapon as a free action.

+1 bonus to ranged attack checks per rank.

Use Deception to redirect a missed attack at another target.

Transfer the benefit of an interaction skill to an ally.

Free extra attack when you incapacitate a minion.

+1 damage bonus with thrown weapons per rank.

Not vulnerable when surprised or caught off-guard.

Free disarm attempt when you actively defend.

Free smash attack when you actively defend.

GENERAL

SKILL, RANKED (2)

You’re able to quickly size up an opponent’s combat capa-
bilities. Choose a target you can accurately perceive and
have the GM make a secret Insight check for you as a free
action, opposed by the target’s Deception check result.

If you win, the GM tells you the target’s attack and defense
bonuses  relative  to  yours  (lower,  higher,  or  eq

[... truncated ...]
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

**Chunk 15** (`9b4ab26032fa`):

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

**Chunk 16** (`b6064e74b184`):

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

**Chunk 17** (`b95c26d52ee0`):

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

**Chunk 18** (`c84a4002269b`):

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

**Chunk 20** (`d5fc086574e9`):

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

**Chunk 22** (`e53b2f1b3ca2`):

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

**Chunk 23** (`e6cd24549519`):

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

**Chunk 24** (`eab98ce0e1fc`):

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

**Chunk 25** (`f45e1af7c8dc`):

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

**Chunk 26** (`f8e903dbf3d7`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

*If you rolled Vampire for Abilities, then you have Abilities
44, Powers 73, and Defenses 17; otherwise, you have Abili-
ties 62, Powers 52, and Defenses 20.

•  Motivation—Acceptance:  The  Supernatural  Crea-

ture is usually an outcast.

•  Motivation—Doing  Good:  Some  Supernatural
Creatures  attempt  to  go  against  the  grain  and  use
their powers for good.

•

•

•

Power Loss: Some Supernatural Creatures only have
their powers at night, or lose their powers when on
holy  ground  or  when  they  assume  human  form...  if
they have one.

Quirk—Angst:  The  Supernatural  Creature  often
feels great anguish over its lost humanity.

Reputation:  Most  humans  regard  Supernatural
Creatures with fear and hatred as a result of folklore
and myth.

•  Weakness:  Supernatural  Creatures  may  be  vulner-
able to holy weapons. Others may be unable to func-
tion in sunlight.

TOTEM

AVIAN

STRENGTH
4
STAMINA
6

AGILITY
8
DEXTERITY
4
CARNIVORAN

STRENGTH
7
STAMINA
6

AGILITY
5
DEXTERITY
2
PACHYDERM

STRENGTH
12
STAMINA
7
REPTILE

AGILITY
2
DEXTERITY
2

FIGHTING
8
INTELLECT
0

AWARENESS
4
PRESENCE
0

FIGHTING
10
INTELLECT
0

AWARENESS
3
PRESENCE
1

FIGHTING
5
INTELLECT
0

AWARENESS
3
PRESENCE
3

The Totem is a superhero whose powers are closely tied to
a particular animal. The Totem may have acquired its pow-
ers  through  an  accident  of  science,  an  invocation  of  the
animal spirits, or may even be an exceptional, self-aware
animal. Totem heroes tend to be as varied as the animals
they represent, and they can resemble other archetypes
such as the Martial Artist, Warrior, and Powerhouse.
ABILITIES

STRENGTH
10
STAMINA
8

AGILITY
4
DEXTERITY
3

FIGHTING
6
INTELLECT
1

AWARENESS
2
PRESENCE
0

Roll 1d20 once and record the result

Roll  on  both  the  Behavioral  Advantages  table  and  the
Social Advantages table.

1-4

Arthropod: Your totem is a spider, scorpion, wasp,
or even an insect swarm.

5-8

Avian: Your totem is a bird like a falcon or owl.

9-14

15-17

18-20

Carnivoran: Your totem is a carnivore from the
canine, lupine, or feline family.

Pachyderm: Your totem is a massive, thick-hided
mammal, such as an elephant or rhinoceros.

Reptile: Your totem is a reptile, such as a crocodile,
lizard, or snake.

ARTHROPOD

Roll 1d20 once and record the result.

1-4

5-8

9-12

Active: You are in constant motion.

Catch and Hold: You like to grab hold of your prey.

Mystic: Yo

[... truncated ...]
```

**Chunk 27** (`fe13616b260d`):

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
