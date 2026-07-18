# Front recon: [W-matter] — can W_Pi be species-resolved at the structural level?

Date: 2026-07-07 (fourth session of the line; follows front-matter-era-recon.md).
Scope fixed by Jerome (7 Jul ruling, verbatim): ``The matter-era reconstruction has shown that the
main obstruction is not the absence of a preferred history-entropy insertion, but the absence of a
projected matter functional able to distinguish conformal radiation from pressureless matter.
The task is therefore to test whether W_Pi can be made species-resolved at the structural level,
before any off-equilibrium closure [H-dyn] is adopted.''
Status: working recon, untracked (working-notes rule), nothing deposited, no tex touched.
Sources read directly (bias-independent rule): gauge-structure/q12/tex/q12.tex (abstract + Theorem 1
usage), gauge-gravity-stratification/q13/tex/q13.tex (abstract, lem:YM-stress, thm:EYM, proofs),
fermionic-matter/q14/tex/q14.tex (abstract, lem:projective-endomorphism, ssec:comparison-cc,
chiral-admissibility opening), spectral-gravity/thermodynamics/tex/Thermodynamics.tex (carried over
from the previous recon, full).

## 0. Verdict up front

The recon lands on a THREE-PART verdict, the sharpest of the line so far.

POSITIVE (structural, largely corpus-supplied): species resolution EXISTS in the corpus — but it does
not live in W_Pi.
It lives one level below, in the OPERATOR STRATIFICATION that Q12-Q14 have already built:
radiation = the connection-twist sector of the admissible operator (a_4 response, stress tensor
traceless in d=4, hence p = rho/3 structurally); massive matter = the endomorphism sector (E_Pi,
canonical, Q14), whose stress-tensor trace is carried by the mass bilinears.
Conformal vs massive = twist vs endomorphism = traceless vs trace-bearing response of the same
operator family.
The radiation era needs NO matter functional at all: the joint variational problem
delta_{g,A} S_Pi[g,A] = 0 already yields the coupled Einstein--Yang--Mills system with
8 pi G_N = c_YM/c_EH fixed spectrally (thm:EYM of Q13).

COHERENCE OBLIGATION (the Thermodynamics clarification this front was hoped to produce): the corpus
carries TWO bookkeeping conventions that any host paper must reconcile.
Thermodynamics treats matter as EXTERNAL (F = S_Pi[g] - beta_*^{-1} W_Pi, with S_Pi of the pure
Laplacian and W_Pi formal); Q12-Q14 treat matter as INTERNAL (gauge and fermionic sectors are
Seeley--DeWitt levels of the single functional S_Pi[g, A, D_Pi]).
The natural reconciliation, recorded as a structural reading to be verified in any construction
session: W_Pi is the IR effective sub-functional carried by the twist + endomorphism sectors of the
full spectral functional, and the equilibrium value beta_* = 1 is then not a normalisation choice
but the SINGLE-DETERMINANT VALUE — the relative weight of the geometric and matter responses is
fixed because both descend from one log det' (Q13 fixes 8 pi G_N = c_YM/c_EH with no multiplier).
This would upgrade the status of beta_*: the off-equilibrium hook beta_* != 1 becomes a departure
from the single-determinant identity — giving [H-dyn], if ever adopted, a structurally meaningful
driver instead of an arbitrary multiplier.

CONDITIONAL NO-GO (narrowed, honest): DUST IS A REGIME, NOT A SPECIES.
Pressureless matter is the non-relativistic occupation regime of the massive endomorphism sector,
and the corpus has NO occupation object: no number density, no statistical filling of the projected
fermionic modes, no kinetic or hydrodynamic limit.
Named load-bearing object of the negative: [W-occ] — the projected occupation construction.
Without it, p ~= 0 cannot be derived (though a^{-3} dilution follows from Bianchi once p ~= 0 holds),
and the radiation/matter transition TIMING stays out of reach even though its STRUCTURE is now clear
(crossover from twist-dominated to endomorphism-dominated response).
Independent secondary blockers: the fermion mass amplitude (deferred by Q14 to the cascade
normalisation — an existing open front, NOT reopened here) and the Lorentzian/FRW evaluation (K3',
carried over).

## 1. Kill-switches declared up front

