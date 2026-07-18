# Front recon: [W-occ] — is a projected-occupation functional constructible from corpus objects alone?

Date: 2026-07-07 (fifth session of the line; follows front-wmatter-recon.md).
Scope fixed by Jerome (7 Jul ruling, verbatim): ``The front therefore asks whether an occupation
functional for projected fermionic modes can be defined from corpus objects alone, before any
off-equilibrium closure [H-dyn] is adopted.''
Kill-switches fixed by Jerome (verbatim): ``The front stops if the occupation rule requires a thermal
ensemble, a Fock-space postulate, or a phenomenological number density not derived from
admissibility.
It also stops if TrajBr counting is used only as dictionary matching rather than as a forced
projected-occupation ledger.
The mass-amplitude problem is not reopened: the front may use the existence of the endomorphism
channel, but not attempt to fix its absolute scale.''
Minimal objective: decide whether [W-occ] is constructible, or dust stays gated until explicit
statistical import.
Status: working recon, untracked (working-notes rule), nothing deposited, no tex touched.
Sources read directly (bias-independent rule):
non-injective/projection-conditional-expectation-note/tex/ProjectionConditionalExpectation.tex
(abstract, thm:ceiling section, saturation-status passage),
quantum-structure/quantum-structure-note/tex/QuantumStructureNote.tex (abstract),
entanglement/e2-two-entropies (abstract), white-paper spin-statistics section
(2-dynamics/04/006-fermions-bosons-spin.tex), Q14 (carried over), TrajBr objects via 05b (carried
over).

## 0. Verdict up front

[W-occ] is NOT constructible from corpus objects alone today: CONDITIONAL NO-GO, and the front
stops cleanly on Jerome's own kill-switches — every candidate rule either presupposes a statistical
import or fails a forced-ledger test.
Dust stays gated.

But the no-go comes with a RECLASSIFICATION that improves the programme's dependency graph: the
required import is NOT an ad hoc thermal/Fock postulate to be invented.
It is an EXISTING NAMED FRONTIER of the corpus: the quantum-structure note lists ``extension to
arbitrary observables, MULTIPARTITE SYSTEMS, and continuous spectra'' as its PRIMARY OPEN
DELIVERABLE, and an occupation functional (what fills which modes, in what numbers) presupposes
exactly the multipartite extension.
[W-occ] is therefore not a cosmology object at all: it sits downstream of the quantum-structure
frontier, and the clean dependency chain is now
dust dynamics <- [W-occ] <- multipartite extension (quantum-structure primary open deliverable).
The gate points at an internal programme frontier, not at an external postulate — a strictly better
outcome than a bare no-go.

## 1. Kill-switch audit (Jerome's three, applied)

KS1 (no thermal ensemble / Fock postulate / phenomenological density): FIRES on every constructive
route found (sections 3.1-3.4) — each needs either a multi-mode state space (Fock-type: not in the
corpus, explicitly open) or an equilibrium filling rule (thermal-type: not in the corpus).
KS2 (TrajBr as forced ledger, not dictionary): the forced-ledger test was RUN and FAILED on scaling
grounds (section 3.2) — TrajBr counting is structurally EXCLUDED as a dust ledger, which protects
against any future dictionary temptation.
KS3 (mass amplitude untouched): respected — the endomorphism channel is used only as ``the
trace-bearing sector exists''; no scale fixed, no fermionic-matter wall approached.

## 2. Inventory: every corpus object with occupation flavour

1. ProjCE capacity ceiling (thm:ceiling, theorem-level): for a complex Gaussian mode supported on N
   distinguishable histories, the retained power fraction is at most (N-1)/N.
   The closest proto-occupation object in the corpus: per-mode, parameter-free, counting-indexed.
   CRITICAL LIMIT: it is an INEQUALITY (a ceiling), and ProjCE itself explicitly assigns the
   saturation reading (``data sit near the maximal power'') to CONSUMERS as interpretation — the
   corpus does not force ceiling = filling.
2. TrajBr distinguishable-history count N_dist(n) ~ (1+sqrt2)^n, i.e. a^{h_b} under [H-dict]
   (h_b ~= 0.881): the only growing corpus counter; per-rank, homogeneous, domain-free.
3. E1/E2 residual pair rank r_pair(n) = R_infty - R(n): the only DECREASING corpus counter —
   inventoried for completeness; it is a two-body entanglement rank on the conjugate Weil pair,
   saturating at finite q, not a number density (section 3.3).
