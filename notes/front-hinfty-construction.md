# Front: explicit driven-equilibrium functional on S^4 of radius 1/H

Date: 2026-07-07.
Scope fixed by Jerome (7 Jul ruling, second H_infty session): construct the driven-equilibrium
functional explicitly on S^4_{1/H} (Dowker-type sphere zeta values), check whether stationarity in H
is well-posed, grade C1-C3; STRICTLY structural level — the value-tier no-go (K1/K2/R4 of
front-hinfty-recon.md) is acted and is NOT reopened (anti-relapse).
Deliverable: this internal recon note first; placement arbitrage only if the construction holds.
Status: working recon, untracked (working-notes rule), nothing deposited, no tex touched.
Companion script (untracked): notes/hinfty_s4_zeta.py (mpmath, 40 dps).

## 0. Verdict up front

The double-outcome front lands on the SECOND branch: stationarity in H is NOT well-posed on the
universal content under any intensive reading of the production term — K4 FIRES.
The clean negative is banked, and it gates [H-ent-id] more precisely than before: only an EXTENSIVE
insertion of the history entropy, with an imported substrate domain volume, can produce a stationary
H on S^4; every intensive insertion is structurally excluded by an exact invariance of the de Sitter
instanton (Lemma, section 2).
Within the gated extensive branch the construction is fully explicit and the critical point is unique
(section 3), so the gate is sharp, not vague.
Cosmology 2.2's subsection stays a PROPOSITION (it does not rise to construction); its three safety
sentences are confirmed verbatim by this computation.

## 0bis. Status summary (Jerome's verbatim, 7 Jul 2026 validation — banked for any future host paper)