K1'' (operator anchoring): if the species-resolving operator extension is a new choice, it is an
import.
Audit below: PASSES for radiation (the twisted operator A_{g,A} is corpus-anchored — admissible
principal fibre, G_Pi inherited from the admissibility programme, SU(3) sector unconditional);
CONDITIONAL for the fermionic sector (Q14's symbol-compatibility hypothesis is a named coherence
condition, carried as a label).
K2'' (regime/limit): if a target needs a statistical or non-relativistic limit that the corpus does
not define, the step is blocked, not constructed.
K3'' (EoS discriminator): the test of species resolution is the equation of state — the construction
must OUTPUT tracelessness for radiation and p ~= 0 for dust, not assume them.
K4''' (double counting): S_Pi[g] (Thermodynamics) and S_Pi[g,A,D] (Q12-Q14) overlap; any W-matter
construction that places gauge content in BOTH the entropy term and W_Pi double-counts.
This is the bookkeeping reconciliation obligation of section 0.

## 2. Inventory: what the corpus supplies, sector by sector

1. Radiation (gauge) sector — Q12/Q13, SUPPLIED AND CLOSED at the structural level:
   - Vertical variation of S_Pi[g,A] with A_{g,A} = -(nabla^A)^2 + E on the associated bundle of the
     admissible principal fibre; a_4 extraction gives the Yang--Mills term; delta_A S_Pi = 0 gives
     D_mu F^{a mu nu} = 0 (Q12 Theorem 1).
   - Metric variation gives the STANDARD Yang--Mills stress tensor (lem:YM-stress of Q13):
     T^YM_munu = -4 Tr(F_{mu rho} F_nu^rho) + g_munu Tr(F^2).
     Trace in d=4: g^munu T^YM_munu = -4 Tr(F^2) + 4 Tr(F^2) = 0 EXACTLY — the radiation EoS
     p = rho/3 is a structural output, not an input.
     K3'' PASSES on the radiation side.
   - Joint system: G_munu = 8 pi G_N T^YM_munu with 8 pi G_N = c_YM/c_EH fixed by the Seeley--DeWitt
     expansion alone (thm:EYM) — no multiplier, no import.
   - Strata: theorem-level within Q12/Q13's stated hypotheses (Euclidean, IR, corpus operator).
2. Massive (fermionic) sector — Q14, SUPPLIED AT OPERATOR LEVEL, OPEN AT VALUE LEVEL:
   - Projected Dirac operator D_{Pi,g,A} on the admissible spinor bundle (spinorial face of the Weil
     module); its square differs from the Lichnerowicz square by a CANONICAL zero-order endomorphism
     E_Pi (lem:projective-endomorphism) — ``internal fermionic structure is not input but output''
     (explicit anti-Connes--Chamseddine inversion, ssec:comparison-cc).
   - E_Pi = 0 iff the spinorial projection is injectively resolved: the endomorphism sector is the
     spinorial residue of non-injectivity itself — the mass channel is where non-injectivity bites.
   - Dirac trace identity (standard): the stress-tensor trace of the fermionic sector is carried by
     the mass bilinears (T^mu_mu ~ m <psi-bar psi> on-shell) — the trace channel IS the mass channel.
   - Mass amplitude: deferred by Q14 to the cascade normalisation (fermionic-matter sub-programme,
     x_1/Phi line) — open, walls respected.
   - Conditional layer: symbol-compatibility (named hypothesis of Q14).
3. Thermodynamics' W_Pi: formal placeholder with the standard variational identity — supplies the
   NORMALISATION convention (factor 2) and nothing species-resolved.
   Its own limitations paragraph concedes exactly the gap this front examines.
4. What does NOT exist anywhere in the corpus: an occupation/number-density object for projected
   matter (no Fock-type filling, no statistical state on the projected modes, no kinetic limit).
   This absence is the hard core of the front.

## 3. The three-level answer to the scoped question

### (a) Can W_Pi distinguish conformal radiation from pressureless matter?

W_Pi itself: NO — and it never will as currently defined, because it is a formal placeholder.
The corpus: YES, structurally — the distinction is already made at operator level, by WHERE the
sector enters the admissible operator: connection twist (traceless response, radiation) vs zero-order
endomorphism (trace-bearing response, massive matter).
The correct statement of species resolution is therefore not ``resolve W_Pi'' but ``replace W_Pi by
the twist + endomorphism sectors of the single spectral functional''.
This is a REFRAMING RESULT: the front's question dissolves into a sharper one, and the obstruction
identified by the matter-era recon (K2') is RESOLVED on the radiation side and NARROWED to [W-occ]
on the dust side.

### (b) The radiation era needs no matter functional

Direct corollary, worth stating because it feeds back into the matter-era front: the radiation-era
equilibrium problem is delta_{g,A} S_Pi[g,A] = 0, a closed corpus problem (thm:EYM), with no W_Pi,
no beta_*, no domain import.
Together with the radiation-silence by-product of the previous recon (R = 0 on-shell for the
traceless sector), the picture is coherent from both ends: the a_2 channel does not hear the
radiation sector (trace-blind), and the radiation sector does not need the matter side of the
equilibrium functional (spectrally induced).
Caveat sharpened from the previous note: within THIS corpus the trace anomaly is not an external
caveat — the anomaly IS the a_4 sector (the log-running of c_YM is the spectral trace of the
radiation sector).
The radiation-era silence is exact at the classical EoS level and receives the induced logarithmic
anomaly correction; small in the IR, labelled, not developed.

### (c) Dust: the residual gap, named precisely

Pressureless matter requires three ingredients; the corpus supplies one.
SUPPLIED: the trace-bearing sector (E_Pi + mass bilinears) — the right channel exists and is
canonical.
MISSING 1 — [W-occ], THE load-bearing object: an occupation construction for the projected
fermionic modes (what fills the states; what is the number density of the homogeneous sector).
Without it, ``non-relativistic'' has no referent: p ~= 0 is a statement about occupied momenta, not
about the operator.
MISSING 2 — the mass normalisation: the amplitude of the fermionic mass scale is an open item of the
fermionic-matter sub-programme (cascade normalisation); this front imports its status, does not
touch it.
Note the order: [W-occ] is prior — even with masses in hand, no occupation means no fluid.
Grade: conditional no-go on the dust construction until [W-occ] exists; the blocker is NEW (never
named in the corpus) and belongs to the quantum-structure/matter interface, not to cosmology proper.

## 4. The bookkeeping reconciliation (K4''' discharged into an obligation)