4. White-paper spin-statistics: pi_1(C_eff) = Z_2 forces 4pi-periodicity, antisymmetry, and Pauli
   exclusion as a topological claim.
   Stratum: white-paper tier (structural, pre-refoundation; pi_2(C_eff) = 0 beyond the canonical
   model is a standing open item).
   NOTE THE GAP TYPE: this supplies STATISTICS (how identical excitations combine), not a STATE
   SPACE (what there is to fill) — exclusion without a multi-mode arena is not yet occupation.
5. Quantum-structure note (abstract, explicit): all results proved within the SU(2) sector;
   ``extension to arbitrary observables, multipartite systems, and continuous spectra remains the
   primary open deliverable.''
   The corpus DOCUMENTS ITS OWN GAP: no multipartite state space exists.
6. BI saturation (born-infeld-paper): fluxes saturate the structural bound c_chi — the corpus's one
   saturation principle; it is FLUX-level (dynamical bound), not capacity-level (mode counting).
7. Conservation structures: NONE for particle number — the corpus has gauge U(1)_Y (charge, not
   number), no global U(1), no Noether particle number, no baryon/lepton number.

## 3. Candidate constructions, each tested to destruction

### 3.1 Occupation by capacity saturation (ceiling -> filling)

Rule: every admissible mode fills to its ProjCE ceiling; occupation = allocated capacity.
Attractive because parameter-free and admissibility-derived.
FAILS twice.
First, forcing: converting the inequality into an equality needs a saturation principle at capacity
level; the only corpus saturation (BI) is flux-level, and the transplant is an analogy — ProjCE
itself labels the saturation reading as interpretation belonging to consumers.
Second, even granted saturation, the rule fills MODES with POWER, not space with PARTICLES: without
a multipartite arena there is no ``N particles in this comoving volume'', and without a kinetic
limit there is no p ~= 0 statement.
KS1 fires (the missing arena is exactly the Fock-type import).
Retained for the future: capacity ALLOCATION is the natural SHAPE of a post-multipartite occupation
functional (the ceiling would cap the filling); recorded as a direction, not a construction.

### 3.2 TrajBr counting as the occupation ledger (the forced-ledger test, KS2)

Rule: occupation of the homogeneous matter sector = N_dist(n).
TESTED AS FORCED, and it fails on exact scaling grounds — the cleanest negative of this recon.
Dust requires a conserved comoving number: rho_m ~ a^{-3} at fixed mass.
The ledger gives occupation ~ a^{h_b}, hence rho ~ a^{h_b - 3} = a^{-2.119}: NEITHER dust (-3) NOR
radiation (-4), and in the same excluded genre as the state-volume reading already killed by the
Cosmology 2.0 ledger (a^{0.881} != a^3).
Conclusion: TrajBr counting is structurally EXCLUDED as a matter-occupation ledger — its object is
histories of the homogeneous cascade, not particles in space.
This negative is BANKED: any future attempt to read N_dist as matter content dies here, which is
the anti-dictionary protection KS2 asked for.

### 3.3 Residual pair rank as occupation (the decreasing counter)

Rule: occupation = r_pair(n), the unresolved fibre rank.
Fails on object type and on trend shape: it is a two-body entanglement rank of the conjugate Weil
pair (not a spatial number density), it saturates at finite q (window-bound, not a power law in a),
and its consumption is rank-driven, not dilution-driven.
Inventoried because it is the ONLY decreasing corpus counter — worth knowing it exists and why it
is not the right object.

### 3.4 Single-mode evasion (does the homogeneous sector even need multipartite?)

Sharpest adversarial attempt: FRW only needs a mean density, so let occupation be the POWER of one
collective homogeneous mode, capped by the ceiling on N_dist(n).
Fails on the dilution law: nothing corpus-supplied makes the collective mode's power dilute as
a^{-3} — adiabatic dilution of occupation is precisely the missing kinetic limit, smuggled back in.
Also fails on the EoS: one mode's power carries no p ~= 0 statement without the dispersion/mass
normalisation (KS3 forbids fixing it).
The evasion reduces to the same two imports; recorded as tested and closed.

## 4. Why the no-go lands where it does (the two-gap structure)

The occupation problem decomposes into exactly two gaps, and the corpus closes neither:
GAP A (state space): WHAT is occupied — requires the multipartite extension (the quantum-structure
primary open deliverable).
Statistics (white-paper spin-statistics) is available but is the wrong ingredient: it constrains
how identical excitations combine ONCE a multi-excitation arena exists; it does not build the arena.
GAP B (conservation/dilution): WHY occupation is conserved comovingly — requires either a Noether
particle number (no global U(1) in the corpus) or a kinetic/hydrodynamic limit (not constructed).
Note that GAP B is what makes dust DUST (a^{-3}); GAP A is what makes occupation a NUMBER at all.
Any honest [W-occ] construction must close both; every shortcut tested in section 3 closes neither
and hides the import.

