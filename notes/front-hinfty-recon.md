# Front recon: H_infty via the spectral-equilibrium route (Beau2026Thermodynamics)

Date: 2026-07-07.
Scope fixed by Jerome (7 Jul ruling): one-session recon with kill-switches — inventory what
Thermodynamics really supplies (variational S_Pi[g], spectral first law, beta(x)); state what the
bridge requires (connect the carrier dS_hist/dt = h_b H to the variational object; extract H_infty
as the normalisation of rank against the physical clock); name the load-bearing object; grade
forced vs imported.
Status: working recon, untracked, nothing deposited, no tex touched.
Sources read directly (bias-independent rule): spectral-gravity/thermodynamics/tex/Thermodynamics.tex
(full), spectral-gravity/gravity (c_Lambda passages), spectral-gravity/lorentz-paper (S_Pi^(L)
definition), cosmology-paper/tex/05b-history-branching (full).

## 1. Kill-switches declared up front

K1 (scheme): if the extraction of H_infty passes through the induced cosmological term c_Lambda(mu),
it inherits its renormalisation-scheme dependence and is NOT forced.
K2 (identification): if the bridge requires identifying the history-branching entropy S_hist with the
spectral entropy S_Pi[g] (or inserting it into the equilibrium functional) without a corpus-forced
statement, the step is at best a construction task, to be graded like [H-centroid] was.
K3 (signature): if the bridge requires evaluating the equilibrium principle on Lorentzian FRW, the
Euclidean-only limitation of Thermodynamics must be discharged by the Lorentzian completion or the
step is conditional.
K4 (domain): if the bridge requires choosing the region on which S_Pi is evaluated (comoving volume
vs horizon patch vs admissibility ball), the choice is an import unless forced — this is the same
``N_dist -> observable'' gap already on the Cosmology 2.0 ledger (the A&A objection re-enters at
substrate level).

## 2. Inventory: what Thermodynamics actually supplies (with epistemic strata)

1. S_Pi[g] = (1/2) log det' A_g with a renormalised metric variation whose IR-dominant local part is
   (16 pi G_N)^{-1} G_munu (eq. 2 of the paper, imported from the gravity companion Beau2026h).
   Stratum: structural, conditional on the companion's renormalisation scheme; Euclidean, IR regime
   R ell_chi^2 << 1.
2. Local multiplier field beta(x)^{-1} = 2/t_* - R(x)/6 + O(t_*) from the diagonal heat kernel
   (def:beta, prop:u-expansion).
   CRITICAL for our purposes: the paper itself states (rem:tstar) that the universal part
   beta_0^{-1} = 2/t_* is scheme-dependent and ``carries no intrinsic thermodynamic meaning''; ONLY
   the covariant content is the a_2 curvature correction -R/6.
   Stratum: proved (Seeley--DeWitt) for the expansion; the physical reading is interpretive.
3. Local spectral first law delta S_Pi = int beta^{-1} delta E_Pi as a compatibility identity,
   holding IFF the geometry satisfies the Einstein equation (thm:first-law).
   Stratum: structural (IR, Euclidean); explicitly an equivalence, not an independent postulate.
4. Spectral equilibrium principle: F = S_Pi - beta_*^{-1} W_Pi stationary => Einstein equation
   ``up to a cosmological term'' (thm:einstein), with 8 pi G fixed by the two normalisations.
   Stratum: structural.
   The cosmological term is NOT pinned: the gravity companion sources it from the a_0 pole
   (proportional to int sqrt(g)), i.e. c_Lambda(mu) is a scheme-dependent UV quantity — the classic
   induced-gravity Lambda problem, unresolved in the corpus.
5. An off-equilibrium hook: beta_*^{-1} != 1 gives G = 8 pi G beta_*^{-1} T, read as ``off-equilibrium
   spectral geometry with an effective renormalisation of the matter coupling''
   (subsec:beta-star-status).
   Stratum: offered reading, undeveloped.
6. Limitations stated by the paper itself: Euclidean setting only; static foliation for E_Pi; W_Pi
   formal (no explicit matter construction).
7. Lorentzian side (lorentz-paper): S_Pi^(L)[g] = (1/2) Re log det' D_g EXISTS as a definition, with
   second variation = retarded Green operator; developed for linearised waves around flat space, NOT
   evaluated on FRW backgrounds and the equilibrium principle is not re-derived there.
   Net for K3: definition supplied, FRW application NOT supplied.

## 3. What the bridge requires (graded)

The Cosmology 05b passage defines the target exactly: H_infty = the normalisation of projective rank
against the physical homogeneous clock; named route = connect S_hist to the variational object.

R1 (signature transfer): evaluate the equilibrium sector on (Euclidean S^4 of radius 1/H, or
Lorentzian FRW).
Partially supplied (S_Pi^(L) exists); the FRW evaluation is a computation, not an obstruction.
Grade: conditional, unobstructed.

R2 (the identification [H-ent-id]): make S_hist a term or constraint of the equilibrium problem.
NOT corpus-forced.
Worse, the corpus carries an ENTROPY POLYSEMY that any write-up must disarm explicitly: at least
three distinct objects share the S_Pi neighbourhood — (a) ENI's measure-level projection entropy
(conditional fibre entropy), (b) Thermodynamics' spectral log-det entropy S_Pi[g], (c) TrajBr's
distinguishable-history counting entropy S_hist.
No corpus theorem identifies any two of them; ENI is measure-level, S_Pi[g] lives on the effective
geometry, S_hist on substrate histories.
Grade: construction task; no obstruction found (nothing forbids a driven-equilibrium functional with
an entropy-production constraint), but nothing forces it either.
This is THE load-bearing object of the front.

