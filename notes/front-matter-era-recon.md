# Front recon: matter-era driven spectral equilibrium (W_Pi != 0, beta_* active)

Date: 2026-07-07 (third session of the H_infty line; follows front-hinfty-recon.md and
front-hinfty-construction.md).
Scope fixed by Jerome (7 Jul ruling): scoped recon only — test whether the radiation/matter transition,
the reading of a(t), and the status of the effective density can be formulated WITHOUT re-importing a
hidden domain; exploit the [H-ent-id-ext] gate, do not circumvent it; strictly structural (the value
tier and the anti-relapse walls are not reopened).
Status: working recon, untracked (working-notes rule), nothing deposited, no tex touched.
Sources read directly (bias-independent rule): spectral-gravity/thermodynamics/tex/Thermodynamics.tex
(full), cosmology-paper/tex/05b-history-branching (full), notes/front-hinfty-recon.md,
notes/front-hinfty-construction.md, cosmology-paper effective-model and voids sections (anchoring).

## 0. Verdict up front

CONSTRUCTION TIER: CONDITIONAL NO-GO under the corpus as it stands.
None of the three targets (radiation/matter transition dynamics, derivation of a(t), a quantitative
law for the effective density) can be formulated without imports, and the blockers are THREE and
independent: (K1') the corpus supplies an equilibrium principle but NO off-equilibrium dynamical
closure — the matter era is off-equilibrium by definition, so any evolution law for the departure is
an import, named [H-dyn]; (K2') W_Pi is formal — no species-resolved matter functional exists, so
radiation vs dust cannot even be distinguished on the spectral side at functional level; (K4')
the domain degeneracy that the S^4 instanton masked SPLITS in any evolving era — the candidate
readings of the history-entropy insertion diverge qualitatively (even in the sign of their trend),
so the inner domain import of [H-ent-id-ext] becomes a time-dependent structural choice, exactly the
hidden re-import the scope was designed to detect.

STRUCTURAL TIER: TWO CLEAN DOMAIN-FREE OBJECTS SURVIVE, one of them new.
(i) The status of the effective density has a sharp answer: within the driven reading, the
matter-era departure from equilibrium is a COUPLING RENORMALISATION (G_eff = 8 pi G beta_*^{-1} on
the matter sector), not a fluid — consistent with, and sharpening, the anti-fluid stance of 05b.
A CONSTANT departure is unobservable (absorbed in the calibration of G_N); the observable content of
the driven reading in the matter era is carried ENTIRELY by the evolution beta_*(n), which is exactly
what [H-dyn] would have to supply.
Same shape as the TrajBr no-go: observable content confined until a closure is adopted.
(ii) NEW BANKED BY-PRODUCT (exact on-shell, domain-free, no import): the covariant channel of the
local multiplier field is BLIND TO RADIATION and switches on at matter domination.
On-shell R = 8 pi G (rho - 3p): the radiation era (p = rho/3) has R = 0 exactly, so
beta(x)^{-1} = beta_0^{-1} - R/6 sits at its flat-space value through the entire radiation era; the
first covariant departure appears exactly when non-conformal matter dominates (R = 8 pi G rho_m > 0).
The radiation era is the SPECTRALLY SILENT era of the a_2 channel; the radiation/matter transition is
marked, not derived, by the corpus objects — formulated with no domain, no new hypothesis.

## 1. Kill-switches declared up front

K1' (dynamical closure): if any target requires a law for the APPROACH to equilibrium (gradient flow,
maximum entropy production, per-tick constrained stationarity...), that law is not in the corpus:
def:equilibrium is stationarity only, and subsec:beta-star-status offers beta_* != 1 as a static
reading, explicitly ``offered, undeveloped''.
Promoting the constant multiplier beta_* to a time-dependent beta_*(n) belongs to the same import.
Any such closure is named [H-dyn] and graded as an import.
K2' (matter functional): Thermodynamics states its own limitation — T^(Pi) is defined formally from
W_Pi, with no explicit construction per species.
If a target needs dust vs radiation resolved on the spectral side, it is blocked until [W-matter] is
constructed.
K3' (signature/foliation): Euclidean-only + static-slice E_Pi.
The S^4 case evaded this by exact homogeneity; a decelerating FRW era has no such evasion (the
Euclidean section is tau-dependent, the slice is not static).
S_Pi^(L) exists at definition level (lorentz-paper) but has no FRW evaluation.
K4' (domain, sharpened from the H_infty front): on the instanton all intensive readings agreed
(2 pi h_b) and the extensive reading reduced to one number (V_c); if the candidate readings diverge
along an evolving era, the domain choice re-enters as a time-dependent import.

## 2. Inventory: what the corpus supplies for the matter era

1. F = S_Pi - beta_*^{-1} W_Pi with delta F = 0 => Einstein up to a cosmological term
   (thm:einstein); beta_* a CONSTANT Lagrange multiplier.
   Stratum: structural (IR, Euclidean).
2. Off-equilibrium hook: constant beta_*^{-1} != 1 gives G = 8 pi G beta_*^{-1} T
   (subsec:beta-star-status).
   Stratum: offered reading, undeveloped — this is the hook the matter era activates, since W_Pi != 0
   makes the multiplier bite.
3. Local field beta(x)^{-1} = beta_0^{-1} - R(x)/6 + O(t_*), with only the -R/6 part covariant
   (def:beta, rem:tstar).
   Stratum: proved (Seeley--DeWitt) for the expansion.
4. Production rate dS_hist/dt = h_b H, per rank, homogeneous, corpus-pinned (TrajBr via 05b);
   H-dict: dn = H dt = d log a.
   Stratum: structural, conditional on [H-dict].
   CRITICAL for K4': this object is domain-free as stated (a per-rank rate of the homogeneous
   cascade, not a density).
5. The [H-ent-id-ext] gate (front-hinfty-construction.md): intensive insertions excluded ON THE
   INSTANTON by the intensive-invariance Lemma; extensive insertion requires the V_c import.
   Scope note: the Lemma's premise is ``the only available time scale is 1/H''.
   With matter present and Einstein NOT yet imposed (off-shell, as a variational analysis must be),
   rho supplies an independent second scale, so the Lemma does NOT transfer to the matter era.
   This reopens NOTHING on the instanton (the asymptotic gate stands, anti-relapse); it only means
   the matter era needs its own analysis — which then hits K1'-K4' below.
6. Cosmology 2.0 ledger (standing): the state-volume reading of N_dist is dead quantitatively
   (a^0.881 != a^3); the phenomenological sector carries no dark-energy fluid.

## 3. The three targets, graded

### (a) Radiation/matter transition

Dynamical formulation: BLOCKED by K2' — nothing in the corpus distinguishes radiation from dust at
the level of W_Pi, so no spectral-equilibrium statement can track which component dominates.
Grade: missing construction ([W-matter]), not a no-go.

Structural formulation: AVAILABLE, domain-free, and apparently unnoticed until now.
On-shell trace of the Einstein response: R = 8 pi G (rho - 3p).
Radiation era: p = rho/3 => R = 0 exactly => the covariant part of beta(x)^{-1} vanishes — the local
multiplier field sits at beta_0^{-1} (its scheme part) through the whole era.
Matter era: p = 0 => R = 8 pi G rho_m > 0 => beta(x)^{-1} = beta_0^{-1} - (4 pi G/3) rho_m ... i.e.
the a_2 channel switches on at the transition and its covariant departure tracks rho_m ~ a^{-3}.
(With a cosmological term, R also carries 4 Lambda — a constant floor, distinct in scaling.)
The transition is therefore MARKED spectrally (the a_2 channel turns on), though not DERIVED (its
timing needs the densities, i.e. [W-matter] again).
Label: structural (on-shell identity + proved Seeley--DeWitt expansion); caveat: the quantum trace
anomaly of conformal matter is not in the corpus and would shift R = 0 by a small amount — flagged,
not developed (adversarial item 4).

### (b) Reading and derivation of a(t)

Reading: under [H-dict], n = log a and the tick lengthens as H^{-1} — domain-free, already corpus.
Derivation: deriving a(t) (deceleration, approach to the de Sitter steady state) requires a dynamical
law for the off-equilibrium departure.
The corpus supplies stationarity (equilibrium) and a static off-equilibrium READING (constant
beta_* != 1); it supplies NO equation of motion for beta_* or for the approach.
K1' FIRES: every candidate closure (gradient flow of F, maximum entropy production, per-tick
constrained stationarity of F at fixed rank budget) is an import.
The most corpus-natural candidate is named for any future constructive session: ADIABATIC DRIVEN
EQUILIBRIUM — at each rank n, delta F = 0 with the production constraint evaluated at that rank,
i.e. a quasi-static sequence of constrained equilibria.
It is a CHOICE (one member of the [H-dyn] family), not forced; it also inherits K3' (foliation) off
the instanton.
Grade: conditional no-go until [H-dyn] is adopted as an explicit labelled hypothesis.