## 5. Grading (C1-C3 battery)

C1 (variable): the candidate variables exist (mode power, counting ledgers) but none is the right
object type — occupation is a number-per-volume, and the corpus has no volume-attached number.
FAILS at object-type level, which is more basic than the previous fronts' C1.
C2 (constraint): trivially FAILS — no candidate is simultaneously forced and correctly scaling.
C3 (principle): no corpus principle selects a filling rule; ProjCE explicitly delegates saturation
to consumers; BI saturation is flux-level.
The battery localises the failure at C1 (no arena), which is why the reclassification (section 0)
is the real content of this recon: the missing principle is upstream, in quantum-structure.

## 6. Adversarial pass (run before this note was written)

1. Is the a^{h_b - 3} exclusion (3.2) convention-proof?
   Yes: it uses only [H-dict] (n = log a, already carried by 05b) and fixed particle mass (dust
   definition); h_b - 3 = -2.119 is not -3 and not -4 for any convention scanned.
2. Could the ceiling become forced equality in some regime (e.g. the low-rank window where the
   low-ell data sit near it)?
   Empirical proximity is not structural forcing; ProjCE's own status sentence keeps saturation
   interpretive.
   No reopening.
3. Does the white-paper spin-statistics claim shortcut GAP A?
   No — statistics without an arena constrains nothing; also its stratum is white-paper tier, and
   this recon does not promote it.
4. Is GAP B really independent of GAP A?
   Yes: even with a Fock arena granted (thought experiment), comoving conservation still needs a
   number symmetry or a kinetic limit — two gaps, not one restated.
5. Anti-relapse audit: mass amplitude untouched (KS3); no thermal object invoked anywhere; H_infty
   gates, hierarchy wall, Koide arena, V3 note, instanton branch — all untouched.
6. Load-bearing objects (named): of the negative — the multipartite gap (GAP A, corpus-documented)
   and the conservation gap (GAP B); of the banked exclusion — the h_b - 3 scaling arithmetic.

## 7. Entropy polysemy (wagon item, standing instruction)

This front touches S_hist (as a candidate ledger, excluded) and the entanglement entropies of E1/E2
(as inventory); no identification made anywhere.
The disarm still rides with the first paper touching two of the three entropies.

## 8. Outcome ledger and follow-ups

Banked (internal):
1. The [W-occ] conditional no-go with its two-gap structure (state space + conservation), each gap
   named and corpus-located.
2. THE RECLASSIFICATION: [W-occ] belongs downstream of the quantum-structure primary open
   deliverable (multipartite extension) — dust dynamics <- [W-occ] <- multipartite.
   This is a dependency-graph fact the program paper can carry when the line is ever synthesised.
3. The TrajBr-ledger EXCLUSION (a^{h_b-3} = a^{-2.119}, neither dust nor radiation) — permanent
   anti-dictionary protection for the matter sector.
4. The single-mode evasion tested and closed (3.4); the capacity-allocation SHAPE recorded as the
   natural post-multipartite candidate (3.1, direction only).
Answer to the minimal objective: dust stays GATED until explicit statistical import — and the
import is now precisely located as an existing internal frontier (multipartite), not an external
postulate to invent.
Follow-up candidates (each on explicit go):
(a) the multipartite front itself (quantum-structure sub-programme) — the actual prerequisite; a
    heavy, genuinely new front that should be scoped from the quantum-structure side (Q1-Q3 tools),
    not from cosmology;
(b) Thermodynamics revision cycle (unchanged from the [W-matter] recon: reconciliation + polysemy
    disarm + radiation-silence reading — editorial, independent of this no-go);
(c) nothing else from this front.
Placement: none now (recon note only, per the scoped go).
The cosmological line (H_infty -> matter era -> [W-matter] -> [W-occ]) is now CLOSED at its
frontier: every remaining opening points outside cosmology proper (multipartite, Thermodynamics
editorial), which is itself the line's final structural result.

## 9. Discipline ledger

Labels: ProjCE ceiling PROVED (imported status, theorem-level); TrajBr exclusion PROVED given
[H-dict] (exact arithmetic); spin-statistics claim WHITE-PAPER TIER (not promoted); multipartite
gap CORPUS-DOCUMENTED (quantum-structure abstract, verbatim); the reclassification STRUCTURAL
(reading of documented gaps together); the no-go CONDITIONAL (on the corpus as it stands); mass
amplitude, value tiers, and all anti-relapse walls UNTOUCHED.
Load-bearing objects named in the main verdict (section 0), not only here.
Kill-switch audit run as section 1, per Jerome's framing; adversarial pass run BEFORE announcement
(section 6).
Nothing deposited; note stays untracked per the working-notes rule.