R3 (domain choice): S_hist is a per-rank count of the homogeneous cascade; S_Pi[g] needs a region.
Volume vs horizon patch changes the scaling qualitatively (the very gap the A&A objection lives in;
Cosmology 2.0 killed the state-volume reading quantitatively, a^{0.881} != a^3).
Grade: import unless a forcing argument is found; K4 currently OPEN.

R4 (the pinning equation): a second equation that fixes H, since the equilibrium condition alone
leaves the cosmological term free.
Two candidate forms surfaced by this recon:
  (i) Lambda-route: read H_infty^2 = Lambda_ind/3 from c_Lambda(mu).
      K1 FIRES: scheme-dependent, not forced.
      Dead as a derivation; alive only as a calibration slot.
  (ii) Balance-route (the structurally natural one): de Sitter as the STEADY STATE of a driven
      spectral equilibrium — stationarity of a total functional in which the branching sector
      contributes its production rate dS_hist/dt = h_b H against the spectral-entropy cost of
      curvature (S_Pi on the S^4 of radius 1/H decreases as H grows: fewer admissible modes below
      the cutoff).
      This is a well-posed variational sketch, and it is exactly ``normalisation of rank against the
      physical clock'': the balance point defines the rank-per-tick scale.
      BUT the dimensional audit blocks the value tier: both sides are set by the same substrate
      scales (t_*, ell_chi), so any O(1) structural balance yields H_infty ~ O(1) in substrate units
      (H_infty ell_chi ~ 1), while the observed value is H_0 ell_chi ~ 10^{-61} for a Planck-scale
      ell_chi (G_N ~ 16 pi^2 ell_chi^2).
      Without an exponentially small forced factor (none is in the corpus today), the balance
      CANNOT land 60 orders of magnitude down.
      Same wall genre as the fermionic ~3477 hierarchy: big numbers need a new lever, not a
      relocation.

## 4. Verdict (two tiers, labelled)

VALUE TIER: CONDITIONAL NO-GO.
Three independent blockers: c_Lambda scheme-dependence (K1), no forced [H-ent-id] (K2/R2), and the
hierarchy wall of the balance route (R4-ii).
The spectral-equilibrium route does NOT derive the numerical value of H_infty under the corpus as it
stands, and no minimal import repairs this (importing the observed H_0 is calibration, not
derivation).

STRUCTURAL TIER: ROUTE OPENS.
The coherent deliverable is: de Sitter as the steady state of a driven spectral equilibrium — the
off-equilibrium hook (beta_*^{-1} != 1) plus the constant production rate dS_hist/dt = h_b H — with
H_infty entering as a CALIBRATED normalisation, the exact epistemic status the corpus already grants
G_N (induced, calibrated, not predicted).
This is not empty: it upgrades ``H(z) is arbitrary'' (the A&A objection) to ``H(z) tends to a
de Sitter steady state whose entropy carrier and production rate are pinned (h_b = log(1+sqrt2)),
with one calibrated scale'' — a structured answer with falsifiable content (the rate, the carrier,
the staircase signature), even though the scale is calibrated.
Deliverable form, if pursued: a short note or a Cosmology section, ``H_infty as a calibrated
steady-state normalisation'', with the no-go of the value tier stated as a labelled negative.

LOAD-BEARING OBJECT (named, per discipline): [H-ent-id] — the insertion of the history-branching
entropy into the spectral-equilibrium functional (R2), with the domain choice (R3) as its inner
import.
Everything else either follows (R1, computation) or dies independently (R4-i).

## 5. Kill-switch audit summary

K1 FIRES for the value tier (Lambda-route dead as derivation).
K2: [H-ent-id] = unobstructed construction task, NOT forced — structural tier only, must carry the
label.
K3: discharged at definition level by lorentz-paper; FRW evaluation = open computation.
K4: OPEN import (volume vs horizon), must be resolved or explicitly hypothesised in any write-up.

## 6. Follow-ups (NOT executed, next-session candidates, each on explicit go)

1. Construct the driven-equilibrium functional explicitly (steady-state extension of
   def:equilibrium with an entropy-production constraint) and check whether stationarity in H is
   well-posed on S^4_{1/H} — uses known sphere log-det results (Dowker-type zeta values).
2. Grade the outcome against C1-C3-style tests; if the balance is well-posed, state the calibrated
   H_infty normalisation and the value-tier no-go together.
3. Disarm the entropy polysemy in whatever paper hosts the result (three named objects, no silent
   identification) — audit-level item even if the front stops here.

## 7. Discipline ledger

Labels: inventory items carry the strata of their source papers; the value-tier no-go is CONDITIONAL
(on the corpus as it stands: no forced [H-ent-id], no forced domain, no Lambda-pinning lever); the
structural-tier opening is a CONSTRUCTION proposal, not a result.
Adversarial check run on the strongest positive reading: the balance-route sketch survives as
structure but its value claim dies on the dimensional audit — the announcement above names the
load-bearing object in the main verdict, not only here.
Nothing deposited; this note stays untracked per the working-notes rule.