### (c) Status of the effective density

Within the driven reading the answer is sharp and domain-free.
Rewrite the off-equilibrium response as
G_munu = 8 pi G [T_munu + (beta_*^{-1} - 1) T_munu]:
the departure from equilibrium acts as an effective component PROPORTIONAL TO THE LOCAL MATTER
CONTENT — a renormalisation of the coupling, not an independent fluid.
Three consequences, all structural:
1. Anti-fluid consistency: the effective component inherits the matter equation of state (it scales
   as a^{-3} in the matter era if beta_* is constant), so it CANNOT mimic a cosmological constant —
   the driven reading never smuggles a dark-energy fluid back in.
   This sharpens 05b's anti-fluid stance from a preference into a structural property of the hook.
2. Degeneracy: a CONSTANT beta_*^{-1} != 1 is exactly degenerate with the calibration of G_N
   (G_eff = G_N beta_*^{-1}), hence unobservable — the observable content of the driven reading in
   the matter era is carried ENTIRELY by the EVOLUTION beta_*(n).
3. Gate: that evolution is precisely what [H-dyn] would supply; until then the observable content is
   confined, in the same shape as the TrajBr conditional no-go confined the compression channel.
   (If a beta_*(a) law is ever pinned, G_eff(z) is constrained by BBN and structure growth — noted as
   falsifiability POTENTIAL of the gated branch, no fit attempted, no dictionary matching.)