Thermodynamics splits F = S_Pi[g] - beta_*^{-1} W_Pi with independent sides (its rem:identity-nature
insists both sides are independently defined — this is what makes its first law non-tautological).
Q12-Q14 put everything inside one functional.
The reconciliation that suggests itself, recorded as a STRUCTURAL READING (to verify in any
construction session, not proved here):
1. W_Pi := the twist + endomorphism sub-functional of S_Pi[g, A, D_Pi], split by Seeley--DeWitt
   level; the sides remain independently computable (different heat-kernel orders), so the
   non-tautology of the first law survives the reconciliation.
2. beta_* = 1 is then the SINGLE-DETERMINANT VALUE: the relative weight of c_EH and c_YM (and of the
   fermionic level) is fixed inside one log det' — Q13 already states 8 pi G_N = c_YM/c_EH with no
   freedom.
   The Euclidean sign conventions of thm:EYM must be tracked before promoting this to a statement
   about the sign structure of F (adversarial item 2).
3. Consequence for [H-dyn] (NOT adopted, just sharpened): the off-equilibrium departure
   beta_* != 1 acquires a candidate meaning — a drift of the level coupling away from its
   determinant-fixed value — giving the matter-era front's load-bearing object a structural target
   instead of a free function.
This reconciliation is the concrete ``clarifies Thermodynamics and Cosmology without reopening
H_infty'' outcome: a Thermodynamics revision hosting it would also naturally host the entropy
polysemy disarm (wagon rule) and the radiation-silence reading.

## 5. Grading (C1-C3 battery)