Front VALIDATED CLOSED by Jerome as a clean negative with a sharper gate than the initial recon.
His retained status points: (i) logical verdict — [H-ent-id] does not become a construction, it
becomes [H-ent-id-ext] = [H-ent-id] + imported extensive substrate domain, so the front confirms
(does not promote) Cosmology 2.2's cautious proposition status; (ii) bankable internal outputs —
zeta_{S^4,det'}(0) = -61/90 (universal log slope) and Delta S_hist^intensive = 2 pi h_b (per-period /
per-patch production constant, no value reading attached); (iii) the extensive branch is clean but
gated, and the sign of zeta(0) that makes H_* exist depends on det'; (iv) MAIN ADVERSARIAL HINGE —
the triplet {minimal scalar Laplacian + det' + zero-mode excluded}: changing any one of the three
reopens the computation; as long as eq:Spi-def stands, the result holds.

His verbatim LaTeX status paragraph (to be consumed as-is by whichever paper ever hosts this front):

```latex
\paragraph{Outcome of the \(H_\infty\) construction test.}
The explicit \(S^4_{1/H}\) test does not promote the steady-state reading to an
ungated construction.
For the corpus operator \(A_g=-\nabla_g^2\) with the zero mode removed, the sphere
zeta scaling gives
\[
  S_\Pi(H)=\zeta(0)\log H-\frac12\zeta'(0),
  \qquad
  \zeta(0)=-\frac{61}{90}.
\]
The logarithmic coefficient is scheme-independent: the local counterterms on
\(S^4_{1/H}\) contribute only \(H^{-4}\), \(H^{-2}\), and \(H^0\) terms.
Any intensive transplant of the history-production rate \(\dot S_{\rm hist}=h_bH\)
onto the instanton is \(H\)-independent, since the only available time scale is
proportional to \(H^{-1}\).
Equivalently, both the Euclidean-period reading and the horizon-patch reading give
\[
  \Delta S_{\rm hist}=2\pi h_b.
\]
Hence the intensive driven functional has
\[
  \frac{dF}{dH}=-\frac{61}{90H}\neq 0,
\]
after scheme subtraction, and admits no critical point.
Stationarity in \(H\) is therefore ill posed under every intensive insertion.
The only well-posed repair is extensive.
If a substrate comoving volume \(V_c\) is imported, then
\[
  \Sigma_{\rm hist}(H)=\frac32 h_bV_cH^3,
  \qquad
  H_\ast^3=\frac{61}{405h_bV_c}.
\]
This yields a unique stationary point, but the calibration is precisely the imported
domain volume.
Thus the admissible statement is not \([H\text{-ent-id}]\), but the gated hypothesis
\([H\text{-ent-id-ext}]\): an extensive insertion with an explicit substrate-domain
import.
The value tier is not reopened.
```

His recommended next action: nothing in Cosmology 2.2 for now — the front produced a discipline
bound, not an immediately publishable section.

## 1. The spectral entropy of the instanton (computed, exact where stated)

Setup: minimal scalar Laplacian A_g = -nabla^2 on S^4 of radius a = 1/H (the corpus operator,
eq:Spi-def of Beau2026Thermodynamics with det', i.e. zero mode excluded).
Spectrum lambda_n = n(n+3)/a^2, degeneracy d_n = (n+1)(n+2)(2n+3)/6, n >= 1.

Scaling law (exact): zeta_a(s) = a^{2s} zeta_1(s), hence
S_Pi(H) = (1/2) log det' A_{1/H} = zeta(0) log H - (1/2) zeta'(0),
where zeta is the spectral zeta of the UNIT sphere.

Computed values (script, two independent internal checks):
- zeta(0) = -61/90 EXACTLY. Heat-kernel prediction B_4 - N_0 = 29/90 - 1 matched to 25 digits;
  representation validated against the direct eigenvalue sum at s=3.
  (Unit-S^4 inputs: R = 12, |Ric|^2 = 36, |Riem|^2 = 24, a_4 = 29/15 pointwise, Vol = 8 pi^2/3.)
- zeta'(0) = -0.55212694979... (numeric; additive constant, NOT load-bearing for stationarity).

Renormalisation structure: the scheme freedom of Beau2026h consists of local counterterms
int sqrt(g), int sqrt(g) R, and quadratic curvature invariants; on S^4_{1/H} these contribute
H^{-4}, H^{-2}, and H^0 respectively (quadratic invariants are scale-invariant in d=4; box R
integrates to zero).
Therefore
S_Pi^ren(H) = ctilde_4 H^{-4} + ctilde_2 H^{-2} + zeta(0) log H + const,
with ctilde_4, ctilde_2 scheme-dependent and the LOG COEFFICIENT zeta(0) = -61/90 UNIVERSAL
(scheme-independent — no local counterterm produces log H at fixed renormalisation point).
Sign check: zeta(0) < 0, so the universal part of S_Pi strictly DECREASES as H grows — the recon's
qualitative sentence (``fewer admissible modes below the cutoff'') is now quantitative, with slope
dS_Pi/dlog H = -61/90.

Stationarity of the scheme terms alone reproduces the classical sphere condition (Einstein + Lambda,
H^2 = Lambda_ind/3): this is K1 territory, scheme-dependent, dead as derivation — acted, untouched.

## 2. Lemma (intensive invariance): the instanton kills every intensive driving term

Claim: ANY intensive transplant of the production rate dS_hist/dt = h_b H onto the instanton yields a
constant independent of H.
Reason: the only time scale available on S^4_{1/H} is proportional to H^{-1}, so every intensive
reading integrates the rate over a window c/H and gives h_b H * (c/H) = c h_b, for any convention c.
The two corpus-natural readings even agree on the constant:
(i) one Euclidean period tau in [0, 2 pi/H]: Delta S_hist = 2 pi h_b;
(ii) per horizon patch (V_H = (4 pi/3) H^{-3}) integrated over the full instanton 4-volume
     (Vol = (8 pi^2/3) H^{-4}): (h_b H / V_H) * Vol = 2 pi h_b.
Numerically 2 pi h_b = 5.5378... — an H-independent pure number.
The lemma is convention-independent (the factor 2 pi never enters the conclusion).

## 3. Consequence: ill-posedness (intensive) and the unique repair (extensive)

Driven functional, additive form: F[H] = S_Pi^ren(H) + lambda Sigma_hist(H).
On the pure instanton W_Pi = 0 (no matter), so the off-equilibrium multiplier beta_* is IDLE here:
the driving structure is carried entirely by the production term.

Intensive branch (Sigma_hist = const by the Lemma):
dF/dH = zeta(0)/H = -(61/90)/H != 0 for all H > 0, after scheme subtraction.
Strictly monotone, NO critical point.
The same holds in Lagrange-multiplier form F = S_Pi - lambda (Sigma_hist - sigma): the H-derivative
of the constraint term vanishes identically, and the constraint itself fixes no H.
CONCLUSION: stationarity in H is ILL-POSED under every intensive reading.
K4 FIRES, and it fires precisely: well-posedness itself (not merely the location of the stationary
point) requires an extensive domain choice.

Extensive branch (the only repair): fix a substrate comoving volume V_c (IMPORT) and count patches,
N_p(H) = V_c/V_H = (3/(4 pi)) V_c H^3, so Sigma_hist(H) = 2 pi h_b N_p(H) = (3/2) h_b V_c H^3.
Stationarity of S_tot = S_Pi^ren + Sigma_hist (universal content):
zeta(0)/H + (9/2) h_b V_c H^2 = 0  =>  H_*^3 = -2 zeta(0) / (9 h_b V_c) = 61 / (405 h_b V_c).
Existence and uniqueness: a unique positive critical point exists BECAUSE zeta(0) < 0.
Stability character: d^2 S_tot/dH^2 > 0 at H_* — a MINIMUM of S_tot (S_tot diverges to +infinity at
both ends H -> 0 and H -> infinity).
The corpus principle is stationarity (delta F = 0, def:equilibrium), which selects H_* uniquely; a
maximum-entropy selection would instead run to the boundary.
The stability/selection character is NOT corpus-fixed — flagged as an open structural item of the
gated branch, not resolved here.

Calibration identity: H_* ~ V_c^{-1/3} — the calibrated normalisation of the steady state IS the
imported domain volume, made explicit.
One import (the late-time fit value of H_infty) is traded for exactly one import (V_c).
Status remark (value tier, single sentence, no reopening): with V_c = O(1) in substrate units the
critical point lands at H_* ell_chi = O(1) (numerically H_* = 0.555 for V_c = 1), reconfirming R4
from inside the construction; the value-tier no-go is unchanged.

## 4. Grading (C1-C3 battery)

C1 (variable): does the driving act on the right physical variable?
The rate h_b H is corpus-pinned (Beau2026tb); its transplant to the Euclidean instanton uses the
instanton clock (any window ~ H^{-1}).
The Lemma makes the conclusion convention-independent, so the imported clock normalisation is
harmless for the verdict.
Conditional, benign.

C2 (constraint): is the construction parameter-free?
The two branches SPLIT exactly here: the intensive branch is parameter-free (2 pi h_b, no import)
and yields NO stationarity; the extensive branch yields stationarity and imports V_c.
No branch passes both — this is the precise content of the gate.
FAILS on the only well-posed branch.

C3 (principle): is [H-ent-id] corpus-forced?
NO (unchanged from front-hinfty-recon.md), and now SHARPENED: the identification, if ever adopted,
must specifically be an extensive insertion with a fixed substrate domain; intensive identifications
(per-period, per-patch) are structurally excluded by the Lemma.
[H-ent-id] is henceforth gated as [H-ent-id-ext] = [H-ent-id] + extensive domain import.

## 5. Adversarial pass (run before this note was written)

1. Is the log coefficient really scheme-independent?
   YES: the counterterm basis in d=4 (volume, Einstein-Hilbert, quadratic invariants, box R) spans
   H^{-4}, H^{-2}, H^0 only; a renormalisation-point change shifts the CONSTANT via zeta(0) log mu,
   not the H-dependence at fixed mu.
2. Zero-mode sensitivity (load-bearing, corpus-anchored): the SIGN of zeta(0) = 29/90 - 1 comes from
   the excluded constant mode; without the det' convention the slope would be +29/90 and even the
   extensive branch would lose its critical point (both terms positive).
   The det' convention is explicit in eq:Spi-def of Beau2026Thermodynamics — anchored, but any future
   change of operator or zero-mode treatment re-opens this computation.
3. Operator dependence: zeta(0) is operator-specific (a conformally coupled scalar would give a
   different value); the corpus pins the minimal scalar Laplacian (Beau2026h) — anchored.
4. Lagrange-multiplier form: same ill-posedness (checked above); the negative is not an artefact of
   the additive form.
5. beta_* idle: on the empty instanton the off-equilibrium hook never enters; Cosmology 2.2's
   wording (production-driven off-equilibrium reading) survives because it concerns the approach with
   matter, but the asymptotic S^4 state is driven by the production term alone — worth one clarifying
   sentence if the subsection is ever revised.
6. Load-bearing object of the NEGATIVE (named): the intensive-invariance Lemma (section 2) plus the
   universality of the log slope (section 1).
   Both are short, exact, and independent of every convention scanned.

## 6. Entropy polysemy (wagon item, standing instruction)

This construction touches TWO of the three entropies: Thermodynamics' log-det S_Pi[g] and TrajBr's
counting S_hist (ENI's measure-level entropy is not involved).
Per the standing decision, the polysemy disarm (three named objects, no silent identification) rides
in the write-up of the first paper that touches two of the three — i.e. exactly the paper that would
host this result if it is ever promoted.
In this note the two objects are kept notationally distinct throughout (S_Pi vs S_hist / Sigma_hist).

## 7. Outcome ledger and follow-ups

Banked (internal): the precise K4 negative — stationarity in H on S^4_{1/H} is ill-posed under every
intensive insertion of the production term (exact Lemma), and well-posed only under [H-ent-id-ext]
(extensive insertion, imported substrate volume), where the critical point is unique with
H_*^3 = 61/(405 h_b V_c) and an unresolved stability character.
By-products worth keeping: zeta(0) = -61/90 as the universal log-slope of the instanton spectral
entropy (quantifies ``fewer admissible modes'' exactly); the per-period production constant 2 pi h_b
(pure number, no interpretation attached — vigilance rule).
Cosmology 2.2: NO change needed; the subsection's proposition status and safety sentences are
confirmed, not upgraded.
Placement: none now (negative branch of Jerome's double outcome); if [H-ent-id-ext] is ever forced or
adopted as an explicit hypothesis, the natural host is a Cosmology revision, which then also carries
the polysemy disarm.
Follow-up candidates (each on explicit go): (a) stability/selection character of the extensive
critical point (min vs stationarity-only); (b) matter-era version (W_Pi != 0, beta_* active) — a
genuinely different computation; (c) nothing else from this front.

## 8. Discipline ledger

Labels: zeta(0) = -61/90 PROVED (heat-kernel identity + 25-digit numerical match); scaling law and
Lemma PROVED (exact arithmetic); scheme-independence of the log slope STRUCTURAL (counterterm basis);
ill-posedness CONSEQUENCE (proved given the Lemma); extensive repair CONSTRUCTION (conditional on the
V_c import); stability character OPEN; value tier UNTOUCHED (single reconfirming sentence only).
Load-bearing objects named in the main verdict: the intensive-invariance Lemma and the universal log
slope (for the negative); the V_c import (for the gated positive).
Adversarial pass run BEFORE announcement (section 5).
Nothing deposited; note and script stay untracked per the working-notes rule.