## 4. The domain-divergence computation (K4' made exact)

The instanton masked the domain choice; any evolving era splits it.
Take the three candidate readings of the history-entropy insertion and follow their trend through a
decelerating era (exact scalings, given the definitions; H ~ a^{-3/2} matter, H ~ a^{-2} radiation):

1. Homogeneous per-rank reading (TrajBr native, domain-free): cumulative S_hist = h_b n = h_b log a.
   Trend: INCREASING, always.
2. Horizon-patch extensive reading (the [H-ent-id-ext] repair, V_c comoving import):
   N_p = V_c a^3 H^3, so Sigma_hist ~ 2 pi h_b N_p ~ a^{-3/2} (matter), ~ a^{-3} (radiation).
   Trend: DECREASING through both decelerating eras.
3. State-volume reading: already dead on the Cosmology 2.0 ledger (a^0.881 != a^3), listed only for
   completeness.

Readings 1 and 2 diverge IN SIGN of their trend everywhere outside exact de Sitter.
On the Euclidean instanton (constant H, no a(t)) this divergence is invisible — which is exactly why
the H_infty construction could close with a single number V_c.
CONSEQUENCE (the recon's central negative): in the matter era the inner domain import of
[H-ent-id-ext] is no longer one calibration constant; it is a time-dependent structural choice that
even decides whether the inserted entropy grows or decays.
No corpus object forces the choice.
A naive comoving-extensive transplant would carry a DECREASING Sigma_hist through the matter era —
a wrong-way entropy bookkeeping that any future adoption of [H-ent-id-ext] must confront explicitly
(second-law probe, adversarial item 5).

## 5. Grading (C1-C3 battery)

C1 (variable): the departure acts on the coupling (beta_*), the hook the corpus itself offers, and
the driver (h_b H) is corpus-pinned.
Right variable available.
Conditional, benign.
C2 (constraint): FAILS on every quantitative route — [H-dyn] (closure) + domain choice (K4') are
imports; only the carrier h_b H and the beta_*-reading are parameter-free.
Mirror of the H_infty C2 verdict: no branch is simultaneously well-posed and import-free.
C3 (principle): the off-equilibrium principle is NOT corpus-forced; Thermodynamics itself labels the
beta_* != 1 reading as offered and undeveloped.
[H-dyn] is henceforth the NAMED load-bearing object of the matter-era front, with the time-dependent
domain choice (K4') as its inner import — the exact analogue of the [H-ent-id] -> [H-ent-id-ext]
sharpening, one level down the cosmological history.

## 6. Adversarial pass (run before this note was written)

1. Does the on-shell Friedmann tie (H^2 ~ rho) restore the single-scale premise and re-export the
   intensive-invariance Lemma to the matter era?
   Only on-shell; a variational analysis is off-shell by construction, where rho and H are
   independent.
   The Lemma neither transfers nor is weakened (anti-relapse: the instanton gate stands).
2. Could per-tick (adiabatic) stationarity count as corpus-supplied dynamics?
   No — it is a closure CHOICE (named as the natural [H-dyn] candidate in 3b), and it inherits the
   foliation limitation K3'.
3. Is the coupling-renormalisation identity (3c) robust to the local field beta(x)?
   Yes at the relevant order: the covariant part of beta(x)^{-1} is O(R ell_chi^2) and is absorbed
   in the IR remainder (rem:gauge); the global multiplier carries the departure.
   The two objects stay distinct, as the paper insists (rem:beta-star).
4. Radiation-era silence (R = 0): exact for classical conformal matter; the quantum trace anomaly
   would give R != 0 at loop level.
   The corpus contains no anomaly sector; flagged as the single caveat on the banked by-product —
   the statement is exact WITHIN the corpus.
5. Second-law probe on reading 2 (decreasing Sigma_hist): not overclaimed — [H-ent-id-ext] is gated
   anyway; recorded as a constraint any future adoption must discharge (choose a domain rule whose
   trend is defensible, or accept and interpret the decay).
6. Load-bearing object of the negative (named): the ABSENCE of an off-equilibrium closure ([H-dyn])
   — everything else either follows (readings, scalings: exact) or is independently blocked
   ([W-matter], K3').

## 7. Entropy polysemy (wagon item, standing instruction)

This front touches S_Pi[g] and S_hist (ENI's measure entropy uninvolved).
Notation kept distinct throughout; the disarm rides in whatever paper first hosts two of the three.
Nothing to do now.

## 8. Outcome ledger and follow-ups

Banked (internal):
1. The matter-era conditional no-go with its three independent blockers and [H-dyn] as the named
   load-bearing object (sections 0, 5).
2. The domain-divergence result: outside exact de Sitter the candidate insertions diverge in the
   SIGN of their trend, making the [H-ent-id-ext] domain import time-dependent (section 4, exact).
3. NEW POSITIVE: the radiation era is spectrally silent in the covariant a_2 channel of beta(x);
   the channel switches on at matter domination (R = 8 pi G rho_m) — exact on-shell, domain-free,
   import-free (section 3a).
   Natural host if ever promoted: a Thermodynamics or Cosmology revision; it is a READING of the
   transition, not a derivation, and must carry that label.
4. The effective-density status: coupling renormalisation, never a fluid; constant departure
   unobservable (G_N degeneracy); observable content confined to the gated evolution beta_*(n) (3c).
Follow-up candidates (each on explicit go): (a) adopt [H-dyn] explicitly (adiabatic driven
equilibrium as the candidate closure) and construct the matter-era sequence — heavy, imports
declared up front; (b) [W-matter]: explicit projected functional for dust and radiation — a
different front (matter sector), prerequisite for any transition dynamics; (c) nothing else from
this front.
Placement: none now (recon note only, per the scoped go).

## 9. Discipline ledger

Labels: domain-divergence scalings PROVED (exact arithmetic from definitions); radiation-era silence
STRUCTURAL (on-shell identity + proved expansion; anomaly caveat flagged); coupling-renormalisation
identity STRUCTURAL (algebraic rewrite of the corpus hook); conditional no-go CONDITIONAL (on the
corpus as it stands: no [H-dyn], no [W-matter], no forced domain); value tier UNTOUCHED; anti-relapse
walls UNTOUCHED (instanton gate, hierarchy, Koide arena, V3 note).
Load-bearing objects named in the main verdict: [H-dyn] (for the negative), the time-dependent
domain import (its inner import), [W-matter] (independent blocker).
Adversarial pass run BEFORE announcement (section 6).
Nothing deposited; note stays untracked per the working-notes rule.