C1 (variable): PASSES — species live in operator sectors (twist vs endomorphism), both
corpus-anchored (E_Pi canonical; gauge bundle from admissibility; symbol-compatibility as the named
conditional layer).
The right variables exist and are the corpus's own.
C2 (constraint): SPLITS — the radiation branch is parameter-free (induced couplings, no multiplier,
EoS an output); the dust branch fails pending [W-occ] + mass normalisation.
Sharper than the matter-era C2 (which failed globally): the failure is now localised to one named
missing construction.
C3 (principle): the reconciliation (W_Pi as level sub-functional) is SUGGESTED by the corpus's own
stratification principle (Q13's central message) but not forced; Thermodynamics' external-matter
convention remains internally consistent on its own terms.
The obligation is coherence between papers, not a forced identification — label accordingly.

## 6. Adversarial pass (run before this note was written)

1. Is T^YM tracelessness robust?
   Classical d=4 identity, exact (lem:YM-stress algebra checked directly).
   The quantum trace is the induced anomaly = the a_4 sector itself; within this corpus it is the
   log-running of c_YM — present by construction, logarithmic, IR-small; the radiation EoS statement
   is classical-exact and anomaly-corrected, stated with that label.
2. Sign conventions: thm:EYM works in Euclidean signature with a sign remark; before the
   single-determinant reading of beta_* = 1 is promoted anywhere, the relative signs of the
   geometric and matter responses in F must be tracked through the same conventions.
   Flagged as the first check of any construction session.
3. Does the reconciliation destroy Thermodynamics' first-law non-tautology (rem:identity-nature)?
   No — the split by heat-kernel order keeps the two sides independently computable; but the
   revision must restate the independence argument in the level language.
   Recorded as a revision obligation, not a contradiction.
4. Fermionic functional form: Q14 works with S_Pi[g, A, D_Pi] (spinorial spectral action) — the
   fermionic sector enters through the operator, not through a Grassmann path integral; the
   occupation gap ([W-occ]) is therefore not an artefact of missing formalism choice but a genuine
   missing object in EITHER convention.
5. Anti-relapse audit: nothing here touches the H_infty gates, the hierarchy wall, epsilon = 1/10,
   x_1(q), or the Koide arena; the mass amplitude is imported as ``open elsewhere'', full stop.
6. Load-bearing objects (named): of the positive — the operator stratification (twist vs
   endomorphism) with canonical E_Pi; of the reconciliation — the single-determinant structure; of
   the negative — [W-occ].

## 7. Entropy polysemy (wagon item, standing instruction)

This front touches S_Pi[g] and its extensions (S_hist uninvolved; ENI uninvolved).
No identification made; the reconciliation of section 4 is about FUNCTIONAL bookkeeping, not entropy
identification.
The disarm still rides with the first paper touching two of the three entropies — the Thermodynamics
revision suggested in section 4 remains the natural host.

## 8. Outcome ledger and follow-ups

Banked (internal):
1. REFRAMING RESULT: species resolution exists at operator level (twist = radiation, traceless,
   p = rho/3 output; endomorphism = massive, trace-bearing); W_Pi is a placeholder to be replaced,
   not resolved.
2. The radiation era is a CLOSED corpus problem (delta_{g,A} S_Pi = 0, thm:EYM): no matter
   functional, no multiplier, no domain — feeds back as a resolution of K2' (radiation side) of the
   matter-era front.
3. The bookkeeping reconciliation obligation + the single-determinant reading of beta_* = 1
   (structural reading, sign-check pending) — the concrete Thermodynamics clarification.
4. [W-occ] named as THE missing object for dust (prior even to the mass amplitude); conditional
   no-go on the dust construction until it exists.
Follow-up candidates (each on explicit go):
(a) [W-occ] recon: what could an occupation construction look like on corpus grounds (projected
    modes, admissibility filling, TrajBr counting as a candidate occupation ledger?) — genuinely
    new, interfaces with quantum-structure; scope carefully to avoid dictionary matching.
(b) Thermodynamics revision cycle: host the reconciliation + polysemy disarm + radiation-silence
    reading in one coordinated pass (editorial-heavy, produces coherence, no new theorem needed
    beyond the sign check).
(c) Nothing else from this front.
Placement: none now (recon note only, per the scoped go).

## 9. Discipline ledger

Labels: T^YM tracelessness PROVED (classical algebra; anomaly labelled); EYM system THEOREM-LEVEL
within Q12/Q13 hypotheses (imported status); E_Pi canonicity LEMMA-LEVEL conditional on
symbol-compatibility (imported status); species-resolution reframing STRUCTURAL (reading of proved
corpus objects together); single-determinant beta_* = 1 STRUCTURAL READING (sign check pending);
[W-occ] no-go CONDITIONAL (on the corpus as it stands); value tier and all anti-relapse walls
UNTOUCHED.
Load-bearing objects named in the main verdict (section 0), not only here.
Adversarial pass run BEFORE announcement (section 6).
Nothing deposited; note stays untracked per the working-notes rule.
